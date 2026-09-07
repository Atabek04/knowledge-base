import json, urllib.request

MODEL = "English Card"
NEW_FIELDS = ["Example", "Collocations", "Synonyms", "Forms", "Pattern"]

CSS = r"""
* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

.card {
    font-family: -apple-system, 'SF Pro Display', 'Inter', 'Helvetica Neue', Arial, sans-serif;
    background: #1a1815;
    color: #e8e2d5;
    padding: 24px 16px;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ── Card surface ─────────────────────────────────────────────────────────── */
.surface {
    max-width: 640px;
    margin: 0 auto;
    background: #252220;
    border: 1px solid rgba(232,226,213,0.10);
    border-radius: 14px;
    padding: 24px 22px 20px;
    position: relative;
}

/* ── Deck tag (top-right marginalia label) ────────────────────────────────── */
.tag {
    position: absolute;
    top: 14px;
    right: 16px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    opacity: 0.55;
    color: #a8b4d0;
}

/* ── Prompt (centred, both faces) ─────────────────────────────────────────── */
.title {
    font-size: 21px;
    font-weight: 600;
    color: #e8e2d5;
    text-align: center;
    margin: 14px 0 0;
    line-height: 1.4;
}
.recap {
    font-size: 18px;
    font-weight: 600;
    color: #e8e2d5;
    text-align: center;
    margin: 14px 0 14px;
    line-height: 1.45;
}

/* ── Divider (soft fade hairline) ─────────────────────────────────────────── */
.divider {
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(232,226,213,0.18) 50%,
        transparent 100%
    );
    margin: 16px 0;
    border: none;
}

/* Answer body — left-aligned: English prose and bullets are unreadable centred.
   No inset box: the surface is already a card, and nesting one inside it costs
   ~40px of line length on a phone and adds nothing the divider does not. */
.answer {
    font-size: 15.5px;
    color: #cbc3b4;
    line-height: 1.7;
    text-align: left;
    direction: ltr;
}
.answer > *:first-child { margin-top: 0; }
.answer > *:last-child  { margin-bottom: 0; }
.answer p { margin: 8px 0; }

/* The lead sentence carries the claim — lift it out of the body */
.answer > p:first-child,
.answer > div:first-child {
    color: #e8e2d5;
    font-size: 16.5px;
}

.answer ul, .answer ol { margin: 10px 0 0; padding-left: 20px; }
.answer li { margin: 6px 0; }
.answer li::marker { color: #a8b4d0; }

.answer b, .answer strong { color: #f0e9da; font-weight: 600; }
.answer i, .answer em     { color: #a8a195; }

.answer code {
    font-family: 'JetBrains Mono', 'SF Mono', monospace;
    font-size: 12.5px;
    background: rgba(232,226,213,0.06);
    padding: 1px 5px;
    border-radius: 3px;
    color: #a8b4d0;
}
.answer a { color: #a8b4d0; text-decoration: none; border-bottom: 1px solid rgba(168,180,208,0.35); }

.answer blockquote {
    margin: 10px 0;
    padding: 2px 0 2px 14px;
    border-left: 2px solid rgba(232,226,213,0.18);
    color: #a8a195;
    font-style: italic;
}

/* ── Example sentence — a rule, not a box: it is quoted material ──────────── */
.example {
    margin: 14px 0 2px;
    padding: 2px 0 2px 14px;
    border-left: 2px solid #a8b4d0;
    font-size: 15px;
    font-style: italic;
    color: #cbc3b4;
    line-height: 1.65;
    text-align: left;
}
.example b, .example strong { color: #f0e9da; font-style: normal; font-weight: 600; }

/* ── Optional detail rows (only render when the field is filled) ──────────── */
/* No margin here: an empty .meta must collapse to nothing on a bare Q&A card.
   The spacing lives on the first rendered row instead. */
.meta { margin: 0; }
.row {
    padding: 11px 0;
    border-top: 1px solid rgba(232,226,213,0.08);
    text-align: left;
}
.row:first-child { border-top: none; margin-top: 14px; }
.row-lbl {
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: #6b665d;
    display: block;
    margin-bottom: 5px;
}
.row-val {
    font-size: 15px;
    color: #cbc3b4;
    line-height: 1.65;
}
.row-val b, .row-val strong { color: #f0e9da; font-weight: 600; }
.row-val i, .row-val em     { color: #a8a195; }
.row-val code {
    font-family: 'JetBrains Mono', 'SF Mono', monospace;
    font-size: 12.5px;
    background: rgba(232,226,213,0.06);
    padding: 1px 5px;
    border-radius: 3px;
    color: #a8b4d0;
}
.row-val ul { margin: 4px 0 0; padding-left: 18px; }
.row-val li { margin: 4px 0; }
.row-val li::marker { color: #6b665d; }

/* Forms and Pattern are structural, not prose — set them apart */
.row-forms .row-val,
.row-pattern .row-val {
    font-family: 'JetBrains Mono', 'SF Mono', monospace;
    font-size: 13.5px;
    color: #d6cdbc;
    line-height: 1.8;
    /* One pattern per line without needing <br> in the field */
    white-space: pre-line;
}

/* ── Mobile tuning (single breakpoint) ────────────────────────────────────── */
@media screen and (max-width: 480px) {
    .card    { padding: 16px 10px; }
    .surface { padding: 20px 16px 16px; border-radius: 12px; }
    .title   { font-size: 18.5px; }
    .recap   { font-size: 16.5px; }
    .answer  { font-size: 15px; }
    .answer > p:first-child, .answer > div:first-child { font-size: 16px; }
    .example, .row-val { font-size: 14.5px; }
    .row-forms .row-val, .row-pattern .row-val { font-size: 13px; }
}
"""

