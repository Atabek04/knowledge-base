import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"
import { visit } from "unist-util-visit"
import type { Root, Element } from "hast"
import fs from "fs"
import path from "path"
import { slugifyFilePath } from "./quartz/util/path"

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

// ── Home page: subject index ───────────────────────────────
// site/index.md carries a `<!-- subjects -->` marker; at build time it is
// replaced with every category and the MOCs inside it, read straight from
// 01-MOCs/ (plus Incidents/), so the home page never goes stale. Links carry
// data-no-popover so the home page stays quiet on hover.
const CATEGORY_ORDER: [string, string][] = [
  ["Languages", "Languages"],
  ["Backend", "Backend"],
  ["Frameworks", "Frameworks"],
  ["Architecture", "Architecture"],
  ["Infrastructure", "Infrastructure"],
  ["Networking", "Networking"],
  ["Security", "Security"],
  ["AI-ML", "AI and ML"],
  ["Math", "Math"],
  ["Engineering", "Engineering"],
  ["Interview-Prep", "Interview Prep"],
  ["Economics & Business", "Economics and Business"],
  ["Personal", "Personal"],
  ["IELTS", "IELTS"],
]
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;")
const mocName = (base: string) => base.replace(/\s*(-\s*)?MOC$/i, "")

config.plugins.transformers.push({
  name: "HomeSubjectIndex",
  textTransform: (ctx: any, src: string) => {
    if (!src.includes("<!-- subjects -->")) return src
    const root: string = ctx.argv.directory
    const mocRoot = path.join(root, "01-MOCs")
    const known = new Map(CATEGORY_ORDER)
    const dirs = fs.readdirSync(mocRoot, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name)
    const ordered = [
      ...CATEGORY_ORDER.map(([d]) => d).filter((d) => dirs.includes(d)),
      ...dirs.filter((d) => !known.has(d)).sort(),
    ]
    const sections: string[] = []
    for (const dir of ordered) {
      const label = known.get(dir) ?? dir
      const files = fs.readdirSync(path.join(mocRoot, dir)).filter((f) => f.endsWith(".md"))
      const entries = files
        .map((f) => ({ name: mocName(f.slice(0, -3)), slug: slugifyFilePath(`01-MOCs/${dir}/${f}` as any) }))
        .sort((a, b) => {
          const aMain = a.name.toLowerCase() === label.toLowerCase() || a.name.toLowerCase() === dir.toLowerCase()
          const bMain = b.name.toLowerCase() === label.toLowerCase() || b.name.toLowerCase() === dir.toLowerCase()
          if (aMain !== bMain) return aMain ? -1 : 1
          return a.name.localeCompare(b.name, undefined, { numeric: true })
        })
      const folderSlug = slugifyFilePath(`01-MOCs/${dir}/index.md` as any).replace(/\/index$/, "/")
      const items = entries
        .map((e) => `<li><a href="${e.slug}" data-no-popover="true">${esc(e.name)}</a></li>`)
        .join("")
      sections.push(
        `<section class="subject"><div class="subject-name"><a href="${folderSlug}" data-no-popover="true">${esc(label)}</a></div><ul class="subject-mocs">${items}</ul></section>`,
      )
    }
    // incidents: one entry, its five post-mortems beneath
    const incDir = path.join(root, "Incidents")
    if (fs.existsSync(incDir)) {
      const items = fs
        .readdirSync(incDir)
        .filter((f) => f.endsWith(".md") && f.toLowerCase() !== "readme.md")
        .sort()
        .reverse()
        .map((f) => `<li><a href="${slugifyFilePath(`Incidents/${f}` as any)}" data-no-popover="true">${esc(f.slice(0, -3))}</a></li>`)
        .join("")
      sections.push(
        `<section class="subject"><div class="subject-name"><a href="incidents/" data-no-popover="true">Incidents</a></div><ul class="subject-mocs">${items}</ul></section>`,
      )
    }
    return src.replace("<!-- subjects -->", `<div class="subject-index">${sections.join("")}</div>`)
  },
})

