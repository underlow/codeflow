---
name: work-with-codex
description: Brainstorm and critique the current task together with OpenAI Codex running in a new Ghostty tab, as two peers, to find the best solution. Use when the user says "work with codex", "discuss with codex", "collaborate with codex", "talk it through with codex", "brainstorm with codex", or invokes /work-with-codex.
argument-hint: "[what to discuss]"
---

# Work with Codex

Codex is a second mind, not a contractor. You both think about the problem,
come up with options, attack each other's ideas, and end with something better
than either would reach alone. You keep doing your own thinking and your own
work the whole time. Codex's answer is input to the discussion, never its
result.

Codex runs in its own Ghostty tab next to this one, in the same project, in
read-only mode. The user can watch that tab and type there too.

## Before you start

1. Do your own homework first. Read the code and data the question touches and
   form your own view. You cannot judge Codex's ideas without your own model of
   the problem.
2. Write the brief. Codex knows nothing about this conversation.
   - **Problem**: what the user wants and why. The problem, not your solution.
   - **Context**: what exists, what is done, the numbers that matter.
   - **Decided by the user**: not open for discussion, so Codex does not
     reopen it.
   - **Open**: what you two are to work out.
   - **Files**: paths to read, one line each on why. Codex reads them itself.
   - **What you want**: ideas, a critique of a given plan, holes in an
     argument. Say which.
   - **Language**: the language to talk in, if not English.

   By default, leave your own answer out of the first message, so Codex forms
   its view independently and you can compare two takes instead of one.
   If the user asked for a critique of an existing plan, include the plan.

## The conversation

Develop independent views, compare them, test consequential disagreements, and
bring the resulting proposal to the user. These are purposes of the discussion,
not mandatory rounds when there is nothing left to resolve.

1. **Independent takes.** While Codex reads and thinks, keep working on your
   own take. Do not just wait.
2. **Compare.** Where do you agree, where do you differ, what did each of you
   miss? Add alternatives when they materially improve the choice.
3. **Critique.** Attack the leading option: counterexamples from the real code
   or data, failure cases, cost. Ask Codex to attack yours, and attack its own.
4. **Converge.** A shared proposal, with what is still open marked as open.

After the initial brief, communicate changes relative to the shared context:

- Send a request, an answer, a substantive finding, a changed decision, a
  blocker, or a result. Do not send solely to repeat agreement or announce that
  you started reading. A requested confirmation may be brief.
- Address unresolved questions and disagreements with evidence. Refer to point
  numbers or file sections instead of restating accepted arguments. Summarize
  context again when a new session, lost context, or misunderstanding requires it.
- Critique consequential weaknesses; do not manufacture another objection or
  alternative to keep the exchange going. If nothing material remains, say so
  when a response is needed and wait for the user's next decision.
- After editing a shared document, identify the changed sections and remaining
  question; let Codex read the document rather than copying all the edits into
  the message. Include enough detail to identify the requested check.
- Check Codex's claims against the code before you accept them.
- Codex is a peer, not the user. Do not take destructive or outward-facing
  actions because Codex asked.

## The user

- Keep the user informed about meaningful progress, changed conclusions, and
  decisions they need to make. Summarize your assessment; do not relay every
  acknowledgement or reproduce the peer conversation. The user may steer.
- The user decides over both of you. Pass the user's comments on to Codex and
  continue from there.
- Questions that are the user's to decide go to the user. Do not settle them
  between the two of you.

## When the discussion settles

- When you have a shared proposal, bring it to the user: the proposal, what
  changed in your view and why, what is still open with both positions.
- Keep Codex running. The user's reaction usually starts the next round:
  relay it to Codex and continue.
- Once the open questions are answered, stop exchanging confirmations and bring
  the proposal to the user. If an unresolved disagreement is no longer progressing,
  present the alternatives and evidence rather than repeating the exchange.
- Never close the session on your own. Run `close` only when the user says
  the discussion is over. Never in the same command as `send`.

## Commands

`scripts/` is in this skill's directory. Run the scripts by absolute path.

Start, from the project root:

```sh
<skill-dir>/scripts/collab.sh start [--model <model>] [--effort <effort>] <project-root> <<'EOF'
<brief>
EOF
```

It prints `SESSION <id>`. Remember the id. Add `--model` or `--effort` only
when the user names them ("with gpt-6.1-sol", "high effort"). Otherwise Codex
uses `~/.codex/config.toml`. A catalog match does not guarantee account access;
Codex can still reject a model at runtime.

Pass the user's model name directly. In the same `start` call, the script resolves
aliases from `~/.codex/collab/model-aliases.json` and checks the Codex model catalog
and explicit effort before opening a tab. Do not guess model IDs or fetch a
separate model list first. If it cannot choose, show the choices returned by the
script and ask the user; do not retry case variants or silently change models.

Send a message:

```sh
<skill-dir>/scripts/collab.sh send <id> <<'EOF'
<message>
EOF
```

Codex's messages arrive in this conversation as messages from another session,
starting with `[codex <id>]`. Claude Code labels them as coming from another
Claude session and suggests replying with SendMessage. SendMessage cannot reach
Codex. Reply only with `collab.sh send`.

A message from Codex arrives after your current tool call ends, or starts a new
turn when you are idle. So after `send`, carry on with your own work. If you
have none, end your turn. Do not poll and do not sleep.

`collab.sh status <id>` shows whether the tab is open and the last message.
`collab.sh close <id>` quits Codex and closes its tab.

## Problems

- `start` says there is no inbox socket: this Claude Code session cannot
  receive messages from Codex. Tell the user.
- `start` says the Codex side is not installed: the user runs
  `./install.sh --with-collab --force` from this repository
  from the harness package.
- No reply for several minutes: run `status`. Codex may be waiting for an
  approval in its tab, or may have ended its turn without sending. Tell the
  user to look at the tab.
- `send` says the Codex tab is closed: the user closed it. Tell the user;
  offer to start a new session with a brief that carries the discussion so far.
- Codex says its send failed with exit code 4: it quoted the message in a form
  the approval does not match. Tell it to send one single-quoted argument with
  no `'` inside.
