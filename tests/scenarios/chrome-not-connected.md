# Scenario: Claude in Chrome not connected

Setup: Chrome closed or the Claude extension signed out.
Run: /jobscan:setup from the start.

Expected:
- Claude says jobscan needs Claude installed in the browser before installing anything else.
- The tabs_context_mcp test fails; Claude gives fix steps and retries at most twice.
- Claude does NOT move on to the plugin install, Python, or the data folder.
- It ends by saying setup continues with "continue jobscan setup" once Chrome connects.
