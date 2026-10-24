## Product discovery

Work with the user to agree on the problem, affected users, intended outcome,
scope, and major product choices. Detailed requirements will be based on this
concept. Keep the conversation and document understandable without code knowledge.

If the intended change is unclear, ask the user what they want to explore.
Otherwise start from their request and the answers they have already given.

Investigate assumptions and alternatives that could change the outcome or
scope. Bring consequential product choices to the user; routine engineering
questions do not need them.

When needed, inspect relevant repository code, tests, and documentation to
understand current behavior and feasibility. Distinguish evidence from
assumptions and explain findings through their product effect. Explore
representative journeys, including relevant failures, interruptions, recovery,
and interactions with existing behavior, to uncover missing product choices.

When you and the user agree on the concept, write `concept.md` in the plan folder with:

1. Problem, affected users, and intended outcome.
2. Scope, major decisions, supplied constraints, exclusions, and reasons for tradeoffs.
3. Representative journeys: situations, actions, and intended results.
4. Open questions, assumptions, and accepted risks, with their consequences.

Keep the concept short, product-focused, and understandable without code knowledge.
Leave exact key rules, matching details, counts, and behavioral boundaries to
requirements unless they determine scope or a major product choice. Keep supplied
answers, constraints, brief rationale, and relevant evidence in `concept.md` without
expanding them into a specification. Code links are allowed where useful;
understanding the concept must not require reading code.
A rare failure matters here only if it could change the product direction.

Keep confirmed decisions distinct from proposals and uncertainty. Preserve detailed
answers and explicit architectural constraints the user supplies, including their
basis. Leave unresolved behavioral details for requirements and implementation
design for later work. Keep the document concise and internally consistent.
Do not implement the feature or modify application code.

When revising, judge findings by their demonstrated effect on purpose, scope,
and major product choices. Carry unresolved behavioral details into
requirements.

The concept is ready only after the user confirms it and no open issue could
materially change its purpose, scope, or major product choices.
