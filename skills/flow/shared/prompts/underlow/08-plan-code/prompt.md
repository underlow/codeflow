Turn the requirements and design into an ordered implementation plan. The plan
must give the implementer enough information to do the work without inventing
product behavior or design decisions. Do not ask the user questions.

Use the requirements to decide what the feature must do and what is in scope.
Use the design to decide how the system should be changed. Do not reconsider
decisions already settled in the requirements or design. Return to an earlier
step only when the documents contradict each other or leave out a decision
needed for the plan.

Read enough of the repository to find the affected code, existing patterns,
dependencies, and useful validation commands. Do not inspect unrelated areas.

Split the work into tasks that each produce a specific result. Order the tasks so
that earlier tasks provide everything later tasks need. Make sure every
requirement is handled by a task. When several tasks must use the same data or
behavior, explain what they must agree on. Include the work needed to join the
completed tasks into the working feature.

Describe what each task must achieve, not every step the implementer should take.
Do not prescribe private helpers, algorithms, file organization, exact private
signatures, pseudocode, or detailed test bodies unless the design already decided
them. File paths may show the implementer where to start; they are not a complete
list of files that may change.

Use these sections in `{{step_output}}`:
1. A plain-language summary of what the work will deliver.
2. Links to the tasks in execution order, with their dependencies.
3. Anything that several tasks must agree on.
4. A map from requirements to tasks and checks for the complete feature.

Put a short reason beside a planning choice when the reason matters. Do not create
separate risk, evidence, decision, or agreement documents. Keep relevant answers
to review findings in `{{step_output}}`. Put task files under `tasks/`.

Write one numbered file per task, in execution order. Each task contains:
1. Result: what must be true when the task is finished, with the relevant
   requirement IDs.
2. Inputs and dependencies: the documents, current behavior, or earlier task
   results it needs.
3. Work: what it must deliver and how that work joins the rest of the feature.
   Name useful starting places when needed.
4. Behavior to preserve: limits and existing behavior that must not be broken.
5. Verification: what to observe, where to observe it, anything the check needs
   first, and the harmful mistake the check must catch. Do not prescribe the test
   body.

Refer to requirements and acceptance cases instead of copying them. A task must
make sense without conversation history. Expected results must come from the
requirements, not from one possible implementation. Give each task only the
checks needed to show that it produced its result. Put checks that cover several
tasks in `{{step_output}}` instead of repeating them in every task.

Before returning, check that:
- every required result is assigned to a task;
- each task has the inputs it needs before it starts;
- tasks that must agree describe the same data or behavior;
- the tasks join into the complete feature;
- every named check can run and can catch the mistake it names.

If requirements or acceptance cases contradict each other, return
`revise-requirements` and state the conflict and the decision needed. If the
design must change, return `revise-approach`. Do not settle an
open product or design question inside the plan. If essential information is
missing or unusable, preserve the draft and return `blocked`.

When revising after review, check each finding against the requirements, design,
and repository. Address verified findings selected for correction. Preserve
accepted or nonblocking findings for the implementer without changing the plan
only because a reviewer assigned a priority label.
Update every affected task and every agreement between tasks, not only the place
named by the reviewer. Record what happened to each finding in `{{step_output}}`.
Explain rejected findings and consequential impact disagreements.

When revising after an implementation failure, inspect the work that already
exists. Keep valid completed work. Update tasks that are obsolete or still
needed so the implementer does not repeat finished work.

Return `ready` only when the plan and tasks can be followed as written and no
required product or design decision is missing.

Write only `{{step_output}}`, task files, and the required step result files. Do not
implement code, edit earlier documents, run reviewers, or create other artifacts.
