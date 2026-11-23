# Phase 1: preflight, install and data folder

Do these in order. Show each step before doing it and get a yes. Stop with plain fix steps if a hard requirement is missing.

## 1. Where are we?
- jobscan needs **Claude Code in the Claude desktop app** (the Code tab) on a **Pro plan or higher**, on Windows or Mac.
- If you're running in claude.ai chat, the phone app, or anywhere without a shell and file access: say jobscan can't be installed here. Tell them to install the Claude desktop app (claude.ai/download), sign in, open the **Code** tab, choose an empty folder, and send the same message there. Stop.
- If they say they're on the Free plan: say jobscan needs Claude Code, which Free doesn't include; Pro or higher is required. Stop.

## 2. Say what it is (short)
In a few lines: jobscan finds new jobs on a schedule and scores them against rules they choose, shows them on a private board, and when they press Apply it tailors an honest resume, writes a letter and note, and fills the form, always stopping before submit. It never submits, sends, messages or connects for them. Their data stays in a private folder on their computer and in their own Claude account.

Then, plainly: **jobscan only works with Claude installed in your browser** (Google Chrome with the Claude in Chrome extension, signed in to this same Claude account). That's how it reads job sites and fills application forms.

Also say: setup asks a lot of questions (it's their job search, so they make every choice), can be paused any time, and uses part of their plan's usage. Ask to begin.

## 3. Claude in Chrome (first; blocks everything else)
1. Google Chrome installed? If not: chrome.google.com, install, open it.
2. The Claude extension: in Chrome, open the Chrome Web Store, search "Claude", add **Claude** (by Anthropic), pin it to the toolbar, open it and **sign in with the same Claude account** as this app.
3. Sign in to the job sites they'll use (LinkedIn, Indeed, and any others) in that Chrome, themselves.
4. Test: load the Chrome tools (ToolSearch "select:mcp__claude-in-chrome__tabs_context_mcp") and call `tabs_context_mcp`. It must return their tabs.
   - Fails: walk through the extension's own connection steps (open the extension, check it says connected, restart Chrome, then try again). Don't continue to step 4 until this test passes. If it still fails after two tries, stop and tell them setup will continue once Chrome connects ("continue jobscan setup").

## 4. Install the plugin (skip if you're already running from it)
- Run `claude plugin install jobscan --marketplace stephenprescott/jobscan` (from the shell). Show them the command first.
- Then ask them to type `/reload-plugins` in this chat (you can't run it for them) so the jobscan skills load, and say "continue jobscan setup".
- Auto-update question: `references/questions.md` § Install → `auto_update`. If yes, tell them how: type `/plugin`, open **Marketplaces**, select **jobscan**, turn on auto-update.

## 5. Python and PDF tools
- Check `python --version` (Windows) or `python3 --version` (Mac). Missing: give the install link (python.org/downloads; on Windows tick "Add python.exe to PATH") and wait.
- Check the PDF libraries: `python -c "import pypdf, pypdfium2"`. Missing: ask, then run `python -m pip install pypdf pypdfium2`.
- Check Chrome or Edge exists for printing PDFs (Chrome from step 3 counts).

## 6. Claude Docs
Their base resume lives in a Claude Doc. Check the docs tools are available (load the docs skill or `guide`). If not, tell them to turn on Claude Docs in claude.ai settings (it's on every plan) and continue when done.

## 7. The data folder
- Ask where to keep their jobscan folder: `references/questions.md` § Install → `data_folder_location`.
- Refuse a folder inside a git repo (`git -C <folder> rev-parse` succeeds) or inside a shared/public synced folder; explain why (their resume, pay and personal answers would go with it).
- Copy every file from `${CLAUDE_PLUGIN_ROOT}/templates/` into it, keeping the folder tree. Never overwrite an existing file.
- Write `data_folder` in `jobscan.config.md`. Create `setup-progress.md` from the template there and log Phase 1 answers.
- If this session isn't running in that folder: tell them that from now on they should open **that folder** in the Code tab for jobscan (and send "continue jobscan setup" there). Continue setup in this session using full paths until they switch.
