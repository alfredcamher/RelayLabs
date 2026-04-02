# WORKFLOW_AUTO.md - Autonomous Operations Master Workflow

*"The system that runs itself, learns from itself, and improves itself."*

**Purpose:** Master orchestration document for 24/7 autonomous operations  
**Scope:** All self-running workflows: operations, learning, healing, QA, improvement  
**Updated:** Continuously via learning loops  

---

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Morning Routine Workflow](#morning-routine-workflow)
3. [Continuous Learning Workflow](#continuous-learning-workflow)
4. [Self-Healing Workflow](#self-healing-workflow)
5. [QA Agent Workflow](#qa-agent-workflow)
6. [Auto-Improvement Workflow](#auto-improvement-workflow)
7. [Research Automation Workflow](#research-automation-workflow)
8. [Launch/GTM Workflow](#launchgtm-workflow)
9. [Emergency Protocols](#emergency-protocols)

---

## System Architecture

### The Four Pillars of Autonomy

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW_AUTO SYSTEM                      │
├──────────────┬──────────────┬──────────────┬────────────────┤
│  OPERATIONS  │   LEARNING   │    QA/REVIEW │   HEALING      │
│              │              │              │                │
│  ├─ Morning  │  ├─ Fetch    │  ├─ Spawn QA │  ├─ Detect     │
│  ├─ Health   │  ├─ Analyze  │  ├─ Evaluate │  ├─ Diagnose   │
│  ├─ Execute  │  ├─ Synthesize│  ├─ Feedback │  ├─ Recover    │
│  └─ Report   │  └─ Integrate│  └─ Iterate  │  └─ Prevent    │
├──────────────┼──────────────┼──────────────┼────────────────┤
│              │   IMPROVEMENT│   RESEARCH   │   MONITORING   │
│              │              │              │                │
│              │  ├─ Reflect  │  ├─ Schedule │  ├─ Heartbeat  │
│              │  ├─ Optimize│  ├─ Execute  │  ├─ Metrics    │
│              │  ├─ Document│  ├─ Synthesize│ ├─ Alert    │
│              │  └─ Apply    │  └─ Archive  │  └─ Escalate   │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

### The Autonomous Cycle

**Every 15 minutes (heartbeat):**
1. **SCAN** → Check backlog for incomplete tasks
2. **EXECUTE** → Process highest priority task
3. **QA** → Spawn QA agent for deliverables
4. **LEARN** → Extract patterns, update memory
5. **HEAL** → Check system health, fix issues
6. **IMPROVE** → Optimize for next cycle
7. **REPORT** → Log outcomes, notify if needed

---

## Morning Routine Workflow

### Trigger: 09:00 AM Daily (America/Mexico_City)

```cron
0 9 * * *
```

### Steps

#### Step 1: System Health Check
```bash
# Tasks:
subagents(action="list")  # Active agents
cron(action="status")      # Cron jobs health
sessions_list()            # Session status
```

**Decision Matrix:**
- All healthy → Continue
- Agent stalled → Restart with fresh context
- Cron failed → Log + investigate
- Session error → Escalate to human

#### Step 2: Revenue Pulse
```bash
# Check metrics:
# - Stripe: new signups, revenue
# - Plausible: traffic, conversions
# - Support: ticket volume
# - AI costs: spend vs budget
```

**Flags:**
- Revenue ±20% → Alert + analyze
- Traffic spike → Check source + opportunity
- AI cost >50% daily budget → Pause optional agents

#### Step 3: Memory Maintenance
```bash
# Tasks:
# 1. Hot (today.md) → consolidate to warm
# 2. Warm (7+ days) → migrate to cold
# 3. Cold → LightRAG index update
python3 ~/.openclaw/tools/setup-lightrag.py index
```

#### Step 4: Backlog Review
```
# Check BACKLOG.md for:
# - Overdue tasks
# - Blocked items
# - New opportunities
# - Research tasks ready
```

#### Step 5: Daily Plan
```
# Output: memory/morning-plan-YYYY-MM-DD.md
# Include:
# - Top 3 priorities
# - Blockers requiring human
# - Research tasks to execute
# - Expected deliverables
```

---

## Continuous Learning Workflow

### Trigger: Multiple schedules

| Learning Type | Frequency | Trigger |
|--------------|-----------|---------|
| **Morning Research** | Daily 9:30 AM | Top of mind topics |
| **Deep Research** | Weekly (Sun) | 2-hour focused session |
| **Reactive Learning** | On-demand | User request |
| **Continuous Feed** | Every 4 hours | RSS + newsletters |

### The Learning Loop

#### Phase 1: DISCOVER
```
Sources (priority order):
1. admnt.com (Jason Yeh) - Fundraising
2. lennyrachitsky.com (Lenny) - Product/Growth
3. andrewchen.substack.com - Growth frameworks
4. ycombinator.com/blog - Startup patterns
5. MIT Sloan / HBR - Strategy
6. Indie Hackers - Solopreneur tactics
```

#### Phase 2: COLLECT
```
Actions:
- web_fetch() top 3 articles
- Extract key insights
- Save raw content
```

#### Phase 3: SYNTHESIZE
```
Template: memory/learn-[topic]-YYYY-MM-DD.md

Required sections:
- Executive Summary (3 bullets)
- Key Insights (5-7 points)
- Actionable Takeaways (specific actions)
- Application to Relay Labs (custom)
- Sources & Further Reading
```

#### Phase 4: INTEGRATE
```
- Update EXPERTISE.md with new frameworks
- Add to relevant sections
- Cross-reference with existing knowledge
```

#### Phase 5: QA
```
- Spawn QA agent
- Verify accuracy (30%)
- Check actionability (15%)
- Ensure alignment (10%)
```

#### Phase 6: APPLY
```
- Before next similar task: reference learning
- Update decision-making with new patterns
- Share insights in reports
```

### Auto-Research Triggers

**Condition:** User says "research X" or "learn about Y"
**Action:**
1. Queue R-[ID] task in BACKLOG
2. Execute web_search + web_fetch
3. Synthesize to memory/
4. QA review
5. Update EXPERTISE.md
6. Report findings

### Research Quality Gates

```
Before marking COMPLETE:
□ At least 3 sources fetched
□ Key findings synthesized (not just copy-paste)
□ Actionable items identified
□ QA agent APPROVED
□ EXPERTISE.md updated (if applicable)
□ Learning documented in continuous-learning-*.md
```

---

## Self-Healing Workflow

### Trigger: Every 15 minutes (heartbeat)

### Components

#### Agent Health Monitor
```
Check every 15 min:
- Agent check-in timestamp
- Git activity (commits in last 30 min)
- Process status (ps aux | grep)
- Output files existence
```

**Conditions & Actions:**
| Condition | Action |
|-----------|--------|
| Silent >30 min | Ralph loop restart |
| Failed 3x | Escalate to human |
| No commits >1h | Restart session + context |
| Process dead | Respawn from checkpoint |

#### Git Health Check
```
Check every 30 min:
- Uncommitted changes >2h old
- No commits in 24h on active project
- Large deletions without context
- Merge conflicts
```

**Auto-Actions:**
- Uncommitted work: Notify + suggest commit
- Stale repo: Yellow flag alert
- Conflicts: Escalate immediately

#### Cost Spike Recovery
```
Check daily:
- AI spend vs budget
- Per-task cost tracking
```

**If daily cost >50% weekly budget:**
1. Identify high-cost operations
2. Pause optional expensive agents
3. Switch non-critical tasks to Haiku
4. Notify human with breakdown

#### System Health Dashboard
```
Output: memory/system-health-YYYY-MM-DD.json

{
  "timestamp": "2026-04-02T...",
  "checks": {
    "agents": {"status": "healthy", "count": 0, "stalled": 0},
    "git": {"status": "healthy", "uncommitted": false},
    "revenue": {"status": "healthy", "anomalies": []},
    "security": {"status": "healthy", "suspicious": 0}
  },
  "actions_taken": [...],
  "next_check": "2026-04-02T..."
}
```

---

## QA Agent Workflow

### The Golden Rule: NO EXCEPTIONS

**Every single deliverable MUST pass QA before COMPLETE.**

### Trigger: Task completion

### Workflow

#### Step 1: Spawn QA Agent
```python
sessions_spawn(
  task="QA REVIEW - Evaluate deliverable:\n"
       "File: {filepath}\n"
       "Type: {content_type}\n\n"
       "Criteria:\n"
       "1. Accuracy (