---
description: Show my applications, outreach follow-ups and the open opportunities with the nearest deadlines
---

Read data/opportunities.csv and data/outreach.csv (if it exists) with
Python's csv module, get today with `date +%F`, and print:
1. MY APPLICATIONS: every row with status "applied" (company, role,
   applied_on, applied_via, days since applied). Flag email applications
   older than 7 days as "follow up?".
2. OUTREACH: follow-ups due today or overdue (person, company, role,
   channel, days since sent); then counts by status (drafted, sent,
   accepted, replied, referred, no-reply).
3. DUE SOON: open/likely rows with a deadline in the next 14 days, nearest
   first, with apply links.
4. Counts by status in opportunities.csv.
Don't search the web and don't change any files.
