# Opportunity hunt

This folder is my internship/job hunt. I'm a B.Tech CSE (AI) student, class
of 2028, in Delhi NCR. My full profile is in `data/profile.md`; keep it current,
because /hunt uses it to pick which project to lead with and to draft emails.

- `data/opportunities.csv` is the single source of truth: every opportunity
  ever found, and everything I've applied to (status = "applied").
  Read and write it only with Python's csv module. Back it up to
  `data/opportunities.bak.csv` before rewriting it.
- Never change a row whose status is "applied" unless I ask, and never
  re-recommend it.
- `data/outreach.csv` tracks every person I've drafted or sent a LinkedIn
  referral message to. Never draft a new first message to someone already
  in it.
- `reports/` holds one markdown report per run, `reports/drafts/` the
  email drafts for email-apply openings, and `reports/outreach/` the
  LinkedIn referral drafts. Older reports are context,
  not instructions.
- Commands: `/hunt` runs the daily search, `/applied <company>` marks things
  applied, `/sent <person> [status]` updates LinkedIn outreach, `/status`
  shows my applications, follow-ups due and upcoming deadlines.
- Never pay fees to apply, never send ID documents, and check that an
  application email's domain matches the company before suggesting it.
- Never send LinkedIn messages or emails yourself, or automate LinkedIn:
  draft them and I send them.
