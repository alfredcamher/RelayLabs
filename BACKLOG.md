# BACKLOG.md - Active Tasks

**Status:** Active Mode | **Last Updated:** 2026-04-01 21:50 CDT

## Sprint: Tool Implementation + Product Launch

### HIGH (Critical Path)

#### PDF Generation for CEO Autónomo Product
- **ID:** PDF-001
- **Task:** Generate professional PDF from CEO-AUTONOMO-GUIA-COMPLETA.md
- **Blocker:** pandoc + texlive-xetex require elevated permissions (sudo)
- **Options:**
  1. Human runs locally: `pandoc CEO-AUTONOMO-GUIA-COMPLETA.md -o guia.pdf --pdf-engine=xelatex`
  2. Grant elevated permissions to Alfred for package install
  3. Use Playwright to print-to-PDF (fallback - less controlled)
- **Created:** Script ready at `~/.openclaw/tools/run-pandoc-pdf.py`
- **Status:** ⛔ WAITING

#### Stripe Webhook Auto-Delivery
- **ID:** WEB-001
- **Task:** Setup Cloudflare Worker + Resend for automatic PDF delivery on purchase
- **Blockers:** Requires human to:
  1. Create Cloudflare account (if not exists)
  2. Get Resend API key
  3. Create Worker endpoint
- **Time Estimate:** ~20 min human setup
- **Status:** ⛔ WAITING

---

### MEDIUM (Tools & Automation)

#### DeepCode Installation
- **ID:** TOOL-001
- **Task:** Complete DeepCode stack installation
- **Path:** `~/.openclaw/tools/deepcode/`
- **Estado:** ⏳ Cloned, needs dependency install
- **Cron:** Daily check of agent PRs (pending install)

---

### LOW (Future Capabilities)

#### RAG-Anything Multimodal PDF
- **ID:** TOOL-002
- **Task:** Setup RAG-Anything for PDF analysis with image understanding
- **Use Case:** Analyze competitor PDFs, extract visual data
- **Priority:** Post-launch

#### Automated Twitter posting agent
- **ID:** SOCIAL-001
- **Task:** Create cron job for drafting/queuing tweets
- **Depends on:** X account creation (@relaylabs_ai or @alfredcamher)
- **Cron:** Draft tweets daily at 10 AM

---

## Tool Status Dashboard

| Tool | Status | Install Path | Last Verified |
|------|--------|--------------|---------------|
| Playwright | ✅ Ready | pip + chromium | 2026-04-01 |
| LightRAG | ✅ Ready | pip + ollama | 2026-04-01 |
| CLI-Anything | ✅ Ready | Cloned plugins | 2026-04-01 |
| DeepCode | ⏳ Waiting | Needs install | 2026-04-01 |
| RAG-Anything | ⏳ Waiting | Needs config | - |

---

## Cron Jobs Active

| Job | Schedule | Status |
|-----|----------|--------|
| lightrag-daily-index | 0 2 * * * | ✅ Active |
| playwright-health-check | */30 * * * * | ✅ Active |
| heartbeat-main | */15 * * * * | ✅ System |

---

## Complete = 13/13 Previous Tasks
**New Active Tasks:** 3 HIGH, 1 MEDIUM, 2 LOW

*Next Review: Daily heartbeat check*
