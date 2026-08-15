/*
  Smoke-test a built card:  node tools/smoke-card.js <card.html>

  Runs the card's real renderer against a minimal DOM shim and prints the tree it
  produced as indented text. Catches what reading the file cannot: renderer
  exceptions, rows that come out blank, vocabulary gaps that fall through to raw
  ids, and mis-nested chain stages.

  The renderer is tools/card-runtime.js, inlined into every card. This harness
  evaluates it, then calls FTLCard.render() itself rather than running the card's
  own bootstrap — the same entry point sector pages use.

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
// Two plain scripts now: the runtime and the card's three-line bootstrap. The
// runtime is the long one.
const runtime = scripts.filter(m => !m[1]).map(m => m[2]).sort((a, b) => b.length - a.length)[0];

const mk = tag => ({
  tag, className: "", innerHTML: "", textContent: "", hidden: false, children: [],
  style: { setProperty() {} }, attrs: {},
  setAttribute(k, v) { this.attrs[k] = v; },
  getAttribute(k) { return this.attrs[k]; },
  addEventListener() {},
  appendChild(c) { this.children.push(c); return c; },
});

const document = { createElement: mk, getElementById: () => null };
const scope = {};
new Function("document", "globalThis", runtime)(document, scope);

const root = mk("div");
scope.FTLCard.render(root, JSON.parse(json["event-data"]), JSON.parse(json["card-vocab"]));

/* The renderer builds the skeleton, so find its parts by class rather than by id. */
const find = (el, cls) => {
  for (const c of el.children) {
    if (c.className.split(" ").includes(cls)) return c;
    const hit = find(c, cls);
    if (hit) return hit;
  }
  return null;
};
const firstTag = (el, tag) => {
  for (const c of el.children) {
    if (c.tag === tag) return c;
    const hit = firstTag(c, tag);
    if (hit) return hit;
  }
  return null;
};

const nodes = {
  eyebrow: find(root, "eyebrow"), title: firstTag(root, "h1"), hail: find(root, "hail"),
  arrival: find(root, "arrival"), note: find(root, "note"),
  tree: find(root, "card"), chain: find(root, "chainbox"),
};

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
