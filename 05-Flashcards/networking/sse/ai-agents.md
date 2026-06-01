TARGET DECK: Tech-KB::Networking::SSE::AI Agents
Tags: networking sse ai-agents
**Related:** [[SSE MOC]]

START
Coding Questions
Why do AI agents use SSE to stream LLM responses instead of returning a full JSON response?
Back:
LLMs generate output **token by token**. Without streaming, users wait seconds staring at a blank screen.

SSE lets the server forward each token the moment the LLM produces it → users see text appear word by word (the "typewriter" effect in ChatGPT and Claude).

SSE is a natural fit: one persistent connection handles the entire generation stream.
Tags: networking sse ai-agents
<!--ID: 1780311500804-->
END

START
Coding Questions
How does a typical AI agent streaming flow work step by step?
Back:
1. Client sends user message via **POST**
2. Server opens **SSE response**, starts agent loop
3. Each LLM token → `event: token` pushed immediately
4. Agent calls a tool → `event: tool_start` pushed
5. Tool executes (REST, DB, MCP, etc.) → `event: tool_result` pushed
6. Agent continues with tool output → more `event: token`
7. Agent finishes → `event: done`, connection closed

The POST and SSE are **separate HTTP requests** — SSE is receive-only, user messages still go via POST.
Tags: networking sse ai-agents
<!--ID: 1780311500827-->
END

START
Coding Questions
What does agent SSE event data look like for token streaming and tool calls?
Back:
```
event: token
data: {"text": "Let me check the database..."}\n\n

event: tool_start
data: {"tool": "query_db", "input": "SELECT * FROM orders WHERE id=42"}\n\n

event: tool_result
data: {"tool": "query_db", "output": {"id": 42, "status": "shipped"}}\n\n

event: token
data: {"text": "Your order ships April 30th."}\n\n

event: done
data: \n\n
```

Named `event:` fields let the client route token text vs tool progress to different UI handlers.
Tags: networking sse ai-agents
<!--ID: 1780311500847-->
END

START
Coding Questions
What is SSE **backpressure**, and when does it become a problem?
Back:
**Backpressure** = when the client consumes data slower than the server produces it.

SSE has no built-in flow control. If the client is slow (bad network, backgrounded tab), chunks pile up in the TCP send buffer. When the buffer fills, the server's `write()` blocks — the LLM call stalls.

**Problems:**
- Slow client → server coroutine/thread hangs
- Agent tool calls get delayed because the loop is blocked on network I/O
- Memory grows if tokens queue up before flush
Tags: networking sse ai-agents
<!--ID: 1780311500868-->
END

START
Coding Questions
What are the mitigations for SSE backpressure in an AI agent?
Back:
1. **Use async I/O** (`asyncio`, Node streams) — a slow client doesn't block other requests
2. **Set write timeout** — drop the connection if client can't keep up
3. **Decouple LLM generation from SSE delivery** with an internal queue:
   - LLM runs freely, enqueues tokens
   - SSE flush loop drains the queue at the client's pace
   - Generation doesn't stall waiting for network

The internal queue pattern is the most robust for production agents.
Tags: networking sse ai-agents
<!--ID: 1780311500888-->
END
