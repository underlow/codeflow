Review the plan before implementation. The contract is `specification.md`, or
`requirements.md` with the technical approach inside the plan. Do not ask for
documents or task files the plan does not need.

Each task will go to a separate developer who has only the documents. Separate
verifiable results with their own dependencies need separate tasks, which may
share `plan.md`; flag one task that bundles several. A single task is fine for
one bounded result.

Check that required results, dependencies, shared contracts, real entry points,
important failures, integration, documentation, and whole-feature checks are
assigned. Check tasks in order for the inputs they need. Named checks need
independent expected results and must catch plausible harmful mistakes. Verify
technical claims against code. When there is no design document, check that
consequential technical decisions in the plan record user agreement or explicit
delegation.
