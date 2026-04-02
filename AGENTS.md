# AGENTS.md - Agent Orchestration & Coding Operations

*This folder is your headquarters. Own it.*

---

## Active Agent Registry

**File:** `memory/active-agents.json`
**Updated:** Every heartbeat (30 min)

**Format:**
```json
{
  "agents": [
    {
      "id": "codex-2026-03-31-feature-x",
      "type": "coding",
      "status": "running|stalled|failed|completed",
      "start_time": "2026-03-31T14:20:00Z",
      "last_checkin": "2026-03-31T14:45:00Z",
      "tmux_session": "felix-codex-001",
      "scope": "Implement user auth system",
      "retry_count": 0,
      "blockers": null
    }
  ]
}
```

---

## Agent Types

### 1. Coding Agents (Ralph Loop Pattern)

**Purpose:** Long-running development tasks (hours to days)
**Model:** Kimi K2.5
**Pattern:** Ralph loop (retry with fresh context)

**Spawn Command:**
```
sessions_spawn(
  task="[SCOPE] + [CONSTRAINTS] + [SUCCESS CRITERIA]",
  agent_id="coding-alpha",
  run_timeout_seconds=3600
)
```

**Ralph Loop Protocol:**
1. **Spawn** → agent with explicit scope, deadline, check-in interval (30 min)
2. **tmux** → `tmux -S ~/.tmux/sock new-session -s {session-name}`
3. **Monitor** → check-in every 30 min: git status + output summary
4. **Decision Matrix:**
   - On track → continue
   - Stalled (>30 min silent) → retry with fresh context
   - Failed → analyze logs, retry or escalate
   - 3 retries max → human escalation

**Verification Checklist (Every Check-in):**
```bash
# On agent check-in, verify:
git log --oneline -5 --since="30 minutes ago"  # commits?
git diff --stat HEAD~3..HEAD  # files changed?
ls -la build/ 2>/dev/null || echo "no build"  # output exists?
cat logs/last-output.log 2>/dev/null  # recent stdout?
```

**Never declare done without:**
- [ ] Process returned 0 (or documented non-zero success)
- [ ] Git commit exists with timestamp in window
- [ ] Files changed match expected scope
- [ ] If compiled: binary/artifact exists
- [ ] If tested: test output shows pass

### 2. Support Agents (3-Tier Ladder)

**Purpose:** Handle customer support autonomously

**Tiers:**
- **L1:** Auto-respond to common issues (FAQs, password resets)
- **L2:** Draft responses for human review (complex issues)
- **L3:** Escalate to human (refunds, complaints, edge cases)

**Escalation Rules (AUTO):**
- Refund request >$50
- Legal threat or compliance issue
- VIP customer (defined in CUSTOMERS.md)
- Negative sentiment + urgency combo

**Output:** All responses logged to `memory/support-YYYY-MM-DD.md`

### 3. Monitor Agents (Heartbeat)

**Purpose:** Watch systems, report anomalies

**Types:**
- **Revenue Monitor:** Check metrics APIs, flag anomalies
- **Error Monitor:** Sentry integration, auto-file issues
- **Status Monitor:** Website uptime, API health
- **Social Monitor:** Brand mentions, opportunities

**Auto-Response Matrix:**
- Error rate >5% → file issue + notify human
- Revenue drop >20% → immediate alert
- Downtime >1 min → check + escalate
- Viral mention → notify + draft response

### 4. Social Agents (xpost CLI)

**Purpose:** Manage X/Twitter presence

**Tool:** `xpost` CLI (bundled)

**Autonomy Level:**
- **Read:** All mentions, DMs, trends (full autonomy)
- **Draft:** Responses, threads (human review optional)
- **Post:** Scheduled content only (pre-approved queue)
- **Engage:** Real-time replies (human approval required)

**Content Queue:** `memory/social-queue.json`
**Posted Log:** `memory/social-posted.json`

---

## Session Management

### tmux Best Practices

**Socket:** `~/.tmux/sock` (not `/tmp`, survives macOS cleanup)

**Create:**
```bash
tmux -S ~/.tmux/sock new-session -d -s {name}
```

**Attach:**
```bash
tmux -S ~/.tmux/sock attach -t {name}
```

**List:**
```bash
tmux -S ~/.tmux/sock list-sessions
```

