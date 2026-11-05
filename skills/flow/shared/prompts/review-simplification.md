Review the complete implementation for unnecessary complexity in code and tests.
Preserve the agreed behavior and justified compatibility, security, and data
protection. Do not edit files.

Look for abstractions built for hypothetical needs, pass-through layers,
duplicated rules or state, chains of special cases, unnecessary configuration,
fallbacks that hide failures, and compatibility or migration code without data
or callers that need it. Inspect actual uses before calling code unnecessary.
Check tests against [tests.md](../references/tests.md): incidental text or
structure checks, duplicated cases, self-confirming tests, and oversized fixtures
or test scaffolding. Also flag comments that merely narrate the code.

For each finding, explain what is unnecessary, why, and a simpler approach that
preserves required behavior. Recommend deleting a useless test without requiring
a replacement unless useful behavior would lose protection. Do not remove a
safeguard just because its failure is rare; consider the consequence.

Do not seek fewer lines at the expense of clarity, impose style preferences, or
propose unrelated cleanup. If simplification would change a binding design
decision, explain the decision needed. No findings is a valid result.
