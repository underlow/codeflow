Update the project's maintained documentation to accurately describe the
implemented change.

Use requirements and binding design decisions only where they affect maintained documentation.
Inspect the final implementation, affected code, current validation, review and correction evidence,
and existing documentation; establish
delivered behavior from implementation and available checks, not completion
claims.

Update only documentation affected by the change. Follow its existing
organization, terminology, and audience. Preserve unrelated content; no change
is valid when existing documentation remains accurate.

Edit only maintained documentation. Do not edit
AGENTS.md, CLAUDE.md, planning inputs, or generated files. Report documentation
updates that require changes to code or generators. Commit completed
documentation changes with a concise message.

Verify changed claims, examples, commands, paths, and links against the
implementation and available evidence. Review the diff for inaccuracies and
unrelated changes. Distinguish inspected behavior from checks actually run.

If you discover a conflict with requirements or an agreed decision, record the
evidence and explain the consequence in product terms. Do not resolve it by
changing the agreement, fixing code, or treating it as accepted. Document only
what can be stated accurately; do not ask the user or reopen development.

Report the result concisely in the final response:
1. Documentation changes: documents and sections changed, or why no update is needed.
2. Accuracy checks: checks actually performed, their results, and relevant source
   or report references. Distinguish inspection from executed checks.
3. Conflict preventing accurate documentation, only when present: the deviation
   or missing prerequisite, consequence, and decision or source change needed.
   A recorded conflict is not accepted or resolved merely by documenting it.
Do not add an implementation narrative, routine risks section, or authored report.
Maintained documentation changes remain the primary output.

If essential evidence is missing or unusable, record the specific blocker in
the final response.
