# Stripe Auto-Delivery Setup - CEO Autónomo

## Status
**Last Updated:** 2026-04-20 23:05 CDT
**Stripe CLI:** ✅ Authenticated
**Product:** CEO Autónomo (prod_UFoP8JQIWob942)
**Landing:** https://alfredcamher.github.io/RelayLabs/

## Current State
```
Customer Clicks → Stripe Checkout → Payment → Manual PDF Email
```
## Target State (Auto-Delivery)  
```
Customer Clicks → Stripe Checkout → Payment → Webhook → Auto Email PDF
```

## Webhook Listener

### Start Listener
```bash
# Terminal 1: Start webhook listener
stripe listen --events checkout.session.completed --print-json

# Terminal 2: Monitor logs
cd ~/workspace/webhook-stripe && ./start-webhook.sh
```

### Manual Test
```bash
# Create test checkout
./webhook-stripe/test-checkout.sh

# Or open live link:
https://buy.stripe.com/aFabJ28NrfiHdFl3jfcMM00
```

## Auto-Delivery Options

### Option A: Resend (Recommended)
**Setup:**
1. Create Resend account: resend.com
2. Verify domain: relaylabs.com
3. Get API key: re_xxxxxxxx
4. Add to .env: `RESEND_API_KEY=re_xxx`

**Code:** See `webhook-stripe/auto-deliver.js` - ready for Resend integration

### Option B: Cloudflare Worker + Email
- Worker triggers on Stripe webhook
- Stores customer in KV
- Queues email delivery

### Option C: Manual (Current)
- Check webhooks manually
- Send PDF via Gmail personal
- Update spreadsheet

## Customer Workflow

| Step | Current | Auto |
|------|---------|------|
| 1. Landing visit | ✅ GitHub Pages | Same |
| 2. Click buy | ✅ Stripe link | Same |
| 3. Checkout | ✅ Stripe | Same |
| 4. Payment | ✅ Stripe | Same |
| 5. Webhook | ⏳ CLI logs | Same |
| 6. PDF delivery | ❌ Manual | ⏳ Needs config |
| 7. Welcome email | ❌ Manual | ⏳ Needs config |

## Next Steps

1. **Priority 1:** Configurar Resend (10 min, $0)
2. **Priority 2:** Integrar webhook con Resend
3. **Priority 3:** Test end-to-end purchase
4. **Priority 4:** Revenue tasks (outreach, content)

## Test Card
`4242 4242 4242 4242` - Any future date, any CVC, any ZIP

## Commands
```bash
# View products
stripe products list --live

# View webhook events
stripe events list --limit 5

# Start listener
stripe listen --events checkout.session.completed --print-json
```
