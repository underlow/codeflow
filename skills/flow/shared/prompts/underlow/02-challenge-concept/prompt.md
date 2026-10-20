Review the agreed concept for problems that must be resolved before requirements.
Work noninteractively. Review the complete concept before finalizing the report;
finding one problem is not a reason to stop searching.

Check whether the problem, intended outcome, scope, major choices, exclusions, and
representative journeys agree. Challenge assumptions that could change the outcome,
scope, feasibility, or a major product choice.

List the proposed journeys and major decisions before checking them. Review each
separately through the current system: source or input, interpretation or resolution,
preconditions and side effects, validation or failure, and final observable state.
Include alternative supported sources and entry paths. Record a short conclusion
for each item as you check it. If a problem involves a shared assumption or rule,
check every listed journey and decision that relies on it. Complete the list before
classifying findings and choosing the verdict, even if you find a blocker early.

A missing decision or current-system interaction that makes a stated journey fail,
changes its scope, or adds a consequential side effect is a concept blocker, not a
detail to defer to requirements. Defer only behavioral choices that can vary without
changing any stated journey or major decision. Preserve explicit owner decisions
unless evidence changes their meaning.

Report credible discovery blockers. The discovery agent will verify each finding
and may reject it with evidence. Do not report wording preferences or questions
that requirements can settle without changing the concept.

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
High and medium findings require revision before advancing. Record low findings for
the next responsible stage or owner, but do not route the concept back for them.

Write `{{step_output}}` with a one-line verdict followed by findings in this
compact form:
`[ID] [priority] [concept section] - problem and trigger; likely consequence; required outcome.`
Separate blocking findings from low nonblocking findings. If there are no high or
medium findings, write `No discovery blockers`. On repeat review, recheck the complete
current concept and update coverage. List only unresolved or new findings. Read the
prior report and correction dispositions; do not repeat a resolved finding as
history. Reuse its ID if the same defect persists or regresses.

Include a short `Coverage` section in `{{step_output}}`, even when there are no
findings. For each listed item, give its finding IDs or the concrete reason it
satisfies this review's criteria, with a supporting document section or code
location. If an item cannot be assessed, name the missing evidence. Record check
conclusions, not a reading log: a filename, `checked`, or `passed` alone is not
enough. Keep each entry brief and reference findings instead of repeating them.

Keep the engine-required `result.md` to the outcome, a link to
`{{step_output}}`, and the unresolved finding IDs. Do not repeat or expand the
findings there.

Return `revise` when high or medium findings remain, `passed` when none remain even
if low findings were recorded, or `blocked` only
when missing essential information prevents the review. Write only the review and
required result files. Do not edit the concept or application code, ask questions,
or launch agents or workflows.
