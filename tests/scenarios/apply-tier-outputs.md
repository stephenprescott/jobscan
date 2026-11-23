# Scenario: /apply makes only what the tier's settings list

Setup: fictional jobscan folder, setup complete, `apply_outputs: {A: [resume, cover_letter, hm_note], B: [resume], C: []}`, `hm_search: {A: true, B: false, C: false}`, `form_fill: true`, `mode: light`. `profile.md` "Ask me each time" includes "Desired salary".
Posting: fictional job that scores Tier B.

Run: `/jobscan:apply <date> #<n>` for that job.

Expected:
- Fit check says Tier B with Want/Match breakdown.
- One batch of gap questions (or none if no gaps).
- Only a tailored resume is built: no cover letter, no hiring-manager search or note.
- Form is filled from profile.md; the salary field is left blank and listed; nothing submitted.
- Tracker row added (Tailoring → Review form); board status `applying`.
Variant: a Tier C job → Claude stops after the fit check and asks before doing anything.
