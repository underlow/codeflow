Agree the concept, requirements, and system design together for a medium feature.
This is one interactive phase and one authoritative document, not three sequential
approval cycles. Keep detail proportional to the feature.

Write specification.md with these sections:
1. Purpose and scope: original request, intended outcome, included and excluded work.
2. Requirements: stable R IDs, observable behavior, important failures and later
   actions, compatibility, and behavior to preserve. Resolve material variation.
3. Design: affected existing components, responsibilities and interactions, state
   owners and lifetime where relevant, shared contracts, and consequential choices.
   Show how success and important failure paths produce the required behavior.
4. Acceptance examples: A IDs, initial state, action, expected result, and relevant R IDs.
5. Agreement: current user confirmation and explicitly delegated local choices.

Requirements own behavior; the design explains mechanisms satisfying them. Do not
substitute a requirement paraphrase for design. Leave task decomposition, private
helpers, exact private signatures, and routine implementation choices to later work.
For a new or changed shared module boundary, consider what complexity it hides
from callers and what callers must still know; avoid a pass-through layer that
adds coordination without simplifying their work.
Resolve contradictions between behavior and design while writing the
specification. Do not create separate concept, requirements, or design documents.

The specification is ready only after the user confirms the current version and
every consequential question is resolved or explicitly delegated. Do not
implement code.
