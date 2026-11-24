# Changelog

## 0.1.2
- Apply always works: pressing Apply saves the job to a queue on the board ("Queued · 2nd in line") before anything else, and the jobscan session works the queue oldest-first, so no click is lost while the session is busy, closed or restarting.
- Boards update themselves: the next scan or Apply after an update republishes the user's board (same link, all jobs kept), tracked by `board_version`.
- Setup tells users to open the board in the Claude desktop app: in a web browser, Apply's wake-up goes to claude.ai's own chat instead of the jobscan session.
- Board: the fit bar only narrows "To review" (shortlisted, queued, applied and skipped jobs always show and count); pay sort compares annual dollars across "$137K", "$120,000" and hourly formats.
- Scan: starts Chrome itself when it isn't open; asks the user to clear a site's "verify you are human" check and retries that site last; follows LinkedIn's "Apply on company website" to store the employer's own URL, never a search page; people-management must-haves count only with confirmed experience; tag-like concerns go in `flags`.

## 0.1.1
- Fresh-install fixes: README Chrome test uses `createIfEmpty: true`; `data_folder` written in single quotes or forward slashes (double quotes break on Windows paths); Claude Docs check says when it passes.
- Years filter compares a posting's years in a named area with the user's years in that area.

## 0.1.0
- End-to-end test fixes: Chrome test uses `createIfEmpty`; read-only checks need no yes; resume answers kept in the progress log until the doc exists; batched open questions per job and for Direction; headline rule for step-up targets; target-company search links tested before saving; scheduled task checks for an existing `jobscan` task; board copied to the scratchpad and retitled before publishing; Built In searched remote-only; hourly-posted full-time roles compared at x 2,080; typed /apply marks the board card; "covered" requirements must trace to a fact; cover-letter template; drug-test consent asked separately; Workday sign-in pause and "continue".
- First version: setup interview with an honest base resume builder, job scan with configurable sources and window, Jobscan Board, /apply driven by per-tier settings, resume tailoring and PDF builder.
