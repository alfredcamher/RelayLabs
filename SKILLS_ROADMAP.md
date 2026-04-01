# Skills Installation Roadmap

**Objective:** Install 6 critical skills for autonomous CEO operations
**Timeline:** Immediate → Revenue Phase → Scale Phase

---

## Phase 1: Immediate (Install Now)

### 1. Healthcheck
**Source:** `/usr/lib/node_modules/openclaw/skills/healthcheck/`
**Status:** ✅ Already available locally
**Purpose:** Security hardening, system audits
**Install:** None needed — already in skills path

### 2. Agent Browser
**Source:** ClawHub
**Slug:** `agent-browser` or `web-client`
**Purpose:** Autonomous web browsing, scraping, validation
**Risk:** Medium (web access requires careful sanitization)
**Install:** `clawhub install agent-browser`

### 3. xpost (Twitter/X)
**Source:** ClawHub or OpenClaw core
**Slug:** `xpost` or `opentweet`
**Purpose:** Social media automation
**Risk:** Low (read=draft autonomy, post=human approval per my protocol)
**Install:** `clawhub install xpost`

---

## Phase 2: Revenue Critical (Before First $)

### 4. Stripe
**Source:** ClawHub
**Slug:** `stripe`
**Purpose:** Payments, subscriptions, billing
**Risk:** High (financial — requires human approval for >$50)
**Install:** `clawhub install stripe`
**Requires:** Stripe API keys, webhook endpoint

### 5. PostgreSQL
**Source:** ClawHub
**Slug:** `postgres` or `postgresql`
**Purpose:** Data persistence, customer records
**Risk:** Low (internal data only)
**Install:** `clawhub install postgres`
**Requires:** DB credentials

---

## Phase 3: Scale Phase (After $10k MRR)

### 6. Capability Evolver
**Source:** ClawHub
**Slug:** `capability-evolver`
**Purpose:** Self-improving agent, auto-code generation
**Risk:** High (self-modifying requires oversight)
**Install:** `clawhub install capability-evolver`
**Note:** #1 most installed skill on ClawHub (35k+ installs)

---

## Installation Commands

```bash
# Check what's already installed
ls ~/.openclaw/skills/

# Install via ClawHub (one at a time, verify each)
clawhub install agent-browser
clawhub install xpost
clawhub install stripe
clawhub install postgres
clawhub install capability-evolver

# Manual install (alternative)
cp -r /path/to/skill ~/.openclaw/skills/{skill-name}
```

---

## Security Review

Before installing each:
- [ ] Read SKILL.md for permissions required
- [ ] Verify no excessive file system access
- [ ] Check network permissions (external APIs?)
- [ ] Confirm no自动 execution without verification

---

## Dependency Map

```
Healthcheck (baseline)
    ↓
Agent Browser → xpost (social research + posting)
    ↓
Stripe + PostgreSQL (accounts + data)
    ↓
Capability Evolver (compound improvement)
```

---

_Last updated: 2026-03-31 | Skills found: 6 | Installed: 1 (healthcheck)_
