Review whether the tasks, in their stated order, can deliver the requirements
and follow the design. The implementer must not need conversation history or
have to invent a product or design decision. Read every task before finalizing the
report. Do not stop after finding the first problem.

Check that:
- every required result is assigned to a task and no task adds unrelated work;
- each task says what it must produce and gives the implementer enough information
  to begin;
- each task has everything it needs from earlier tasks;
- tasks that use the same data or behavior agree on what one provides and the
  others receive;
- the completed tasks join into a working feature through the same paths used by
  users or other code;
- a task handles each required failure and recovery case;
- every named check can run and can catch the harmful mistake it names.

List the required outcomes, task dependencies, shared contracts, and whole-feature
checks before reviewing them. Check each separately against the tasks and their
order, and record a short conclusion as you go. If a gap or contradiction affects
several tasks, check every task that depends on the same result or contract.
Complete the list before classifying findings and choosing the verdict, even if
you find a defect early. On repeat review, reassess the full current plan and
update these conclusions, not just the tasks changed by the last correction.

Use the requirements to judge behavior and scope. Use the design to judge the
planned system changes. Do not reconsider decisions already settled in the
requirements or design. If the documents contradict each other or leave out a
decision needed for the plan, report that specific problem.

Check important statements about the current repository against its code and
tests. Report only problems that could lead to an incorrect implementation or
allow an important defect to escape. Do not require pseudocode, private
signatures, helper organization, copied requirements, or detailed test bodies.

Read the previous review and the planner's responses. Do not repeat resolved
findings. Reuse the previous ID when the same problem remains or returns.

Assign priority by what can happen if the finding is left unresolved. Consider
both how often the trigger can occur and how much harm follows:
- high: ordinary or required use is likely to fail, or there is a credible risk
  of data loss, a security breach, or another irreversible consequence;
- medium: supported use can fail materially, or a material defect can escape, but
  the trigger or impact is limited or recoverable;
- low: the feature remains shippable; the problem is rare or narrow and its impact
  is small and recoverable.
Do not raise priority for a theoretical worst case without a credible trigger. For
planning and test gaps, classify the defect that could escape, not the missing
detail or test by itself.

High and medium findings require plan correction. Record low findings for the
implementer, but do not send the plan back for them.

Write `{{step_output}}` with a one-line verdict followed by findings in this
form:
`[ID] [priority] [task/requirement] - problem and trigger; likely failure or
escaped defect; required result.`

Separate findings that require correction from low findings that do not. Do not
add suggestions, long evidence descriptions, other notes, or
resolved-finding history. If there are no findings, say so briefly.

Include a short `Coverage` section in `{{step_output}}`, even when there are no
findings. For each listed item, give its finding IDs or the concrete reason it
satisfies this review's criteria, with a supporting document section or code
location. If an item cannot be assessed, name the missing evidence. Record check
conclusions, not a reading log: a filename, `checked`, or `passed` alone is not
enough. Keep each entry brief and reference findings instead of repeating them.

Keep the engine-required `result.md` to the outcome, a link to
`{{step_output}}`, and unresolved finding IDs. Do not repeat the findings there.

Return `findings` when high or medium findings remain. Return `passed` when none
remain, even if low findings were recorded. Return `blocked` only when missing
essential information prevents review. Write only the review and required result
files. Do not edit the plan, implement code, run tests, create commits, or launch
agents.
