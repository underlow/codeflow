# Repository backlog

Preserve unfinished work so someone without this conversation can resume it.
Use the user's language. Backlog capture does not authorize implementation.

## Locate and review

Honor a configured or user-specified backlog path. Otherwise use
`docs/backlog/` at the current Git worktree root; outside Git, use the working
directory. If the repository already names another backlog, use it instead.
Resolve an ambiguous destination before writing. Do not read other
repositories' backlogs.

Each item is one file `docs/backlog/<YYYY-MM-DD>-<slug>.md`, dated by creation;
the file name without `.md` is the item ID. Closed items move to
`docs/backlog/closed/`; items taken into a flow move to its plan directory. If a single-file `backlog.md` exists, read it as part of
the backlog and offer once to split it into item files.

At session start, list open item files and read their title and status lines
once; read a full item only when it is relevant. Do not create empty files or
directories.
If the user has given a concrete task, continue it; mention only directly
relevant entries. If no task is chosen, offer up to three open items with their
impact or reason to resume. Do not repeatedly offer the same items during a
session. Explicit invocation without arguments also reviews the backlog.

Before implementing an item, check whether the behavior and referenced code
still exist. Treat an old record as evidence from its date, not current truth.
The user's choice of an item supplies the task; use the normal development
workflow rather than implementing as part of capture. A flow takes over the
item file. Without a flow, the item stays open during the work and is closed in
the commit that completes it.

## Decide what to capture

Save immediately, without asking again, when:
- The user explicitly defers concrete work: later, separately, not in this change.
- A confirmed bug is outside the active task and is intentionally left unfixed.
- An agreed requirement is removed from current scope but remains wanted.

Give one short notification with the item ID and title after saving.
Do not capture rejected alternatives, idle brainstorming, unsolicited cleanup,
or work still being completed in the current task. Never label your own idea
as an agreed requirement. If it is unclear whether work remains wanted, ask a
short question before recording it. A suspected bug may be saved as an
research task only when the user wants it tracked; do not promote it to fact.
If saving is blocked, report that it was not saved.

Before finishing the active task, check the available conversation for deferred
work that was missed. Do not invent missing details from a compacted history.

## Write for a reader without the conversation

Check existing titles before creating an item. Update a matching item instead
of duplicating it; match behavior and scope, not just title. Preserve existing
conventions. Use a short English kebab-case slug and today's date; if the file
name is taken, choose another slug rather than overwriting.

Dates use `YYYY-MM-DD`. Use statuses `open`, `done`, and `cancelled`. When
closing, record the outcome and validation evidence, or the reason for
cancelling, set the status, and move the file to `closed/`; do not close on an
unverified claim.
Keep uncertainty in the text, not in invented severity scores or priorities.

### Feature or deferred change

```markdown
# Concrete desired behavior
Type: feature | Status: open

## Situation and purpose
Who is doing what, what is missing today, and why it matters. Include a concrete
input/action and desired result when useful.

## Agreed behavior and boundaries
What should change, what was explicitly excluded, and why those choices were
made. Distinguish accepted decisions from options merely discussed.

## Starting points and open questions
Relevant repository-relative files/symbols and durable evidence, if known.
Preserve useful findings and failed attempts with their outcomes. Record an
implementation approach only if actually established; label proposals as such.
State what remains unknown and the first useful investigation step.

## Completion check
Observable behavior that would demonstrate the request is satisfied.

## Why deferred
The actual scope decision, dependency, or user instruction that left this open.
```

### Bug

```markdown
# Observed failure under a specific condition
Type: bug | Status: open

## Reproduction and evidence
Relevant environment/version and prerequisites, if known.
1. Concrete action/input.
2. Trigger the failure.
Expected: observable correct behavior.
Actual: observed behavior, exact relevant error, or failing test.
State whether reproduced by the agent, reported by the user, or established by
another concrete artifact. Link evidence when available; include the essential
facts here so the record survives a missing log or conversation link.

## Impact
Who or what is affected and how; known frequency/scope and workaround.
Mark unknown scope as unknown rather than extrapolating.

## Findings and next step
Known code locations and investigation results. Separate observed facts from
suspected causes. Preserve failed fixes and why they failed, if relevant.
If reproduction details are unavailable, say exactly what is missing and how
to obtain it; never fabricate a successful reproduction.

## Completion check
The reproduction now produces the expected behavior, plus any known regression
case needed to distinguish a fix from masking the symptom.

## Why deferred
Why this confirmed problem is outside the current work.
```

For agreed research use `Type: research`, record the observed
signal, hypothesis, missing evidence, and a check that would confirm or reject
it. Its completion criterion is resolving uncertainty, not necessarily a fix.

These headings are prompts for concrete content, not text to copy verbatim.
Omit genuinely inapplicable details; explicitly mark important unknowns. Do not
fill fields with generic phrases such as "improve handling" or "add tests".
Never copy credentials, tokens, or private payloads into evidence.

## Check the saved result

Read the entry as if the conversation were unavailable:
- Can you identify the scenario and expected result without "this", "that",
  "as discussed", or an unexplained internal nickname?
- Is the reason for doing and deferring the work preserved?
- Can you distinguish verified facts, user reports, agreed decisions, and guesses?
- Is there a useful starting point and an observable completion check?

Repair missing context using available evidence; ask only when an essential
decision cannot be recovered. Do not do a new investigation just to fill every
field. Verify the actual file after writing and report its path and item ID.
