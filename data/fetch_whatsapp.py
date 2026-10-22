import sqlite3, shutil, os, re, json, subprocess

SRC = os.path.expanduser(
  "~/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite")
STATE = os.path.expanduser("~/.elip_state.json")
KEEP = re.compile(r"full ?stack|backend|ai\b|ml\b|software|sde|python|react|node|developer", re.I)
SKIP = re.compile(r"product manag|\bapm\b|growth|sales|embedded|java\b|flutter|analyst", re.I)

last = json.load(open(STATE))["last"] if os.path.exists(STATE) else 0

shutil.copy(SRC, "/tmp/wa.sqlite")
db = sqlite3.connect("/tmp/wa.sqlite")
rows = db.execute("""
SELECT m.ZMESSAGEDATE, m.ZTEXT
FROM ZWAMESSAGE m JOIN ZWACHATSESSION c ON m.ZCHATSESSION = c.Z_PK
WHERE c.ZPARTNERNAME LIKE '%Jobs Internships%' AND m.ZTEXT IS NOT NULL
  AND m.ZMESSAGEDATE > ?
ORDER BY m.ZMESSAGEDATE ASC
""", (last,)).fetchall()

# "1. *Title* · _Company_ · 0–2 yrs\n     elip.cc/xxxx"
pat = re.compile(r"\*(.+?)\*\s*·\s*_(.+?)_(?:\s*·\s*([^\n]*))?\s*\n\s*(elip\.cc/\S+)")
hits = []
for ts, text in rows:
    for title, company, exp, link in pat.findall(text):
        if KEEP.search(title) and not SKIP.search(title):
            hits.append(f"{title} | {company} | {exp or '-'} | https://{link}")

for h in hits:
    print(h)

if rows:
    json.dump({"last": rows[-1][0]}, open(STATE, "w"))
if hits:
    subprocess.run(["osascript", "-e",
        f'display notification "{len(hits)} new matching roles" with title "Elip jobs"'])