FRONT = """<div class="surface">
  <div class="tag">{{Subdeck}}</div>
  <div class="title">{{Front}}</div>
</div>"""

BACK = """<div class="surface">
  <div class="tag">{{Subdeck}}</div>
  <div class="recap">{{Front}}</div>
  <div class="divider"></div>

  <div class="answer">{{Back}}</div>
  {{#Example}}<div class="example">{{Example}}</div>{{/Example}}

  <div class="meta">
    {{#Forms}}
    <div class="row row-forms">
      <span class="row-lbl">Forms</span>
      <div class="row-val">{{Forms}}</div>
    </div>
    {{/Forms}}

    {{#Pattern}}
    <div class="row row-pattern">
      <span class="row-lbl">Pattern</span>
      <div class="row-val">{{Pattern}}</div>
    </div>
    {{/Pattern}}

    {{#Collocations}}
    <div class="row">
      <span class="row-lbl">Collocations</span>
      <div class="row-val">{{Collocations}}</div>
    </div>
    {{/Collocations}}

    {{#Synonyms}}
    <div class="row">
      <span class="row-lbl">Synonyms &mdash; and how they differ</span>
      <div class="row-val">{{Synonyms}}</div>
    </div>
    {{/Synonyms}}
  </div>
</div>"""


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request("http://localhost:8765", data=payload)
    res = json.load(urllib.request.urlopen(req, timeout=20))
    if res.get("error"):
        raise SystemExit(f"{action} failed: {res['error']}")
    return res["result"]


existing = call("modelFieldNames", modelName=MODEL)
for f in NEW_FIELDS:
    if f not in existing:
        call("modelFieldAdd", modelName=MODEL, fieldName=f)
        print("+ field:", f)

call("updateModelStyling", model={"name": MODEL, "css": CSS})
call("updateModelTemplates",
     model={"name": MODEL, "templates": {"Card 1": {"Front": FRONT, "Back": BACK}}})

print("fields:", call("modelFieldNames", modelName=MODEL))
