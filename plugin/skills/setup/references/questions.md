# Setup questions

Every personal decision, grouped by phase. Each entry: what to ask, the choices to offer (always plus "Other"), the recommendation to mark "(Recommended)" with its reason, and where the answer is written. Batch related questions into one card (up to 4). Ask open questions in chat where the entry says so. Never pre-fill an answer.

Paths are inside the user's jobscan folder. `config` = `jobscan.config.md`. Any answer of "ask me each time", in any phase, is also added to `applications/profile.md` § Ask me each time.

## Install

### data_folder_location
- Asks: Where should your private jobscan folder live?
- Choices: The folder this session is open in (if it's empty or holds only your resume, ignoring a `.claude` folder, and isn't a git repo); a different folder you name (you'll then reopen the Code tab there).
- Recommended: the folder this session is open in. The board's Apply button sends jobs to this session, so jobscan works best in the folder you're in now.
- Writes: jobscan.config.md: `data_folder` (full path). Then copy the templates there.

### auto_update
- Asks: Should jobscan update itself when its author releases fixes?
- Choices: Yes, turn on auto-update; No, I'll update by asking Claude.
- Recommended: Yes. Fixes (for example when a job site changes its layout) reach you without effort.
- Writes: jobscan.config.md: `auto_update` (true/false). If yes, guide them through `/plugin` → Marketplaces → jobscan → auto-update.

## Resume

### resume_source
- Asks: What should we start your base resume from?
- Choices: My current resume file (Word or PDF); my LinkedIn profile PDF; start from scratch by interview.
- Recommended: your current resume file, if you have one. It's the fastest start; we still check every line.
- Writes: setup-progress.md (answer only). Then follow honest-resume.md.

### contact_details
- Asks: Which contact details go on your resume header? (multi-select)
- Choices: Email; phone; city and state; LinkedIn URL; portfolio or GitHub.
- Recommended: email, phone, city and state, LinkedIn. That's what recruiters expect; a street address isn't needed.
- Writes: the base resume doc header. Values asked in chat.

### resume_sections
- Asks: Which sections, in what order?
- Choices: Summary, Experience, Skills, Education (classic); Summary, Experience, Projects, Skills, Training, Education (shows side projects, courses and certifications); Summary, Skills, Experience, Education (skills first, for career changers).
- Recommended: the classic order, plus Projects, Training or Certifications only if you have real ones.
- Writes: the base resume doc structure; setup-progress.md.

### resume_max_pages
- Asks: How long may a tailored resume be?
- Choices: 1 page; 2 pages.
- Recommended: 1 page under about 8 years of experience, 2 pages above that.
- Writes: jobscan.config.md: `resume_max_pages`.

## Direction (asked in chat, then confirmed)

### current_situation
- Asks: Where are you now: working and looking, between jobs, or finishing school or a contract? Any timing that matters? (chat)
- Choices: open answer; then confirm a one-line summary.
- Recommended: none.
- Writes: CLAUDE.md "Current situation" (status and timing only: never why they left a job, even if they mention it; that goes in `applications/profile.md` only if they give exact wording and ask). Also write CLAUDE.md "Name" from the resume header.

### target_roles
- Asks: What job do you want next, and why? (open question in chat)
- Choices: open answer; then confirm a one-line summary.
- Recommended: none; this is yours. Help them put it in one sentence.
- Writes: CLAUDE.md "Next role I want, and why".

### step_level
- Asks: Compared with your last role, are you aiming to...
- Choices: Step up (more senior or more scope); same level, better fit; change direction (new field or role type); open to any of these.
- Recommended: none; offer the trade-off (stepping up narrows the list; same level widens it).
- Writes: CLAUDE.md "Direction"; feeds the Want score.

### move_away_from
- Asks: What do you want to move away from? (open question)
- Choices: open answer (e.g. a kind of work, an industry, a work setup).
- Recommended: none.
- Writes: CLAUDE.md "Moving away from"; may become a role filter.

### industries
- Asks: Industries you want, or want to avoid?
- Choices: No preference; prefer some (name them); avoid some (name them); both.
- Recommended: No preference unless one matters to you; every preference shrinks the list.
- Writes: avoided industries → applications/criteria.md § 1 "My own filters" now; preferred industries → carried into `want_categories` (Phase 4) as a Want row, since the Want table is written there. Their choice which way each goes.

## Job rules

### titles_main
- Asks: Which job titles should the scan search for first? (open question; suggest titles that fit their resume and target, and let them edit)
- Choices: your suggested list; their own list.
- Recommended: 4–8 titles that match the target role and their real experience.
- Writes: applications/criteria.md § Titles to search, Main; and § 1 Role "keep" (a one-line summary of the roles these titles describe).

### titles_stretch
- Asks: Any stretch titles, one level up or a neighboring role?
- Choices: None; your suggested stretch list; their own.
- Recommended: a short list (2–5) if they said step up; none otherwise.
- Writes: applications/criteria.md § Titles to search, Stretch.

### role_filter
- Asks: What kinds of roles should be dropped even if the title matches?
- Choices: None; roles that are mainly routine reporting for requesters; roles with no hands-on building; their own description.
- Recommended: whatever they said they're moving away from.
- Writes: applications/criteria.md § 1 Role.

### pay_target
- Asks: What pay are you aiming for (annual base)?
- Choices: open number.
- Recommended: none; suggest checking the ranges on a few target postings.
- Writes: applications/criteria.md § 1 Pay, target.

### pay_floor
- Asks: The lowest annual base you'd accept?
- Choices: open number.
- Recommended: none. Note: the scan drops jobs whose posted range tops out below this.
- Writes: applications/criteria.md § 1 Pay (floor, and "drop if top of range is under").

### pay_not_posted
- Asks: When a posting shows no pay range, should it be kept?
- Choices: Keep all; keep only senior-level titles and above; drop.
- Recommended: keep only senior-level and above, if their target is senior; keep all otherwise. Many good jobs hide pay.
- Writes: applications/criteria.md § 1 Pay, no range posted.

### hourly_gigs
- Asks: Hourly gig or piece work (e.g. AI training tasks)?
- Choices: Drop; keep.
- Recommended: Drop, unless they want side income.
- Writes: applications/criteria.md § 1 Pay, hourly gigs.

### work_setup
- Asks: Which work setups? (multi-select)
- Choices: Remote (US); hybrid near home; on-site near home.
- Recommended: none; ask what their life needs.
- Writes: applications/criteria.md § 1 Location; applications/profile.md § Logistics "Work setup".

### home_zip
- Asks: Your home ZIP code and state? (chat) Used only for commute checks and your state's job site.
- Choices: open answer.
- Recommended: none.
- Writes: jobscan.config.md: `home_zip` and jobscan.config.md: `state`.

### max_commute
- Asks: Longest one-way commute for hybrid or on-site jobs?
- Choices: 20 minutes; 30 minutes; 45 minutes; 60 minutes.
- Recommended: 30 minutes, a common balance between options and daily time.
- Writes: jobscan.config.md: `max_commute_minutes`; applications/criteria.md § 1 Location.

### remote_states
- Asks: Many remote jobs only hire in certain states. Drop remote jobs that exclude your state?
- Choices: Yes, drop them; keep and flag them.
- Recommended: Yes. You can't take a job that doesn't hire where you live.
- Writes: applications/criteria.md § 1 Location.

### employment_types
- Asks: Which employment types? (multi-select)
- Choices: Full-time; contract-to-hire; contract only.
- Recommended: Full-time and contract-to-hire. Contract-only work usually lacks benefits.
- Writes: applications/criteria.md § 1 Employment type.

### contract_to_hire_rate
- Asks: (only if contract-to-hire is kept) Lowest hourly rate for a contract-to-hire role?
- Choices: open number; "any rate".
- Recommended: about your annual target divided by 1,900, so the contract period pays like the full-time job (and covers lost benefits).
- Writes: applications/criteria.md § 1 Employment type.

### max_travel
- Asks: Most travel you'd accept?
- Choices: None; up to 10%; up to 25%; up to 50%.
- Recommended: none; ask what works for them.
- Writes: applications/criteria.md § 1 Travel.

### levels_to_drop
- Asks: Which levels should be dropped? (multi-select)
- Choices: Entry/junior; VP and above; Director at large companies; none.
- Recommended: entry/junior if they're experienced; leave senior leadership in only if they want it.
- Writes: applications/criteria.md § 1 Level.

### max_years
- Asks: Drop roles that require more years than you have by a wide margin?
- Choices: Drop if they ask for 3+ more years than I have; drop if 5+ more; never drop on years.
- Recommended: drop if 3+ more years. Those rarely get past screening.
- Note: this applies to total years and to years in a specific area the posting names ("6+ years in healthcare" is compared with their healthcare years), so record years by area, including industries, in `years_experience`.
- Writes: applications/criteria.md § 1 Level.

### clearance
- Asks: Do you hold an active security clearance?
- Choices: No, drop jobs that require one (keep "able to obtain"); yes, keep them.
- Recommended: whichever is true for them.
- Writes: applications/criteria.md § 1 Clearance.

### recruiters
- Asks: Postings from staffing agencies or aggregators that hide the real employer?
- Choices: Drop them (direct employers only); keep them.
- Recommended: Drop. You can't judge a job when you don't know the employer, and the same job often appears direct.
- Writes: applications/criteria.md § 1 Recruiters and aggregators.

### want_categories
- Asks: What makes a job more appealing to you? Pick what should earn points. (multi-select, then add their own)
- Choices: The kind of work you want next (e.g. AI or a specific specialty); pay at or above target; a modern tool stack you want; company size; preferred industry; scope (owning design or leading others); remote.
- Recommended: start from what they said in Direction; 4–6 categories keeps it meaningful.
- Writes: applications/criteria.md § 2 Want score (one row per category).

### want_weights
- Asks: How many points should each category be worth? (show their categories; propose weights that put the most on their main goal)
- Choices: your proposed weights; equal weights; their own.
- Recommended: the main goal worth the most (e.g. 3), others 1–2, total around 10 so scores read easily.
- Writes: applications/criteria.md § 2 Want score (points and "Total possible").

### years_experience
- Asks: How many years of experience do you have, total, in each main tool or skill, and in each industry (e.g. healthcare)? (chat; check against the resume)
- Choices: open answer.
- Recommended: count from the resume dates; confirm with them.
- Writes: applications/criteria.md § 3 My years of experience.

### close_equivalents
- Asks: Which tools you've used should count for similar ones a posting asks for? (suggest pairs from their skills; let them edit)
- Choices: your suggested pairs; none; their own.
- Recommended: only true near-equivalents they could explain in an interview.
- Writes: applications/criteria.md § 3 Close equivalents.

### tier_thresholds
- Asks: Tiers decide how much work /apply does. Where should Tier A and Tier B start?
- Choices: A: Want 70% of max and Match 3+; B: Want 40% and Match 2+ (balanced); stricter (A needs Match 4+); looser (A needs Match 2+).
- Recommended: balanced. Converted to points from their Want total.
- Writes: applications/criteria.md § 4 Tiers.

### fit_bar
- Asks: What should your board show by default? (They can always switch to "Any".)
- Choices: Tier A jobs only (the Tier A thresholds); Tier A and B; everything that passes the filters.
- Recommended: Tier A only, so the daily list stays short.
- Writes: jobscan.config.md: `fit_bar` (want, match); applications/criteria.md § 4 Board default; later the board's `settings/board` doc.

### target_companies
- Asks: Any companies you especially want to work for? (chat, list)
- Choices: None; a list.
- Recommended: a short list (up to about 10) of companies whose jobs you'd always want to see.
- Writes: applications/criteria.md § Target companies. For each company, find its careers page and job system (Workday, Greenhouse, Lever, Ashby, iCIMS, Phenom and so on) with Chrome, then open the search address you plan to write and confirm it actually lists matching jobs (search links often ignore their keyword, or error) before writing the "how to read it" note (the job list address and any filter or search to use). This costs a few browser steps per company: with more than 3 companies, offer to research the rest during the first scan instead. Ask whether target companies are always Tier A when Match is high enough.

## Scan

### mode
- Asks: Light or Full scanning?
- Choices: Light (fewer sources, opens only the strongest listings; uses noticeably less of your plan); Full (every source you pick, every listing that passes opened).
- Recommended: Light on a Pro plan; Full on Max plans. Show the usage estimate from the README.
- Writes: jobscan.config.md: `mode`.

### sources
- Asks: Which job sites should the scan search? (multi-select; explain each in a few words)
- Choices: LinkedIn; Indeed; Google Jobs; employer hiring systems (Greenhouse, Lever, Workday and similar); Built In; Wellfound (startups); Dice (tech, many recruiters); your state's job site; USAJobs (federal); your target companies' career sites.
- Recommended: for Light: LinkedIn, Indeed, Google Jobs, employer hiring systems, and target companies (if any). For Full: add the rest that fit their field.
- Writes: jobscan.config.md: `sources` (ids: linkedin, indeed, google_jobs, hiring_systems, builtin, wellfound, dice, state_site, usajobs, target_companies). Then ask them to sign in, in Chrome, to each chosen site that has accounts (LinkedIn, Indeed, Dice, Wellfound), themselves; wait until they say done.

### state_site
- Asks: (only if `state_site` chosen) Find your state's job site now?
- Choices: Yes, find it; skip it.
- Recommended: Yes, if you'd consider public-sector jobs.
- Writes: applications/criteria.md § Sources, state job site (name, address, how to search it, found with Chrome).

### window
- Asks: Which jobs should each scan look at?
- Choices: Everything posted since the last successful scan (nothing is lost if a scan is missed); only the last 24 hours (strictly fresh postings).
- Recommended: since the last scan, especially with one scan a day: a scheduled scan skips when your computer is off.
- Writes: jobscan.config.md: `window` (`since_last` or `24h`).

### window_cap_days
- Asks: (only for "since the last scan") How far back may a scan reach after a long gap?
- Choices: 2 days; 3 days; 7 days.
- Recommended: 3 days. Older postings have many applicants already.
- Writes: jobscan.config.md: `window_cap_days`.

### scan_times
- Asks: How often should the scan run, and when?
- Choices: Once a day (pick a time); twice a day (pick two times); three times a day.
- Recommended: once a day in the morning on a Pro plan; each scan uses a good share of your usage.
- Writes: jobscan.config.md: `scan_times` (list of HH:MM).

### notify
- Asks: Desktop notification after each scan?
- Choices: Yes; no.
- Recommended: Yes. It tells you when a job meets your bar.
- Writes: jobscan.config.md: `notify`.

## Apply

### apply_outputs
- Asks: When you press Apply, what should be made for each tier? (one question per tier, multi-select)
- Choices: Tailored resume; cover letter; hiring-manager note; nothing (ask me first).
- Recommended: A: resume, cover letter, note. B: resume and note. C: nothing (ask first). Letters take the most usage and matter most for top jobs.
- Writes: jobscan.config.md: `apply_outputs` (A, B, C lists of `resume`, `cover_letter`, `hm_note`).

### hm_search
- Asks: Should /apply search LinkedIn for the hiring manager? (per tier)
- Choices: Yes for Tier A; yes for A and B; never.
- Recommended: Tier A only, if LinkedIn is one of their sources and they're signed in to it; otherwise never (the search needs a signed-in LinkedIn). It's useful but adds browsing time and usage.
- Writes: jobscan.config.md: `hm_search` (A, B, C true/false).

### form_fill
- Asks: Should /apply fill in the application form for you? It always stops before submit.
- Choices: Yes, fill it and stop before submit; no, just give me the files.
- Recommended: Yes. It saves the most time, and you review everything before you submit.
- Writes: jobscan.config.md: `form_fill`.

### salary_entry
- Asks: When a form requires a desired salary number, what should be entered?
- Choices: My target; the top of the posted range; the midpoint of the range; leave it for me each time.
- Recommended: leave it for you each time, until you've seen how it goes.
- Also asks: when the salary field is optional, leave it blank or fill it the same way?
- Writes: applications/profile.md § Pay (both lines). If "each time", also add it to "Ask me each time".

### ask_each_time
- Asks: Which form questions should always be left blank for you to answer? (multi-select; reason for leaving is always on the list)
- Choices: Non-compete or prior agreements; criminal history; salary; references; disability or other EEO questions; none beyond the default.
- Recommended: non-compete and criminal history, since those depend on details only you know.
- Writes: applications/profile.md § Ask me each time.

## Profile

### contact
- Asks: Fill the form answers from what you already gave (the resume header and your ZIP) and confirm them; then ask only what's new: full legal name (for forms that ask) and street address (only if they want forms that require it filled).
- Choices: confirm / correct; open answers for the new items.
- Recommended: none.
- Writes: applications/profile.md § Contact.

### work_authorization
- Asks: Are you authorized to work in the US? Are you 18 or older?
- Choices: Yes; no; ask me each time.
- Recommended: none.
- Writes: applications/profile.md § Eligibility.

### sponsorship
- Asks: Do you need visa sponsorship now or in the future?
- Choices: No; yes; ask me each time.
- Recommended: none.
- Writes: applications/profile.md § Eligibility.

### start_date
- Asks: Earliest start date to put on forms?
- Choices: Immediately; two weeks' notice; a specific date; ask me each time.
- Recommended: none.
- Writes: applications/profile.md § Logistics.

### relocation
- Asks: Willing to relocate?
- Choices: No; yes; depends, ask me each time.
- Recommended: none.
- Writes: applications/profile.md § Logistics.

### travel_willingness
- Asks: How should forms answer "willing to travel"? (defaults to your travel rule)
- Choices: Match my travel rule; ask me each time.
- Recommended: match your travel rule.
- Writes: applications/profile.md § Logistics.

### screening
- Asks: Common screening questions: currently employed? OK to receive texts during hiring? Related to an employee? Marketing consent? Background-check consent? Drug-test consent? How to answer "years of experience" ranges?
- Choices: per question, yes / no / ask me each time.
- Recommended: none; "ask me each time" for anything they're unsure about.
- Writes: applications/profile.md § Screening questions.

### eeo
- Asks: Voluntary self-identification (gender, race/ethnicity, veteran status, disability). Answer each or decline. These are optional and don't affect hiring decisions by law.
- Choices: per question, their answer / decline to answer / ask me each time.
- Recommended: none; "decline to answer" is always fine.
- Writes: applications/profile.md § Voluntary self-identification.

## Writing

### voice_rules
- Asks: Here are the default writing rules for letters and notes. Keep, change or drop each one. (show `voice-rules.md`, a few rules per card)
- Choices: per rule, keep / change / drop.
- Recommended: keep most; they make letters sound like a person, not a template.
- Writes: voice-rules.md (edit the rule lines).

### own_rules
- Asks: Any rules of your own? (e.g. a phrase you never use, a tone you prefer)
- Choices: None; their own lines.
- Recommended: none needed.
- Writes: voice-rules.md § My own rules.

### sign_off
- Asks: How should letters and notes be signed?
- Choices: your full name; your first name; their own.
- Recommended: full name on letters.
- Writes: voice-rules.md "Sign-off".

## Board

### publish_board
- Asks: Create your Jobscan Board (a private page in your Claude account that shows jobs and has the Apply button)?
- Choices: Yes; not now (use the daily files instead).
- Recommended: Yes. It's the easiest way to review jobs and start applications.
- Writes: jobscan.config.md: `board_url` after publishing (see finish.md).

### pin_board
- Asks: Pin the board to your Claude sidebar?
- Choices: Yes; no.
- Recommended: Yes, if you'll open it daily.
- Writes: setup-progress.md (answer); pin with the Artifact tool if yes.
