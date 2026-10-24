Plan the medium feature from its confirmed specification. The specification
owns requirements, binding design, and acceptance examples. Follow settled
decisions; do not invent a consequential product or design choice. Inspect
affected code, dependencies, project instructions, and usable checks.

Write one ordered plan that states the result, technical approach, shared
contracts, integration work, and how requirements and acceptance examples will be
verified. Divide the work into tasks with independently verifiable results and
explicit dependencies. Each task is a separate assignment for a fresh developer,
whether stored as a numbered section of plan.md or a file under tasks/. Create
separate task files only when they make the work clearer. Each task must name
its result, inputs, dependencies, behavior to preserve, and checks with expected
observations and the harmful mistake they catch. Use one task only when the
change delivers one bounded result, not merely to keep the plan in one file. In
that case, the plan itself must provide those details without depending on this
conversation. Leave private implementation choices to the developer.

Assign whole-feature checks and documentation updates to the work after the
necessary implementation exists. Do not duplicate checks across every task or
claim planned checks ran. When implementation shows the plan is wrong, keep
valid completed work and do not tell a developer to repeat it.

Revise the specification first if agreed behavior or binding design is
contradictory or needs a consequential change. Do not implement code.
