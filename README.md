# jobscan

A personal job search assistant that runs in your own Claude account. It finds new jobs on a schedule, scores each one against rules **you** choose, shows them on a private board, and when you press **Apply** it tailors an honest resume, writes a cover letter and a note to the hiring manager, and fills in the application form. It always stops before submit. You review everything and submit it yourself.

Built for people in data and tech roles (analytics, BI, data engineering and similar), but you set every rule, so you can shape it to your own search.

## Get started

A friend sent you here. In the Claude desktop app, open the **Code** tab, create and choose a new empty folder (for example `Documents/Job Search`), then copy this message and send it to Claude:

```text
My friend sent me a link to have their Jobscan app setup on my claude account. This link: https://github.com/stephenprescott/jobscan will give you all the information you need to help me set it up.
```

Claude installs jobscan and then walks you through every choice. Nothing about your search is pre-set: your resume, your target jobs, your pay range, which sites to search, how often, and what gets written for you are all your decisions.

## What you need

1. **Claude installed in your browser:** Google Chrome with the **Claude in Chrome** extension, signed in to the same Claude account. jobscan can't work without it: it's how Claude reads job sites and fills application forms.
2. A Claude **Pro plan or higher**. The Free plan doesn't include Claude Code.
3. The **Claude desktop app** (Windows or Mac) with the **Code** tab: [claude.ai/download](https://claude.ai/download).
4. **Python 3** (Claude checks for it and helps you install it if needed). It builds your resume PDFs.

## What setup covers

1. **Install:** checks the requirements above, installs jobscan, and creates a private jobscan folder on your computer.
2. **An honest base resume:** starting from your current resume, your LinkedIn PDF, or from scratch, Claude goes through each job with you: official titles and dates (what background checks verify), what you actually did, and numbers you can back up. It pushes back on anything inflated and keeps a "don't claim" list of skills you don't have yet. Every tailored resume is built only from this resume and facts you confirm.
3. **Your direction and job rules:** target titles, pay, location and commute, job types, travel, levels, what makes a job appealing to you (your "Want" score) and how well you fit it (your "Match" score).
4. **Scanning:** which job sites, Light or Full mode, how often, and how far back each scan looks.
5. **Applying:** what gets made for each tier of job, whether forms get filled, and which questions are always left for you.
6. **Your application answers and writing style.**
7. **Your board and schedule,** then a short test scan.

Setup asks a lot of questions, because it's your job search. You can stop at any point: say **continue jobscan setup** in your jobscan folder to pick up where you left off. To change a setting later, just ask ("change my pay floor", "add a target company").

## What it never does

- Never submits an application, sends a message, connects with or messages anyone, saves jobs, or clicks Easy Apply. Forms stop before submit.
- Never types your passwords or solves CAPTCHAs: you sign in to sites yourself.
- Never stores your Social Security number, date of birth, driver's license or bank details.
- Never invents experience. Resumes, letters and form answers use only your approved resume and facts you confirmed.

## Privacy

Your resume, rules, answers and job lists stay in your private jobscan folder on your computer and in your own Claude account. Nothing is sent to the author of jobscan. Don't make your jobscan folder a git repo, and don't put it in a shared or public synced folder.

## Usage

jobscan uses part of your Claude plan's usage, shared with your regular Claude chats. The heaviest parts are the setup interview (spread it over a few sittings if you like), each scan, and each Apply (resume, letter, note and form). Real numbers for a Pro plan aren't measured yet; they'll be added here from early users. You can watch your own usage in claude.ai under Settings → Usage.

On a Pro plan, Light mode with one scan a day is the comfortable choice. If a scan hits a usage limit, it saves what it found and the next scan picks up the rest.

## A note on job sites

jobscan reads job sites through your own signed-in browser, the way you would, and only reads (it never applies or messages). Even so, very heavy automated reading can trigger a site's limits or a temporary restriction on your account. Light mode and fewer scans a day keep this low.

## Updating

If you turned on auto-update during setup, fixes arrive by themselves; type `/reload-plugins` (or start a new session) to load them. Otherwise ask Claude to "update jobscan". Your board updates too: the next scan or Apply after an update republishes it for you, keeping all your jobs.

Open your board inside the Claude desktop app (not a web browser). Every Apply click queues the job either way, but in the app it also wakes your jobscan session right away.

## Getting help

Ask the friend who sent you this link. If you open a GitHub issue, never paste your resume, job lists, settings or any personal details into it: issues are public.

## For Claude: setting this up

You're Claude, and someone sent you the message above. Do this:

1. **Check where you are.** You need Claude Code with shell and file access (the Code tab of the Claude desktop app) and a Pro plan or higher. If you're in claude.ai chat, the phone app, or anything without a shell: tell them jobscan must be installed from the Claude desktop app's Code tab on a Pro plan or higher, give the download link (claude.ai/download), and ask them to open the Code tab in a new empty folder (e.g. `Documents/Job Search`) and send the same message there. If they're on the Free plan, say it can't run there and why. Install nothing, and stop.
2. **Explain briefly** what jobscan does and what it never does (above), that it needs **Claude in Chrome**, that setup asks many questions and can be paused, and that it uses part of their plan's usage. Ask to begin.
3. **Install** (show each step and get a yes first):
   - Claude in Chrome comes first: walk them through Chrome, the extension, signing in to the same account, and test it by calling `tabs_context_mcp` with `createIfEmpty: true` (it may open a new Chrome tab group; it passes when it returns a tab group with a tab). Don't continue until that test passes.
   - Then install the plugin from the shell: `claude plugin install jobscan --marketplace stephenprescott/jobscan`. If `claude` isn't found, ask them to type `/plugin install jobscan --marketplace stephenprescott/jobscan` in the chat.
   - Ask them to type `/reload-plugins` in the chat so the jobscan skills load (you can't run it for them), then to say "continue jobscan setup".
4. **Run `/jobscan:setup`** (start the `jobscan:setup` skill with the Skill tool, so its file paths are filled in). That skill carries the whole interview (Python check, data folder, honest resume, every rule, board, schedule, test run) and is the source of truth: follow it exactly. They make every personal decision; you recommend.

## License

MIT. See [LICENSE](LICENSE).
