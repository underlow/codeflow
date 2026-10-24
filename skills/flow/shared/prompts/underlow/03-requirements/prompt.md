Turn the agreed concept into complete, confirmed requirements that settle
consequential product behavior. Keep the conversation and `requirements.md`
understandable without code knowledge.

Establish current behavior and constraints from the repository; distinguish
evidence from assumptions. Explore relevant journeys: normal use, boundaries,
failures, interruptions, recovery, subsequent actions, and interactions with
existing behavior. Leave implementation mechanisms to design; preserve explicit
architectural constraints supplied by the user.

Use these sections in `requirements.md`:
1. Purpose and scope: intended change, included behavior, and explicit exclusions.
2. Requirements grouped by user activity, with stable IDs, applicable conditions,
   short titles, observable results and transitions, and consequential exceptions. Preserve
   explicitly required behavior, output details, and compatibility. Examples
   are optional; use small, fixed examples when they clarify a rule, not current
   checkout dates or folder counts. Examples illustrate general rules rather than
   replace them. State each rule once;
   refer to it instead of creating narrower or conflicting restatements.
3. Quality expectations: observable outcomes, verification basis where needed,
   and relevant limitations. Qualify promises by the conditions under which they
   hold. Do not invent numeric targets or present an implementation mechanism as
   proof of an outcome.
4. Constraints and compatibility: user-specified constraints and existing behavior
   that must remain unchanged, separate from observable product requirements.
5. Decisions and unresolved matters: allowed variation, consequential assumptions,
   accepted tradeoffs, and material open questions with their consequences. Put
   brief decision rationale beside the relevant requirement where practical;
   do not repeat rules here or reproduce the investigation history.
6. Agreement: the version the user confirmed and a brief summary of subsequent
   changes. Confirmation of an earlier version does not confirm changed behavior.

Trace requirements to the concept or confirmed decisions. Keep all binding
behavior, relevant decisions, brief rationale, and confirmation in
`requirements.md`. State current behavior as observable product behavior, not as
code structure. Do not include source paths, line numbers, function or type
names, code fragments, internal control flow, or implementation evidence;
repository inspection informs the requirements but is not copied into them.

On revision, leave accepted or nonblocking variation for design to settle. If
purpose, scope, or major product choices must change, revise the concept first.

Before presenting the final proposal, read it as the user would. Remove implementation
material and replace it, only where it is behaviorally necessary, with the observable
condition and outcome. A developer must be able to choose an implementation during
design without contradicting the requirements.

Could someone implement materially different behavior while following these
requirements? Settle consequential differences with rules or allowed variation.
When walking the user through the consolidated behavior, focus on new or changed
decisions. The requirements are ready only after the user confirms this version
and no consequential behavioral or quality choice remains unresolved.

Do not edit application code or tests.
