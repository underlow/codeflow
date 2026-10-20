Independently review whether the design can satisfy the reviewed requirements and is
ready for implementation planning. Review the complete design before finalizing the
report; finding one defect is not a reason to stop searching.

Trace important requirements and acceptance cases through the cooperating parts.
Check that the design names the actual current entry points and components, describes
the specific changes from the current system, assigns state and responsibility to owners, defines shared
contracts, and explains event and data flow through success, failure, cancellation,
recovery, and subsequent behavior. Verify repository claims against relevant code,
tests, and documentation. Look for missing mechanisms or incompatible contracts that
would force planning to invent a consequential decision. Check that the design does
not narrow or change requirements.

A behaviorally correct restatement of requirements is not a design. For every
consequential behavior, require a responsible component and a supporting mechanism,
state rule, shared contract, or component flow. When the design assigns responsibility
to existing code, require the actual package, subsystem, type, or representative file
where needed to show that the component exists and planning can locate it. Do not require line
numbers, exhaustive file lists, private helper organization, or exact local
signatures.

Reject planning content in the design: documentation or file-edit inventories, task
breakdown, delivery order, and test implementation. Reject review history, finding
dispositions, obsolete alternatives, and repeated confirmation history. Important
scenarios belong only when they explain cross-component cooperation, lifecycle, or
failure handling; behavior already authoritative in requirements should be referenced
rather than copied.

List every consequential requirement and acceptance case before checking them.
Review each separately through its entry point, participating parts, ownership,
state and information changes, validation, failure and partial completion, cleanup
or recovery, consumers, final observable result, alternative paths, and shared
dependencies. Record a short conclusion for each item as you check it. If a problem
involves a shared mechanism or contract, check every listed behavior that relies on
it. Complete the list before classifying findings and choosing the verdict, even
if you find a defect early.

On repeat review, check every item against the complete revised design and add
newly affected behavior. Read the prior report and correction dispositions. Do not
repeat resolved findings as history; reuse the prior ID when the same defect
persists or regresses.

Report credible architectural defects and missing required agreement. The designer
will verify each finding and may reject it with evidence. Route an essential
unsettled product choice to requirements. Do not report routine local implementation
choices, missing walkthrough detail, or absent code pointers.

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
High and medium findings require design correction. Record low findings as
implementation freedom or for the responsible downstream stage, but do not route the
design back for them.

Write `{{step_output}}` with a one-line verdict followed by findings in this
compact form:
`[ID] [priority] [requirement/design section] - problem and trigger; likely consequence; required outcome.`
Separate blocking findings from low nonblocking findings. Do not add other
nonblocking implementation notes, long evidence narratives, or resolved-finding history.
If there are no findings, say so briefly.

Include a short `Coverage` section in `{{step_output}}`, even when there are no
findings. For each listed item, give its finding IDs or the concrete reason it
satisfies this review's criteria, with a supporting document section or code
location. If an item cannot be assessed, name the missing evidence. Record check
conclusions, not a reading log: a filename, `checked`, or `passed` alone is not
enough. Keep each entry brief and reference findings instead of repeating them.

Keep the engine-required `result.md` to the outcome, a link to
`{{step_output}}`, and unresolved finding IDs. Do not repeat or expand the
findings there.

Return `findings` for high or medium architectural defects or missing agreement,
`revise-requirements` for an essential unsettled product choice, `passed` when none
remain even if low findings were recorded, or `blocked` only when missing essential
information prevents assessment.
Write only the review and required result files. Do not implement or launch agents
or workflows.
