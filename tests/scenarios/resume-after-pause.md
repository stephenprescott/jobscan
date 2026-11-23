# Scenario: setup resumes after a pause

Setup: run /jobscan:setup with a fictional persona through Phase 3 (Direction), then close the session.
Run: open a new session in the jobscan folder and say "continue jobscan setup".

Expected:
- Claude reads setup-progress.md first and says it is resuming at Phase 4 (Job rules).
- The first question asked is the first Phase 4 question (titles_main).
- No Phase 1-3 question is asked again; earlier answers are still in their files.
