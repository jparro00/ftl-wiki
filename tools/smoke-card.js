/*
  Smoke-test a built card:  node tools/smoke-card.js <card.html>

  Runs the card's real renderer against a minimal DOM shim and prints the tree it
  produced as indented text. Catches what reading the file cannot: renderer
  exceptions, rows that come out blank, vocabulary gaps that fall through to raw
  ids, and mis-nested chain stages.

  Exit code is non-zero if the renderer throws.
*/
const fs = require("fs");

const file = process.argv[2];
if (!file) {
  console.error("usage: node tools/smoke-card.js <card.html>");
  process.exit(2);
}

const html = fs.readFileSync(file, "utf8");
const scripts = [...html.matchAll(/<script(?: type="application\/json" id="([\w-]+)")?>([\s\S]*?)<\/script>/g)];
const json = Object.fromEntries(scripts.filter(m => m[1]).map(m => [m[1], m[2]]));
const body = scripts.find(m => !m[1])[2];

const mk = tag => ({
  tag, className: "", innerHTML: "", textContent: "", hidden: false, children: [],
  style: { setProperty() {} }, attrs: {},
  setAttribute(k, v) { this.attrs[k] = v; },
  getAttribute(k) { return this.attrs[k]; },
  addEventListener() {},
  appendChild(c) { this.children.push(c); return c; },
});

const nodes = {
  eyebrow: mk("p"), title: mk("h1"), hail: mk("p"), arrival: mk("p"),
  note: mk("p"), tree: mk("div"), chain: mk("div"),
};
nodes["event-data"] = { textContent: json["event-data"] };
nodes["card-vocab"] = { textContent: json["card-vocab"] };

const document = { getElementById: id => nodes[id], createElement: mk };
new Function("document", body)(document);

const strip = s => s.replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();

function dumpTree(el, depth = 0) {
  for (const c of el.children) {
    if (c.className.split(" ")[0] === "row") console.log("  ".repeat(depth) + "· " + strip(c.innerHTML));
    else if (c.className === "klabel") console.log("  ".repeat(depth) + "[" + c.textContent + "]");
    dumpTree(c, c.className === "kids" ? depth + 1 : depth);
  }
}

function dumpChain(el) {
  for (const c of el.children) {
    /* A stage's arrival effects are set via innerHTML, not textContent — printing only
       leaf text hid an entire quest reward from the required pre-publish check. */
    if (c.className === "arrival") { console.log("arrival: " + strip(c.innerHTML)); continue; }
    if (c.className === "card") dumpTree(c);
    else if (c.children.length) dumpChain(c);
    else if (c.textContent) console.log("\n" + c.textContent);
  }
}

/* The header is part of the card. The hail is the only place the event's own text
   appears, and #arrival the only place the root record's effects appear — omitting
   them here once hid a card that never mentioned the player was being boarded. */
/* §7.2 claims this catches blank rows and raw-id fallthrough. It only did so if a
   human read the dump, which is how a labelless row shipped. Now it asserts. */
const problems = [];
const PROSE_CAPS = new Set(["FURIOUS", "ABADOTH", "ABATODH", "ANODYNE", "EMP", "AE", "FTL", "PDS"]);

function audit(el) {
  for (const c of el.children) {
    if (c.className.split(" ")[0] === "row") {
      const html = c.innerHTML;
      const label = (html.match(/<span class="choice">([\s\S]*?)<\/span>/) || [, ""])[1];
      if (!strip(label)) problems.push("blank row label: " + strip(html).slice(0, 70));
      for (const tok of strip(html).match(/[A-Z][A-Z0-9_]{3,}/g) || []) {
        if (!PROSE_CAPS.has(tok)) problems.push("raw id on card: " + tok);
      }
    }
    audit(c);
  }
}

console.log("== " + nodes.title.textContent + " ==");
console.log(nodes.eyebrow.textContent);
console.log("hail: " + strip(nodes.hail.textContent));
if (strip(nodes.arrival.innerHTML)) console.log("arrival: " + strip(nodes.arrival.innerHTML));
console.log(nodes.note.textContent + "\n");
dumpTree(nodes.tree);
dumpChain(nodes.chain);

audit(nodes.tree);
audit(nodes.chain);
if (problems.length) {
  console.error("\n" + problems.length + " problem(s):");
  for (const p of [...new Set(problems)]) console.error("  " + p);
  process.exit(1);
}
