# Job criteria

The only rules Jobscan and `/apply` use to judge a posting. Written by `/jobscan:setup` from your answers. Every `[ ]` is blank until you answer.

## How a posting is judged
1. **Filters** (pass/fail). Fail any one and the job is dropped.
2. **Want score**. How well the job fits what you want.
3. **Match score** (0–5). How well you meet the job's required qualifications.
4. **Tier** (from both scores). Decides how much work `/apply` does.
The daily list shows Want and Match as separate columns, sorted by Want + Match (highest first; ties by Match).

## 1. Filters (any fail = drop)
- **Role:** keep: [ ]. Drop: [ ] (kinds of roles you don't want, e.g. mainly building reports for requesters).
- **Pay:** target [ ]. Lowest you'd accept: [ ].
  - Drop if the top of the posted range is under: [ ]
  - No range posted: [ ] (keep / keep only at certain levels / drop)
  - Hourly gigs and piece work: [ ]
  - Full-time or contract-to-hire roles posted with an hourly range (common in healthcare) are not gigs: compare them at hourly x 2,080.
- **Location:** [ ] (remote US / hybrid / on-site). Max commute from home: [ ] minutes. Remote jobs must allow my state: [ ].
- **Employment type:** [ ] (full-time / contract-to-hire and its minimum hourly rate / contract).
- **Travel:** at most [ ].
- **Duplicate:** already in `tracker.md` or `jobscan/seen.csv`: drop.
- **Level:** drop [ ] (levels too junior or too senior). Drop roles requiring [ ]+ more years than I have, in total or in the specific area the posting names (compare with my years by area in § 3).
- **Clearance:** [ ] (drop roles needing an active clearance I don't have / keep).
- **Recruiters and aggregators:** [ ] (drop postings that hide the real employer / keep).
- **My own filters:** [ ]

## 2. Want score
Categories and points are yours. Total possible: [ ].

| Points | What earns them |
|---|---|
| [ ] | [ ] |

## 3. Match score (0–5)
Compare the posting's **required** qualifications (not nice-to-haves) with the base resume and `confirmed-facts.md`, including its "don't claim" list. Read both before scoring, every run. Never estimate Match from memory.

| Match | Meaning |
|---|---|
| 5 | Meets every required qualification |
| 4 | Meets every must-have. Misses only nice-to-haves, or one tool where a close equivalent counts |
| 3 | Misses one must-have |
| 2 | Misses two must-haves |
| 0–1 | Misses three or more |

- **My years of experience:** [ ] (total, and by area). A posting asking for this many or fewer is never a gap.
- **Close equivalents that count:** [ ] (tools you've used that cover similar ones). A 4 allows at most one substitution.
- "Don't claim" items are real gaps when required.
- Name gaps in the "gaps" note, must-haves first.

## 4. Tiers
- **A:** Want [ ]+ and Match [ ]+.
- **B:** Want [ ]+ and Match [ ]+, not A.
- **C:** everything else that passes the filters.
- A company on the target list below is always Tier A when Match is [ ]+.
- **Board default ("fit" filter):** Want [ ]+ and Match [ ]+.

## Titles to search
- **Main:** [ ]
- **Stretch:** [ ]

## Sources
Set in `jobscan.config.md` (`sources`). Notes on searching any of them:
- State job site: [ ] (name, address and how to search it, found during setup)

## Target companies
Searched on their own career sites every scan (the scan window doesn't apply; each current matching opening is shown once).

| Company | Job system | How to read it |
|---|---|---|
