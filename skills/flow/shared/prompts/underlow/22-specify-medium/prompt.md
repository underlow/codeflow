Discuss drafts in chat. Write the agreed deliverable only after any required
agreement. If work is blocked or cancelled, explain why in the response rather
than saving an unfinished document.

Agree the concept, requirements, and system design together for a medium feature.
This is one interactive stage and one authoritative document, not three sequential
approval cycles. Keep detail proportional to the feature.

Write specification.md with these sections:
1. Purpose and scope: original request, intended outcome, included and excluded work.
2. Requirements: stable R IDs, observable behavior, important failures and later
   actions, compatibility, and behavior to preserve. Resolve material variation.
3. Design: affected existing components, responsibilities and interactions, state
   owners and lifetime where relevant, shared contracts, and consequential choices.
   Show how success and important failure paths produce the required behavior.
4. Acceptance examples: initial state, action, expected result, and relevant R IDs.
5. Agreement: current owner confirmation and explicitly delegated local choices.

Requirements own behavior; the design explains mechanisms satisfying them. Do not
substitute a requirement paraphrase for design. Leave task decomposition, private
helpers, exact private signatures, and routine implementation choices to later work.
For a new or changed shared module boundary, consider what complexity it hides
from callers and what callers must still know; avoid a pass-through layer that
adds coordination without simplifying their work.
Resolve contradictions between behavior and design in this session. Do not create
separate concept, requirements, or design documents.

When review or implementation returns work, verify each finding against the current
contract and code. Address verified findings selected for correction throughout
the document; preserve unaffected decisions. Explain rejected findings and any
consequential disagreement for the coordinator and user to resolve.
Return ready only after current agreement and resolution or explicit delegation of
every consequential question. Return blocked if essential evidence or a required
decision is unavailable, or cancelled if the user cancels the work.

Inspect the affected repository code, tests, and instructions before proposing
behavior or technical decisions. Ask the user only for missing intent, constraints,
or consequential choices that repository evidence cannot answer. Reuse answers
already given. Explain choices with concrete behavior and a recommendation.
Present the consolidated proposal in the conversation and wait for explicit
confirmation of the current version before writing specification.md. Silence or
confirmation of an earlier draft is not approval.
On revision, discuss changed consequential decisions; local repairs within an
agreed contract need no renewed decision. Record confirmation and explicit
delegations. Preserve the initial request and any supplied source link here.
Do not implement code or launch reviewers. Commit this deliverable document with
a concise message, staging only files belonging to this step.
