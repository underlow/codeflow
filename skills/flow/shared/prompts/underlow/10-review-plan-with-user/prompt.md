Discuss drafts in chat. Write {{step_output}} and task changes only at step
completion, after any required agreement. Waiting for an answer requires neither
files nor a blocked outcome. If the step ends blocked, cancelled, or returning
upstream, write its reason instead of an unfinished deliverable.

Review the existing implementation plan with the product owner, who may also act
as architect. Help them understand what will be delivered, in what order, and the
consequential risks and tradeoffs; revise the plan using their feedback.

Review the implementation plan and every task document. Requirements govern behavior, quality,
purpose, and scope; the design governs binding design decisions. Investigate
technical questions in the repository yourself and reuse recorded answers.

Start with a short plain-language walkthrough of delivery order, dependencies,
and risks. Focus on scope, delivery order, consequential tradeoffs, and changes
since prior review, not a line-by-line technical audit. Expand task details only
when requested or needed for a decision. Invite concerns or pasted review feedback. Discuss consequential
choices one at a time, with options, effects, and a supported recommendation.
Use code details only when needed for an architectural decision. Do not ask the
user to verify technical facts or choose routine implementation details.

Check feedback against the agreed requirements, design, and repository evidence.
Explain unsupported findings and discuss disagreements. Apply supported planning
corrections, updating affected tasks, dependencies, coverage, and verification
together. Write {{step_output}} as the revised overview with ordered task links, shared contracts,
requirement coverage, and whole-change checks. Keep numbered tasks bounded and
actionable: outcome, explicit inputs and prerequisites,
required outcomes and integration work, boundaries, and observable completion
checks. Tasks are outcome contracts, not implementation recipes. Leave helpers,
algorithms, file organization, and test construction to implementation within
agreed design; do not prescribe local signatures or call sequences.
Assign an executor and completion point for manual verification.
Do not add separate risks, evidence, decisions, or agreement sections; necessary
safeguards become actual work and brief rationale stays beside the relevant choice.
Map relevant acceptance-case IDs to task or whole-change
checks. Reference upstream rules instead of copying them; leave private helpers
and routine algorithms to implementation. Do not write code or pseudocode.

If feedback requires a behavioral or quality decision to change or be settled,
return revise-requirements; for a changed binding design decision, return
revise-approach. Preserve the proposal and explain the evidence, affected work,
and decision needed without changing upstream documents.

Before finishing, check task order, shared contracts, coverage, and end-to-end
verification. Summarize changes and remaining concerns in plain language and
confirm with the user that this review is complete. Return ready only then and
when the plan is coherent and actionable. If essential evidence or a needed
decision cannot be obtained, report the reason and return blocked.

Record feedback dispositions and the user's confirmation in `{{step_output}}`.
Write only {{step_output}}, task files, and required step result files. Do not implement
changes or launch reviewers.
