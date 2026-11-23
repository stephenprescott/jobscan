---
name: setup
description: Install and personalize jobscan for a new user. Use when someone says a friend sent them a jobscan link and asks to set it up, types /jobscan:setup, says "continue jobscan setup", or asks to change one of their jobscan settings ("change my pay floor", "redo my job rules"). Walks them through every decision in a resumable interview, starting with an honest base resume.
---

# jobscan setup

You're setting up jobscan for someone who may not be technical. They make **every** personal decision; you recommend, explain, and write down what they choose. Nothing personal is pre-filled or guessed.

## How to ask
- Use `AskUserQuestion` cards. Up to 4 related questions per card, each with 2–4 concrete choices. Put your recommended choice first and label it "(Recommended)", with a one-line reason in its description. "Other" is always available for their own answer.
- Open-ended facts (their name, what they did in a job) are asked as plain questions in chat, one topic at a time.
- Plain words. Explain jargon in a few words the first time (e.g. "Match score: how well you meet a job's must-have requirements").
- Never use anyone else's values as defaults. Example choices are generic.
- If they say "you pick", give your recommendation and ask them to confirm it; record it as their choice only when they say yes.

## Resumable (always)
- The progress file is `setup-progress.md` in their jobscan folder. **Before asking anything**, read it if it exists, and continue at its "Current position", without re-asking anything already in "Answers".
- After **every** answer: write it to its target file (per `references/questions.md`) and append a line to "Answers" (`date | phase | question id | answer | file/key`), then update "Current position". Do this before asking the next question, so a usage limit or a closed app loses nothing.
- When a phase is done: play back what was set in a few lines, let them change anything, then tick the phase.
- If they need to stop: say "Say **continue jobscan setup** in your jobscan folder any time to pick up where you left off."
- "Change my <setting>" later: find that question in `references/questions.md`, ask only it, write it, and log it.

## Phases (in order)
1. **Preflight, install and data folder:** follow `references/preflight.md`. Claude in Chrome comes first, and setup does not go on until the browser test passes. Then create their jobscan folder from `${CLAUDE_PLUGIN_ROOT}/templates` (copy the whole tree; never overwrite an existing file) and write `data_folder` in `jobscan.config.md`.
2. **Honest base resume:** follow `references/honest-resume.md`. It comes before the job rules because scoring and tailoring depend on it.
3. **Direction:** `references/questions.md` § Direction. Write the answers to `CLAUDE.md` § Who and the goal.
4. **Job rules:** § Job rules, written to `applications/criteria.md` (and the config keys named there).
5. **Scan setup:** § Scan.
6. **Apply setup:** § Apply.
7. **Application profile:** § Profile, written to `applications/profile.md`.
8. **Writing rules:** § Writing. Show each default rule in `voice-rules.md`; they keep, change or drop it.
9. **Board and schedule:** follow `references/finish.md` (publish the board, settings, pin, scheduled scan).
10. **Test run and daily routine:** `references/finish.md` § Test run.

Rough time: phases 1–2 take the longest (installing, and the resume interview, about 30–60 minutes). The rest is mostly clicking choices. Tell them it can span several sittings.

## Rules that never bend
- Honesty first: the resume and `confirmed-facts.md` hold only what they confirm. See `references/honest-resume.md`.
- Ask before every install, download, or account action, and show what it does. They sign in to sites themselves; never type their passwords, never solve CAPTCHAs.
- Never store passwords, Social Security number, date of birth, driver's license or bank details.
- The jobscan folder must never be a git repo or sit in a shared or public synced folder.
- Nothing about why they left a job unless they give the exact wording.
