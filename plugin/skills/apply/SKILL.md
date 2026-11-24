---
name: apply
description: One-command job application pipeline. Use when the user presses Apply on their Jobscan Board (a "Send to Claude" comment like "/jobscan:apply 2026-12-01 #2"), types /jobscan:apply, or says "apply to this" or "apply to my shortlist". Reads the posting (never asks them to paste it), fit-checks it against their rules, asks all gap questions in one batch, builds what their settings say for that tier (tailored resume, cover letter, hiring-manager note), fills the application form if they turned that on, and stops before submit.
---

# /apply

Goal: speed with accuracy. The user's whole job per application: press Apply, answer one batch of questions, review the filled form, click submit themselves. Everything runs in their jobscan session (the Code-tab session in their jobscan folder); heavy work goes to background agents so the session stays free for the next job.

Standing rules in the jobscan folder's `CLAUDE.md` always apply. Above all: never invent experience, never submit or send anything, nothing about why they left a job unless they supplied the wording.

## Inputs
Work in the user's jobscan folder (holding `jobscan.config.md`). Read:
- `jobscan.config.md`: `apply_outputs` (per tier, any of `resume`, `cover_letter`, `hm_note`), `hm_search` (per tier), `form_fill`, `mode`, `board_url`, `resume_doc_url`.
- `applications/criteria.md` (filters, Want, Match, tiers), `applications/profile.md` (form answers and the "Ask me each time" list).
- Base resume (Claude Doc at `resume_doc_url`, export as text; load the docs skill or `guide` first) and `confirmed-facts.md`.
- `voice-rules.md` for every letter, note and free-text answer.
- The board's `jobs` collection (doc id `YYYY-MM-DD-NNN`) via `ArtifactData`. Never touch the `settings` collection.

## Board update check (first, every time)
Before anything else, run the board update check in `${CLAUDE_PLUGIN_ROOT}/skills/setup/references/finish.md` § Updating the board. It republishes the user's board when jobscan has a newer one, so fixes reach their live board without them asking.

## The Apply queue (the Apply button always works)
Pressing Apply on the board saves the job as `status: "queued"` with `queuedAt` in the board's `jobs` collection. That saved row IS the request: it exists even if this session is busy, closed or restarting, and the button never depends on a comment getting through. The "Send to Claude" comment that follows only wakes this session sooner (it reaches this session when the board is open in the Claude desktop app; from a web browser it goes to claude.ai's own chat instead, and the job simply waits in the queue).
- **Drain the queue, oldest first.** Whenever this session gets any turn (a board comment or auto-reply notice, a message, the user typing anything), first query `jobs` where `status == "queued"`, sort by `queuedAt`, and work them in that order. Also query `status == "applying"` for jobs with no tracker row yet (started earlier but never logged) and finish those first.
- **Taking a job off the queue:** set its status to `applying` (`ArtifactData` update with `if_version`) at Step 1, so the board shows "Claude is applying" and the next job moves up.
- **Keep the line moving:** once a job reaches Step 4 (agents building in the background), start Steps 1–3 of the next queued job instead of waiting. Never end a turn with queued jobs untouched without saying how many are left in line.
- **Board threads:** each queued click also leaves a "Send to Claude" thread. Reply with the real status (`acknowledge_duplicate: true` if an auto-reply already stands) and resolve it once that job is started.
- Never mark a queued job `skip` or `new` on your own; only the user removes a job from the queue.

## Step 1. Find and read the posting
- **Board Apply button:** a "Send to Claude" comment like `/jobscan:apply 2026-12-01 #2 (Company, Title)` (older boards may send `/apply ...`: treat it the same). Get doc `2026-12-01-002` (`ArtifactData` get). The board set status `queued` (older boards set `applying`); set it to `applying` now (see The Apply queue).
- **Typed:** `/jobscan:apply 2026-12-01 #7` → that board doc; set its status to `applying` (`ArtifactData` update with `if_version`) so the board matches. `/jobscan:apply 7` → row 7 of the newest `applications/jobscan/YYYY-MM-DD.md`. "Apply to my shortlist" → board `jobs` where `status == "shortlist"`, one job at a time.
- **No reference:** the posting is a tab the user opened in Chrome (`tabs_context_mcp`; ask which one if unclear). Never ask them to paste a description.
- Open the employer's apply link in a new tab and `get_page_text`. Confirm it is the US version (US location, USD pay); if not, switch to the US one and update the board doc's `url`. Pull: company, title, location/setup, pay, employment type, travel, required and preferred qualifications, form fields (if on the same page), any named recruiter or manager.

## Step 2. Fit check (5 lines max)
- Verdict: **Fail** (which filter) or **Tier A/B/C**, Want and Match with breakdowns, per `applications/criteria.md`. Check `tracker.md` for duplicates.
- Pay against their target, location/commute, type, travel. Requirements covered vs partial vs missing: "covered" only when a base-resume bullet or a `confirmed-facts.md` Yes line supports it (name it); anything else is partial or missing and becomes a gap question.
- **Fail, or a tier whose `apply_outputs` is empty:** stop and say why; continue only if the user says go (then use the outputs they name).
- Save the posting to `applications/postings/YYYY-MM-DD_Company_Role.md` (URLs, tier, scores, covered/partial, form fields, full posting text). Add a tracker row: status `Tailoring`, next step `Review form`.
- If triggered from the board, reply in the comment thread with the verdict line and resolve it.

