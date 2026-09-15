# Public wiki (Quartz)

The vault is published as a static site with [Quartz 5](https://quartz.jzhao.xyz) at `https://atabek04.github.io/kb` (the path is the repo name).

| File | Role |
|---|---|
| `quartz.config.yaml` | site config: title, theme, fonts, plugins, layout, `ignorePatterns` (what never leaves the vault) |
| `quartz.ts` | code-only overrides: explorer tree (hides `02-Zettelkasten`, renames `01-MOCs` to Subjects) and the SVG embed path fix |
| `custom.scss` | highlight palette, definition/theorem callouts, landing-page cards |
| `index.md` | landing page; copied to the vault root only during a build |

Published: `01-MOCs`, `02-Zettelkasten`, `Incidents`, `Assets` (minus `Assets/Books`). Everything else is ignored.

- Deploy: `.github/workflows/publish.yml` builds on every push to `main` and deploys `public/` to GitHub Pages from this repo (Settings, Pages, Source: GitHub Actions).
- Preview: `.\scripts\site-preview.ps1` (Node 22+), then open `http://localhost:8080`.
- Frontmatter must be valid YAML: quote aliases that start with `@`, `!`, `*`, `&` or contain `: `. A build fails on the first bad file.
