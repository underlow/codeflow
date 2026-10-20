# Architecture review

Find architectural friction that makes real changes harder, then show a small
number of evidence-backed options in a visual HTML report. A candidate is a
proposal to discuss, not an approved refactor. Do not change application code,
project documentation, Git state, or issue trackers during this command.

## Choose and inspect the scope

If the user names a subsystem, path, or pain point, start there. Otherwise inspect
recent Git history for areas repeatedly changed and choose one or two coherent
areas to examine. State the chosen scope in the report. Read applicable repository
instructions, relevant domain and architecture documents, current code, callers,
tests, and enough history to understand why the code has its present shape.
Do not infer a problem from file count, line count, or naming alone.

Look for concrete friction: a behavior change that must be repeated across
callers, an interface that exposes incidental steps, ownership split across
modules, a pass-through layer that adds coordination, or a useful behavior that
cannot be verified through a stable interface. Ask what complexity a proposed
boundary hides from callers and what they still must know. Check whether removing
an existing boundary would scatter complexity or simply remove a forwarding step.
Respect existing constraints and decisions; note a conflict when an improvement
would require reopening one.

For each credible candidate, identify the current code path, actual callers,
the change or failure it makes difficult, a bounded proposed shape, expected
benefit, and cost or migration risk. Separate observed facts from inference.
Prefer candidates tied to recent change pressure or a demonstrated testability
problem. If the evidence does not support a useful recommendation, say so;
do not manufacture a refactor to fill the report.

## Produce the report

Write one standalone `.html` file in an OS temporary directory, using a unique
name such as `architecture-review-<repo>-<timestamp>.html`. Use embedded CSS and
HTML/SVG diagrams; the file must remain readable offline. Do not load remote
scripts, fonts, or styles. Escape repository-derived text before inserting it
into HTML. Keep any code excerpts short and free of secrets.

The report should contain:

- Repository, checkout/commit, date, scope, and a brief account of how the scope
  was chosen and what was inspected.
- A compact overview of the current area, with file links or paths.
- A card for each credible candidate: specific evidence and affected files;
  the maintenance or verification problem; a before/after diagram showing the
  actual responsibility or call-flow change; expected benefit; cost, tradeoff,
  and uncertainty; and a recommendation of **strong**, **worth exploring**, or
  **speculative**, justified by the evidence.
- A top recommendation, or an explicit conclusion that no change is warranted.

Use diagrams to explain the candidate, not to decorate the page. A two-column
before/after view is useful when responsibilities or calls move. Use simple
boxes and arrows or an inline SVG where that communicates better than prose.
Make the report scannable and legible on a laptop and a narrow screen. Avoid a
fixed number of candidates; a few well-supported ones are better than a catalog
of hypothetical cleanups.

Check that the file exists, opens as HTML, and contains all report sections and
readable diagrams. Open it for the user with the local platform command when
available; if opening fails, still provide the absolute path. In the response,
give the path, the main finding and its evidence, and the most important limit.
Then discuss which candidate, if any, deserves deeper design work. Do not turn
the chosen candidate into implementation within this command.
