# Email Marketing Infrastructure - Setup Guide

## Overview
Complete email automation system for CEO Autónomo.

## Sequences Implemented

| Sequence | Purpose | Emails | Duration |
|----------|---------|--------|----------|
| `nurture-sequence.md` | Lead magnet → Customer | 5 | 14 days |
| `customer-onboarding.md` | Post-purchase → Success | 5 | 30 days |

## Tools Required

### Primary: SendGrid (Recommended)
- Free tier: 100 emails/day
- Paid: $14.95/mo for 40k emails
- Existing integration with payment system

### Alternative: ConvertKit
- Better for creators
- Visual automation builder
- $29/mo for 1k subscribers

### Alternative: MailerLite
- Free tier: 1k subscribers
- Affordable paid plans
- Good automation features

## SendGrid Configuration

### 1. Account Setup
```
signup.sendgrid.com
→ Create account
→ Verify domain (ceoautonomo.com)
→ Add SPF/DKIM records
```

### 2. Create Sender Identity
```
Settings → Sender Authentication
→ From: Alfred <alfred@ceoautonomo.com>
→ Reply-to: support@ceoautonomo.com
```

### 3. API Integration
```python
# Already in webhook_handlers.py
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

def send_nurture_email(user_email, sequence_day, template_id):
    """Send specific nurture email based on day in sequence"""
    pass
```

### 4. Automation Triggers
```
Event: User downloads lead magnet (checklist)
  ↓
Delay: 0 hours
  ↓
Action: Send Email 1 (Welcome)
  ↓
Wait: User purchases?
  ├─ YES → Exit sequence → Customer onboarding
  └─ NO → Continue sequence

Wait: 3 days
  ↓
Action: Send Email 2 (Problem agitation)
  ↓
Repeat check...
```

## Database Schema

### email_subscribers
```sql
CREATE TABLE email_subscribers (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100),
    source VARCHAR(50), -- 'lead_magnet', 'purchase', 'webinar'
    tags TEXT[], -- ['lead', 'warm', 'customer']
    nurture_day INTEGER DEFAULT 0,
    customer_since DATE,
    unsubscribed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### email_logs
```sql
CREATE TABLE email_logs (
    id SERIAL PRIMARY KEY,
    subscriber_id INTEGER REFERENCES email_subscribers(id),
    email_type VARCHAR(50), -- 'nurture', 'transactional', 'broadcast'
    template_id VARCHAR(100),
    subject VARCHAR(255),
    sent_at TIMESTAMP,
    opened_at TIMESTAMP,
    clicked_at TIMESTAMP,
    opened BOOLEAN DEFAULT FALSE,
    clicked BOOLEAN DEFAULT FALSE
);
```

## Templates Upload

### In SendGrid:
```
Marketing → Templates → Create Template
→ Paste HTML from email templates
→ Add unsubscribe footer (required)
→ Test with "Send Test"
```

### Template IDs:
- `d-123456789`: Email 1 - Welcome
- `d-234567890`: Email 2 - Problem
- `d-345678901`: Email 3 - Social Proof
- `d-456789012`: Email 4 - Objections
- `d-567890123`: Email 5 - Last Call

## Testing Protocol

### Pre-Launch
1. Setup test account (your email)
2. Trigger sequence manually
3. Review each email in inbox
4. Check mobile rendering
5. Verify links work
6. Test unsubscribe

### Soft Launch
1. Add 10 beta testers
2. Monitor opens/clicks for 1 week
3. Adjust subject lines if <30% open
4. A/B test if needed

### Full Launch
1. Import existing contacts (if any)
2. Monitor daily metrics
3. Respond to replies within 24h

## Compliance

### GDPR/CCPA
- [ ] Consent checkbox on signup
- [ ] Clear privacy policy link
- [ ] Easy unsubscribe (1-click)
- [ ] Data deletion capability
- [ ] Double opt-in (optional)

### CAN-SPAM
- [ ] Physical address in footer
- [ ] Clear from name
- [ ] Truthful subject lines
- [ ] Unsubscribe honored within 10 days
- [ ] 30-day compliance record

## Metrics Dashboard

### Track Daily:
- Subscribers gained/lost
- Open rate by email
- Click rate by email
- Conversion rate (email → purchase)
- Revenue attributed to email

### Target Metrics:
| Metric | Target | Action if Below |
|--------|--------|-----------------|
| List growth | +5% monthly | Add more signup forms |
| Open rate | 35% | Test subjects |
| Click rate | 8% | Improve copy |
| Conv. rate | 5% | Better offers |
| Unsubscribe | <1% | Review frequency |

## Cost Estimation

| Tool | Subscribers | Emails/Month | Cost/Month |
|------|-------------|--------------|------------|
| SendGrid | 1,000 | ~4,000 | $0 (free tier) |
| SendGrid | 5,000 | ~20,000 | $14.95 |
| ConvertKit | 1,000 | ~4,000 | $29 |
| MailerLite | 1,000 | ~4,000 | $0 (free) |

### Recommended:
Start with **SendGrid free tier** (100 emails/day).
Scale to paid when >1,000 subscribers.

## Next Steps

1. [ ] Create SendGrid account
2. [ ] Authenticate domain
3. [ ] Upload 5 nurture templates
4. [ ] Setup automation workflow
5. [ ] Install signup forms on landing page
6. [ ] Test end-to-end sequence
7. [ ] Launch lead magnet

---

Ready to start nurturing leads!
*Created