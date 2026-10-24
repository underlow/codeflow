## Product discovery

Agree with the user on the problem, affected users, intended outcome, scope, and
major product choices; requirements will be built on this concept. Keep the
conversation and the document understandable without code knowledge.

If the intended change is unclear, ask what the user wants to explore. Inspect
the repository when you need current behavior or feasibility, and explain
findings by their product effect. Walk through representative journeys,
including failures, interruptions, recovery, and interaction with existing
behavior, to find product choices nobody has made yet. A rare failure matters
here only if it could change the product direction.

Write `concept.md`:

1. Problem, affected users, and intended outcome.
2. Scope, major decisions, supplied constraints, exclusions, and reasons for tradeoffs.
3. Representative journeys: situation, action, and intended result.
4. Open questions, assumptions, and accepted risks, with their consequences.

Keep it short. Leave exact rules, counts, and behavioral boundaries to
requirements unless they decide scope or a major choice. Keep the user's
detailed answers and architectural constraints with their basis. Separate
confirmed decisions from proposals and uncertainty. Code links are fine, but
understanding the concept must not depend on them.

The concept is ready when the user confirms it and no open issue could change
its purpose, scope, or major choices.
