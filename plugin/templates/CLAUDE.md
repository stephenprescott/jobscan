# Job search: shared context

Every Claude session in this folder reads this file first. It's written by `/jobscan:setup` from your answers; change facts here, not in each session.

## Who and the goal
- Name: [ ]
- Current situation: [ ]
- Next role I want, and why: [ ]
- Direction (step up / same level, better fit / change direction): [ ]
- Moving away from: [ ]

## Standing rules
- Draft only. Never submit an application, send a message, connect, follow or apply anywhere without my explicit OK. Forms stop before submit.
- Read-only on job sites: never click Easy Apply, save jobs or message anyone.
- Never invent experience. Every resume, letter or form claim comes from my approved base resume or `confirmed-facts.md`.
- Questions on my "Ask me each time" list (`applications/profile.md`) are always left blank and listed for me.
- Never write anything about why I left a job unless I give the exact wording.
- Never enter passwords, solve CAPTCHAs, or store my Social Security number, date of birth, license or bank details.
- Ask before deciding for me.

## Files
| Path | What |
|---|---|
| `jobscan.config.md` | Settings: resume and board links, mode, sources, schedule, apply outputs |
| `applications/criteria.md` | Job rules: filters, Want and Match scores, tiers, titles, target companies |
| `applications/profile.md` | Standard application-form answers |
| `applications/tracker.md` | One row per application |
| `applications/jobscan/` | Daily ranked job lists and `seen.csv` |
| `applications/postings/` | Saved posting text, one file per `/apply` |
| `confirmed-facts.md` | Facts beyond the base resume, and the "don't claim" list |
| `voice-rules.md` | Writing rules for cover letters and notes |
| `resumes/`, `cover-letters/` | Tailored PDFs, named `YYYY-MM-DD_Company_Role` |

This folder is private. Don't make it a git repo or put it in a shared or public synced folder.
