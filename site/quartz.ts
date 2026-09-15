import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"
import { visit } from "unist-util-visit"
import type { Root, Element } from "hast"

// ── Explorer: subject tree ─────────────────────────────────
// The vault keeps 1,100+ atomic notes flat in 02-Zettelkasten, so that folder
// is hidden here: notes are reached through their MOC, backlinks, the graph,
// or search. The tree shows only 01-MOCs (renamed "Subjects") and Incidents.
//
// Two constraints shape this block:
//   - the explorer is installed from npm, so there is no generated
//     .quartz/plugins index to import; overrides are registered directly
//     under the plugin's source name;
//   - the callbacks are serialised to strings and re-evaluated in the
//     browser, so they must be self-contained (no outer variables).
type TrieNode = { displayName: string; isFolder: boolean }

componentRegistry.setOptionOverrides("@quartz-community/explorer", {
  order: ["filter", "sort", "map"],
  filterFn: (node: TrieNode) => {
    const name = node.displayName.toLowerCase()
    return (
      name !== "02-zettelkasten" && name !== "tags" && name !== "tag index" && name !== "readme"
    )
  },
  mapFn: (node: TrieNode) => {
    if (node.displayName === "01-MOCs") node.displayName = "Subjects"
    // "Spring Ecosystem - MOC" / "Java MOC" -> "Spring Ecosystem" / "Java"
    node.displayName = node.displayName.replace(/\s*(-\s*)?MOC$/i, "")
  },
})

const config = await loadQuartzConfig()

// ── Display math fences ────────────────────────────────────
// Obsidian accepts `$$\begin{array}` and `\end{array}$$` on the fence line;
// remark-math treats text after an opening `$$` as an ignored info string
// and does not recognise a closing `$$` with content before it, so the block
// swallows the rest of the note. Put every multi-line fence on its own line.
config.plugins.transformers.push({
  name: "DisplayMathFences",
  textTransform: (_ctx: unknown, src: string) => {
    const out: string[] = []
    let inCode = false
    let inMath = false
    for (const line of src.split("\n")) {
      if (/^\s*```/.test(line)) inCode = !inCode
      if (inCode) {
        out.push(line)
        continue
      }
      const trimmed = line.trim()
      if (!inMath) {
        // `$$content` (no closing fence on the same line) opens a block
        if (trimmed.startsWith("$$") && trimmed.length > 2 && !trimmed.slice(2).includes("$$")) {
          out.push("$$", trimmed.slice(2))
          inMath = true
          continue
        }
        if (trimmed === "$$") inMath = true
        out.push(line)
        continue
      }
      // inside a block: `content$$` closes it
      if (trimmed.endsWith("$$") && trimmed.length > 2) {
        out.push(trimmed.slice(0, -2), "$$")
        inMath = false
        continue
      }
      if (trimmed === "$$") inMath = false
      out.push(line)
    }
    return out.join("\n")
  },
})

// ── SVG embeds ─────────────────────────────────────────────
// Obsidian-flavored-markdown turns ![[diagram.svg|650]] into
// <object data="diagram.svg">, but crawl-links only rewrites <img src>, so the
// bare filename 404s from any subfolder. Every SVG in the vault lives in
// Assets/ (emitted as assets/), so point the object there with a path
// relative to the page, which survives the /kb subpath on GitHub Pages.
config.plugins.transformers.push({
  name: "SvgEmbedPath",
  htmlPlugins: () => [
    () => (tree: Root, file: { data: { slug?: string } }) => {
      const depth = (file.data.slug ?? "").split("/").length - 1
      const up = "../".repeat(depth)
      visit(tree, "element", (node: Element) => {
        const data = node.properties?.data
        if (node.tagName !== "object" || typeof data !== "string") return
        if (data.endsWith(".svg") && !data.includes("/")) {
          node.properties!.data = up + "assets/" + data
        }
      })
    },
  ],
})

// ── Scoped explorer ────────────────────────────────────────
// The full tree (14 categories, 60+ MOCs) is too tall to navigate. Once a
// page is open, the sidebar shows only the current category: its folder row
// as the root, its MOCs beneath, and an "All subjects" link above to go back
// up. Atomic notes take the category of the first MOC that links to them.
const scopedExplorer = `
(() => {
  const CLEAN = () => {
    document.querySelectorAll("[data-scoped]").forEach((e) => {
      e.style.display = ""
      e.classList.remove("scoped-root", "scoped-active")
      e.removeAttribute("data-scoped")
    })
    document.querySelector(".explorer-scope")?.remove()
  }
  const hide = (el) => { el.style.display = "none"; el.setAttribute("data-scoped", "1") }
  const mark = (el, cls) => { el.classList.add(cls); el.setAttribute("data-scoped", "1") }

  const scope = () => {
    const ex = document.querySelector(".explorer")
    const ul = ex && ex.querySelector(".explorer-ul")
    if (!ul) return
    CLEAN()

    const slug = document.body.dataset.slug || ""
    let folder = null, mocHref = null, m
    if ((m = slug.match(/^01-mocs\\/([^/]+)\\//))) folder = "01-mocs/" + m[1] + "/index"
    else if (slug.startsWith("incidents/")) folder = "incidents/index"
    else if (slug.startsWith("02-zettelkasten/")) {
      const a = document.querySelector('.backlinks a[href*="/01-mocs/"]')
      if (a && (m = a.getAttribute("href").match(/01-mocs\\/([^/]+)\\/.*$/))) {
        folder = "01-mocs/" + m[1] + "/index"
        mocHref = m[0] // path from 01-mocs/ on; the tree uses absolute hrefs
      }
    }
    if (!folder) return

    const target = ul.querySelector('.folder-container[data-folderpath="' + folder + '"]')
    if (!target) return
    const targetLi = target.closest("li")

    // hide every branch that is not on the path to the target
    const onPath = new Set()
    for (let el = targetLi; el && el !== ul; el = el.parentElement) if (el.tagName === "LI") onPath.add(el)
    ul.querySelectorAll("li").forEach((li) => {
      if (!onPath.has(li) && !targetLi.contains(li) && li.querySelector(".folder-container, a")) hide(li)
    })
    // the ancestor folder row (Subjects) gives way to the breadcrumb; its list loses its indent
    for (let el = targetLi.parentElement; el && el !== ul; el = el.parentElement) {
      if (el.tagName === "LI") {
        const row = el.querySelector(":scope > .folder-container")
        if (row) hide(row)
        const outer = el.querySelector(":scope > .folder-outer")
        if (outer) { outer.classList.add("open"); mark(outer, "scoped-root") }
      }
    }
    const outer = targetLi.querySelector(":scope > .folder-outer")
    if (outer) { outer.classList.add("open"); mark(outer, "scoped-open") }
    mark(target, "scoped-active")

    if (mocHref) {
      const link = [...ul.querySelectorAll("a")].find((l) => l.getAttribute("href").endsWith(mocHref))
      if (link) mark(link, "active")
    }

    const base = document.body.dataset.basepath || ""
    const crumb = document.createElement("div")
    crumb.className = "explorer-scope"
    crumb.innerHTML = '<a href="' + base + '/">\\u2190 All subjects</a>'
    ex.querySelector(".explorer-content").prepend(crumb)
  }

  const run = () => setTimeout(scope, 0)
  document.addEventListener("nav", run)
  run()
})()
`

config.plugins.transformers.push({
  name: "ScopedExplorer",
  externalResources: () => ({
    js: [{ loadTime: "afterDOMReady", contentType: "inline", script: scopedExplorer }],
  }),
})

export default config
export const layout = await loadQuartzLayout()