**Kill:**
```bash
tmux -S ~/.tmux/sock kill-session -t {name}
```

### Process Health Checks

**Check if agent alive:**
```bash
# Agent via tmux
tmux -S ~/.tmux/sock has-session -t {name} 2>/dev/null && echo "alive"

# Process by PID
ps -p {pid} > /dev/null && echo "running"

# Sub-agent via sessions_list
sessions_list(agent_id="{id}")
```

**Restart on death:**
- Heartbeat detects → log death → restart → verify → notify if pattern

---

## Sub-Agent Steering

### List Active
```
subagents(action="list")
```

### Send Message to Agent
```
sessions_send(sessionKey="{key}", message="{message}")
```

### Kill Agent
```
subagents(action="kill", target="{session_id}")
```

### Rules
- Never leave agents hanging >30 min without check-in
- Always verify death before respawning (prevent duplicate work)
- Log all steering actions to daily memory

---

## Cron Agent Scheduling

**Example: Daily Revenue Check**
```json
{
  "name": "daily-revenue",
  "schedule": {
    "kind": "cron",
    "expr": "0 9 * * *",
    "tz": "America/Mexico_City"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Check revenue metrics: MRR, churn, new signups. Log to memory/today.md. Flag anomalies."
  },
  "sessionTarget": "isolated",
  "delivery": {"mode": "none"}
}
```

**Example: Ralph Loop Coding Session**
```json
{
  "name": "agent-checkin-{id}",
  "schedule": {
    "kind": "every",
    "everyMs": 1800000
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Check on coding agent {id}. Verify git commits, logs. If stalled >30min, restart with fresh context."
  },
  "sessionTarget": "isolated",
  "delivery": {"mode": "none"}
}
```

---

## QA Subagent Pattern (MANDATORY)

### The Rule

**Every deliverable MUST be reviewed by QA subagent before marking COMPLETE.**

**No exceptions. No shortcuts. No "intent as completion."**

### QA Agent Protocol

**Step 1: Developer creates deliverable**
- Write content/code/output
- Self-review for obvious errors
- **DO NOT mark COMPLETE**

**Step 2: Spawn QA Subagent**
```bash
sessions_spawn(
  agentId="qa-reviewer",
  task="REVIEW ONLY - Evaluate deliverable against quality criteria:
    1. Accuracy: Is information correct?
    2. Completeness: All requirements met?
    3. Professionalism: Format, tone, polish?
    4. Actionability: Can user act on this?
    Output: APPROVED / NEEDS_REVISION with specific feedback",
  timeout=600
)
```

**Step 3: QA Evaluation**
- QA reviews deliverable
- Returns verdict: APPROVED or NEEDS_REVISION
- If NEEDS_REVISION: Specific feedback on what's wrong

**Step 4: Revision Loop**
```
IF APPROVED:
  → Mark task COMPLETE
  → Document approval in git commit
  → Proceed
IF NEEDS_REVISION:
  → Fix issues identified
  → Re-spawn QA for re-review
  → Repeat until APPROVED
```

### Never Declare Done Without:
- [ ] QA verdict: APPROVED
- [ ] Specific feedback addressed
- [ ] Git commit with approval documented
- [ ] Task moved to "Complete"

### Maximum Iterations
- **3 reviews max per task**
- After 3: Escalate to human for direction

---

## POST-TASK LEARNING LOOP (MANDATORY)

### Golden Rule

**After EVERY completed task, mandatory reflection before marking COMPLETE.**

**Purpose:** Continuous improvement, pattern recognition, avoid repeated failures

### Reflection Template

Append to `memory/continuous-learning-YYYY-MM.md`:

```markdown
### Task Reflection: [TASK-ID]
**Deliverable:** [What was created]
**QA Status:** [APPROVED/NEEDS_REVISION]
**Effort:** [Time/cycles spent]

#### What Worked? ⭐
- [Specific success to repeat]

#### What Failed? ❌
- [Specific failure to avoid]
- [Tool that didn't work]
- [Assumption that was wrong]

#### What Was Inefficient? ⏱️
- [Waste to eliminate]
- [Tool that could have helped]

#### What I'll Do Better Next Time? 🎯
- [Concrete improvement for similar tasks]

#### Tools Discovered?