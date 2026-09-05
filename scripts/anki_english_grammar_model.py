import json, urllib.request

MODEL = "English Grammar"

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

/* ── The sentence — this is the whole test ────────────────────────────────── */
.sentence {
    font-size: 20px;
    color: #e8e2d5;
    text-align: left;
    margin: 16px 0 0;
    line-height: 1.75;
}
.sentence b, .sentence strong { color: #f0e9da; font-weight: 600; }
.sentence i, .sentence em     { color: #a8a195; }

/* The gap you must fill */
.cloze {
    color: #a8b4d0;
    font-weight: 600;
}
/* Unrevealed gap: a rule, so the sentence keeps its shape while you think */
.card.cloze-front .cloze { border-bottom: 2px solid rgba(168,180,208,0.45); }

/* ── Divider (soft fade hairline) ─────────────────────────────────────────── */
.divider {
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(232,226,213,0.18) 50%,
        transparent 100%
    );
    margin: 18px 0 0;
    border: none;
}

/* ── Explanation ──────────────────────────────────────────────────────────────
   Deliberately quieter and smaller than the sentence. You are not graded on
   recalling this. It is here to remind you why the gap took that form, and
   nothing more — if it competes visually with the sentence, you will start
   testing yourself on it and the card stops working.                          */
.why-lbl {
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: #6b665d;
    display: block;
    margin: 14px 0 6px;
}
.why {
    font-size: 14.5px;
    color: #a8a195;
    line-height: 1.65;
    text-align: left;
}
.why > *:first-child { margin-top: 0; }
.why > *:last-child  { margin-bottom: 0; }
.why p { margin: 6px 0; }
.why ul, .why ol { margin: 6px 0 0; padding-left: 18px; }
.why li { margin: 4px 0; }
.why li::marker { color: #6b665d; }
.why b, .why strong { color: #cbc3b4; font-weight: 600; }
.why i, .why em     { color: #a8a195; }
.why code {
    font-family: 'JetBrains Mono', 'SF Mono', monospace;
    font-size: 12.5px;
    background: rgba(232,226,213,0.06);
    padding: 1px 5px;
    border-radius: 3px;
    color: #a8b4d0;
}

/* ── Mobile tuning (single breakpoint) ────────────────────────────────────── */
@media screen and (max-width: 480px) {
    .card     { padding: 16px 10px; }
    .surface  { padding: 20px 16px 16px; border-radius: 12px; }
    .sentence { font-size: 18px; }
    .why      { font-size: 14px; }
}
"""

FRONT = """<div class="surface">
  <div class="tag">{{Subdeck}}</div>
  <div class="sentence">{{cloze:Text}}</div>
</div>"""

BACK = """<div class="surface">
  <div class="tag">{{Subdeck}}</div>
  <div class="sentence">{{cloze:Text}}</div>
  {{#Explanation}}
  <div class="divider"></div>
  <span class="why-lbl">Why</span>
  <div class="why">{{Explanation}}</div>
  {{/Explanation}}
</div>"""


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request("http://localhost:8765", data=payload)
    res = json.load(urllib.request.urlopen(req, timeout=20))
    if res.get("error"):
        raise SystemExit(f"{action} failed: {res['error']}")
    return res["result"]


if MODEL in call("modelNames"):
    call("updateModelStyling", model={"name": MODEL, "css": CSS})
    call("updateModelTemplates",
         model={"name": MODEL, "templates": {"Cloze": {"Front": FRONT, "Back": BACK}}})
    print("updated:", MODEL)
else:
    call("createModel",
         modelName=MODEL,
         inOrderFields=["Text", "Explanation"],
         css=CSS,
         isCloze=True,
         cardTemplates=[{"Name": "Cloze", "Front": FRONT, "Back": BACK}])
    print("created:", MODEL)

print("fields:", call("modelFieldNames", modelName=MODEL))
