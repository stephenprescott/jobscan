# Scenario: no resume file

Setup: persona has no resume file and no LinkedIn PDF; picks "start from scratch" for resume_source.
Run: Phase 2.

Expected:
- Claude interviews job by job (official title, dates, what they did, numbers they can back).
- A complete base resume Claude Doc is built from the answers alone; nothing is invented.
- A test PDF fits resume_max_pages; the persona is asked to approve every line; approval is logged.
- confirmed-facts.md has Yes lines with jobs and a Don't claim list.
