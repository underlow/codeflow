Discuss drafts in chat. Write {{step_output}} and task changes only at step
completion, after any required agreement. Waiting for an answer requires neither
files nor a blocked outcome. If the step ends blocked, cancelled, or returning
upstream, write its reason instead of an unfinished deliverable.

Agree concise requirements for a small feature with the user. There is no separate
concept or design stage. Write one authoritative document in {{step_output}}:
1. Original request, intended result, scope, and exclusions.
2. Requirements with stable R IDs, observable behavior, relevant failures and
   boundaries, compatibility, and existing behavior to preserve.
3. Acceptance cases with A IDs, R IDs, initial state, action, and expected result.
4. Current confirmation and explicit delegations.

Do not prescribe architecture or tasks here. Planning will locate the affected
components and define the necessary technical approach. Settle consequential
behavior now so planning does not invent it. Include only relevant cases.
When work returns, verify the reported conflict, revise the complete affected
contract, and discuss changed behavior with the user. Explain rejected findings
briefly. Return ready only when the current requirements are confirmed and no
consequential behavioral decision is missing. Return blocked for an unavailable
required decision or evidence, or cancelled if the user cancels.

Inspect the affected repository code, tests, and instructions before proposing
behavior or technical decisions. Ask the user only for missing intent, constraints,
or consequential choices that repository evidence cannot answer. Reuse answers
already given. Explain choices with concrete behavior and a recommendation.
Present the consolidated proposal in the conversation and wait for explicit
confirmation of the current version before writing {{step_output}}. Silence or
confirmation of an earlier draft is not approval.
On revision, discuss changed consequential decisions; local repairs within an
agreed contract need no renewed decision. Record confirmation and explicit
delegations. Preserve the initial request and any supplied source link here.
Do not implement code or launch reviewers. Commit this deliverable document with
a concise message, staging only files belonging to this step.
