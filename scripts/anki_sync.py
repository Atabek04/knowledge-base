"""
Standalone Obsidian→Anki sync for this vault — no Obsidian needed.
(VAULT auto-resolves from this file's location: scripts/ -> vault root.)

Replicates the Obsidian_to_Anki plugin (v3.6.0) sync pipeline, batched the same
way the plugin does it (nested AnkiConnect `multi` actions → ~4 HTTP round-trips
for the whole vault):
  scan md files (skip unchanged via md5 hash cache shared with the plugin)
  → parse START/END blocks → markdown→HTML (validated byte-identical against
  the plugin's showdown output on the live collection) → batched add/update/
  move/tag via AnkiConnect → write <!--ID: ...--> back into the md
  → update the plugin's File Hashes in data.json so the in-Obsidian button
  stays consistent.

Improvements over the plugin:
  - Only writes to Anki when a field/tag/deck actually differs (no AnkiWeb churn).
  - Uploads <img src> media from the vault and rewrites src to the basename
    (the plugin passes raw <img> through untouched → broken images in Anki).
  - Auto-retries duplicate-first-field adds (e.g. Mushaf pages all titled "Худ").

Usage:
    Anki must be open (AnkiConnect addon 2055492159).
    python3 scripts/anki_sync.py                          # incremental, whole vault
    python3 scripts/anki_sync.py 07-Flashcards/Tafsir     # limit to paths
    python3 scripts/anki_sync.py --deck "Quran::Surah An-Naba"  # only files targeting deck (prefix match)
    python3 scripts/anki_sync.py --force                  # ignore hash cache
    python3 scripts/anki_sync.py --dry-run                # report, change nothing

Not supported (unused in this vault): DELETE blocks, STARTI inline notes,
FROZEN fields, $LaTeX$ conversion, ![[embeds]] (use raw <img src> instead).

Requires: pip install markdown
"""

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import quote

import markdown

VAULT = Path(__file__).resolve().parent.parent
DATA_JSON = VAULT / ".obsidian/plugins/obsidian-to-anki-plugin/data.json"
def _detect_anki_url():
    for url in ("http://localhost:8765", "http://172.25.144.1:8765"):
        try:
            urllib.request.urlopen(
                urllib.request.Request(url, json.dumps({"action":"version","version":6}).encode()), timeout=2)
            return url
        except Exception:
            continue
    return "http://localhost:8765"

ANKI_URL = _detect_anki_url()
SKIP_DIRS = {".obsidian", ".git", ".trash", ".claude", "node_modules", "scripts"}

BLOCK_RE = re.compile(r"^START\n(.*?)^END$", re.M | re.S)
ID_RE = re.compile(r"\n?<!--ID: (\d+)-->")
TARGET_DECK_RE = re.compile(r"^TARGET DECK:\s*(.+)$", re.M)
FILE_TAGS_RE = re.compile(r"^FILE TAGS:\s*(.+)$", re.M)
LIST_ITEM_RE = re.compile(r"^(\s*)([-*+]|\d+\.)\s")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]")
# plugin cloze regex: {text} / {1:text} / {c1:text} / {c1|text}; {{...}} excluded
CURLY_CLOZE_RE = re.compile(r"(?<!\{)\{(?:c?(\d+)[:|])?(?!\{)((?:[^\n{}]+?))\}(?!\})")
IMG_RE = re.compile(r'(<img\b[^>]*\bsrc=")([^"]+)(")')


# ── AnkiConnect ───────────────────────────────────────────────────────────────

