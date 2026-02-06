# RULES.md - System Initialization & Operating Constraints

## RATELIMITS
- 5 seconds minimum between API calls
- 10 seconds between web searches
- Max 5 searches per batch, then 2-minute break
- Batch similar work (one request for 10 leads, not 10 requests)
- If you hit 429 error: STOP, wait 5 minutes, retry

## SESSION INITIALIZATION RULE
On every session start:

### 1. Load ONLY these files:
- SOUL.md
- USER.md
- IDENTITY.md
- memory/YYYY-MM-DD.md (if it exists)

### 2. DO NOT auto-load:
- MEMORY.md
- Session history
- Prior messages
- Previous tool outputs

### 3. When user asks about prior context:
- Use memory_search() on demand
- Pull only the relevant snippet with memory_get()
- Don't load the whole file

### 4. Update memory/YYYY-MM-DD.md at end of session with:
- What you worked on
- Decisions made
- Leads generated
- Blockers
- Next steps

**This saves 80% on context overhead.**

---

## MODEL ROUTING STRATEGY (2026-02-06)

### Haiku (Default, 80% of calls)
- Routine tasks: reading, research, writing summaries
- Execution: feedback on docs, code reviews
- Status updates, progress tracking
- Batch operations (lists, tables, formatting)
- **Cost:** ~$0.001/1K tokens

### Sonnet (Planning/Complex, 20% of calls)
- Strategic planning, analysis, recommendations
- Complex decision-making
- Architecture/system design
- Investor decks, high-impact communications
- Business model refinement
- **Cost:** ~$0.003/1K tokens

### Ollama (Heartbeats, 0 API cost)
- Periodic checks (every 1 hour)
- Model: `llama3.2:3b` (local inference)
- Runs on-device, zero API charges
- Fast, light, no network dependency

---

**Cost Optimization Summary:**
- Session overhead reduced: 80% (50KB → 8KB per session)
- Heartbeat API cost eliminated: $0.50/mo → $0
- Model routing savings: ~30% on complex tasks
- **Target run rate:** $6-15/month (vs. $70-90 before)

---
**Status:** Active since 2026-02-05 21:30 CST
**Updated:** 2026-02-06 11:18 CST (full optimization deployed)
**Owner:** Bernardo
