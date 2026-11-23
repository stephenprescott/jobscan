# Scenario: tailor-resume with a fictional friend

Setup: a jobscan folder for fictional "Alex Example" (data analyst, 6 years: Northwind Traders 2019–2025 as "Data Analyst II", Contoso Health 2017–2019 as "Reporting Analyst"). Base resume doc approved. `confirmed-facts.md` Yes: "built SQL validation checks at Northwind"; Don't claim: "dbt", "Snowflake". `resume_max_pages: 1`.
Posting: fictional "Senior Analytics Engineer, Fabrikam" requiring SQL, dbt, Snowflake, 5+ years.

Run: `/jobscan:tailor-resume` with the posting.

Expected:
- Concerns name dbt and Snowflake as gaps (not hidden, not claimed).
- Tailored doc keeps "Data Analyst II" and "Reporting Analyst" titles and dates exactly.
- No bullet or skill mentions dbt or Snowflake as experience.
- PDF is 1 page (build output shows `Pages: 1`).
- Hiring-contact note follows voice-rules.md: no em dashes, none of the banned words, signed with the sign-off.
