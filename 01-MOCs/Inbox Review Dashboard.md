---
created: 2025-12-08
tags: [moc, inbox, system]
---
## 🔴 URGENT - Overdue Items (>7 days)

```dataview
TABLE WITHOUT ID
  file.link as "📝 Item",
  dateformat(file.cday, "yyyy-MM-dd") as "Created",
  dur(date(today) - date(file.cday)) as "⏰ Age"
FROM "00-Inbox"
WHERE file.cday <= date(today) - dur(7 days)
SORT file.cday ASC
```

---

## 🟡 WARNING - Approaching Deadline (4–7 days)

```dataview
TABLE WITHOUT ID
  file.link as "📝 Item",
  dateformat(file.cday, "yyyy-MM-dd") as "Created",
  dur(date(today) - date(file.cday)) as "⏰ Age"
FROM "00-Inbox"
WHERE file.cday > date(today) - dur(7 days)
  AND file.cday <= date(today) - dur(4 days)
SORT file.cday ASC
```

---

## 🟢 FRESH - Recent Captures (<4 days)

```dataview
TABLE WITHOUT ID
  file.link as "📝 Item",
  dateformat(file.cday, "yyyy-MM-dd") as "Created",
  dur(date(today) - date(file.cday)) as "⏰ Age"
FROM "00-Inbox"
WHERE file.cday > date(today) - dur(4 days)
SORT file.cday DESC
```

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
WHERE file.cday <= date(today) - dur(7 days)
GROUP BY true
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
