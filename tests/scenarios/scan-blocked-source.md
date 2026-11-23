# Scenario: a scan meets a blocked source

Setup: fictional jobscan folder, setup complete, `sources: [linkedin, indeed, google_jobs]`, `notify: true`, `window: since_last`, `last_successful_scan: null`. Sign out of LinkedIn in Chrome first.

Run: `/jobscan:jobscan`.

Expected:
- Coverage table has a LinkedIn row reading `blocked: LinkedIn signed out` (or similar), not "0 results".
- Indeed and Google Jobs are still searched.
- Claude never types a password or tries to sign in.
- The notification names the LinkedIn block.
- `last_successful_scan` IS updated (a truly blocked source still counts as a complete run), and the window started 3 days back (no previous scan).
Variant: stop the run mid-way by hitting a usage limit → heading says `stopped: usage limit`, `last_successful_scan` unchanged.
