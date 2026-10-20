Plan the small feature from its confirmed requirements and accepted examples.
Include the needed technical approach in the plan; there is no separate design
document. Inspect affected code, project instructions, and usable checks. Decide
routine local engineering details from existing patterns.

Discuss consequential choices about shared contracts, compatibility, ownership,
or lifecycle with the user unless already delegated. Explain the mechanism and
meaningful alternatives, then wait for an actual answer. A choice changing
observable behavior belongs back in requirements. Keep drafts in the conversation
until the necessary agreement is obtained.

Write one plan that states the result, approach, work order, integration, and
verification. Create task files only if separate bounded units help a fresh
developer. Each unit of work needs its inputs, behavior to preserve, expected
result, and checks that would catch a plausible harmful mistake. A one-unit plan
must be executable without the planning chat. Leave private helpers, exact
signatures, and test bodies to the developer.

Place required whole-feature checks and documentation work after the relevant
implementation. Do not claim planned checks ran. On revision, verify review
findings and address those selected for correction; preserve valid completed
work. Return to requirements for a consequential behavioral decision. Commit
the agreed plan and optional tasks. Do not implement code here.
