---
description: Mark opportunities as applied, e.g. /applied emotorad (email), temple swe intern
argument-hint: <company or id> [(email|linkedin|portal)] [, more...]
---

Mark these as applied in data/opportunities.csv: $ARGUMENTS

For each item (comma-separated):
1. Find the matching row(s) by id, company or role with Python's csv module
   (case-insensitive, partial match). If more than one row matches, list
   them and ask which one; if none matches, ask whether to add a new row.
2. Set prev_status = the current status, status = "applied",
   applied_on = today (YYYY-MM-DD) unless I gave a date, and applied_via =
   the channel I gave, or else infer it from apply_url (mailto: → email,
   linkedin.com → linkedin, anything else → portal).
3. Copy the file to data/opportunities.bak.csv, then rewrite it with
   csv.DictWriter in the same column order.

Then print one line per row changed, plus how many rows are now "applied".
