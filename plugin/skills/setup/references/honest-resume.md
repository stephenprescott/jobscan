# Phase 2: building an honest base resume

Purpose: a resume where every claim is something the user can explain in an interview and that matches what a background check will find. It's the only source (with `confirmed-facts.md`) that tailored resumes, letters and forms may draw from.

Say why up front, briefly: background checks verify employers, job titles, dates and degrees; interviewers ask about every bullet and call references. An inflated claim can cost an offer. So we build it carefully once, and every tailored version stays honest.

## 1. Starting point (their choice)
Card (`references/questions.md` § Resume → `resume_source`): their current resume file (Word or PDF), a LinkedIn profile PDF (LinkedIn profile → More → Save to PDF), or start from scratch by interview.
- A file: ask them to copy it into their jobscan folder (or drag it into the chat). PDF: read it fully. Word (.docx): ask them to also save it as PDF (File → Save As → PDF) and read that, or to paste the text into the chat. Treat it as a draft to check, not as truth.
- From scratch: build everything from the interview below.
Never fill a gap with a guess.

## 2. Header and contact
Ask what to show: name as they want it shown, email, phone, city and state, LinkedIn, portfolio or GitHub (`contact_details`). Show only what they choose.

## 3. One job at a time (most recent first)
For each job:
1. **Employer, official title, start and end month/year.** Ask for the title **as HR records it** and dates as their records show (offer letter, pay stubs, LinkedIn). If they used a working title, keep the official title; the working title may follow in parentheses only if they confirm it's accurate. Flag any date or title that differs from the existing resume; don't smooth it over.
2. **What they did.** Open questions, one or two at a time: What did you build or run? For whom? With what tools? How big (people, records, money, systems)? What changed because of it? What are you proudest of there?
3. **Draft bullets from their answers only.** Show the bullets and ask: "Is each of these accurate as written?"
4. **Numbers:** keep a number only if they can say how they know it. Estimates say "about". No number? The bullet describes the work without one.
5. **Push back on inflation, kindly, with the reason.** Examples: "led" when they were one of several ("Were you the lead, or one of the team? Interviewers will ask who reported to you."); "expert" after light use; "managed" with no direct reports; a team or budget size they can't back up. Write the accurate version.
6. Gaps between jobs are fine. Never invent a role or stretch dates to cover one.

## 4. Projects (optional)
Ask whether they have personal, volunteer or side projects worth showing. Describe each as what it is, with their role.

## 5. Skills
- For each skill they list, ask where they used it in real work. Record it in `confirmed-facts.md` with the job ("SQL: daily at <employer>").
- Anything only studied, tried once or "familiar with" goes on the **Don't claim** list (or a clearly labeled "Learning" line in the resume if they prefer; ask). Explain: Match scoring treats these as gaps, so the app never claims them.

## 6. Education and certifications
Exactly as conferred: degree, field, school, and year if they want it shown. In-progress items say "expected <month year>". Never imply a degree or certificate that wasn't earned. Anything they want on applications but not on the resume goes to `applications/profile.md` § Education and certifications.

## 7. Endings
Don't write anything about why they left any job. If they want wording for that, they give it; it goes in `profile.md` only if they ask.

## 8. Summary and headline (last)
Draft from confirmed content only. A headline is the role they're targeting, never a claimed title. They approve the wording.

## 9. Build the doc
- Choose sections and order with them (`resume_sections`) and the page limit (`resume_max_pages`).
- Create a Claude Doc named "<Their name> - Base Resume" (load the docs skill or `guide` first). Fill one section per edit so they can watch it build.
- Write its link to `jobscan.config.md` → `resume_doc_url`.
- Build a test PDF: copy `resumes/_template.html` to the scratchpad, put the resume in its body (keep the CSS), run `python -I "${CLAUDE_PLUGIN_ROOT}/scripts/build_pdf.py" <html> resumes/base-resume-test.pdf <scratchpad>/pages --max-pages <resume_max_pages>` (`python3` on Mac). Look at every page image; fix overflow by tightening wording with them.
- Show them the doc and the PDF. **Ask for approval: "Is every line in this resume true and something you can explain in an interview?"** Fix anything they flag. The app uses it only after a yes; log the approval in `setup-progress.md`.

## 10. confirmed-facts.md
Write it as you go:
- **Yes:** each confirmed fact with today's date and which job (or "employer not specified: claim in Skills or Summary only").
- **Don't claim:** skills or experience they don't have or only studied.
Later, `/jobscan:apply` gap questions add to this file; the base resume changes only when they ask.
