# Visual / Diagram Cards

Some knowledge is spatial, not verbal — a system-design topology, a tree rotation, a
B-tree split, an ML loss curve, a request/response sequence. **Dual coding** (Paivio): a
memory encoded both verbally *and* visually is recalled faster and more reliably than one
encoded as text alone. Use a visual when the concept *is* a shape, a layout, or a flow.

This is a lightweight convention — no asset ledger, no enforcement script. Just three
patterns and one rule.

## The one rule: the image is the cue, never the answer

A card that asks "What does a red-black tree look like?" with the picture on the back tests
**recognition** — you nod at the image and feel you knew it. That's the weakest form of
review. Recall means *producing* something. So the image goes on the **front** as the cue,
or alongside a text answer as support — never alone on the back.

## Three valid patterns

**1. Forward-ID card** — image in the question, text answer.
> Front: `<img>` of a traversal pattern → "Which traversal order does this represent?"
> Back: "In-order (left → node → right)."

Tests identification from a visual cue. For symmetric concepts (diagram ↔ name), also make
the reverse card (name → "sketch / describe the diagram").

**2. Diagram-anchored text card** — normal Q&A, with a diagram embedded under the answer
for dual coding.
> Front: "What are the three nodes in a read-replica topology and how does write traffic flow?"
> Back: text answer **+** a small mermaid diagram of primary → replicas.

The question is still a real text-recall question; the diagram strengthens the trace.

**3. Image-in-Notes** — attach a diagram to an *existing* text card's `Notes`/`Back`
field. No new card created; it just enriches the visual memory on review.

## Asset convention (lightweight)

- Store images under `05-Flashcards/{topic}/_assets/`.
- Prefer **Mermaid** for diagrams you generate — keep both the `.mmd` source and the
  rendered `.png` so the diagram is editable later.
- Reference with HTML so you can control size: `<img src="_assets/btree-split.png" alt="B-tree node split" width="500">`. Keep `width` ≤ ~800.
- Always set `alt` text — it doubles as a fallback if the image is missing.
- For an external image, drop its source URL in the card's `Notes` field so provenance
  isn't lost. (No formal ledger — just don't orphan the source.)

The Obsidian→Anki plugin copies referenced images into Anki's media folder on sync, so
local relative paths work once the file is in the vault.
