# Opportunity hunt — Claude Code setup

Everything lives in this folder, so every run knows what you've already
found and applied to.

    data/opportunities.csv   all 280 opportunities so far (EMotorad already marked applied)
    reports/                 one report per run
    .claude/commands/        /hunt, /applied, /status
    CLAUDE.md                rules Claude Code reads every time it opens this folder
    .mcp.json                Tavily + Firecrawl search tools

## One-time setup

1. Install Node.js 18+ and Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Put this folder somewhere permanent (e.g. Documents/opportunity-hunt).
3. Add your API keys as environment variables (Tavily: app.tavily.com, free
   tier; Firecrawl: firecrawl.dev):
   - macOS/Linux: add `export TAVILY_API_KEY=...` and
     `export FIRECRAWL_API_KEY=...` to ~/.zshrc or ~/.bashrc
   - Windows: `setx TAVILY_API_KEY "..."` and `setx FIRECRAWL_API_KEY "..."`,
     then open a new terminal
4. `cd` into the folder and run `claude`. Approve the two MCP servers when
   asked, and run `/mcp` to check that both are connected.
5. Optional: `git init`, then commit after each run so you have history
   (and a backup on a private GitHub repo if you want it on other machines).

## Daily use

    claude            then type:
    /hunt             run the search; updates the CSV and saves reports/DATE.md
    /applied emotorad, temple swe intern (email)
    /status           your applications + deadlines in the next 14 days

You can also open data/opportunities.csv in Excel/Sheets and set status to
`applied` yourself. Save it as CSV, keep the column names, and close it
before running /hunt.

## Running it automatically (optional)

This only runs while your laptop is on and logged in.

- macOS/Linux (cron, 3:05 PM daily): `crontab -e`, then
  `5 15 * * * cd ~/Documents/opportunity-hunt && claude -p "/hunt" >> reports/cron.log 2>&1`
- Windows: Task Scheduler → Create Basic Task → Daily → Program `cmd`,
  arguments `/c cd /d C:\Users\YOU\Documents\opportunity-hunt && claude -p "/hunt" >> reports\cron.log 2>&1`

Headless runs use the permissions in .claude/settings.json, so they don't
stop for approvals. Nothing pings your phone: check reports/ for the newest
file.
