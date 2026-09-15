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

export default config
export const layout = await loadQuartzLayout()
