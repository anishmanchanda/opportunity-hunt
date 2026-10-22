# Open-source starter list — checked with the GitHub API on 2026-10-18

Picked for your stack (Python/FastAPI, TypeScript/React, RAG/agents, Swift). "gfi" = open issues labelled `good first issue`. "External merges" = of the last ~20–26 merged PRs, how many came from non-members (a rough measure of how newcomer-friendly a repo is). All 10 have a CONTRIBUTING.md and a commit in the last week.

## Suggested order

1. **dify** or **marimo**: fresh, barely-discussed issues and Python + React, which matches your full-stack work.
2. **docling** or **llama_index**: RAG repos that map directly to BookBuddy and Ask the Policy Book.
3. **vllm**: FastAPI serving layer and AI infrastructure; a bigger signal on a resume.

Comment on the issue to claim it before you start coding, and read the thread first.

## The list

| # | Repo | Stack / why it fits | gfi | External merges | Notes |
|---|---|---|---|---|---|
| 1 | [langgenius/dify](https://github.com/langgenius/dify) | Python backend + React/TS frontend; RAG, agents, workflows | 12 | 12 of 25 | Best for fresh issues: #43787 (Oct 10), #43768 (Oct 9), #43358 (Oct 2), each with 3–5 comments |
| 2 | [marimo-team/marimo](https://github.com/marimo-team/marimo) | Python notebook backend + React/TS | 3 | 11 of 22 | Newest gfi #11176 (Oct 11), 2 comments |
| 3 | [docling-project/docling](https://github.com/docling-project/docling) | Python document parsing for RAG (IBM / LF AI) | 3 | 25 of 26 | Very newcomer-friendly: a first-timer's PR was merged 6 days after opening. Few labelled issues, so also look at bugs and "help wanted" |
| 4 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | Python RAG framework | 3 | all recent merges external | Activity is bursty. gfi #23339, #23246, #22947 |
| 5 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | Python; OpenAI-compatible FastAPI server, inference | 18 | 14 of 19 | Newest gfi are from Mar–Apr with 15–30 comments, so check they're not already claimed |
| 6 | [langfuse/langfuse](https://github.com/langfuse/langfuse) | TypeScript (Next.js) + Postgres; LLM observability and evals | 1 | 17 of 23 | Maps to your LLM-as-a-Judge work. Few labelled issues but strong external merges |
| 7 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python agents framework | 10 | only 2 of 21 | Unclaimed gfi #8069–#8071 (Oct 12), but maintainer-heavy, so expect slower merges |
| 8 | [tldraw/tldraw](https://github.com/tldraw/tldraw) | TypeScript/React canvas SDK | 6 | 14 of 22 | Newest gfi is from June |
| 9 | [apple/swift-argument-parser](https://github.com/apple/swift-argument-parser) | Swift; Apple-org credibility | 5 | 22 of 26 | Labelled issues are old (2022–2025). An outside PR was merged in ~16 days |
| 10 | [realm/SwiftLint](https://github.com/realm/SwiftLint) | Swift; adding lint rules is a well-scoped newcomer task | 8 | 12 of 16 | gfi labels are stale (newest Oct 2024) |

## Checked and left off

- **fastapi, langchain, litellm, openai-agents-python, mem0, haystack, mastra:** zero open good-first-issues. For FastAPI you can still help with docs, translations and reviewing PRs.
- **chroma:** its gfi labels are from 2024, so they're stale.
- **autogen:** effectively in maintenance.

## Paid and structured programs (dates not announced yet for 2027)

- **Season of KDE:** official page still shows only the 2026 cycle (applications closed 2026-01-14). Expect an announcement around mid-December.
- **Summer of Bitcoin:** the 2026 cycle ran applications Feb 1–15.
- **GSoC:** 2026 contributor applications were Mar 16–31; the 2027 timeline isn't posted yet.
- **Outreachy:** the December 2026 round's initial applications closed 2026-08-31. May 2027 dates aren't announced.
- **LFX Mentorship 2027 Term 1:** mentee applications 2027-02-03 to 02-16 (CNCF schedule); term runs Mar–May 2027.
- **MLH Fellowship:** its FAQ says it isn't open to India/APAC applicants.
