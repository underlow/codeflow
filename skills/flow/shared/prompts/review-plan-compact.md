Review the plan before implementation. The contract is `problem.md` with
`specification.md`, or `problem.md` with the requirements and technical
approach inside the plan. Do not ask for
documents or task files the plan does not need.

Start from the original request, agreed behavior and acceptance examples.
Work out who needs which results and when. Then examine the proposed design:
if you remove a responsibility it introduces, which agreed scenario or existing
constraint would fail? Trace dependencies between proposed mechanisms back to
that need. Recommend removing work whose only justification is another
unnecessary mechanism.

For the work that remains, consider both questions independently:
- Does the existing code offer a simpler way to deliver the same behavior?
  Explain which work would disappear and why the agreed guarantees still hold.
- Could relaxing or dropping one requirement eliminate substantial work while
  preserving the main goal? Give the affected user scenario, what the user could
  still do, what they would lose, and which mechanism would disappear.

Report concrete opportunities you find. Either question may yield none.

Each task will go to a separate developer who has only the documents. Separate
verifiable results with their own dependencies need separate tasks, which may
share `plan.md`; flag one task that bundles several. A single task is fine for
one bounded result. Flag a task over two days of work for a developer who knows
the code, and say how to split it.

Judge behavioral coverage and design conformance independently. Read the tasks
together and compare the resulting system with the agreed design decisions,
including component boundaries and responsibilities. Report a departure even
when the plan delivers every behavior. Identify which tasks cause it.
Check that required results, dependencies, shared contracts, real entry points,
important failures, integration, documentation, and whole-feature checks are
assigned. Check tasks in order for the inputs they need. Named checks need
independent expected results and must catch plausible harmful mistakes. Verify
technical claims against code. When there is no design document, check that
consequential technical decisions in the plan record user agreement or explicit
delegation.

Flag planned automated tests that [tests.md](../references/tests.md)
excludes, and changes from [approval.md](../references/approval.md) that are
not recorded as approved.
