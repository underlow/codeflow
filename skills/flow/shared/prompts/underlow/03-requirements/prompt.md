Turn the agreed concept into confirmed requirements that settle consequential
product behavior. Keep the conversation and `requirements.md` understandable
without code knowledge.

Explore normal use, boundaries, failures, interruptions, recovery, later
actions, and interaction with existing behavior. Leave mechanisms to design, but
keep architectural constraints the user stated.

Sections of `requirements.md`:

1. Purpose and scope: intended change, included behavior, and exclusions.
2. Requirements grouped by user activity, each with a stable ID, short title,
   conditions, observable results and transitions, and consequential exceptions.
   State each rule once and refer to it elsewhere. Optional examples must be
   small and fixed (no current dates or folder counts) and illustrate a rule
   rather than replace it.
3. Quality expectations: observable outcomes with the conditions under which
   they hold. Do not invent numeric targets; a mechanism is not proof of an
   outcome.
4. Constraints and compatibility: user constraints and existing behavior that
   must stay unchanged.
5. Decisions and open matters: allowed variation, assumptions, accepted
   tradeoffs, and open questions with their consequences. Put brief rationale
   next to the requirement it explains.
6. Agreement: the confirmed version and a short summary of later changes.
   Confirming an earlier version does not confirm changed behavior.

Describe current behavior as the user observes it: no source paths, function or
type names, code fragments, or internal control flow.

Before presenting, read the requirements as the user would and replace
implementation material with the observable condition and outcome. Then ask:
could someone build materially different behavior that still satisfies this
text? Settle each such difference with a rule or an explicit allowed variation.
When walking the user through it, focus on new or changed decisions.

The requirements are ready when the user confirms this version and no
consequential behavioral or quality choice is open.
