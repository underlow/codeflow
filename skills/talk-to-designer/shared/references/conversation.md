# Talk to a designer

This skill organizes communication with a separate Claude session. The calling
agent supplies the task and decides how to use the answer. It does not prescribe
a design process, deliverable format, implementation, or design review.

## Choose a session

When design help would be useful, briefly offer to consult Claude Design. An
explicit request to talk to the designer already authorizes that consultation.
After agreement, discover open sessions. Offer a relevant existing session by
name and project, explaining the match; let the user select it. A generic name
alone does not establish that it belongs to this task. Honor an explicitly
selected session without asking again.

If none fits, offer a new session. Use a real session-creation tool when it is
available and the user chooses that option; otherwise ask the user to open one.
Then refresh the session list. Do not replace an unavailable design session with
an ordinary coding agent without telling the user.

## Establish the conversation

In the first message to the selected session, include:
- Who is contacting it, the project, and the task or question.
- How to reply to this caller: the live return address and available messaging
  tool, or the exact reply command from the shared script.
- A request to use that return route for answers, questions, and completion.
- Any context and materials the calling agent considers necessary.

For the script's reply route, tell the designer to run the returned command with
its answer on stdin, using a quoted heredoc. Ask it to report if that command or
the materials are inaccessible. Do not claim a shared disk path is accessible
to a remote session. Keep task-specific requirements in the task message, not
in this skill.

Continue the conversation within the user's selected task. Relay the user's
steering and bring decisions requiring the user back to them. Do not repeatedly
ask for permission to send ordinary follow-ups in the authorized conversation.
Do not close or stop the designer session unless the user asks.

## Script transport

Requires Python 3 and local Claude session registry/socket access. Run by absolute
path, using the installed skill's `scripts/designer.py`. No account or global
agent configuration changes are needed.

```sh
python3 <skill-dir>/scripts/designer.py list
python3 <skill-dir>/scripts/designer.py connections --project <project-root>
python3 <skill-dir>/scripts/designer.py connect <selected-session-uuid> --project <project-root>
python3 <skill-dir>/scripts/designer.py send <connection-id> <<'MESSAGE'
<first-message instructions and task, then ordinary follow-ups>
MESSAGE
python3 <skill-dir>/scripts/designer.py wait <connection-id> --after <last-cursor> --timeout 50
python3 <skill-dir>/scripts/designer.py read <connection-id> --after <last-cursor>
python3 <skill-dir>/scripts/designer.py history <connection-id>
```

`list` reads the local Claude registry and lists same-user session sockets.
`connect` returns the connection ID and exact `reply_command`; it sends nothing.
The designer runs that command with its answer on stdin. Replies are retained
under `~/.cache/codeflow/talk-to-designer/`, outside the repository. `read` and
`wait` return replies and a cursor; pass the cursor next time to avoid rereading.
`wait` returns within 55 seconds. If a sandbox blocks socket access, use the
normal permission mechanism rather than changing permissions or settings.
Transport errors are reported; do not blindly resend when delivery is uncertain.

## Resume

For native Claude messaging, rediscover the selected designer from available
conversation context or saved task notes, then send the caller's current return
address. If the selection cannot be recovered, ask which session to continue.

For the script, `connections --project` finds saved selections. Read `history`
for the prior task and retained answers, confirm the intended connection if there are several, refresh `list`,
and run `connect` again for the selected live session. Send its current reply
instructions before continuing. If the designer has closed, offer another or a
new session; carry forward the relevant task context. Do not treat an old socket
path as a permanent address or silently select another session with the same name.
