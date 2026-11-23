# Phases 9–10: board, schedule, test run

## Phase 9: Board
1. Ask `publish_board` (`references/questions.md` § Board). The board is needed for the Apply button and the visual job list; without it they use the daily files in `applications/jobscan/`.
2. Copy `${CLAUDE_PLUGIN_ROOT}/board/jobscan-board.html` into the session scratchpad (the Artifact tool only publishes files under the working folder or the scratchpad, and the plugin folder is neither), and in the copy change the first line `<title>Jobscan Board</title>` to `<title><Their first name>'s Jobscan Board</title>` (the page's own `<title>` wins over the tool's `title`). Run the Artifact tool's `quickstart` once if it asks, then publish the copy as a new private artifact on their account: title "<Their first name>'s Jobscan Board", `icon: "briefcase"`, `capabilities: {db: {}, comments: {}, user: {}}` (load the `artifact-capabilities` skill first). The full `comments` form is what lets the Apply button send the job to this session.
3. Write its URL to `jobscan.config.md` → `board_url`.
4. Seed the board's settings with `ArtifactData` (ToolSearch "select:ArtifactData"): collection `settings`, doc `board`, op `set`, data `{title, fit_want, fit_match, want_max}` from their answers (`fit_bar` and the Want total in `applications/criteria.md`).
5. Check it: `ArtifactData` list on `settings` shows the doc. Say what you checked.
6. Ask `pin_board`. If yes, pin it.
7. Tell them: the Apply button sends the job to this jobscan session, so keep it open (not archived). If the button says the session isn't watching, it copies `/jobscan:apply <date> #<n>` to paste here instead.

## Phase 9: Scheduled scan
1. Use `scan_times` (asked in § Scan). Build a cron expression in their local time, e.g. one scan at 08:00 → `0 8 * * *`; two scans at 08:00 and 17:00 → `0 8,17 * * *`.
2. First list existing tasks (ToolSearch "select:mcp__scheduled-tasks__list_scheduled_tasks,mcp__scheduled-tasks__create_scheduled_task"). If a task with id `jobscan` already exists (a reinstall, or another tool by that name), show it and ask: replace it (update_scheduled_task with the new schedule and prompt), or keep it and create this one as `jobscan-2` with title "Jobscan 2". Otherwise create the task: `taskId: "jobscan"`, `title: "Jobscan"`, `description: "Scheduled job scan"`, the cron expression, and this self-contained prompt (fill in the folder path):

   > Run the jobscan scan. Work only in the folder <data_folder>, using full paths for every file. Read <data_folder>/CLAUDE.md first, then run the jobscan skill (/jobscan:jobscan) exactly as written, using <data_folder>/jobscan.config.md for all settings. Read only on job sites: never apply, submit, message, save jobs, enter passwords, or solve CAPTCHAs; mark a blocked source "blocked: <reason>" and continue. Coverage is the job: search every enabled source. Finish with the skill's notification (if notify is on) and a 3-line report.

3. **First run now, to clear permission prompts:** ask them to open the app's scheduled tasks list, choose the Jobscan task and press **Run now**, and to approve its prompts (choose "always allow" where offered, for the Chrome sites, Python and the board) so later unattended runs don't stall waiting. The task may be saved without a permission mode (the create result says so), so its runs start in the default mode: if the app offers a permission mode on the task's page, explain the choice and let them pick.
4. Tell them, plainly:
   - Scans start a few minutes after the set time (the app spreads load), so say "around 8:00", not "at 8:00".
   - Scheduled scans run only while the Claude desktop app is open and the computer is awake; a missed scan runs when the app next opens, and with `window: since_last` nothing is lost.
   - In `light` mode, suggest choosing a smaller model for the task: open the task in the app's scheduled tasks list and pick it from the model menu. (You can't set the model from here.)

## Phase 10: Test run
1. Ask before running: a short test scan on 1–2 of their enabled sources (to keep usage low), using `/jobscan:jobscan` with the source list limited for this run only. Don't run `--mark-success` for this partial test.
2. Show the result: the daily file and the board with jobs (or the reason none passed).
3. Explain the daily routine in a few lines:
   - Scans run on their schedule; a notification says how many jobs meet their bar (if `notify`).
   - Open the board, read the cards, shortlist or skip.
   - Press **Apply** on a job (or type `/jobscan:apply <date> #<n>` in this session). Answer one batch of questions. Many employer sites (Workday especially) need an account per employer: when the form stops at sign-in, they create the account or sign in in that tab, then say "continue" and Claude fills the rest. Review the files and the filled form. **Submit it themselves.**
   - Say "submitted" (or mark it applied) so the tracker updates.
   - Change any setting by asking ("change my pay floor", "add a target company").
4. Now that they've seen real scores, offer to adjust `tier_thresholds` and `fit_bar` (ask those two questions again). 
5. Tick Phase 10 in `setup-progress.md` and congratulate them briefly.