def anki(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    try:
        resp = json.load(urllib.request.urlopen(
            urllib.request.Request(ANKI_URL, payload), timeout=120))
    except urllib.error.URLError:
        sys.exit("✗ Cannot reach AnkiConnect at localhost:8765 — is Anki open?")
    if resp.get("error"):
        raise RuntimeError(f"AnkiConnect {action}: {resp['error']}")
    return resp["result"]


def anki_multi(actions):
    """One HTTP round-trip for many actions. Returns list of per-action results;
    failed actions yield {'error': ...} instead of raising."""
    if not actions:
        return []
    payload = [{"action": a, "version": 6, "params": p} for a, p in actions]
    return anki("multi", actions=payload)


_fields_cache = {}

def model_fields(model):
    if model not in _fields_cache:
        _fields_cache[model] = anki("modelFieldNames", modelName=model)
    return _fields_cache[model]


_cloze_cache = {}

def model_is_cloze(model):
    """Ask Anki rather than guessing from the name: a cloze note type need not
    have 'cloze' in its title (e.g. 'English Grammar'), and one that does may
    not actually be cloze."""
    if model not in _cloze_cache:
        tpls = anki("modelTemplates", modelName=model)
        _cloze_cache[model] = any("{{cloze:" in side
                                  for t in tpls.values() for side in t.values())
    return _cloze_cache[model]


# ── Markdown → HTML (showdown-compatible, validated against live collection) ──

def _preprocess(text):
    # showdown starts a list even without a preceding blank line; python-markdown
    # needs the blank line — insert it so both produce identical HTML
    lines, out = text.split("\n"), []
    for line in lines:
        if LIST_ITEM_RE.match(line) and out and out[-1].strip() and not LIST_ITEM_RE.match(out[-1]):
            out.append("")
        out.append(line)
    return "\n".join(out)


def _ellipsis(html):
    # showdown replaces ... with … outside code spans
    parts = re.split(r"(<code>.*?</code>)", html, flags=re.S)
    return "".join(p if p.startswith("<code>") else p.replace("...", "…") for p in parts)


def _indent_blockquotes(html):
    # showdown indents blockquote inner lines by 2 spaces
    def fix(m):
        inner = "\n".join("  " + l if l.strip() else l for l in m.group(1).split("\n"))
        return f"<blockquote>\n{inner}\n</blockquote>"
    return re.sub(r"<blockquote>\n(.*?)\n</blockquote>", fix, html, flags=re.S)


def _wikilinks(text):
    # plugin renders [[target|alias]] as obsidian:// links (target without .md)
    return WIKILINK_RE.sub(
        lambda m: f'<a href="obsidian://open?vault={VAULT.name}&file={quote(m.group(1))}">{m.group(2) or m.group(1)}</a>',
        text)


def curly_to_cloze(text):
    # CurlyCloze (per flashcard-creator skill): {c1:x} / {c1|x} / {1:x} / {x}
    counter = [0]
    def sub(m):
        if m.group(1):
            n = m.group(1)
        else:
            counter[0] += 1
            n = str(counter[0])
        return "{{c%s::%s}}" % (n, m.group(2))
    return CURLY_CLOZE_RE.sub(sub, text)


def md_to_html(text, cloze=False):
    text = text.strip()
    if not text:
        return ""
    if cloze:
        text = curly_to_cloze(text)
    text = _wikilinks(text)
    html = markdown.markdown(_preprocess(text), extensions=["nl2br", "tables"])
    # showdown formats loose-list items as <li><p>…</p></li> on one line
    html = html.replace("<li>\n<p>", "<li><p>").replace("</p>\n</li>", "</p></li>")
    html = _indent_blockquotes(_ellipsis(html))
    # plugin strips the outer <p>…</p> pair only when BOTH ends have it
    if html.startswith("<p>") and html.endswith("</p>"):
        html = html[3:-4]
    return html


def localize_media(html, file_dir, media_queue):
    """Rewrite <img src="relative/path.png"> to basename + queue upload.
    Anki's media folder is flat — subpaths never render."""
    def fix(m):
        src = m.group(2)
        if src.startswith(("http://", "https://", "data:")):
            return m.group(0)
        for base in (file_dir, VAULT):
            p = (base / src).resolve()
            if p.is_file():
                media_queue[p.name] = str(p)
                return m.group(1) + p.name + m.group(3)
        return m.group(0)  # unresolvable — leave as-is
    return IMG_RE.sub(fix, html)


# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_block(body):
    """body = text between START and END. Returns (model, fields, tags, id|None)."""
    m = ID_RE.search(body)
    note_id = int(m.group(1)) if m else None
    body = ID_RE.sub("", body)
    lines = body.strip().split("\n")
    model = lines[0].strip()
    fnames = model_fields(model)
    fields = {f: "" for f in fnames}
    cur, tags = fnames[0], []  # content before any "Field:" header → first field
    for line in lines[1:]:
        fm = re.match(r"^([^:\n]+):\s?(.*)$", line)
        if fm and fm.group(1) in fields:
            cur = fm.group(1)
            fields[cur] = fm.group(2)
        elif line.startswith("Tags: "):
            tags = line[6:].split()
            cur = None
        elif cur is not None:
            fields[cur] += "\n" + line
    return model, fields, tags, note_id


def collect_file(path, media_queue, errors):
    """Parse one file into note dicts (no network)."""
    text = path.read_text(encoding="utf-8")
    deck_m = TARGET_DECK_RE.search(text)
    deck = deck_m.group(1).strip() if deck_m else "Default"
    ftags_m = FILE_TAGS_RE.search(text)
    file_tags = ftags_m.group(1).split() if ftags_m else []
    rel = str(path.relative_to(VAULT))

    notes = []
    for m in BLOCK_RE.finditer(text):
        try:
            model, fields, tags, note_id = parse_block(m.group(1))
        except Exception as e:
            errors.append(f"{rel}: parse failed — {e}")
            continue
        cloze = model_is_cloze(model)
        html = {f: localize_media(md_to_html(v, cloze=cloze), path.parent, media_queue)
                for f, v in fields.items()}
        notes.append({
            "path": path, "rel": rel, "block_start": m.start(),
            "model": model, "fields": html,
            "tags": sorted(set(tags + file_tags)),
            "deck": deck, "id": note_id,
        })
    return notes


# ── Sync ──────────────────────────────────────────────────────────────────────

def run_sync(notes, media_queue, dry_run, allow_dup, stats):
    adds = [n for n in notes if n["id"] is None]
    upds = [n for n in notes if n["id"] is not None]

    # round-trip 1: existence of every referenced id + info for diffing
    existing = set(anki("findNotes", query="")) if upds else set()
    live, dead = [], []
    for n in upds:
        (live if n["id"] in existing else dead).append(n)
    for n in dead:
        stats["errors"].append(f"{n['rel']}: ID {n['id']} not found in Anki (deleted?) — skipped")

    infos = anki("notesInfo", notes=[n["id"] for n in live]) if live else []

    # round-trip 2: current deck of live notes' cards (for deck moves)
    all_cards = [c for i in infos for c in i["cards"]]
    cards_info = anki("cardsInfo", cards=all_cards) if all_cards else []
    card_deck = {c["cardId"]: c["deckName"] for c in cards_info}

    # decide updates locally
    field_updates, tag_actions, deck_moves = [], [], []
    for n, cur in zip(live, infos):
        if any(cur["fields"].get(f, {}).get("value", "") != v
               for f, v in n["fields"].items() if f in cur["fields"]):
            field_updates.append(n)
        want, have = set(n["tags"]), set(cur["tags"])
        if want != have:
            tag_actions.append((n["id"], sorted(want - have), sorted(have - want)))
        wrong = [c for c in cur["cards"] if card_deck.get(c) not in (None, n["deck"])]
        if wrong:
            deck_moves.append((wrong, n["deck"]))
    stats["updated"] = len(field_updates)
    stats["moved"] = len(deck_moves)
    stats["retagged"] = len(tag_actions)
    stats["new"] = len(adds)

    if dry_run:
        for n in adds:
            print(f"  + would add [{n['model']}] → {n['deck']}: "
                  f"{next(iter(n['fields'].values()))[:60]!r}")
        for n in field_updates:
            print(f"  ~ would update fields of {n['id']} ({n['rel']})")
        for nid, add_t, del_t in tag_actions:
            print(f"  ~ would retag {nid}: +{add_t} -{del_t}")
        for cards, deck in deck_moves:
            print(f"  ~ would move {len(cards)} card(s) → {deck}")
        if media_queue:
            print(f"  ~ would upload {len(media_queue)} media file(s)")
        return

    # round-trip 3: all writes in one multi
    actions = []
    # base64 data upload — Anki itself can't read ~/Documents (macOS TCC)
    import base64
    actions += [("storeMediaFile", {"filename": fn,
                                    "data": base64.b64encode(Path(p).read_bytes()).decode()})
                for fn, p in media_queue.items()]
    n_media = len(media_queue)
    actions += [("createDeck", {"deck": n["deck"]}) for n in adds]
    add_offset = len(actions)
    actions += [("addNote", {"note": {
                    "deckName": n["deck"], "modelName": n["model"],
                    "fields": n["fields"], "tags": n["tags"],
                    "options": {"allowDuplicate": allow_dup, "duplicateScope": "deck"}}})
                for n in adds]
    actions += [("updateNoteFields", {"note": {"id": n["id"], "fields": n["fields"]}})
                for n in field_updates]
    for nid, add_t, del_t in tag_actions:
        if add_t:
            actions.append(("addTags", {"notes": [nid], "tags": " ".join(add_t)}))
        if del_t:
            actions.append(("removeTags", {"notes": [nid], "tags": " ".join(del_t)}))
    actions += [("changeDeck", {"cards": cards, "deck": deck})
                for cards, deck in deck_moves]

    results = anki_multi(actions)

    # collect add results; retry duplicate rejections individually
    for i, n in enumerate(adds):
        r = results[add_offset + i]
        err = r.get("error") if isinstance(r, dict) else None
        nid = r["result"] if isinstance(r, dict) else r
        if err and "duplicate" in err.lower() and not allow_dup:
            try:
                nid = anki("addNote", note={
                    "deckName": n["deck"], "modelName": n["model"],
                    "fields": n["fields"], "tags": n["tags"],
                    "options": {"allowDuplicate": True}})
                err = None
                print(f"  + added (dup first field allowed): {n['rel']}")
            except RuntimeError as e:
                err = str(e)
        if err or not nid:
            stats["errors"].append(f"{n['rel']}: add failed — {err or 'no id returned'}")
        else:
            n["new_id"] = nid
            stats["added"] += 1

    # surface any failed updates
    for j, r in enumerate(results[add_offset + len(adds):]):
        if isinstance(r, dict) and r.get("error"):
            stats["errors"].append(f"write action failed — {r['error']}")
    for j in range(n_media):
        r = results[j]
        if isinstance(r, dict) and r.get("error"):
            stats["errors"].append(f"media upload failed — {r['error']}")


def write_ids_back(notes):
    """Insert <!--ID: ...--> before END for newly added notes, grouped per file."""
    by_file = {}
    for n in notes:
        if n.get("new_id"):
            by_file.setdefault(n["path"], {})[n["block_start"]] = n["new_id"]
    for path, ids in by_file.items():
        text = path.read_text(encoding="utf-8")
        out, prev = [], 0
        for m in BLOCK_RE.finditer(text):
            if m.start() in ids:
                end_at = m.end() - len("END")
                out.append(text[prev:end_at])
                out.append(f"<!--ID: {ids[m.start()]}-->\n")
                prev = end_at
        out.append(text[prev:])
        path.write_text("".join(out), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Sync vault flashcards to Anki (no Obsidian)")
    ap.add_argument("paths", nargs="*", help="files/dirs to scan (default: whole vault)")
    ap.add_argument("--deck", help="only files whose TARGET DECK starts with this")
    ap.add_argument("--force", action="store_true", help="ignore hash cache")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-dup", action="store_true")
    ap.add_argument("--no-hash-write", action="store_true", help="don't update plugin data.json")
    ap.add_argument("--no-web-sync", action="store_true", help="skip AnkiWeb sync before/after")
    args = ap.parse_args()

    anki("version")  # connectivity check

    def web_sync(label):
        # AnkiWeb sync around the run prevents cross-machine deck-merge
        # duplicates ("Deck+" twins). Best-effort: warn, never abort.
        if args.no_web_sync or args.dry_run:
            return
        try:
            anki("sync")
            print(f"⇅ AnkiWeb sync ({label})")
        except RuntimeError as e:
            print(f"⚠ AnkiWeb sync failed ({label}): {e} — continuing")

    web_sync("before")

    data = json.loads(DATA_JSON.read_text(encoding="utf-8"))
    hashes = data.setdefault("File Hashes", {})

    roots = [VAULT / p for p in args.paths] if args.paths else [VAULT]
    files = []
    for root in roots:
        if root.is_file():
            files.append(root)
            continue
        for p in root.rglob("*.md"):
            if not SKIP_DIRS.intersection(p.relative_to(VAULT).parts):
                files.append(p)

    stats = {"new": 0, "added": 0, "updated": 0, "moved": 0, "retagged": 0,
             "errors": [], "files": 0}
    media_queue, all_notes, synced_files = {}, [], []

    for path in sorted(files):
        rel = str(path.relative_to(VAULT))
        content = path.read_text(encoding="utf-8")
        if not args.force and hashes.get(rel) == hashlib.md5(content.encode("utf-8")).hexdigest():
            continue
        if "START\n" not in content:
            if rel in hashes:  # changed but cardless — just refresh hash
                hashes[rel] = hashlib.md5(content.encode("utf-8")).hexdigest()
            continue
        if args.deck:
            m = TARGET_DECK_RE.search(content)
            if not m or not m.group(1).strip().startswith(args.deck):
                continue
        stats["files"] += 1
        print(f"⟳ {rel}")
        all_notes += collect_file(path, media_queue, stats["errors"])
        synced_files.append(path)

    run_sync(all_notes, media_queue, args.dry_run, args.allow_dup, stats)

    if not args.dry_run:
        write_ids_back(all_notes)
        if not args.no_hash_write:
            for path in synced_files:  # hash POST-write content (plugin semantics)
                rel = str(path.relative_to(VAULT))
                hashes[rel] = hashlib.md5(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
            # flashcard-creator skill mandates CurlyCloze: true — keep plugin aligned
            data["settings"]["Defaults"]["CurlyCloze"] = True
            DATA_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    if stats["added"] or stats["updated"] or stats["moved"] or stats["retagged"] or media_queue:
        web_sync("after")

    print(f"\n{'DRY RUN — ' if args.dry_run else ''}files: {stats['files']} · "
          f"new: {stats['new']} (added {stats['added']}) · updated: {stats['updated']} · "
          f"moved: {stats['moved']} · retagged: {stats['retagged']} · "
          f"media: {len(media_queue)} · errors: {len(stats['errors'])}")
    for e in stats["errors"]:
        print(f"  ✗ {e}")


if __name__ == "__main__":
    main()
