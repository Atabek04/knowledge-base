---
created: 2026-04-28
tags: [networking/sse, ai-agents]
sr-due:
sr-interval:
sr-ease:
---

# AI agents use SSE to stream LLM tokens to browser as they are generated

LLMs generate output token by token. Waiting for the full response before sending creates poor UX — users stare at a blank screen for seconds.

SSE maps perfectly: the backend forwards each token the moment the LLM produces it, creating the streaming typewriter effect seen in ChatGPT and Claude.

---

### Typical agent streaming flow

1. Client sends user message via POST
2. Server opens SSE response, starts agent loop
3. Each LLM token → `event: token` pushed immediately
4. Agent decides to call a tool → `event: tool_start` pushed
5. Tool executes (REST call, DB query, MCP server, etc.) → `event: tool_result` pushed
6. Agent continues reasoning with tool output → more `event: token`
7. Agent finishes → `event: done`, connection closed

The POST and SSE are separate HTTP requests — SSE is receive-only, user messages still go via POST.

---

### Agent action events

```
event: token
data: {"text": "Let me check the database..."}\n\n

event: tool_start
data: {"tool": "query_db", "input": "SELECT * FROM orders WHERE id=42"}\n\n

event: tool_result
data: {"tool": "query_db", "output": {"id": 42, "status": "shipped"}}\n\n

event: tool_start
data: {"tool": "call_rest", "input": "GET /api/shipment/42"}\n\n

event: tool_result
data: {"tool": "call_rest", "output": {"eta": "2026-04-30"}}\n\n

event: token
data: {"text": "Your order ships April 30th."}\n\n

event: done
data: \n\n
```

---

### Common agent tools streamed via SSE

| Tool type | Example |
|---|---|
| REST API call | fetch weather, payment gateway, CRM |
| Database query | PostgreSQL, MongoDB lookup |
| MCP server | filesystem, browser control, custom tools |
| LLM sub-call | summarize, classify, translate |
| Code execution | run Python sandbox |

SSE lets the UI show live progress — which tool is running, what it returned — instead of a spinner until everything finishes.

## Read more
- [[SSE is unidirectional server-to-client unlike WebSocket bidirectional channel]]
- [[SSE event field lets server label events so client routes them separately]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[SSE MOC]]
