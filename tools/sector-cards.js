/*
  Sector page → event cards, without leaving the page.

  A beacon box is a <details>; opening one loads that event's card and renders it
  underneath. Three things arrive on demand, and nothing before the first open:

    cards/runtime/card.js    the renderer + vocabulary — once per page
    cards/runtime/card.css   the card's styling — once per open box, into its shadow root
    cards/data/<slug>.js     one FTLCard.define() call — once per event

  All three come in through a <script>/<link> tag rather than fetch(), because that is
  the only cross-directory read a file:// page is allowed (tools/SECTOR-PAGE.md §6.1).
  Verified in Chrome and in Firefox with stock prefs; fetch, XHR and dynamic import are
  all blocked there, script tags are not.

  Each card renders into its own shadow root. The two stylesheets collide on five class
  names and both define the palette variables, so isolation is not a nicety — without it
  a card would repaint the page around it.

  build-sector.py inlines this file and a <script type="application/json"> config block
  holding the paths and every word this file can show.
*/
(function () {
  "use strict";

  const config = document.getElementById("sector-card-loader");
  if (!config) return;
  const CFG = JSON.parse(config.textContent);

  const pending = new Map();

  function load(src) {
    if (pending.has(src)) return pending.get(src);
    const done = new Promise((resolve, reject) => {
      const tag = document.createElement("script");
      tag.src = src;
      tag.onload = () => resolve();
      tag.onerror = () => reject(new Error(src));
      document.head.appendChild(tag);
    });
    pending.set(src, done);
    return done;
  }

  /* The card's palette lives on :host, so the page's explicit theme — an artifact host
     stamps data-theme on the document — has to be handed across the shadow boundary.
     :host-context() would do it without this, but Firefox does not implement it. */
  function theme(host) {
    const mode = document.documentElement.getAttribute("data-theme");
    if (mode) host.setAttribute("data-theme", mode);
  }

  function stylesheet(root) {
    return new Promise(resolve => {
      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = CFG.css;
      /* Resolve either way: a missing stylesheet should still show the card. */
      link.onload = resolve;
      link.onerror = resolve;
      root.appendChild(link);
    });
  }

  async function fill(box) {
    const slug = box.getAttribute("data-card");
    const panel = box.querySelector(".cardpanel");
    if (!slug || !panel || box.getAttribute("data-state")) return;
    box.setAttribute("data-state", "loading");
    panel.textContent = CFG.strings.loading;
    try {
      await load(CFG.runtime);
      await load(CFG.data.replace("{slug}", slug));
      const data = window.FTLCard.get(slug);
      if (!data) throw new Error("no payload for " + slug);
      panel.textContent = "";
      theme(panel);
      const shadow = panel.attachShadow({ mode: "open" });
      await stylesheet(shadow);
      const root = document.createElement("div");
      root.className = "wrap";
      shadow.appendChild(root);
      window.FTLCard.render(root, data);
      box.setAttribute("data-state", "ready");
    } catch (err) {
      panel.textContent = CFG.strings.failed;
      /* Cleared, not left as "loading": closing and reopening should try again. */
      box.removeAttribute("data-state");
    }
  }

  /* toggle does not bubble, so listen in the capture phase. */
  document.addEventListener("toggle", event => {
    const box = event.target;
    if (box instanceof HTMLDetailsElement && box.classList.contains("evbox") && box.open) {
      fill(box);
    }
  }, true);

  /* The corner link opens the standalone card page; without this it would also toggle
     the box on the way out. */
  document.addEventListener("click", event => {
    const link = event.target.closest && event.target.closest("a.cardlink");
    if (link) event.stopPropagation();
  }, true);
})();