// ── Aliases ────────────────────────────────────────────────
// Frontmatter aliases are the names a reader knows a note by. They become a
// quiet "Also known as" line at the top of the body, which also puts them in
// the search index and in hover previews.
config.plugins.transformers.push({
  name: "AliasLine",
  htmlPlugins: () => [
    () => (tree: Root, file: { data: { frontmatter?: { aliases?: unknown } } }) => {
      let aliases = file.data.frontmatter?.aliases
      if (typeof aliases === "string") aliases = aliases.split(",").map((s) => s.trim())
      if (!Array.isArray(aliases)) return
      const names = aliases.map((a) => String(a).trim()).filter(Boolean)
      if (names.length === 0) return
      const children: Element["children"] = [
        { type: "element", tagName: "span", properties: { className: ["aka-label"] }, children: [{ type: "text", value: "Also known as" }] },
      ]
      names.forEach((n, i) => {
        if (i > 0) children.push({ type: "element", tagName: "span", properties: { className: ["aka-sep"] }, children: [{ type: "text", value: "·" }] })
        children.push({ type: "element", tagName: "span", properties: { className: ["aka-name"] }, children: [{ type: "text", value: n }] })
      })
      tree.children.unshift({ type: "element", tagName: "p", properties: { className: ["aka"] }, children })
    },
  ],
})

// ── MOC navigation index ───────────────────────────────────
// The sidebar shows each MOC's atomic notes in the order the MOC lists them,
// grouped by the MOC's sections. That order lives in the MOC body, not in
// folders, so an emitter reads every MOC's rendered tree and writes
// static/nav.json: { "<moc slug>": { title, sections: [{ name, items: [{ s, t, c }] }] } }
// (s = note slug, t = link text as written in the MOC, c = nested items).
type NavItem = { s: string; t: string; c?: NavItem[] }
type NavSection = { name: string; items: NavItem[] }

const textOf = (node: any): string => {
  if (!node) return ""
  if (node.type === "text") return node.value
  return (node.children ?? []).map(textOf).join("")
}
const resolveHref = (fromSlug: string, href: string): string | null => {
  if (!href || href.startsWith("#") || /^[a-z]+:/i.test(href)) return null
  const clean = href.split("#")[0].split("?")[0]
  if (!clean) return null
  const base = fromSlug.split("/").slice(0, -1)
  for (const seg of clean.split("/")) {
    if (seg === "..") base.pop()
    else if (seg !== "." && seg !== "") base.push(seg)
  }
  const slug = base.join("/")
  return slug.startsWith("02-zettelkasten/") || slug.startsWith("incidents/") || slug.startsWith("01-mocs/")
    ? slug
    : null
}
const firstLink = (li: any): any => {
  for (const child of li.children ?? []) {
    if (child.type !== "element") continue
    if (child.tagName === "ul" || child.tagName === "ol") continue
    if (child.tagName === "a" && String(child.properties?.className ?? "").includes("internal")) return child
    const inner = firstLink(child)
    if (inner) return inner
  }
  return null
}
const readItems = (list: any, fromSlug: string): NavItem[] => {
  const items: NavItem[] = []
  for (const li of list.children ?? []) {
    if (li.type !== "element" || li.tagName !== "li") continue
    const a = firstLink(li)
    const s = a ? resolveHref(fromSlug, String(a.properties?.href ?? "")) : null
    const nested = (li.children ?? []).find((c: any) => c.type === "element" && (c.tagName === "ul" || c.tagName === "ol"))
    const c = nested ? readItems(nested, fromSlug) : []
    if (s) items.push(c.length ? { s, t: textOf(a).trim(), c } : { s, t: textOf(a).trim() })
    else items.push(...c) // an unlinked bullet: lift its linked children
  }
  return items
}

config.plugins.emitters.push({
  name: "MocNavIndex",
  async emit(ctx: any, content: any[]) {
    const { write } = await import("./quartz/plugins/emitters/helpers")
    const nav: Record<string, { title: string; sections: NavSection[] }> = {}
    for (const [tree, file] of content) {
      const slug: string = file.data.slug ?? ""
      if (!/^01-mocs\/[^/]+\/(?!index$).+/.test(slug)) continue
      const sections: NavSection[] = []
      let current: NavSection = { name: "", items: [] }
      const push = () => {
        if (current.items.length && !/^(read more|related)$/i.test(current.name.trim())) sections.push(current)
      }
      const walk = (node: any) => {
        for (const child of node.children ?? []) {
          if (child.type !== "element") continue
          if (child.tagName === "h2" || child.tagName === "h3") {
            push()
            current = { name: textOf(child).trim(), items: [] }
          } else if (child.tagName === "ul" || child.tagName === "ol") {
            current.items.push(...readItems(child, slug))
          } else {
            walk(child)
          }
        }
      }
      walk(tree)
      push()
      const title = String(file.data.frontmatter?.title ?? "").replace(/\s*(-\s*)?MOC$/i, "")
      nav[slug] = { title, sections }
    }
    return [await write({ ctx, slug: "static/nav" as any, ext: ".json", content: JSON.stringify(nav) })]
  },
  getQuartzComponents: () => [],
} as any)

