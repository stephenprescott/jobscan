---
name: tailor-resume
description: Tailor the user's honest base resume to one job posting. Produces a tailored Claude Doc, a styled PDF in resumes/, and a short note to the hiring contact. Use when the user shares a job posting or link and says "tailor my resume", "resume for this job", "write a note to the recruiter", or asks to rebuild a resume PDF. Also run by /jobscan:apply.
---

# Tailor resume

Goal: a strong, honest, tailored resume in one pass, with as few round trips as possible. **Every claim must trace back to the approved base resume or to `confirmed-facts.md`.** Background checks verify employers, titles, dates and education, and interviewers probe every bullet; an invented or inflated claim can cost the user the offer.

## Before you start
- Work in the user's jobscan folder: the folder holding `jobscan.config.md` (normally this session's working folder). If it's missing, tell the user to open their jobscan folder in the Code tab, or run `/jobscan:setup`.
- Read `CLAUDE.md` (standing rules), `jobscan.config.md` (`resume_doc_url`, `resume_max_pages`), `confirmed-facts.md` (Yes list and "don't claim" list) and `voice-rules.md`.
- **Base resume:** the Claude Doc at `resume_doc_url`. Load the docs skill or the docs `guide` before any docs call. Never edit the base resume; tailored versions are new docs.
- **PDF layout:** `resumes/_template.html` in the jobscan folder.
- Python command: `python` on Windows, `python3` on Mac.

## Steps

1. **Read the posting.** Pull out: title, must-haves, nice-to-haves, pay range, location and time-zone rules, travel, and the background-check scope.

2. **Raise concerns plainly, up front, in a few lines:**
   - Pay against the user's floor in `applications/criteria.md`.
   - Fit: which must-haves the resume covers well and which it doesn't.
   - Travel, location and time-zone requirements against their rules.
   - Anything the background check will verify that the resume states differently from official records (the user told you about it during setup if so: check `confirmed-facts.md`).

3. **Create the doc first, then fill it.** Name it `YYYY-MM-DD_Company_Role` (e.g. `2026-12-01_Acme_SeniorAnalyticsEngineer`). Use the base resume's sections in its order. Fill one section per call so the user can watch it build. It's a doc you made, so write edits directly, not as suggestions. No byline under the title (skip the docs connector's usual date and author line): a resume has none.
   Tailoring moves, using only facts:
   - **Headline:** aim it at the target role. A headline is a target, never a claimed title.
   - **Summary:** lead with the user's most relevant fact for this posting.
   - **Experience:** reorder bullets so the posting's priorities come first; cut the least relevant. Keep official job titles, employers and dates exactly as in the base resume.
   - **Projects** (if the base has them): worded as in the base resume; trim bullets when space is tight.
   - **Earlier career** (if the base has it): condense to one line per role.
   - **Skills and training:** reorder so the posting's keywords come first. Never add a skill that isn't in the base resume or the Yes list. "Don't claim" items never appear.
   - **Contact info:** as in the base resume.

4. **Ask gap questions after the draft is up** (skip this step when `/jobscan:apply` already asked them). Use one `AskUserQuestion` card with up to 4 questions, one per unmet requirement, each answerable with a click. Options name where it happened when that matters ("at <employer>", "employer not specified"). Never lead toward a yes. Add only what the user confirms; a "no" adds nothing to the resume and goes on the "don't claim" list if it's a skill they lack. Record every new fact in `confirmed-facts.md` with today's date. Ask whether it should also go into the base resume; the default is this version only.

5. **Build the PDF.**
   - Export the final doc text with the docs `export` tool (markdown). It may include the user's own edits, so never rebuild from memory.
   - Copy `resumes/_template.html` to the session scratchpad and replace the body content with the final text. Keep the CSS. The doc follows the base resume's order and wording; the PDF uses the template's layout blocks (header, sections, job heads) for that same content.
   - Run `python -I "${CLAUDE_PLUGIN_ROOT}/scripts/build_pdf.py" <html> "resumes/<name>.pdf" <scratchpad>/pages --max-pages <resume_max_pages>`.
   - Look at every page image. It must fit `resume_max_pages`, with no awkward wraps or orphaned headings. If it runs over, cut the weakest bullets in the doc first, then rebuild.
   - Don't use the docs PDF export for the final file: its spacing is much looser.

6. **Hiring-contact note.** Address it to the contact by name if the posting or the user gives one; otherwise open with "Hello," and suggest swapping in a name. Follow `voice-rules.md` (length, banned words, sign-off). Name 1–2 specific facts that match the role and add a soft ask for a call. Don't claim anything unconfirmed, such as willingness to relocate: flag it so the user can add it. Give it in a plain-text code block, ready to paste.

7. **Stop at delivery.** Never submit an application or send anything. Remind the user to log the application in `applications/tracker.md` (or let `/jobscan:apply` do it).

## Output checklist
- The doc is named `YYYY-MM-DD_Company_Role`, and its link is given once.
- The PDF is in `resumes/` with the same name, within `resume_max_pages`, checked page by page.
- Every claim traces to the base resume or `confirmed-facts.md`; no "don't claim" item appears.
- The hiring-contact note is given, ready to paste, following `voice-rules.md`.
- Concerns (pay, fit, travel, verification) are stated in a few lines.
- Nothing about why the user left any job unless they supplied the wording.
