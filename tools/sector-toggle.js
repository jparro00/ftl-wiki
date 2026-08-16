/*
  A box that is its own toggle.

  The blue-options block is a <details> whose whole body is clickable, not just its
  <summary>: a summary-only toggle can be opened from the visible rows but never closed
  from the rows it just revealed, which reads as a broken control.

  Two clicks are left alone — one that lands on the summary (the browser toggles that
  one itself, and handling it here would toggle twice), and one that ends a text
  selection, so selecting a row's text does not collapse the box under the cursor.

  Holds no English and no paths, like tools/sector-cards.js; build-sector.py inlines it.
*/
(function () {
  "use strict";

  document.querySelectorAll(".gtoggle").forEach(function (box) {
    box.addEventListener("click", function (event) {
      if (event.target.closest("summary")) return;
      if (String(window.getSelection())) return;
      box.open = !box.open;
    });
  });
})();
