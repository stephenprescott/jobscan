# Job sources

The scan searches only the source ids listed in `sources` in `jobscan.config.md`. Every enabled source is searched every run. `<query A>` and `<query B>` are built from the titles in `applications/criteria.md` (see the skill, step 2). `<since>` values come from `scan_window.py`.

**Location modes**, both run for each source unless the user's rules exclude one:
- **Remote, all of the US:** location "United States" plus the site's Remote filter (not a city).
- **Local:** the user's metro area around `home_zip`, radius matching `max_commute_minutes` (about 25 miles for 30 minutes). Skip this mode if the user wants remote only.

| id | Source | How |
|---|---|---|
| `linkedin` | LinkedIn | `linkedin.com/jobs/search/?keywords=<query>&f_TPR=<linkedin_f_TPR>` with `location=United States&f_WT=2` (remote), then `location=<user's metro>&distance=25` (local). Requires the user to be signed in |
| `indeed` | Indeed | `indeed.com/jobs?q=<query>&fromage=<indeed_fromage>` with `l=Remote`, then `l=<home_zip>&radius=25` |
| `google_jobs` | Google Jobs | Google "<query> jobs remote" and "<query> jobs <user's city>", open the Jobs panel, date filter matching `google_tbs` (past day / past week). Picks up boards not searched directly (ZipRecruiter, Glassdoor, Monster, state job banks) |
| `hiring_systems` | Employer hiring systems | Two Google searches with `&tbs=<google_tbs>`: (1) `site:boards.greenhouse.io OR site:job-boards.greenhouse.io OR site:jobs.lever.co OR site:jobs.ashbyhq.com <query> (remote OR "<user's city>")`; (2) the same with `site:myworkdayjobs.com OR site:icims.com OR site:jobs.smartrecruiters.com` |
| `builtin` | Built In | builtin.com/jobs/remote, search each query, newest first |
| `wellfound` | Wellfound | wellfound.com/jobs, remote, the user's role types |
| `dice` | Dice | dice.com/jobs, query + Remote, then + the user's city, posted-date filter matching the window. Expect many recruiter postings |
| `state_site` | The user's state job site | As written in `applications/criteria.md` § Sources (found during setup). Usually lists newest first with a posted date; open each match to read pay |
| `usajobs` | USAJobs | usajobs.gov/search with the user's main titles, location Remote and the user's city, sorted newest. Apply the clearance filter and check GS pay against the pay filter. In `light` mode, at most once a day |
| `target_companies` | Target companies' own career sites | Read every company in `applications/criteria.md` § Target companies, using its "How to read it" note. Read the **whole current list** (the scan window doesn't apply), keep titles matching the user's titles or role keywords, and show any not already in `seen.csv` or `tracker.md`. Note the posting age in flags ("posted 9 days ago"). If a site's address changed, find the new one from the company's careers page and update the table |

**Light vs full mode**
- `light`: the scan reads each source's results list and opens only the listings that pass the pre-filter **and** show a title from the user's main titles; stretch titles are opened only when the list shows pay at or above the user's floor.
- `full`: open every listing that passes the pre-filter.
- In both modes every enabled source is searched; nothing is skipped "for time".

Not worth searching (their listings copy the sources above): SimplyHired, Glassdoor, ZipRecruiter, CareerBuilder, Monster. Google Jobs catches what they carry.
