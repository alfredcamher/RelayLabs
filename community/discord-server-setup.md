# Discord Server Setup - CEO Autónomo Community
**Proyecto:** Relay Labs / CEO Autónomo  
**Fecha:** 2026-04-01  
**Type:** Community Server

---

## 🚀 Quick Setup Guide

### Step 1: Create Server
1. Go to https://discord.com/app
2. Click "+ Add a Server"
3. Select "Create My Own" → "For a club or community"
4. Server Name: **"CEO Autónomo"** or **"Relay Labs"**
5. Upload: `/assets/alfred-avatar-primary.png`

### Step 2: Configure Categories & Channels

Copy this structure exactly:

```
📁 WELCOME
├── #👋 welcome        ← Welcome message & rules
├── #📖 getting-started ← Onboarding guide
└── #❓ faq             ← Common questions

📁 GENERAL
├── #💬 general         ← Main chat
├── #🎨 showcase       ← Member projects
└── #💡 ideas           ← Feature suggestions

📁 RESOURCES
├── #📚 guides          ← Product docs & guides
├── #🤖 prompts        ← Shared prompts
├── #🛠️ tools           ← Tool recommendations
└── #📊 wins            ← Celebration channel

📁 PRODUCT
├── #💳 buy-ceo-autonomo ← Purchase & support
├── #🎁 bonuses         ← Extra resources
└── #🐛 bugs            ← Issue reporting

📁 VOICE
├── 🔊 General Voice 1
├── 🔊 General Voice 2
└── 🔊 Office Hours
```

### Step 3: Configure Roles

Add these roles in Settings → Roles:

| Role | Color | Permissions | Auto-assign |
|------|-------|-------------|-------------|
| **@Founder** | 🟡 Gold | Admin | Manual (you) |
| **@Agent-CEO** | 🟢 Lime | Mod, manage messages | Manual (customers) |
| **@Early-Adopter** | 🔵 Cyan | Special access | Manual (first 50) |
| **@Member** | ⚪ White | Send messages | ✅ Yes (default) |
| **@Muted** | ⬛ Grey | View only | Manual |

### Step 4: Welcome Bot Setup

**Option A: Dyno (Recommended)**
1. Go to https://dyno.gg/
2. Add to your server
3. Configure Auto Message:

**Welcome Message (Post in #welcome):**

```
🎯 **Bienvenido al CEO Autónomo, {user}!**

Tu agente nunca duerme. ¿Y tú?

📖 **Empieza aquí:**
• Lee <#getting-started> para setup inicial
• Comparte tu stack en <#showcase>
• Pregunta en <#general> (no hay preguntas tontas)

🎁 **Acceso exclusivo:**
Clientes tienen rol @Agent-CEO con acceso a:
• Canales privados de soporte
• Early features
• Vox calls mensuales

💬 **Código de conducta:**
• Ship or Shut Up (ejecuta, no solo hablas)
• Value-first (antes de pedir, aporta)
• Constructivo siempre

¿Listo para escalar sin contratar? 🚀

- Alfred & Bernardo
```

### Step 5: Channel Permissions

**Restrict #buy-ceo-autonomo:**
```
Everyone: ❌ Send Messages
Agent-CEO: ✅ Send Messages
Founder: ✅ Manage Messages
```

**Make #welcome read-only:**
```
Everyone: ❌ Send Messages
```

### Step 6: Invites & Links

**Create invite:**
- Expires: Never
- Max uses: No limit
- Vanity URL: Apply for discord.gg/relaylabs (after 7 days)

**Add to:**
- [ ] Landing page CTA
- [ ] Email footer
- [ ] PDF guide
- [ ] Newsletter

---

## 🤖 Optional: Discord Bot

**Carl-bot** for:
- Reaction roles
- Auto-moderation
- Logging

**Setup commands:**
```
!autorole Agent-CEO
!reactionrole add "Get Notifications" 🔔 #roles
```

---

## 📋 Pre-Launch Checklist

- [ ] Server created with correct categories
- [ ] Avatar uploaded
- [ ] Roles configured
- [ ] Welcome bot installed
- [ ] Permissions tested (view as @everyone)
- [ ] Invite link generated (permanent)
- [ ] Rules posted in #welcome
- [ ] FAQ populated
- [ ] At least 3 messages in #guides
- [ ] Landing page updated with Discord CTA

---

## 📊 Growth Strategy

### Week 1-2: Foundation
-Invite early buyers only
-5-10 active members needed for energy

### Week 3-4: Expand
- Tweet about community
- Indie hackers cross-promotion
- Newsletter feature

### Month 2: Scale
- Weekly office hours (voice channel)
- AMA sessions
- Member spotlights

---

## 🔗 Integration with Product

**In PDF guide, add:**
```
## Únete a la Comunidad

🔗 discord.gg/YOUR-INVITE

- Soporte directo
- Prompts compartidos por miembros
- Early access a features
- Networking con otros founders

**Código de invitación:** CEO2026
```

---

## 💰 Monetization

**Free tier:**
- General chat access
- Resources channel
- Monthly AMA

**Paid tier (Agent-CEO role):**
- Priority support
- Private channels
- Weekly voice calls
- Direct line to Alfred

---

## 📈 Success Metrics

| Metric | Target Month 1 |
|--------|----------------|
| Members | 50-100 |
| Daily active | 10-20 |
| Messages/day | 50+ |
| Support tickets | <5% of members |

---

**Setup Time:** 30 min  
**Maintenance:** 10 min/day  
**ROI:** Community retention + organic growth

---

*Documentación creada by Alfred - Ready for human setup*