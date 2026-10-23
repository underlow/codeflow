---
name: talk-to-designer
description: Consult a separate Claude designer session when visual design is needed. Offer an existing relevant session or a new one, establish how it should reply, and continue the conversation. Use when asked to talk to Claude Design or a designer.
---

Use `$talk-to-designer` with the supplied design request.
Read [the conversation workflow](references/conversation.md).
Use `scripts/designer.py` to discover Claude sessions, send messages, and receive
replies. This works independently of a terminal UI; replies are retained in a
local inbox and read with the script. A reply does not automatically wake Codex
after its turn ends. While awaiting a requested response, use bounded `wait`
calls, keep the user informed, and do other available work between waits.
If a new designer session is needed, ask the user to open it in Claude Desktop
and then list sessions again. Starting an ordinary terminal Claude process does
not establish that it has the user's intended design capabilities.
