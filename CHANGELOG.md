# Changelog

## 0.1.1
- Fresh-install fixes: README Chrome test uses `createIfEmpty: true`; `data_folder` written in single quotes or forward slashes (double quotes break on Windows paths); Claude Docs check says when it passes.
- Years filter compares a posting's years in a named area with the user's years in that area.

## 0.1.0
- End-to-end test fixes: Chrome test uses `createIfEmpty`; read-only checks need no yes; resume answers kept in the progress log until the doc exists; batched open questions per job and for Direction; headline rule for step-up targets; target-company search links tested before saving; scheduled task checks for an existing `jobscan` task; board copied to the scratchpad and retitled before publishing; Built In searched remote-only; hourly-posted full-time roles compared at x 2,080; typed /apply marks the board card; "covered" requirements must trace to a fact; cover-letter template; drug-test consent asked separately; Workday sign-in pause and "continue".
- First version: setup interview with an honest base resume builder, job scan with configurable sources and window, Jobscan Board, /apply driven by per-tier settings, resume tailoring and PDF builder.
