---
name: jobscan
description: Job scan. Searches the user's chosen job sites in their Chrome (Claude in Chrome), drops jobs that fail their rules in applications/criteria.md, collapses duplicates, scores and tiers the rest, writes a ranked list to applications/jobscan/YYYY-MM-DD.md, and adds the jobs to their Jobscan Board. Runs on the user's schedule; also use when the user types /jobscan:jobscan or asks to "run the job scan" or "find new jobs".
---

# Jobscan

Goal: every new job that passes the user's filters, ranked, with nothing shown twice. Accuracy over speed: never guess pay, location or company size; mark unknowns as unknown.

## 0. Read first
Work in the user's jobscan folder (the folder holding `jobscan.config.md`). A scheduled run names that folder in its prompt: if this session's working folder is different, use the named folder and full paths for every file and command below. If it's missing, stop and say: open your jobscan folder in the Code tab, or run `/jobscan:setup`. If `setup-progress.md` shows Phase 5 not done, stop and say setup isn't finished.

Run the board update check in `${CLAUDE_PLUGIN_ROOT}/skills/setup/references/finish.md` § Updating the board (republishes the user's board when jobscan has a newer one).

Read: `CLAUDE.md`, `jobscan.config.md`, `applications/criteria.md` (the only rules to apply), `applications/tracker.md`, `applications/jobscan/seen.csv`. For the Match score, read the base resume once per run (Claude Doc at `resume_doc_url`; load the docs skill or `guide` first, then export it as markdown with the docs `export` tool, or read the doc and its tab's body node; the doc id is the last part of the link) and `confirmed-facts.md`.

Python command: `python` on Windows, `python3` on Mac.

## 1. Window
Run `python -I "${CLAUDE_PLUGIN_ROOT}/scripts/scan_window.py" jobscan.config.md`. It prints JSON: `start` (the window's start), `linkedin_f_TPR`, `indeed_fromage`, `google_tbs`. Only jobs posted at or after `start` count (`window: since_last` reaches back to the last successful scan, at most `window_cap_days`; `window: 24h` is the last 24 hours).
- Check the age on the posting itself; boards round. Drop anything older than `start`.
- "Reposted" jobs: keep only if the repost is inside the window; flag "reposted".
- No date shown (common on employer hiring systems): keep only if Google's result date is inside the window or the job isn't in `seen.csv`; flag "date unclear".
- Target company sites ignore the window (see `references/sources.md`).

## 2. Search (Claude in Chrome)
Load the Chrome tools in one ToolSearch call (tabs_context_mcp, tabs_create_mcp, navigate, get_page_text, find, read_page, computer, javascript_tool, tabs_close_mcp). Work in this session's own new tabs. The user is signed in to the boards in their Chrome.
- **If Chrome isn't connected** (tabs_context_mcp fails or finds no browser): start Chrome yourself (Windows: `Start-Process chrome` in PowerShell; Mac: `open -a "Google Chrome"`), wait about 15 seconds, and retry tabs_context_mcp up to 3 times. Only if it still fails: write the run as failed, notify (step 10), and tell the user to open Chrome and check the Claude extension is connected. (Scheduled scans were being missed whenever Chrome happened to be closed.)

**Queries.** Build two OR queries from `applications/criteria.md` § Titles to search:
- **Query A (main):** the main titles, each in quotes, joined with OR.
- **Query B (stretch):** the stretch titles, same way. Skip it if there are none.
Where a site doesn't take OR searches, run its 3–4 most common titles instead.

**Sources.** Search every source id in `sources`, using `references/sources.md` for how, and the mode rules there (`mode`: `light` or `full`).

Rules:
- **Coverage is the job.** Search every enabled source, in both location modes, every run. Never skip a source or leave a qualifying listing unopened "for time" or because an earlier run covered it.
- Each run's section starts with a coverage table: `| Source | Remote searched | Local searched | Results seen | Passed |`, one row per enabled source.
- **Blocked sources:** a sign-in wall, CAPTCHA, or a page that fails to load twice. Never sign in for the user, never solve a CAPTCHA, never retry in a loop. Write the coverage row as `blocked: <reason>` (e.g. `blocked: LinkedIn signed out`), keep going with the other sources, and name it in the notification.
- **"Verify you are human" checks (Indeed shows these often):** never click or solve one yourself. Leave that tab open, send the user a notification (ToolSearch "select:PushNotification"): "jobscan: <site> needs you to click its human check in Claude's Chrome tab", search every other source, then return to that site last and reload. Still blocked: `blocked: human check not cleared`.
- **Remote must include the user's state** (`state`). Drop a job whose allowed states exclude it; flag "remote states?" if the posting doesn't say.
- Board filters are unreliable. Always check location and pay from the posting itself.
- Read only: never apply, save, follow, message, or click Easy Apply anywhere.

## 3. Pre-filter from the results lists
Drop without opening when the list already shows: a title clearly outside the user's titles, an on-site/hybrid location outside their commute, a posted pay top under their floor, or anything their filters drop outright (e.g. hourly gigs, pure contract) per `applications/criteria.md`. A full-time role posted with an hourly range is not a gig: compare it at hourly x 2,080.

Job pages are long: when a page's text is large, read the requirements, pay, location and company-size parts rather than keeping the whole page.

## 4. Read each remaining posting
Open it and pull: company, title, location and setup, pay range, employment type (and rate for contract-to-hire), travel, duties, required and preferred skills, years required, company size (from the board's company panel or the company's LinkedIn page; else "unknown"), and the **employer's own posting URL** (follow "Apply on company site" or find it on the employer's hiring system; fall back to the board URL only if none exists).
- **Getting the employer URL (required):** on LinkedIn, Chrome hides the "Apply on company website" link's address, so click it in the same tab with javascript_tool: `const a=[...document.querySelectorAll('a')].find(e=>e.getAttribute('aria-label')==='Apply on company website'); a.target='_self'; a.click();` then read the tab's new URL from tabs_context_mcp and strip tracking parameters (`source=`, `utm_`). Never click Easy Apply. Easy Apply only: search the employer's hiring system (Greenhouse, Lever, Ashby, Workday, iCIMS) by company + title; not found: keep the LinkedIn `/jobs/view/<id>/` URL and flag "LinkedIn only". Do the same on Indeed, Built In, Dice and Google Jobs. Never store a search-results URL (google.com/search, linkedin.com/jobs/search) or an empty url.
- **Always link the US posting.** If the employer's posting is a non-US version (Canada, UK), find the US version on the same hiring system (Greenhouse: `boards-api.greenhouse.io/v1/boards/<company>/jobs` lists every location) and use its URL and pay. No US version: drop it (location filter).

## 5. Duplicates
- **Same job** = same company + same normalized title (lowercase; Sr/Sr./Senior equal; drop level numerals and punctuation) + same location or both remote.
- One row per job; list every board it was seen on.
- Drop it if its key is already in `seen.csv` or the company + role is in `tracker.md`.

## 6. Filter, score, tier
Apply `applications/criteria.md` exactly: the filters (any fail = drop), the Want score (the user's own categories and points), the Match score (its rubric, using the base resume and `confirmed-facts.md` read this run, with the user's years and close-equivalent rules), then the tiers. If the resume export fails (retry once), say so in the report and never estimate Match from memory: write `match: null`, add the flag `match unverified`, and tier provisionally on Want alone (the board always shows flagged jobs). Years: when a posting names years in a specific area ("6+ years in healthcare"), compare it with the user's years in that same area from `criteria.md`, not only their total; apply the years filter to whichever gap is larger. Commute: local on-site/hybrid jobs must be within about `max_commute_minutes` of `home_zip`; when unsure, keep it and flag "commute?".
- **People-management must-haves** ("2+ years managing analysts", "3+ years leading a team" meaning direct reports) are a missed must-have unless `confirmed-facts.md` or the base resume shows that much people management. Informal leadership or mentoring doesn't meet them.
- Put every tag-like concern ("remote states?", "below pay target", "target company", "LinkedIn only") in the `flags` field, not only in prose.

## 7. Write the list
File: `applications/jobscan/YYYY-MM-DD.md` (today). Format:

```
# Jobscan YYYY-MM-DD
Window: <start> to <now>. Mode: <mode>. Sources searched: <list>. Blocked: <source: reason>.
New jobs passing: <n> (A: <n>, B: <n>, C: <n>). Dropped: <n> (pay <n>, location <n>, role <n>, type <n>, duplicate/seen <n>, other <n>).

To apply: press Apply on the board, or type `/jobscan:apply <#>` with the row number below.

| # | Want | Match | Tier | Company | Title | Pay | Location | Size | Why it fits / gaps | Apply link | Seen on |
```
- Sort by Want + Match, highest first; ties by Match, then pay.
- "Why it fits / gaps": one short line.
- If today's file already exists, don't overwrite it: append `## <HH:MM> run` with its own coverage table, counts and table. Row numbers continue from the last row in the file, so every `#` is unique for the day.

## 8. Update the seen log
Append one line per job listed to `applications/jobscan/seen.csv`: `key,company,title,location,first_seen,apply_url`.

## 9. Update the Jobscan Board
Board: `board_url`. Load the `ArtifactData` tool (ToolSearch "select:ArtifactData"). Write every job listed to collection `jobs` with `action: "batch"` (up to 50 per batch), op `set`, doc id `YYYY-MM-DD-NNN` (date + row number, zero-padded to 3), data:
`{date, run ("HH:MM"), num, want, match, tier, company, title, pay, location, size, fits, gaps, flags: [..], url, seenOn, posted, status: "new"}`
- Only create new docs; never overwrite an existing one (it holds the user's status). Don't touch the `settings` collection.
- If the write fails, say so in the report; the markdown file is the fallback.

## 10. Finish
- **Complete run** (every enabled source searched or truly blocked): run `python -I "${CLAUDE_PLUGIN_ROOT}/scripts/scan_window.py" jobscan.config.md --mark-success`.
- **Usage limit hit mid-run:** save what was found (steps 7–9 for the jobs already scored), mark the section heading `stopped: usage limit`, list the sources not reached, and do **not** run `--mark-success`, so the next scan covers this window again.
- **Failed run** (Chrome unreachable, config missing): don't run `--mark-success`.
- Close the tabs this run opened.
- If `notify` is true: one desktop notification (ToolSearch "select:PushNotification", status "proactive"; skip it if unavailable), under 200 characters: "Jobscan: N meet your bar, M new total" plus the top job if any, or the block/stop/failure.
- Report in 3 lines: counts by tier, top 3 jobs (company, title, Want/Match), sources searched (X of Y) with any blocks.
