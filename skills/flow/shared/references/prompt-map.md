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

The numbered directories contain `prompt.md`. Whole-change review has one
`behavior.md` aspect covering completeness, correctness, reliability, and
component connections; do not split it into separate reviewers by those names.
Use only the prompts relevant to
the assigned work. For an independent reviewer, pass the detailed review
criteria and the agreed contract, not the planning conversation. A selected
aspect file supplements `15-review/prompt.md`; it is not a mandatory reviewer.

The library predates the phase-based skill. Preserve its substantive guidance:
questions to investigate, acceptance examples, scope boundaries, evidence
standards, checks, and test-quality criteria. When assembling an agent brief,
**replace** its old transport instructions with the current contract:

- `{{step_output}}`, `result.md`, fixed numbered files, and any required report
  path mean the agent's final response unless the current phase explicitly calls
  for an agreed contract or plan file. Do not create report-only files.
- An old named outcome is a description of the situation, not a YAML route.
  The coordinator decides the next phase from evidence and user decisions.
- Old references to `progress.json` mean `state.json`; use its `base_commit`.
- Old seven-reviewer, all-again re-review, mandatory task-file, consolidation,
  retrospective, and fixed-round instructions are superseded by the phase,
  review, and execution references. Do not schedule or save work only because an
  old prompt names it.
- For a prompt that authors a contract, plan, maintained documentation, or code,
  use the current file boundary and commit rules. Reviewers return findings and
  coverage in their final response without editing project files.

The `16-combine-review`, `31-combine-compact-review`, and `21-retro` prompts remain
as historical source material but are not phases or assignments. The coordinator
combines findings; no separate agent or report is needed. Do not pass an old
prompt verbatim to an agent when its transport clauses conflict with these rules.
