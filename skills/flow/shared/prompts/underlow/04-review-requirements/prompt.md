Independently review the requirements for fidelity to agreed product decisions and
completeness of consequential observable behavior. Review the whole document before
finalizing the report; finding one defect is not a reason to stop searching.

For each behavior, check its entry conditions, observable result, boundaries,
failures, repetition, recovery, and subsequent state where relevant. Check that
general rules settle their examples and exceptions. Look for contradictions,
missing decisions, unsupported examples, and places where materially different
products could satisfy the text. Inspect relevant code, tests, and documentation
only to verify claims about current behavior. Do not invent product decisions or
implementation constraints.

Requirements are a product contract, not implementation documentation. Check that
they describe observable conditions and outcomes without source paths, line numbers,
symbols, code fragments, internal control flow, or implementation evidence. Report
implementation material as one aggregate finding with its behavioral consequence;
do not create one finding per occurrence.

List every consequential behavior and accepted decision before checking them.
Review each separately: source or input, preconditions, action or event, success
and failure outcomes, side effects, recovery, subsequent observable state,
alternative supported entry paths, and interactions between rules. Record a short
conclusion for each item as you check it. If a problem involves a shared rule or
assumption, check every listed behavior that relies on it. Complete the list before
classifying findings and choosing the verdict, even if you find a defect early.

Derive the complete acceptance-case set from what the requirements actually
guarantee before assessing findings. Do not fill a gap while deriving a case: report
the gap as a finding. On repeat review, begin with every prior valid case, re-evaluate
all of them against the complete revised requirements, then add cases only for newly
covered behavior. Keep valid case IDs and update only cases affected by a revision.
A gap exposed by any trace or retained case is not settled by interpretation.
Read the prior report and correction dispositions. Do not repeat resolved findings as
history; reuse the prior ID when the same defect persists or regresses.

Report credible material defects. The requirements author will verify each finding
and may reject it with evidence. Exclude wording improvements that cannot change
observable behavior.

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
High and medium findings require requirements correction. Record low findings as
allowed variation for design or implementation, but do not route requirements back
for them.

Write `{{step_output}}` with a one-line verdict, then findings in this
compact form:
`[ID] [priority] [requirement] - problem and trigger; likely observable consequence; required outcome.`
Separate blocking findings from low nonblocking findings. After them, include the
independently derived acceptance cases. Do not add long evidence narratives, other
nonblocking notes, or resolved-finding history. If there are no findings, say so
briefly.

Include a short `Coverage` section in `{{step_output}}`, even when there are no
findings. For each listed item, give its finding IDs or the concrete reason it
satisfies this review's criteria, with a supporting document section or code
location. If an item cannot be assessed, name the missing evidence. Record check
conclusions, not a reading log: a filename, `checked`, or `passed` alone is not
enough. Keep each entry brief and reference findings instead of repeating them.

Keep the engine-required `result.md` to the outcome, a link to
`{{step_output}}`, and unresolved finding IDs. Do not repeat or expand the
findings there.

Return `findings` when high or medium defects remain, `passed` when none remain even
if low findings were recorded, or
`blocked` only when missing essential information prevents assessment. Write only
`{{step_output}}` and required result files. Do not edit other files,
implement, execute tests, or launch agents or workflows.
