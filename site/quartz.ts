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
    return name !== "02-zettelkasten" && name !== "tags" && name !== "tag index"
  },
  mapFn: (node: TrieNode) => {
    if (node.displayName === "01-MOCs") node.displayName = "Subjects"
    // "Spring Ecosystem - MOC" / "Java MOC" -> "Spring Ecosystem" / "Java"
    node.displayName = node.displayName.replace(/\s*(-\s*)?MOC$/i, "")
  },
})

const config = await loadQuartzConfig()

// ── SVG embeds ─────────────────────────────────────────────
// Obsidian-flavored-markdown turns ![[diagram.svg|650]] into
// <object data="diagram.svg">, but crawl-links only rewrites <img src>, so the
// bare filename 404s from any subfolder. Every SVG in the vault lives in
// Assets/ (emitted as /assets/), so point the object there.
config.plugins.transformers.push({
  name: "SvgEmbedPath",
  htmlPlugins: () => [
    () => (tree: Root) => {
      visit(tree, "element", (node: Element) => {
        const data = node.properties?.data
        if (node.tagName !== "object" || typeof data !== "string") return
        if (data.endsWith(".svg") && !data.includes("/")) {
          node.properties!.data = "/assets/" + data
        }
      })
    },
  ],
})

export default config
export const layout = await loadQuartzLayout()
