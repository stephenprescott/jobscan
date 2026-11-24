---
data_folder: null  # full path in single quotes or with forward slashes; double quotes break on Windows backslashes
resume_doc_url: null
board_url: null
board_version: null
state: null
home_zip: null
max_commute_minutes: null
mode: null
sources: []
window: null
window_cap_days: 3
last_successful_scan: null
scan_times: []
notify: null
fit_bar:
  want: null
  match: null
apply_outputs:
  A: []
  B: []
  C: []
hm_search:
  A: null
  B: null
  C: null
form_fill: null
resume_max_pages: null
auto_update: null
---

# jobscan settings

The settings above are written by `/jobscan:setup` from your answers. To change one, ask Claude ("change my scan times") or rerun setup for that section. Edit by hand only if you know YAML.

| Key | Meaning |
|---|---|
| `data_folder` | This folder's full path |
| `resume_doc_url` | Your base resume (a Claude Doc) |
| `board_url` | Your Jobscan Board page |
| `board_version` | Version of the board page last published to your account; jobscan republishes it when an update brings a newer one |
| `state`, `home_zip`, `max_commute_minutes` | Where you live, for the commute check and your state's job site |
| `mode` | `light` (fewer sources, lower usage, good for Pro) or `full` (every source, every listing opened) |
| `sources` | Job sites to search. Ids: `linkedin`, `indeed`, `google_jobs`, `hiring_systems` (Greenhouse, Lever, Ashby, Workday and similar via Google), `builtin`, `wellfound`, `dice`, `state_site` (your state's job site), `usajobs`, `target_companies` (your target companies' own career sites) |
| `window` | `since_last` (everything since the last successful scan, up to `window_cap_days` back) or `24h` (last 24 hours only) |
| `window_cap_days` | How far back a `since_last` scan may reach (days) |
| `last_successful_scan` | Set by the scan itself after a complete run. Don't edit |
| `scan_times` | Times of day the scheduled scan runs, `HH:MM` |
| `notify` | Desktop notification after each scan (`true`/`false`) |
| `fit_bar` | The board's default filter: show jobs with Want at or above `want` and Match at or above `match` |
| `apply_outputs` | Per tier, what `/apply` makes: any of `resume`, `cover_letter`, `hm_note` |
| `hm_search` | Per tier, whether `/apply` searches LinkedIn for the hiring manager (`true`/`false`) |
| `form_fill` | Whether `/apply` fills the application form (always stops before submit) |
| `resume_max_pages` | Page limit for tailored resumes (1 or 2) |
| `auto_update` | Whether you turned on plugin auto-update |