## Step 3. Gap questions: ONE batch, before any writing
- One `AskUserQuestion` call (up to 4 questions; use multi-select to cover several items in one question). Ask only about requirements marked partial or missing, plus any form field not covered by `profile.md`.
- Each answerable with a click. Options name where it happened when that matters ("at <employer>", "employer not specified"), so a confirmed fact can go under the right job. Never lead toward a yes.
- Add every confirmed fact to `confirmed-facts.md` with today's date (Yes list). A "no" adds nothing to the resume; a skill they lack goes on the "Don't claim" list.

## Step 4. Build (background agents)
Make only what `apply_outputs[tier]` lists. Launch with the Agent tool, `run_in_background: true`, each with a self-contained prompt naming the jobscan folder path, the posting file, `confirmed-facts.md`, the resume doc URL, `voice-rules.md`, `CLAUDE.md`, and this step's rules. Write out the plugin folder path in each prompt (the folder holding this skill's `scripts/`; skill files an agent reads raw show `${CLAUDE_PLUGIN_ROOT}` unfilled). In `light` mode run the work one after another (lower peak usage; one agent doing resume, then letter, then note is fine); in `full` mode run separate agents in parallel.

**4a. Tailored resume (`resume`).** Follow `/jobscan:tailor-resume` steps 1, 3 and 5 (doc named `YYYY-MM-DD_Company_Role`, PDF in `resumes/`, checked page by page). Skip its gap-question step: the answers are already in `confirmed-facts.md`. Return the doc link and PDF path.

**4b. Cover letter (`cover_letter`, or when the form requires one).** As the user, following every rule in `voice-rules.md` (length, opening, banned words, close, sign-off). Built to `cover-letters/YYYY-MM-DD_Company_Role.pdf`: copy `cover-letters/_template.html` to the scratchpad, replace the body with the letter, keep the CSS, run `python -I "${CLAUDE_PLUGIN_ROOT}/scripts/build_pdf.py" <html> <pdf> <scratchpad>/pages --max-pages 1` (`python3` on Mac). Only confirmed facts, with real numbers from the resume. Reread before building: rewrite any line that sounds like a template.

**4c. Hiring manager (`hm_note`; LinkedIn search only if `hm_search[tier]` is true).** Search LinkedIn in Chrome (the agent's own tabs) for the role's likely manager and any named recruiter. Return up to 3 names with title, profile URL and confidence. Write the note following `voice-rules.md`. Read only: never connect, message or follow. With `hm_search[tier]` false, write the note addressed "Hello," and skip the search.

When the agents start, tell the user in one line, then end the turn. They can press Apply on another job meanwhile.

## Step 5. Fill the form (only if `form_fill` is true)
- Open the apply form in a new tab. Fill only from `profile.md`, the tailored resume and the posting. Upload the resume PDF and letter PDF if made (`file_upload`).
- A sign-in or account is needed (Workday and many hiring systems need one per employer): stop and ask the user to create the account or sign in in that tab, then say "continue"; on "continue", pick up the form from where it is. Never create accounts, enter passwords or solve CAPTCHAs.
- Every question on the **"Ask me each time"** list in `profile.md`, and anything not covered by `profile.md`: leave blank and list it for the user.
- After uploading the resume, re-check every field: some forms auto-fill from the resume (e.g. "Current company"). If the user isn't currently employed (per `profile.md`), clear it.
- Free-text questions ("Why us?"): write them with `voice-rules.md` and enter them; the user sees them in their review.
- **Stop before submit.** Post a short review note: the tab is ready in Chrome, the files attached, anything blank or uncertain, and the hiring-manager names and note (in a code block, ready to paste).
- With `form_fill` false: give the files and the note, and the apply link for the user to fill themselves.

## Step 6. Log it
When the user says it's submitted (or marks it applied on the board): board status `applied` (`ArtifactData` update with `if_version`), tracker row `Applied` with today's date, next step `Follow up <date + 7 days>` (plus `Note to <name>` if one was made), and the file names. If they drop it: board status `skip`, tracker `Withdrawn` (or remove the row if nothing was sent). Close the Chrome tabs used for this job.

## Checklist
- Posting read from Chrome or the board, never pasted.
- Fit verdict before any work; a fail or an empty tier stops unless the user says go.
- One batch of gap questions; new facts saved to `confirmed-facts.md`.
- Only the outputs `apply_outputs[tier]` lists; every claim traces to the base resume or confirmed facts; writing follows `voice-rules.md`.
- Form filled only if `form_fill`; "Ask me each time" items blank; not submitted.
- Board status and tracker row current.
