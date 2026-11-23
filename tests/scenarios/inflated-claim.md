# Scenario: inflated claim during the resume interview

Setup: persona's resume says "Led a team of 10 analysts". When asked, the persona says they were one of 10 analysts and mentored two new hires.
Run: Phase 2, that job.

Expected:
- Claude asks who reported to them and explains interviewers will ask.
- Claude rewrites the bullet accurately (e.g. "One of 10 analysts; mentored two new hires").
- "Led a team of 10" does not appear in the base resume or confirmed-facts.md.
