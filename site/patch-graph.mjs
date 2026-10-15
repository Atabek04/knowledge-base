// Adds zoom-to-fit to the expanded (global) graph of @quartz-community/graph.
// The plugin's `scale` option only resizes labels and the view always opens at
// zoom 1, so a page-local graph of a few nodes sits as a speck in the middle of
// a full-screen canvas. While the force layout is still settling, this keeps the
// camera fitted to the nodes' bounding box; the first wheel or pointer action
// hands control back to the user.
//
// Run from the Quartz checkout after `npx quartz plugin install`:
//   node <vault>/site/patch-graph.mjs
// The plugin ships minified, so the patch anchors on exact strings. If an update
// changes them the script fails loudly instead of building a silently broken graph.
import { readFileSync, writeFileSync, existsSync } from "node:fs"
import { join } from "node:path"

const dist = join(process.cwd(), "node_modules", "@quartz-community", "graph", "dist")
const files = [join(dist, "index.js"), join(dist, "components", "index.js")]
const marker = "/*kb-fit*/"

// R, O: canvas size · nu: simulation nodes · au: simulation · et: zoom behaviour
// a: d3 · Z: pixi app · Le: zoom enabled
const fit =
  `${marker}var __fitOn=Le&&!!Z.canvas.closest(".global-graph-container");` +
  `if(__fitOn){var __stop=function(){__fitOn=!1};` +
  `Z.canvas.addEventListener("wheel",__stop,{passive:!0});` +
  `Z.canvas.addEventListener("pointerdown",__stop)}` +
  `function __fit(){if(!__fitOn||au.alpha()<.02)return;` +
  `var x0=1/0,y0=1/0,x1=-1/0,y1=-1/0;` +
  `for(var n=0;n<nu.length;n++){var s=nu[n];if(s.x==null||s.y==null)continue;` +
  `x0=Math.min(x0,s.x),y0=Math.min(y0,s.y),x1=Math.max(x1,s.x),y1=Math.max(y1,s.y)}` +
  `if(x0===1/0)return;var pad=60,` +
  `k=Math.min((R-2*pad)/Math.max(x1-x0,1),(O-2*pad)/Math.max(y1-y0,1));` +
  `k=Math.max(.25,Math.min(k,3));` +
  `var cx=(x0+x1)/2+R/2,cy=(y0+y1)/2+O/2;` +
  `a.select(Z.canvas).call(et.transform,a.zoomIdentity.translate(R/2-cx*k,O/2-cy*k).scale(k))}`

const patches = [
  // declare the fitter right after the zoom behaviour is attached
  ["a.select(Z.canvas).call(et)}var se=!1;", `a.select(Z.canvas).call(et)}var se=!1;${fit}`],
  // run it once per animation frame, alongside the plugin's own redraw
  ["requestAnimationFrame(ce)}}return", "__fit&&__fit(),requestAnimationFrame(ce)}}return"],
]

for (const file of files) {
  if (!existsSync(file)) continue
  let src = readFileSync(file, "utf8")
  if (src.includes(marker)) {
    console.log(`graph fit: already patched ${file}`)
    continue
  }
  for (const [from, to] of patches) {
    if (src.split(from).length !== 2) {
      console.error(`graph fit: anchor not found exactly once in ${file}:\n  ${from}`)
      process.exit(1)
    }
    src = src.replace(from, to)
  }
  writeFileSync(file, src)
  console.log(`graph fit: patched ${file}`)
}
