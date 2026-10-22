# WhatsApp group source (Elip x GGSIPU - Jobs Internships)

`data/fetch_whatsapp.py` reads the "Elip x GGSIPU - Jobs Internships" group from WhatsApp's local database. It keeps engineering titles (backend, AI/ML, full-stack, SDE, Python, React, Node, developer) and drops PM, APM, analyst, growth, sales, embedded, Java and Flutter roles. Each match is one line:

```
Title | Company | Experience | https://elip.cc/xxxx
```

`/hunt` reads `data/whatsapp-links.txt` on every run (Pass B, item 6).

## Files
| Path | What |
|---|---|
| `data/fetch_whatsapp.py` | the script |
| `data/whatsapp-links.txt` | output; cron appends new matches |
| `~/.elip_state.json` | timestamp of the last message read, so each run picks up only new messages. Delete it to re-read the whole chat. |
| `/tmp/wa.sqlite` | temporary copy of the WhatsApp database |
| `data/whatsapp-cron.log` | errors from the cron job |

## One-time setup
1. **Grant Full Disk Access.** WhatsApp's database is protected by macOS, so whatever runs the script needs Full Disk Access. Open System Settings → Privacy & Security → Full Disk Access and add:
   - your terminal app (Terminal or iTerm), for manual runs
   - `/usr/sbin/cron`, for the daily job. In the file picker, press Cmd+Shift+G and type `/usr/sbin/cron`.
2. **Test it by hand** from that terminal:
   ```bash
   cd ~/Downloads/opportunity-hunt && python3 data/fetch_whatsapp.py >> data/whatsapp-links.txt && tail data/whatsapp-links.txt
   ```
   The first run reads the whole chat history; later runs read only new messages.
3. **Install the daily cron job** (runs at 08:00). Run `crontab -e` and add this line:
   ```
   0 8 * * * cd "$HOME/Downloads/opportunity-hunt" && /usr/bin/env python3 data/fetch_whatsapp.py >> data/whatsapp-links.txt 2>> data/whatsapp-cron.log
   ```
   Check that it's installed with `crontab -l`. Cron doesn't run while the Mac is asleep; a missed day is picked up on the next run, because the state file tracks the last message read.

## If the script fails
- **`PermissionError: Operation not permitted`:** Full Disk Access is missing for whatever ran the script (your terminal, or `/usr/sbin/cron` under cron). Grant it, then quit and reopen that app.
- **`no such table: ZWAMESSAGE`, or 0 results after a WhatsApp update:** WhatsApp changed its database layout. Check the table names with `sqlite3 /tmp/wa.sqlite .tables`.
- **No lines for days, though the group is active:** the group may have been renamed, so the `LIKE '%Jobs Internships%'` filter misses it. Or the message format changed, and the `*Title* · _Company_ · exp` + `elip.cc/...` pattern no longer matches.
- **Missed messages:** delete `~/.elip_state.json` and run the script once by hand.
- **`whatsapp-links.txt` is empty during a hunt:** `/hunt` reports it under SEARCH COVERAGE and carries on with the other sources.

## How /hunt uses the links
elip.cc links redirect to `dashboard.tryelip.ai/jobs/<id>`, which needs a login, so the hunt usually can't open them directly. For each new line it:
1. dedups against `data/opportunities.csv` (company + role),
2. tries the link, and if it hits a login wall, searches the company's own careers page or ATS for the title,
3. adds it only once it's verified there; otherwise it lists it under SOCIAL SIGNALS.
