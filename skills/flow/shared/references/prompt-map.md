# Detailed prompt library

The [underlow prompt library](../prompts/underlow/) preserves the detailed
questions and quality criteria from the original workflows. Read the relevant
prompts before an analysis, planning, implementation, or review assignment.
They are source material for the assignment, not a second workflow engine.

| Phase and profile | Detailed prompts to use |
| --- | --- |
| Full analysis | `01-discover`, `02-challenge-concept`, `03-requirements`, `04-review-requirements`, `05-design-approach`, `06-review-design` |
| Medium analysis | `22-specify-medium`, `23-review-medium-spec` |
| Small analysis | `24-specify-small` |
| Bug investigation | `32-investigate-bug` |
| Full planning | `08-plan-code`; `10-review-plan-with-user` when discussing the plan; `11-review-plan` for independent challenge |
| Medium planning | `25-plan-medium`, `27-review-compact-plan` |
| Small planning | `26-plan-small`, `27-review-compact-plan` |
| Full development | `12-implement`; `13-review-task` when task dependency risk warrants independent review |
| Medium or small development | `28-implement-compact` |
| Bug correction | `33-fix-bug` |
| Whole-change review | `15-review` and relevant `15-review/aspects/*.md` for selected specialists; `29-review-single` for a combined reviewer |
| Correct findings | `17-fix` for a substantial change; `30-fix-compact` for a small or medium change; `33-fix-bug` for a bug |
| Documentation and delivery | `18-documentation` and `19-handoff` for their content criteria, when relevant |

The numbered directories contain `prompt.md`. Give every reviewer the current
[review contract](review.md) together with the relevant detailed prompt, its
bounded assignment, and any selected focus guide. The reviewer prompts now use
the current final-response contract; do not wrap them in old report-file rules.
Whole-change review has one
`behavior.md` aspect covering completeness, correctness, reliability, and
component connections; do not split it into separate reviewers by those names.
Use only the prompts relevant to
the assigned work. For an independent reviewer, pass the detailed review
criteria and the agreed contract, not the planning conversation. A selected
aspect file supplements `15-review/prompt.md`; it is not a mandatory reviewer.

The detailed prompts provide substantive questions, acceptance examples, scope
boundaries, and checks. The phase, review, and execution references govern agent
assignments, files, commits, and next steps. An outcome named in a detailed
prompt describes the situation; the coordinator decides what to do from evidence
and user decisions. Do not create report-only files or pass a detailed prompt
verbatim when its assignment instructions conflict with those references.
The coordinator combines review findings; no separate agent or report is needed.
