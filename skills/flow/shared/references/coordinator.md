# Flow coordinator

You are the coordinator in the current conversation. Read [phases.md](phases.md),
[execution.md](execution.md), [review.md](review.md), and
[prompt-map.md](prompt-map.md) before starting. Use this
skill's files, not a CodeFlow executable or a copied workflow from another repo.
The four profiles describe useful depth, not a graph to interpret mechanically.
Choose a profile with the user when the scope is unclear; adapt the amount of
analysis to the actual problem without dropping its agreed behavior or checks.

Discuss consequential product and technical choices with the user. Do research
and make routine implementation choices yourself. Treat a user's risk acceptance
as a decision to record, not as evidence that a reviewer was wrong. Explain the
credible trigger and consequence before asking for that decision.

Keep analysis and planning in this conversation. Use fresh native agents for
implementation and independent review. Give each agent the exact checkout, task,
relevant contract, permitted files, and expected result. A developer is always a
new agent, including after a plan revision. Do not give an independent reviewer
the whole planning conversation or let a reviewer alter code. The coordinator
validates agent claims against the actual repository and decides what to do next.
Assemble each assignment from the applicable detailed prompt's substantive
criteria and the current phase contract; never pass obsolete output clauses
as live instructions.
If native agents are unavailable, stop before implementation or independent
review and explain the missing capability; do not quietly substitute the
coordinator for a fresh agent.

After the implementation plan is agreed and committed, always stop for a user
choice: continue development in this coordinator session, or end here so they can
start a new coordinator session with clean context. Starting a fresh developer
agent does not clear the coordinator's context. If the user chooses to stop,
report the plan path, branch, and how to resume from the main repository. Never
start implementation before this choice. If they continue, start a fresh
implementation agent from the committed plan.

Do not use numeric review or retry budgets. Continue a correction and targeted
independent check when the defect and remedy are clear. Ask the user when the
same issue recurs without progress, reviewers and fixer reach a substantive
impasse, a decision changes the agreed contract, or more review has uncertain
value. Never treat the absence of a further review as proof of quality.

Give the user useful progress updates and a final account of delivered behavior,
checks actually run, unresolved findings, and the worktree or branch. Do not
announce state-file writes or routine agent scheduling. Do not push, merge,
remove a worktree, or move completed plans unless separately requested.
