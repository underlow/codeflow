Discuss drafts in chat. Write {{step_output}} and task changes only at step
completion, after any required agreement. Waiting for an answer requires neither
files nor a blocked outcome. If the step ends blocked, cancelled, or returning
upstream, write its reason instead of an unfinished deliverable.

## Product discovery step

Work with the product owner(PO) to agree on the problem, affected users, intended
outcome, scope, and major product choices. Detailed requirements will be based on this
concept. Keep the conversation and document understandable without code knowledge.

If the intended change is unclear, ask the PO what they want to explore.
Otherwise start from their supplied intent and recorded answers.

Investigate assumptions and alternatives that could change
the outcome or scope. Bring consequential product choices to the owner with
options, their effects, and a recommendation where supported. Resolve factual
questions yourself; routine engineering questions do not need a PO.
Ask focused questions, normally one at a time.

When it is required inspect relevant repository code, tests, and documentation to understand current
behavior and feasibility. Distinguish evidence from assumptions and explain
findings through their product effect. Explore representative journeys, including
relevant failures, interruptions, recovery, and interactions with existing behavior,
to uncover missing product choices.

When you and product owner agreed on concept write `{{step_output}}` in the working documents directory with:

1. Problem, affected users, and intended outcome.
2. Scope, major decisions, supplied constraints, exclusions, and reasons for tradeoffs.
3. Representative journeys: situations, actions, and intended results.
4. Open questions, assumptions, and accepted risks, with their consequences.

Keep the concept short, product-focused, and understandable without code knowledge.
Leave exact key rules, matching details, counts, and behavioral boundaries to
requirements unless they determine scope or a major product choice. Keep supplied
answers, constraints, brief rationale, and relevant evidence in {{step_output}} without
expanding them into a specification. Code links are allowed where useful;
understanding the concept must not require reading code. Do not create separate
decision, evidence, or revision documents.
A rare failure matters here only if it could change the product direction.

Keep confirmed decisions distinct from proposals and uncertainty. Preserve detailed
answers and explicit architectural constraints the user supplies, including their
basis. Leave unresolved behavioral details for requirements and implementation
design for later work. Keep the document concise and internally consistent.
Do not implement the feature or modify application code.

When revising, read the existing concept and the supplied reason for returning.
Check the evidence, preserve unaffected decisions, and discuss necessary product
changes with the owner. Record how each requested revision was addressed or why
it was rejected. High and medium findings require resolution. Low findings are
nonblocking: preserve them for requirements or the final owner, but do not change the
concept solely to resolve them unless the same change is required by a blocking
finding.

Walk the owner through the resulting concept in manageable pieces and incorporate
corrections. Finish as `ready` only after they confirm it and no open issue could
materially change its purpose, scope, or major product choices. If the session
cannot complete, report the reason and return `blocked`. If the owner cancels,
return `cancelled`.
