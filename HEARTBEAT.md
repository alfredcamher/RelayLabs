# HEARTBEAT.md - Autonomous Monitoring & Self-Healing

**Purpose:** Continuous health checks, auto-recovery, pattern detection
**Interval:** Every 30 minutes (configurable via cron)
**Owners:** This file is self-executing via OpenClaw cron
**Last Updated:** 2026-03-31

---

## Checklist (Execute in order)

### 1. Agent Health Check
**What:** Verify all active sub-agents are alive
**How:**
```bash
subagents(action="list")
# Check: any agents with status != "completed" and last_update >30min ago?
```
**Then:**
- If healthy → mark green, continue
- If stalled → Ralph loop restart, notify log
- If 3rd stall → escalate to human
- If crashed → respawn from last checkpoint, notify

**Log to:** `memory/agents-health-YYYY-MM-DD.json`

### 2. Git Health Check
**What:** Check for uncommitted changes, verify recent commits
**How:**
```bash
# For each tracked repo:
git status --short      # uncommitted?
git log --oneline -5   # recent activity?
git diff --stat        # what changed?
```
**Flags:**
- Uncommitted work >2 hours old → notify + consider commit
- No commits in 24h on active project → yellow flag
- Large deletions without context → red flag

**Log to:** `memory/git-health-YYYY-MM-DD.json`

### 3. Revenue Metrics Check
**What:** Update daily pulse, flag anomalies
**How:**
```
Check REVENUE.md → memory/revenue-today.json
Update: signups, AI costs, support tickets
today = new data vs yesterday
```
**Flags:**
- AI cost >50% of weekly budget → investigate efficiency
- Signup spike/fall >50% → dig into source
- Support tickets spike → potential issue

**Log to:** `memory/revenue-today.json`

### 4. Security Scan
**What:** Review security log for suspicious patterns
**How:**
```
Read memory/security-YYYY-MM-DD.json
Count: suspicious patterns, blocked attempts, escalations
```
**Flags:**
- >1 suspicious pattern → medium alert
- Failed verification → log and continue
- Active threat → immediate human escalation

### 5. Memory Tier Maintenance
**What:** Decay hot→warm, warm→cold
**How:**
```
Daily (2 AM):
- Hot (today.md) → append to Warm (memory/YYYY-MM-DD.md)
- Warm (7 days ago) → migrate to Cold (MEMORY.md)
- Cold (quarterly) → review, archive, prune
```
**Auto-execute:** Cron job at 02:00 daily

### 6. Self-Assessment
**What:** Quick sanity check of own state
**How:**
```
- Current model: Kimi? (fallback = alert)
- Token usage today: vs budget?
- Last human contact: <24h? (all good) : notify
- Pending escalations: any?
- Known blockers: any stale >48h?
```

---

## Self-Healing Actions

### Agent Recovery
**Condition:** Agent silent >30 minutes
**Action:**
```python
# Ralph loop restart
kill current session
spawn new session with fresh context
retry_count += 1
if retry_count > 3:
    escalate_to_human("Agent failing repeatedly")
else:
    log("Restarted with fresh context")
```

### Crashed Process Recovery
**Condition:** Agent process dead (check fails)
**Action:**
1. Log crash with timestamp
2. Analyze logs for cause
3. Respawn if recoverable
4. If same crash 2x → escalate with logs

### tmux Session Recovery
**Condition:** tmux socket missing or sessions lost
**Action:**
```bash
# Recreate stable socket
mkdir -p ~/.tmux
chmod 700 ~/.tmux
# Sessions auto-restart from agent registry
```

### Cost Spike Recovery
**Condition:** Daily AI cost >50% of weekly budget
**Action:**
1. Identify high-cost operations
2. Pause optional expensive agents
3. Switch non-critical tasks to Haiku
4. Notify human with breakdown

---

## Cron Schedule (Pre-configured)

```json
{
  "heartbeat-main": {
    "schedule": "*/30 * * * *",
    "action": "Read HEARTBEAT.md, execute checklist",
    "output": "Log to memory/heartbeat-YYYY-MM-DD.json"
  },
  "memory-decay": {
    "schedule": "0 2 * * *",
    "action": "Hot→Warm→Cold migration",
    "output": "Log to memory/decay-YYYY-MM-DD.json"
  },
  "daily-revenue": {
    "schedule": "0 9 * * *",
    "action": "Update REVENUE.md daily metrics",
    "output": "memory/revenue-today.json"
  },
  "weekly-review": {
    "schedule": "0 10 * * 1",
    "action": "Compile weekly metrics, flag patterns",
    "output": "memory/revenue-week-of-YYYY-MM-DD.md"
  }
}
```

---

## Output Format

Each heartbeat writes to `memory/heartbeat-YYYY-MM-DD.json`:

```json
{
  "timestamp": "2026-03-31T15:45:00Z",
  "checks": {
    "agents": {"status": "healthy", "count": 0, "stalled": 0},
    "git": {"status": "healthy", "uncommitted": false, "last_commit": "2026-03-31T10:00:00Z"},
    "revenue": {"status": "healthy", "anomaly_flags": []},
    "security": {"status": "healthy", "suspicious": 0, "blocked": 0},
    "memory": {"status": "healthy"}
  },
  "actions_taken": ["none"],
  "escalations": [],
  "next_check": "2026-03-31T16:15:00Z"
}
```

---

## Escalation Matrix

| Condition | Action | Notification |
|-----------|--------|--------------|
| Agent failed 3x | Stop retry, elevate | Human + log |
| Revenue down 20% | Investigate + alert | Human |
| Security threat | Immediate halt | Human URGENT |
| Cost >budget | Pause ops + alert | Human |
| Git conflicts | Manual resolution | Human |
| System unhealthy >1h | Full stop + alert | Human |

---

## Success Metrics

- Agent uptime: >95%
- Auto-recovery success: >80%
- Healthy checks: >99%
- Human escalations: <5/week (target)
- Issues detected before human notices: >90%

---

_Last heartbeat: 2026-03-31 15:34 CDT | Status: Healthy | Next: 30 min_