// ── Scoped explorer ────────────────────────────────────────
// The full tree (14 categories, 60+ MOCs) is too tall to navigate. Once a
// page is open, the sidebar shows only the current category: its name as the
// heading, its MOCs beneath, and under each MOC (expandable) the atomic notes
// in the MOC's own order, grouped by the MOC's sections, from static/nav.json.
// An atomic note belongs to the first MOC that lists it.
const scopedExplorer = `
(() => {
  let NAV = null, navLoading = null
  const loadNav = () => {
    if (NAV || navLoading) return
    const base = document.body.dataset.basepath || ""
    navLoading = fetch(base + "/static/nav.json").then((r) => r.json()).then((j) => { NAV = j; run() }).catch(() => { NAV = {} })
  }
  const mocOf = (slug) => {
    if (!NAV) return null
    const hit = (items) => items.some((i) => i.s === slug || (i.c && hit(i.c)))
    for (const m in NAV) if (NAV[m].sections.some((sec) => hit(sec.items))) return m
    return null
  }
  const openMocs = new Set()

  const CLEAN = () => {
    document.querySelectorAll("[data-scoped]").forEach((e) => {
      e.style.display = ""
      e.classList.remove("scoped-root", "scoped-open", "scoped-active", "moc-item", "open", "current")
      e.removeAttribute("data-scoped")
    })
    document.querySelectorAll(".moc-notes, .moc-toggle").forEach((e) => e.remove())
  }
  const hide = (el) => { el.style.display = "none"; el.setAttribute("data-scoped", "1") }
  const mark = (el, cls) => { el.classList.add(cls); el.setAttribute("data-scoped", "1") }
  const CHEV = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>'

  // MOC row -> chevron + nested notes
  const decorate = (li, mocSlug, base, pageSlug) => {
    const moc = NAV[mocSlug]
    if (!moc) return
    mark(li, "moc-item")
    const isCurrent = pageSlug.startsWith("01-mocs/") ? mocSlug === pageSlug : mocOf(pageSlug) === mocSlug
    if (isCurrent) openMocs.add(mocSlug)
    if (openMocs.has(mocSlug)) li.classList.add("open")

    const btn = document.createElement("button")
    btn.type = "button"
    btn.className = "moc-toggle"
    btn.setAttribute("aria-label", "Toggle notes")
    btn.innerHTML = CHEV
    btn.addEventListener("click", (e) => {
      e.preventDefault()
      li.classList.toggle("open")
      li.classList.contains("open") ? openMocs.add(mocSlug) : openMocs.delete(mocSlug)
    })
    li.prepend(btn)

    const render = (items) => {
      const ul = document.createElement("ul")
      for (const it of items) {
        const row = document.createElement("li")
        const a = document.createElement("a")
        a.href = base + "/" + it.s
        a.textContent = it.t
        a.className = "note-link" + (it.s === pageSlug ? " active" : "")
        row.appendChild(a)
        if (it.c && it.c.length) row.appendChild(render(it.c))
        ul.appendChild(row)
      }
      return ul
    }
    const box = document.createElement("div")
    box.className = "moc-notes"
    for (const sec of moc.sections) {
      if (sec.name) {
        const h = document.createElement("div")
        h.className = "moc-section"
        h.textContent = sec.name
        box.appendChild(h)
      }
      box.appendChild(render(sec.items))
    }
    li.appendChild(box)
  }

  // returns true once the tree exists and has been handled
  const scope = () => {
    const ex = document.querySelector(".explorer")
    const ul = ex && ex.querySelector(".explorer-ul")
    if (!ex) return true
    if (!ul || !ul.querySelector("li .folder-container")) return false // tree not rendered yet
    if (!NAV) { loadNav(); return false }
    CLEAN()

    const base = document.body.dataset.basepath || ""
    const slug = document.body.dataset.slug || ""
    let folder = null, m
    const owner = slug.startsWith("02-zettelkasten/") ? mocOf(slug) : null
    if ((m = (owner || slug).match(/^01-mocs\\/([^/]+)\\//))) folder = "01-mocs/" + m[1] + "/index"
    else if (slug.startsWith("incidents/")) folder = "incidents/index"
    else if (slug.startsWith("02-zettelkasten/")) {
      // note listed in no MOC: fall back to the first MOC backlink
      const a = document.querySelector('.backlinks a[href*="/01-mocs/"]')
      if (a && (m = a.getAttribute("href").match(/01-mocs\\/([^/]+)\\//))) folder = "01-mocs/" + m[1] + "/index"
    }
    if (!folder) return true

    const target = ul.querySelector('.folder-container[data-folderpath="' + folder + '"]')
    if (!target) return true
    const targetLi = target.closest("li")

    // hide every branch that is not on the path to the target
    const onPath = new Set()
    for (let el = targetLi; el && el !== ul; el = el.parentElement) if (el.tagName === "LI") onPath.add(el)
    ul.querySelectorAll("li").forEach((li) => {
      if (!onPath.has(li) && !targetLi.contains(li) && li.querySelector(".folder-container, a")) hide(li)
    })
    // the ancestor folder row (Subjects) is hidden; its list loses its indent
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

    // MOC rows under the category: chevron + ordered notes
    targetLi.querySelectorAll(":scope > .folder-outer > ul > li > a").forEach((a) => {
      const href = a.getAttribute("href") || ""
      const mocSlug = href.startsWith(base + "/") ? href.slice(base.length + 1) : href.replace(/^\\//, "")
      if (NAV[mocSlug]) decorate(a.parentElement, mocSlug, base, slug)
    })
    return true
  }

  // ── collapsible sidebars ──
  // A panel icon in each sidebar's top row hides it; a small fixed box with a
  // chevron in the page corner brings it back. State lives in localStorage
  // and on <html data-left / data-right>.
  const KEY = "kb-sidebars"
  const state = () => { try { return JSON.parse(localStorage.getItem(KEY) || "{}") } catch { return {} } }
  const apply = () => {
    const s = state()
    document.documentElement.dataset.left = s.left === "closed" ? "closed" : "open"
    document.documentElement.dataset.right = s.right === "closed" ? "closed" : "open"
  }
  const toggle = (side) => {
    const s = state()
    s[side] = s[side] === "closed" ? "open" : "closed"
    try { localStorage.setItem(KEY, JSON.stringify(s)) } catch {}
    apply()
  }
  const SVG = (d) => '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' + d + '</svg>'
  const PANEL_LEFT = SVG('<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M9 3v18"/><path d="m16 15-3-3 3-3"/>')
  const PANEL_RIGHT = SVG('<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M15 3v18"/><path d="m8 9 3 3-3 3"/>')
  const CHEV_RIGHT = SVG('<path d="m9 6 6 6-6 6"/>')
  const CHEV_LEFT = SVG('<path d="m15 6-6 6 6 6"/>')
  const button = (cls, label, icon, onClick) => {
    const b = document.createElement("button")
    b.type = "button"
    b.className = cls
    b.setAttribute("aria-label", label)
    b.innerHTML = icon
    b.addEventListener("click", onClick)
    return b
  }
  const ensureToggles = () => {
    // hide buttons: left one joins the title row, right one sits in the column's top corner
    const left = document.querySelector(".sidebar.left")
    const leftRow = left && left.querySelector(":scope > .flex-component")
    if (leftRow && !leftRow.querySelector(".sidebar-toggle")) {
      leftRow.appendChild(button("sidebar-toggle", "Hide sidebar", PANEL_LEFT, () => toggle("left")))
    }
    const right = document.querySelector(".sidebar.right")
    if (right && !right.querySelector(".sidebar-toggle")) {
      right.prepend(button("sidebar-toggle", "Hide side panel", PANEL_RIGHT, () => toggle("right")))
    }
    // reveal boxes: fixed in the page corners, visible only while that side is closed
    if (!document.querySelector(".sidebar-reveal.left")) {
      document.body.appendChild(button("sidebar-reveal left", "Show sidebar", CHEV_RIGHT, () => toggle("left")))
    }
    if (!document.querySelector(".sidebar-reveal.right")) {
      document.body.appendChild(button("sidebar-reveal right", "Show side panel", CHEV_LEFT, () => toggle("right")))
    }
  }
  apply()
  document.addEventListener("nav", ensureToggles)
  ensureToggles()

  // ── keyboard shortcuts ──
  //   Ctrl/Cmd + \          toggle sidebar
  //   Ctrl/Cmd + Shift + \  toggle side panel
  //   Ctrl/Cmd + K          search (Quartz's own binding; its "/" binding is swallowed)
  //   ?                     this list      Esc  close
  const isMac = /Mac|iPhone|iPad/.test(navigator.platform)
  const MOD = isMac ? "\\u2318" : "Ctrl"
  const SHORTCUTS = [
    [[MOD, "\\\\"], "Toggle sidebar"],
    [[MOD, "\\u21e7", "\\\\"], "Toggle side panel"],
    [[MOD, "K"], "Search"],
    [["?"], "Keyboard shortcuts"],
    [["Esc"], "Close"],
  ]
  const typing = (e) => {
    const t = e.target
    return t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.isContentEditable)
  }
  const modal = () => {
    let m = document.querySelector(".kbd-modal")
    if (m) return m
    m = document.createElement("div")
    m.className = "kbd-modal"
    m.setAttribute("role", "dialog")
    m.setAttribute("aria-label", "Keyboard shortcuts")
    m.innerHTML =
      '<div class="kbd-card"><h2>Keyboard shortcuts</h2><dl>' +
      SHORTCUTS.map(([keys, label]) =>
        "<dt>" + keys.map((k) => "<kbd>" + k + "</kbd>").join("<span>+</span>") + "</dt><dd>" + label + "</dd>").join("") +
      "</dl></div>"
    m.addEventListener("click", (e) => { if (e.target === m) closeModal() })
    document.body.appendChild(m)
    return m
  }
  const openModal = () => { modal().classList.add("open") }
  const closeModal = () => { const m = document.querySelector(".kbd-modal"); if (m) m.classList.remove("open") }
  const modalOpen = () => { const m = document.querySelector(".kbd-modal"); return !!m && m.classList.contains("open") }

  document.addEventListener("keydown", (e) => {
    const mod = e.ctrlKey || e.metaKey
    if (mod && e.code === "Backslash") {
      e.preventDefault()
      toggle(e.shiftKey ? "right" : "left")
      return
    }
    // physical K, so it works on any keyboard layout (Quartz matches e.key === "k", Latin only)
    if (mod && !e.shiftKey && e.code === "KeyK") {
      e.preventDefault()
      e.stopImmediatePropagation()
      const box = document.querySelector(".search-container")
      if (box && box.classList.contains("active")) {
        document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true }))
      } else {
        const btn = document.querySelector(".search-button")
        if (btn) btn.click()
      }
      return
    }
    if (e.key === "Escape" && modalOpen()) { e.preventDefault(); closeModal(); return }
    if (typing(e) || mod || e.altKey) return
    if (e.key === "?") { e.preventDefault(); modalOpen() ? closeModal() : openModal(); return }
    if (e.key === "/") e.stopImmediatePropagation() // search opens with Ctrl/Cmd+K only
  }, true)

  // footer link: the discoverable route to the list
  const ensureFooterLink = () => {
    const ul = document.querySelector("footer ul")
    if (!ul || ul.querySelector(".kbd-link")) return
    const li = document.createElement("li")
    // a button, not an <a href="#">: the SPA router would navigate on the anchor
    li.appendChild(button("kbd-link", "Keyboard shortcuts", SVG('<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M8 14h8"/>') + "<span>Shortcuts</span>", openModal))
    ul.appendChild(li)
  }
  document.addEventListener("nav", ensureFooterLink)
  ensureFooterLink()

  // the explorer fills its tree after fetching the content index; poll until it is there
  let attempt = 0
  const tick = () => {
    if (scope() || ++attempt > 50) return
    setTimeout(tick, 100)
  }
  const run = () => {
    attempt = 0
    setTimeout(tick, 0)
  }
  document.addEventListener("nav", run)
  run()
})()
`

// Light by default: Quartz's darkmode plugin follows the OS preference on the
// first visit; here the first visit is light, and the toggle still persists
// whatever the reader picks afterwards.
const lightByDefault = `
(() => {
  try {
    if (!localStorage.getItem("theme")) localStorage.setItem("theme", "light")
    document.documentElement.setAttribute("saved-theme", localStorage.getItem("theme"))
  } catch {}
})()
`

config.plugins.transformers.push({
  name: "ScopedExplorer",
  externalResources: () => ({
    js: [
      { loadTime: "beforeDOMReady", contentType: "inline", script: lightByDefault },
      { loadTime: "afterDOMReady", contentType: "inline", script: scopedExplorer },
    ],
  }),
})

export default config
export const layout = await loadQuartzLayout()
