Implement the supplied task, including any returned review corrections.
Work noninteractively.

Your job is to implement this concrete task, not to research or reassess the
feature. Read the supplied task first, then the requirements, design, and plan
sections it names. Normally these inputs are enough to begin implementation. If
a concrete question remains unanswered, inspect the exact code location or
document section most likely to answer it. Do not browse other working documents,
reports, or history merely to gather more context.

Referenced requirements govern behavior and expected results; referenced design
decisions are binding; referenced plan sections govern dependencies and shared
contracts. If an input is missing, complete the work it does not affect and
report what remains.

The current checkout contains the source and prerequisite work. Verify what the
task requires and preserve unrelated changes.
On a repeat attempt, continue valid work. Verify every returned finding, including
its trigger, reachability, consequence, and priority, then fix it or reject it with
evidence. Reclassify the finding when the reviewer's label does not fit this
definition. Assign priority by what can happen if the finding is left unresolved.
Consider both how often the trigger can occur and how much harm follows:
- high: ordinary or required use is likely to fail, or there is a credible risk
  of data loss, a security breach, or another irreversible consequence;
- medium: supported use can fail materially, or a material defect can escape, but
  the trigger or impact is limited or recoverable;
- low: the feature remains shippable; the problem is rare or narrow and its impact
  is small and recoverable.
Do not raise priority for a theoretical worst case without a credible trigger. For
planning and test gaps, classify the defect that could escape, not the missing
detail or test by itself. High and medium findings require correction. Low findings are nonblocking:
record them for later ownership, but do not make a separate change solely for them
unless the same change is required by a blocking finding. For every correction, identify affected requirements, acceptance cases,
callers, consumers, failure paths, and tests. Re-evaluate all retained relevant cases
against the complete corrected task, including interactions between corrections.
Resolve defects exposed by the correction instead of leaving them for the next review.

Complete this task within its requirements and binding contracts. Choose local
implementation details using existing project patterns and actual callers.
Suggested helpers and file paths are guidance unless explicitly required by a
contract. Own local engineering decisions; do not seek a design prescription for
private helpers, dependency calls, formulas, or fixture construction. Make necessary supporting changes without adding features or unrelated
refactoring.

Run the checks required by the task and project instructions. Add meaningful
behavioral tests where needed, using requirements and acceptance cases as the
source of expected results. Cover relevant failures, boundaries, and interactions;
for a reported defect, test the underlying failure and affected nearby behavior.
Fix implementation defects, rerun affected checks, and inspect the complete task
diff. Do not weaken expectations merely to make the implementation pass.

For returned findings, record each finding ID and disposition. Use `nonblocking` for
a low finding left for later ownership. Give reasoning only for a rejection, changed
priority, or nonblocking disposition; otherwise name the corrected location.

Return fail if a change to product requirements, binding design, shared contracts,
or task scope or dependencies is needed to deliver a crucial part of the feature.
Explain the conflict, evidence, decision needed, and partial work. A fixable
implementation defect or failed test is not a reason to replan.

Return blocked only when the requested feature cannot be implemented at all, or
a missing part is crucial: without it, the feature's main user journey cannot
work or cannot be used safely. State exactly what is needed to proceed.

In every other case, complete the work you can and return done. Report each
unmet requirement and unavailable required check, what works, what remains
unknown or unfinished, and the consequence for the user. Done means this step
has finished its available work; it does not mean every requirement was met.

Write `{{step_output}}` in the working documents directory. Identify the task and
inspected changes briefly, then report:
1. Delivered outcome: a short plain-language description of what now works for
   this task, not an implementation narrative or file inventory.
2. Validation: checks actually executed and their results. Clearly distinguish
   unavailable or unexecuted required checks from completed validation; proposed
   future checks are not evidence that the task is complete.
3. Corrections, only on retry: previous finding IDs and their dispositions.
4. Deviations, unavailable checks, or blocker, when present: what remains
   unmet or unverified, its consequence, what is needed, and what partial work
   remains valid.
Do not add a routine risks section or another design document.

Keep the engine-required `result.md` to the outcome and a link to
`{{step_output}}`. Do not repeat the report there.

Commit the completed task changes with a concise message that explains the
delivered behavior. Do not edit other planning artifacts, start another task, or
launch reviewers.
