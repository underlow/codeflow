Turn the agreed requirements into a system design settled with the user. Prepare
a recommendation, then discuss and settle the approach together.

Use the agreed requirements and acceptance examples as the behavioral contract. Inspect
the repository code, tests, and documentation to identify the actual current entry
points, components, state owners, and integration boundaries that the change reaches.

Design the technical system that produces the required behavior. For every
consequential behavior, identify the responsible existing component, the state or
shared contract that supports it, and the event or data flow that produces it. A
requirement paraphrase without mechanism, ownership, or component interaction is not
design. Explain how the parts cooperate through success, failure, cancellation,
recovery, and subsequent actions. Support consequential claims with evidence,
distinguish assumptions, and do not invent quality targets.

Settle mechanisms and contracts only when alternatives affect requirements,
ownership, lifecycle, a shared boundary, or compatibility. Leave task decomposition
and routine local implementation details open.
When introducing or changing a shared module boundary, ask what complexity it hides
from callers and what callers must still know. If its value is unclear, consider
whether removing it would scatter that complexity across callers or simply remove
a pass-through layer. Use this to choose a useful boundary, not to demand an
abstraction for every component.

Explain significant alternatives, consequences, risks, and your recommendation.

Keep relevant assumptions, brief rationale, current agreed choices, agreement, and
delegation in design.md. Evidence is optional support for consequential factual
claims, not a mandatory section.

Name existing modules, types, or files when needed to establish real ownership and
integration boundaries. Do not include line-number walkthroughs, exhaustive file or
function inventories, exact private signatures, or prescribed helper organization.

Write design.md using these sections, keeping each proportional to the change:
1. Overview: short plain-language approach and why it fits.
2. Existing system and affected parts: actual entry points, components, and ownership
   boundaries involved. When assigning responsibility to existing code, name the
   actual package, subsystem, type, or representative file so the responsibility is
   real and planning can locate it.
3. Proposed architecture: changed responsibilities, component cooperation, and the
   specific changes from the current system.
4. State and ownership: each consequential state value, its owner, readers, lifetime,
   transitions, reset conditions, and stale or concurrent result handling.
5. Shared contracts: information exchanged across components, its meaning, ownership,
   validation, failure and cancellation behavior, and compatibility. Use conceptual
   data shapes where helpful; do not invent exact private signatures.
6. Consequential decisions: stable IDs, chosen approach, brief rationale, and
   significant alternatives only where they explain a meaningful tradeoff.
7. Component flows: a few end-to-end event and data flows through named components,
   limited to scenarios that demonstrate cooperation, asynchronous work, failure,
   cancellation, recovery, or ownership changes. Reference requirement IDs instead
   of restating the behavioral contract.
8. Current agreement: confirmation of this design and explicit delegations only; no
   confirmation history.

Do not list documentation edits, implementation tasks, delivery order, files to
modify, or tests to add; those belong in planning. Do not copy low-priority review
findings into the design unless one establishes a real architectural constraint.
Resolve consequential risks in the relevant design decisions. Put necessary
safeguards into shared contracts and record explicitly accepted tradeoffs beside
the decision that accepts them. Do not use a risk list as a substitute for
resolving the design. Leave executable verification to planning.
During discussion, raise unresolved consequential questions alongside the affected
decision. Before the design is agreed, resolve each one, explicitly delegate it as
an implementation choice within agreed contracts, or revise the requirements. Do
not silently defer a consequential decision to planning or implementation.
Distinguish binding decisions from implementation freedom. Bind only decisions
that planning or cooperating implementers must share, not routine local details.
Do not silently narrow or expand product behavior to suit a mechanism; revise
the requirements when the proposed design requires a behavioral change.

Define architecture, not a local implementation recipe. Leave private helpers,
exact signatures, dependency-call sequences, local rendering formulas, and test
fixture construction to implementation unless a shared contract or compatibility
constraint requires them. Describe a shared contract by its information, ownership,
lifetime, and invariant. Do not require one helper, handler order, storage shape, or
code location merely to make two paths agree.

Before presenting the design, privately map every consequential requirement and
acceptance example to a responsible component and supporting mechanism or contract.
Resolve any item without an owner or mechanism. Do not include this coverage map in the document.
Then remove any paragraph that only repeats observable behavior without explaining
architectural responsibility, state, contract, flow, or tradeoff. Every remaining
paragraph must define an architectural responsibility, boundary, state rule, shared
contract, lifecycle rule, consequential decision, component flow, or current
agreement.

Verify uncertain dependency behavior with focused disposable probes outside the
application source where permitted. Summarize consequential observations and limits
in design.md only where they affect a decision;
do not present inferred behavior as observed.

On revision, leave accepted or nonblocking implementation freedom to planning
and implementation. Local repairs within agreed contracts need no renewed
architectural decision; honor explicit delegation without adding a new approval
requirement. Renew the recorded agreement when binding decisions change.

The design is ready for independent review only when the user has agreed to the
current version and no consequential question remains unresolved. If purpose or
scope must change, revise the concept first. Do not implement code.
