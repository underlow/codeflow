Plan the medium feature noninteractively. The combined specification owns both
requirements and binding design; its latest independent review owns derived
acceptance cases. These are sections of existing documents, not missing separate
concept, requirements, or design files. Follow settled decisions. Return revise-spec
when a binding design decision must change. Do not ask the user questions here.

Read the current contract and incoming review or implementation feedback. Inspect
the affected code, project instructions, and usable validation commands. Produce
an ordered plan in {{step_output}} and numbered task files in tasks/.

The plan states the delivered result, technical approach and shared contracts,
task order and dependencies, and how requirements and acceptance cases map to
tasks and checks. Each task must be usable without conversation history and give:
- result and relevant requirement IDs;
- exact input document sections and prerequisites;
- work and integration with existing components and other tasks;
- behavior to preserve;
- executable verification, expected observations, and the harmful error it catches.
Use existing project patterns. Leave private implementation choices to the developer.
Prefer one task when that is sufficient; split only into useful deliverable units.

There is no per-task review or separate final validation step. Assign required
whole-feature checks, integration, and documentation updates to the final task,
after its prerequisites. Requirements determine expected results. Do not duplicate
whole-feature checks in every task or claim planned checks have run.

On revision, verify every finding, fix supported high and medium issues throughout
the plan, and explain rejected findings or changed priorities. Keep low findings
nonblocking. When returning from implementation, inspect completed work, preserve
valid changes, and make each retained task explicitly continue or verify existing
work so re-entering the task loop does not blindly repeat it. Remove obsolete task
files owned by this plan. Do not change the behavioral contract inside planning.
Return revise-spec when the agreed behavior is contradictory or missing a required
decision. Return blocked for unavailable essential evidence. Return ready only
when all requirements and important acceptance cases have executable task coverage
and the plan can be followed without unresolved consequential choices.
Commit the plan and task changes. Do not implement code, edit the specification,
or launch reviewers. Write only {{step_output}}, task files, and required results.
