---
description: Update my LinkedIn outreach, e.g. /sent priya microsoft (inmail) · /sent rahul replied · /sent ananya referred
argument-hint: <person and/or company> [sent|accepted|replied|referred|declined] [(connect|inmail|dm|post-reply)] [, more...]
---

Update data/outreach.csv for: $ARGUMENTS

For each item (comma-separated):
1. Find the row by id, person or company with Python's csv module
   (case-insensitive, partial match). If several match, list them and ask
   which; if none matches, ask whether to add a new row (person, company,
   role, channel).
2. Status word missing → "sent". Then:
   - sent: status = sent, sent_on = today, follow_up_on = today + 6 days,
     channel = the one I gave (keep the existing one otherwise).
   - accepted: status = accepted, follow_up_on = today + 4 days (time to
     send the post-accept message from the drafts).
   - replied / referred / declined: set that status and clear
     follow_up_on. For referred, also set the matching row in
     data/opportunities.csv (opportunity_id) notes to start with
     "REFERRED by <person> <date>." without changing its status.
   - Today = `date +%F`.
3. Back up to data/outreach.bak.csv, then rewrite the file with
   csv.DictWriter in the same column order.

Print one line per row changed, then the follow-ups due in the next 3 days.
