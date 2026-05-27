TARGET DECK: Tech-KB::API Design::Pagination
Tags: api-design pagination
**Chapter:** API Pagination Strategies
**Related:** [[API Design - MOC]]

---

START
Coding Questions
How does offset pagination fetch a page, and what query does it use?
Back: It **skips** N rows and returns the next LIMIT rows.
```sql
SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 4980;
```
Client sends `?limit=20&offset=4980` to get page 250.
Tags: api-design pagination
END

START
Coding Questions
Why does offset pagination get slower the deeper you page?
Back: The DB can't jump straight to the offset row.
- It must **read and discard all skipped rows first** (4980 rows for `OFFSET 4980`)
- Cost grows **linearly with the offset**
- Page 1 is instant; page 5000 crawls through ~100k rows just to throw them away
Tags: api-design pagination
END

START
Coding Questions
What consistency problem can offset pagination cause when data changes between requests?
Back: The window **shifts** because offset assumes frozen data:
- A row inserted at the top → last item of page 1 reappears on page 2 (**duplicate**)
- A row deleted → an item is **skipped** entirely
Tags: api-design pagination
END

START
Coding Questions
How does keyset (seek) pagination fetch the next page, and what query does it use?
Back: It **filters on the last value seen** instead of counting an offset — "give me rows after this one".
```sql
SELECT * FROM products WHERE id > 4980 ORDER BY id LIMIT 20;
```
Client sends `?limit=20&since_id=4980`.
Tags: api-design pagination
END

START
Coding Questions
Why does keyset pagination stay fast at any depth?
Back: `WHERE id > 4980` lets the DB **seek directly into the index** and read 20 rows.
- No skipped rows to scan and discard
- Page 1 and page 5000 cost the same → **constant, predictable latency**
Tags: api-design pagination
END

START
Coding Questions
What does keyset pagination require of its sort column, and why a tiebreaker?
Back: Order by a column that is **unique and indexed** (PK, timestamp, or composite).
- For non-unique columns add a **tiebreaker**: `ORDER BY created_at, id`, compared as a pair
- Without it, rows duplicate or are skipped at page boundaries
Tags: api-design pagination
END

START
Coding Questions
What is the main tradeoff of keyset pagination?
Back: You lose **random access**.
- Only **next** (and previous with reversed comparison)
- No "jump to page 250", no cheap total page count
- Acceptable for feeds, infinite scroll, and exports
Tags: api-design pagination
END

START
Coding Questions
What is cursor pagination and how does it differ from keyset?
Back: **Cursor** pagination is keyset with the position wrapped in an **opaque token** the server hands back.
- Client just echoes `cursor=abc123` — never builds the key
- Same seek mechanism and performance underneath
- Difference is the **contract**: cursor hides the key; keyset exposes it (`since_id=40`)
Tags: api-design pagination
END

START
Coding Questions
Why expose an opaque cursor instead of the raw key?
Back: The opacity buys flexibility:
- Client treats it as a **black box** → can't build invalid positions
- Server can change the **internal sort strategy** without breaking clients
- Can pack extra state (direction, filters, version) into one string
This is why Stripe/GitHub/Twitter use cursors.
Tags: api-design pagination
END
