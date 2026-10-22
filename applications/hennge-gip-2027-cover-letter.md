Anish Manchanda
B.Tech Computer Science (AI), USICT, Delhi · Class of 2028
anishmanchanda2006@gmail.com · github.com/anishmanchanda · linkedin.com/in/anish-manchanda

To the HENNGE Global Internship Program team,

I'm applying for the Full-Stack Pathway of the HENNGE Global Internship Program, Batch 2 (June 1 – July 16, 2027). I'm a third-year B.Tech Computer Science (AI) student in Delhi. When something doesn't work, I like to measure it and find out why instead of guessing. Your program asks interns to own their code and explain their trade-offs. That's how I already work, and I'd like to do it with mentors who will push back on my decisions.

Most of my work so far has been full-stack and backend. For MaterialMover, a marketplace for reusing construction waste, my teammates and I built a React frontend, a Node/Express API and a FastAPI search service on PostgreSQL and MongoDB, with JWT auth. We containerised it with Docker and deployed it through a GitHub Actions pipeline. At Pepper Labs AI I shipped a RAG pipeline to production and built a multi-provider LLM layer with fallback handling. I also traced an async bug that was making every request call the model three times. This summer at MCT India Infotech, I built the Python backend for a real-time voice agent: session orchestration, multi-turn streaming and REST integrations.

The project I'm proudest of is one I built alone for a hiring challenge. It's a compliance Q&A service with role-based access control, and it refuses differently when an answer doesn't exist and when it exists but sits above the user's clearance. Responses were taking over 50 seconds, and everyone assumed the model was slow. I instrumented the pipeline instead. Generation took 2.5 seconds; the rest was my own code queued behind a provider rate limit. Fixing that cut latency 34x without changing the model or prompt. I ran sixteen numbered experiments on the system, each with a hypothesis, a measurement and a decision. They showed the bottleneck was answer synthesis, not retrieval. That habit of proving where the problem is before changing anything is what I'd bring to your security-focused full-stack and DevOps projects.

I also work on open source. For sony-ult-ctl, a macOS app that controls Sony headphones over Bluetooth, I reverse-engineered an undocumented binary protocol. By probing candidate payloads and reading the firmware's replies, I found the byte the device was ignoring. That fixed an ambient-sound control that had never worked. I also rebuilt the app's receive path to be event-driven. In my fork of an Apple Watch approval tool for coding agents, I reworked the notification delivery and the bridge server's hook routes, and added support for a second agent. I tested all of it on a physical iPhone and Watch, because the simulator can't reproduce background or networking behaviour. I'm comfortable on Linux and macOS, and I'd like the program's AWS and infrastructure week to deepen that.

I'm drawn to HENNGE because the program is built around feedback and ownership, not just output. You also ask applicants to write their solutions without AI-generated code. I'd welcome six weeks of writing code I fully understand and defending every decision in it. [OPTIONAL — keep only if true: I'm also seriously interested in building my career in Japan, and I see this program as the right first step.]

Thank you for considering my application. I'd be glad to walk you through any of this work, including the private challenge repository, in an interview.

Sincerely,
Anish Manchanda
