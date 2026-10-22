# Hi, I'm Anish 👋

B.Tech CS (AI) student at USICT, Delhi (2028). I build backend systems, AI pipelines, web and native apps, and whatever a hackathon problem statement throws at me. I like debugging things down to the byte.

## ⚡ What I do

- **Backend & APIs:** Python, FastAPI, Node.js/Express, REST, async processing
- **AI/GenAI systems:** RAG (FAISS + BM25 hybrid retrieval), multi-provider LLM integration, agentic workflows, LLM-as-a-Judge evaluation
- **Full-stack:** React, Next.js, PostgreSQL, MongoDB, SQLite
- **Native Apple apps:** Swift, SwiftUI, AppKit, watchOS, Bluetooth protocols
- **Infra:** Docker, CI/CD (GitHub Actions), AWS, Linux

## 🛠 Featured work

**Ask the Policy Book:** a compliance Q&A service I built solo for a hiring challenge. It answers from a fixed set of 34 documents with verbatim source quotes, role-based access control, and different refusals for "not found" vs "above your clearance".
- Ran **16 numbered experiments**, each with a hypothesis, a measurement and a decision. They showed that a 4-point recall gain moved answer correctness by under 2 points, so the bottleneck was answer synthesis, not retrieval.
- I instrumented the pipeline instead of trusting the "slow model" assumption. Generation took 2.5s; the other ~50s was my own code queued behind a provider rate cap. Fixing it cut latency **34x** with no model or prompt change.
- 🔒 The repo is private under the challenge terms. Happy to walk through it.

**BookBuddy (Pepper Labs AI):** a production RAG pipeline for CUET exam prep, using hybrid FAISS + BM25 retrieval with citation-aware context.
- Built a multi-provider LLM layer (OpenAI, Gemini, Groq, SambaNova) with failure handling and fallback, and migrated the backend off Mistral.
- Traced an async bug that fired every LLM call **3x per request** and fixed it so each request makes one call.
- 🔗 [bookbuddy.pepperlabsai.com](https://bookbuddy.pepperlabsai.com/)

**MaterialMover:** a full-stack marketplace for reusing construction waste (UN SDG 12).
- React/Vite frontend, Node/Express API and FastAPI AI-search service, with PostgreSQL + MongoDB, JWT auth, Cloudinary and Mapbox.
- Agentic AI advisor with hybrid RAG (Sentence Transformers + BM25) over live inventory. Dockerized on DigitalOcean with GitHub Actions CI/CD.
- 🔗 [Live](https://home-server.tail9060c1.ts.net) · [GitHub](https://github.com/Aryannnthakurrr/MaterialMover)

**Sorted (AzinHack 2026):** an LLM agent system that compiles its own repeated work into tested code.
- After 3 similar bills, a compiler agent writes a parser plus tests that must pass AST safety checks, a no-network sandbox and held-out tests, cutting LLM calls ~60% (12 → 5/month) in a 6-month simulation.
- Self-repair and safety: shadow mode, LLM fallback and a v2 recompile when a bank changed its email layout; PII redaction, OTP filter, prompt-injection guard. Parsers scored 100% field accuracy on 76 synthetic messages.
- TF-IDF + logistic-regression classifier with a confidence threshold; Telegram bot, MCP server for Claude Desktop/Cursor, TinyFish web-agent integration, 54 offline tests.
- 🔗 [GitHub](https://github.com/anish-codes/sorted)

## 🌱 Open source

**sony-ult-ctl** ([open PR](https://github.com/Leonard013/sony-ult-ctl/pull/1)): a macOS menu-bar app controlling Sony ULT WEAR headphones over Bluetooth RFCOMM.
- Reverse-engineered the undocumented binary protocol by probing candidate payloads and reading the firmware's status replies. Found the level byte the device was ignoring and fixed ambient-sound control that had never worked.
- Added a live 0–20 transparency slider and voice-passthrough toggle in SwiftUI.
- Rebuilt the receive path to be event-driven: every packet is acked and handled on arrival, and replies are matched to queries. Also fixed the app being silently killed by macOS (unsealed Info.plist in the code signature).

**Agent Watch** ([my fork](https://github.com/anishmanchanda/claude-watch) of [shobhit99/claude-watch](https://github.com/shobhit99/claude-watch)): approve your coding agent's actions from your Apple Watch.
- Rewrote notification delivery on watchOS and iOS, with actionable buttons generated per request so each prompt shows its real options.
- Split the bridge server's hook routes to match Claude Code's contract, and fixed cross-agent session collisions.
- Added background polling and persistent pairing, plus **Codex support** by tailing its JSONL session logs.
- All of it was debugged on a physical iPhone + Watch, because the simulator can't reproduce wrist-down, mDNS or background-budget behaviour.

**DockWidgets** ([GitHub](https://github.com/anishmanchanda/DockWidgets)): a native macOS utility that places widgets in unused Dock space, with media controls for Spotify and Apple Music.

## 💼 Experience

- **Pepper Labs AI**, AI/ML Intern (June–Aug 2026): shipped the BookBuddy RAG pipeline to production, built the multi-provider LLM layer and fixed the 3x-call concurrency bug.
- **MCT India Infotech**, Backend Engineering Intern (April–May 2026): Python backend for a real-time conversational voice agent (session orchestration, multi-turn streaming, REST integrations), plus an LLM-as-a-Judge evaluator that ran scheduled regression checks over call logs.
- **Indian Audit & Accounts Department**, Computer Vision Intern (Feb–Mar 2026): OCR pipeline digitising handwritten rural invoices into SQL, with Chart.js dashboards; received a written appreciation note from the department (Jul 2026).
- **Excel Health-Tech Devices**, Software Engineer Intern (Dec 2025–Jan 2026): WhatsApp-first inventory system in FastAPI with an async expiry-alert scheduler for a 10+ person team.

## 🧰 Stack

`Python` `TypeScript/JavaScript` `SQL` `Swift` `C/C++` `Java` `FastAPI` `Node.js` `Express` `React` `Next.js` `SwiftUI` `PostgreSQL` `MongoDB` `SQLite` `FAISS` `Docker` `GitHub Actions` `AWS` `Git` `Linux`

## 🤝 Let's connect

[LinkedIn](https://linkedin.com/in/anish-manchanda) · [GitHub](https://github.com/anishmanchanda) · anishmanchanda2006@gmail.com
