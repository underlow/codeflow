Design how the system will produce the agreed requirements and settle it with
the user: prepare a recommendation, explain significant alternatives and risks,
then agree the approach.

Inspect the repository to find the actual entry points, components, state
owners, and integration boundaries the change reaches. For each consequential
behavior, name the responsible component, the state or shared contract behind
it, and the flow that produces it through success, failure, cancellation,
recovery, and later actions. Restating a requirement without mechanism or
ownership is not design. Verify uncertain dependency behavior with disposable
probes outside the application source, and do not present inferred behavior as
observed.

Settle a mechanism only when alternatives affect requirements, ownership,
lifecycle, a shared boundary, or compatibility. Leave private helpers,
signatures, call order, formulas, and test fixtures to implementation unless a
shared contract requires them; do not require one helper or storage shape just
to make two paths agree. For a new or changed module boundary, check that it
hides real complexity from callers rather than adding a pass-through layer.

Write `design.md`, each section proportional to the change:

1. Overview: the approach in plain language and why it fits.
2. Existing system: the actual entry points, components, and ownership involved,
   named concretely (package, type, or representative file) so planning can find
   them.
3. Proposed architecture: changed responsibilities and how components cooperate.
4. State and ownership: each consequential state value, its owner, readers,
   lifetime, transitions, reset, and handling of stale or concurrent results.
5. Shared contracts: information exchanged between components, its meaning,
   owner, validation, failure and cancellation behavior, and compatibility, as
   conceptual shapes.
6. Decisions: stable IDs, the choice, brief rationale, and alternatives only
   where they explain a real tradeoff. Record accepted tradeoffs beside the
   decision.
7. Component flows: a few end-to-end flows showing cooperation, asynchronous
   work, failure, cancellation, or ownership changes, referencing requirement IDs.
8. Changes needing approval, as described in
   [approval.md](../references/approval.md).
9. Agreement: current confirmation and explicit delegations.

Leave out line-number walkthroughs, file inventories, tasks, delivery order, and
tests to add; those belong in planning. Resolve risks in decisions and shared
contracts instead of listing them.

Before presenting, privately map every consequential requirement and acceptance
example to a component and mechanism, and resolve any gap; do not put the map in
the document. Then delete paragraphs that only restate behavior.

Resolve each consequential question before agreement, delegate it explicitly as
an implementation choice, or revise the requirements; never defer it silently.
Do not narrow or expand behavior to suit a mechanism. Local repairs within agreed
contracts need no new approval; renew the agreement when a binding decision
changes.

The design is ready for independent review when the user agrees to the current
version and no consequential question is open.
