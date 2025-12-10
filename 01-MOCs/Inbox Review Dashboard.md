---
created: 2025-12-08
tags: [moc, inbox, system]
---

# Inbox Review Dashboard

**Daily checkpoint for processing captured knowledge.**

Check this dashboard during your evening 15-minute inbox processing session.

---

## 🔴 URGENT
### Overdue Items (>7 days)

These items MUST be processed today. They've exceeded the 7-day deadline.

```dataview
TABLE WITHOUT ID
  file.link as "📝 Item",
  created as "Created",
  choice(date(today) - date(created) = dur(1 day), "1 day ago", string(round((date(today) - date(created)).days)) + " days ago") as "⏰ Age"
FROM "00-Inbox"
WHERE created <= date(today) - dur(7 days)
SORT created ASC
```

**Action:** Process immediately → move to appropriate folder (Zettelkasten/Reference/Projects) or discard.

---

## 🟡 WARNING
### Approaching Deadline (4-7 days)

These items are aging. Schedule processing soon.

```dataview
TABLE WITHOUT ID
  file.link as "📝 Item",
  created as "Created",
  choice(date(today) - date(created) = dur(1 day), "1 day ago", string(round((date(today) - date(created)).days)) + " days ago") as "⏰ Age"
FROM "00-Inbox"
WHERE created > date(today) - dur(7 days)
  AND created <= date(today) - dur(4 days)
SORT created ASC
```

**Action:** Review and prioritize for next 1-2 days.

---

## 🟢 FRESH
### Recent Captures (<4 days)

Newly captured items. Still within healthy processing window.

```dataview
TABLE WITHOUT ID
  file.link as "📝 Item",
  created as "Created",
  choice(date(today) - date(created) = dur(0 day), "Today", choice(date(today) - date(created) = dur(1 day), "Yesterday", string(round((date(today) - date(created)).days)) + " days ago")) as "⏰ Age"
FROM "00-Inbox"
WHERE created > date(today) - dur(4 days)
SORT created DESC
```

**Action:** No immediate action needed, but keep on radar.

---

## 📊 Inbox Statistics

```dataview
TABLE WITHOUT ID
  choice(length(rows) = 0, "✅ Inbox is empty!",
    choice(length(rows) = 1, "1 item in inbox",
      string(length(rows)) + " items in inbox")) as "Total Items"
FROM "00-Inbox"
GROUP BY true
```

```dataview
TABLE WITHOUT ID
  choice(length(rows) = 0, "✅ No overdue items",
    choice(length(rows) = 1, "⚠️ 1 overdue item",
      "🚨 " + string(length(rows)) + " overdue items")) as "Status"
FROM "00-Inbox"
WHERE created <= date(today) - dur(7 days)
GROUP BY true
```

---

## Processing Decision Tree

```
Quick fact to look up?
  → 03-Reference/ (commands, syntax, cheatsheets)

Concept to understand deeply?
  → 02-Zettelkasten/ (atomic note with links)

Active learning project?
  → 05-Projects/ (course work, study sprint)

Outdated or irrelevant?
  → Delete or 06-Archive/
```

---

## Tips

**Best practice:** Process inbox items in order of age (oldest first).

**Time allocation:** Aim for 15 minutes daily. If you have many overdue items, do multiple 15-minute sessions rather than one marathon.

**Quality over speed:** It's better to process 1-2 items well than to rush through many items poorly.

**When in doubt:** If unsure where something goes, ask yourself: "Will I need to look this up (Reference) or understand it deeply (Zettelkasten)?"

---

## Related

- [[WORKFLOW]] — Complete processing workflow
- [[PROJECT_STRUCTURE]] — Where each type of note belongs
- [[CLAUDE]] — System configuration and rules
