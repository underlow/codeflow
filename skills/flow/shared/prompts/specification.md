Agree behavior and design for a medium feature in one document,
`specification.md`, with one confirmation rather than three. Keep detail
proportional to the feature.

1. Purpose and scope: original request, intended outcome, included and excluded work.
2. Requirements: R IDs, observable behavior, important failures and later
   actions, compatibility, and behavior to preserve.
3. Design: affected components, their responsibilities and interactions, state
   owners and lifetime where relevant, shared contracts, consequential choices,
   and how success and important failures produce the required behavior.
4. Acceptance examples: A ID, initial state, action, expected result, and R IDs.
5. Agreement: current confirmation and delegated local choices.

Requirements say what happens; the design explains the mechanism rather than
paraphrasing the requirement. Leave tasks, private helpers, and signatures to
later work. For a new module boundary, check that it hides real complexity from
callers.

The specification is ready when the user confirms the current version and every
consequential question is resolved or explicitly delegated.
