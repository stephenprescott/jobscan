# Phase 1: preflight, install and data folder

Do these in order. Show each install, download or account step before doing it and get a yes; read-only checks (the Chrome test, version checks) need no yes, just say what you're checking. Stop with plain fix steps if a hard requirement is missing. **Skip any step already done earlier in this session** (the README's "For Claude" steps cover 1–4 before the plugin loads); just confirm it in one line.

## 1. Where are we?
- jobscan needs **Claude Code in the Claude desktop app** (the Code tab) on a **Pro plan or higher**, on Windows or Mac.
- If you're running in claude.ai chat, the phone app, or anywhere without a shell and file access: say jobscan can't be installed here. Tell them to install the Claude desktop app (claude.ai/download), sign in, open the **Code** tab, create and choose a new empty folder (for example `Documents/Job Search`), and send the same message there. Stop.
- If they say they're on the Free plan: say jobscan needs Claude Code, which Free doesn't include; Pro or higher is required. Stop.

## 2. Say what it is (short)
In a few lines: jobscan finds new jobs on a schedule and scores them against rules they choose, shows them on a private board, and when they press Apply it tailors an honest resume, writes a letter and note, and fills the form, always stopping before submit. It never submits, sends, messages or connects for them. Their data stays in a private folder on their computer and in their own Claude account.

Then, plainly: **jobscan only works with Claude installed in your browser** (Google Chrome with the Claude in Chrome extension, signed in to this same Claude account). That's how it reads job sites and fills application forms.

Also say: setup asks a lot of questions (it's their job search, so they make every choice), can be paused any time, and uses part of their plan's usage. Ask to begin.

## 3. Claude in Chrome (first; blocks everything else)
1. Google Chrome installed? If not: google.com/chrome, install, open it.
2. The Claude extension: in Chrome, open the Chrome Web Store, search "Claude", add **Claude** (by Anthropic), pin it to the toolbar, open it and **sign in with the same Claude account** as this app.
3. Test: load the Chrome tools (ToolSearch "select:mcp__claude-in-chrome__tabs_context_mcp") and call `tabs_context_mcp` with `createIfEmpty: true`. Tell them first that a new Chrome window or tab group may open. It passes when it returns a tab group with a tab (it never lists their own tabs; a plain call without `createIfEmpty` only says the session has no tab group yet, which is not a failure).
   - Fails: walk through the extension's own connection steps (open the extension, check it says connected, restart Chrome, then try again). Don't continue until this test passes. If it still fails after two tries, stop and tell them setup will continue once Chrome connects ("continue jobscan setup").
(Signing in to job sites comes later, after they pick which sites to search.)

## 4. Install the plugin (skip if the jobscan skills are already loaded)
- Run `claude plugin install jobscan --marketplace stephenprescott/jobscan` from the shell. Show them the command first.
- If the shell says `claude` isn't found (common when only the desktop app is installed): ask them to type this in the chat instead: `/plugin install jobscan --marketplace stephenprescott/jobscan`
- Then ask them to type `/reload-plugins` in this chat (you can't run it for them) so the jobscan skills load, and then say "continue jobscan setup".

## 5. The data folder (right after the plugin loads)
- Ask where to keep their jobscan folder: `references/questions.md` § Install → `data_folder_location`. Recommend **the folder this session is open in**, when it's empty (or holds only their resume; ignore a `.claude` folder, which the app may create) and isn't inside a git repo: the board's Apply button sends jobs to this session, and jobscan expects to run in its own folder.
- Refuse a folder inside a git repo (`git -C <folder> rev-parse` succeeds) or inside a shared or public synced folder; explain why (their resume, pay and personal answers would go with it).
- Copy every file from the plugin's `templates/` folder (see "Files and paths" in the setup skill) into it, keeping the folder tree. Never overwrite an existing file.
- Write `data_folder` in `jobscan.config.md`. Log the Phase 1 answers so far in `setup-progress.md`.
- If they chose a different folder than this session's: tell them to open **that folder** in the Code tab now and say "continue jobscan setup" there. Stop here; everything else happens in that session, so the board and Apply button connect to it.

## 6. Auto-update
Ask `references/questions.md` § Install → `auto_update`. If yes, tell them how: type `/plugin`, open **Marketplaces**, select **jobscan**, turn on auto-update.

## 7. Python and PDF tools
- Check `python --version` (Windows) or `python3 --version` (Mac). Missing: give the install link (python.org/downloads; on Windows tick "Add python.exe to PATH"), wait, and check again.
- Check the PDF libraries: `python -c "import pypdf, pypdfium2, PIL"`. Missing: ask, then run `python -m pip install pypdf pypdfium2 pillow`.
- Chrome (from step 3) is also used to print PDFs.

## 8. Claude Docs
Their base resume lives in a Claude Doc. Check the docs tools are available (load the docs skill or `guide`). If not, tell them to turn on Claude Docs in claude.ai settings (it's on every plan) and continue when done.

Tick Phase 1.
