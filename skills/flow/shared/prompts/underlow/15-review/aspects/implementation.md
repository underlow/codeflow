Does the delivered behavior meet the requirements without adding product behavior
they do not ask for?

Find required behavior that is missing, incomplete, or not connected to the code
users run. Check behavior that must not change and behavior the requirements rule
out. Placeholders, examples, and unused code do not deliver a requirement.
For each requirement and acceptance case about the changed behavior, find the
code that implements it. Check every supported way to reach that code, its
exceptions, what happens on a later attempt, and the result the user sees.

Report added behavior or unrelated changes only when they cause a concrete problem.
Focus on required behavior and scope. Unnecessary complexity belongs to the
code-quality review.
