Review the implementation plan with the user. Help them understand what will be
delivered, in what order, and the consequential risks and tradeoffs; revise the
plan using their feedback.

Review the implementation plan and any task documents. Requirements govern behavior, quality,
purpose, and scope; the design governs binding design decisions.

Start with a short plain-language walkthrough of delivery order, dependencies,
and risks. Focus on scope, delivery order, and consequential tradeoffs, not a
line-by-line technical audit. When the plan has changed since the user last saw
it, lead with the changes. Expand task details only when requested or needed
for a decision. Invite concerns or pasted review feedback. Use code details only
when needed for an architectural decision. Do not ask the user to verify
technical facts or choose routine implementation details.

Check feedback against the agreed requirements, design, and repository evidence.
Explain unsupported findings and discuss disagreements. Apply supported planning
corrections, updating affected work, dependencies, coverage, and verification
together. Write `plan.md` as the revised overview with ordered work, task links when present, shared contracts,
requirement coverage, and whole-change checks. When task files exist, keep them bounded and
actionable: outcome, explicit inputs and prerequisites,
required outcomes and integration work, boundaries, and observable completion
checks. Tasks state outcomes, not implementation recipes. Leave helpers,
algorithms, file organization, and test construction to implementation within
agreed design; do not prescribe local signatures or call sequences.
For each manual verification, name who performs it and when.
Do not add separate risks, evidence, decisions, or agreement sections; necessary
safeguards become actual work and brief rationale stays beside the relevant choice.
Map relevant acceptance example IDs to work or whole-change
checks. Reference upstream rules instead of copying them; leave private helpers
and routine algorithms to implementation. Do not write code or pseudocode.

If feedback requires a behavioral or quality decision to change or be settled,
revise the requirements first; for a changed binding design decision, revise the
design first. Explain the evidence, affected work, and decision needed.

Before finishing, check work order, shared contracts, coverage, and end-to-end
verification. Summarize changes and remaining concerns in plain language and
confirm with the user that this review is complete. The plan is ready only then
and when it is coherent and actionable. Record the current agreement in
`plan.md`.
