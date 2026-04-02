# Stripe Checkout Setup Guide

## Quick Setup (5 minutes)

### 1. Create Stripe Account
```bash
# Sign up at https://stripe.com
# Complete verification in dashboard
```

### 2. Configure Product
```bash
# In Stripe Dashboard:
# Products → Create Product
# Name: "CEO Autónomo Guide"
# Price: $47 USD (One-time)
# Copy the Price ID: price_xxxxx
```

### 3. Install Dependencies
```bash
pip install stripe flask python-dotenv
# or
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env with your Stripe keys
```

### 5. Run Server
```bash
python stripe-checkout-server.py
# Server starts on http://localhost:4242
```

## Local Testing with Stripe CLI

### Install Stripe CLI
```bash
# macOS
brew install stripe/stripe-cli/stripe

# Linux
curl -s https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg-key | gpg --dearmor | sudo tee /usr/share/keyrings/stripe.gpg
echo "deb [signed-by=/usr/share/keyrings/stripe.gpg] https://packages.stripe.dev/stripe-cli-debian-local stable main" | sudo tee /etc/apt/sources.list.d/stripe.list
sudo apt update && sudo apt install stripe
```

### Login and Test
```bash
stripe login
stripe listen --forward-to localhost:4242/webhook
```

### Test Payment
```bash
# Open browser
curl http://localhost:4242
# Click "Comprar Ahora"
# Use test card: 4242 4242 4242 4242
# Any future date, any CVC, any ZIP
```

## Production Deployment

### Environment Variables (Production)
```bash
STRIPE_SECRET_KEY=sk_live_xxxxx
STRIPE_PUBLISHABLE_KEY=pk_live_xxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxx
DOMAIN=https://yourdomain.com
STRIPE_PRICE_ID=price_live_xxxxx
```

### Webhook Endpoint
```
https://yourdomain.com/webhook
```

### Security Checklist
- [ ] Switch to live keys
- [ ] Enable webhook signature verification
- [ ] Set up HTTPS/TLS
- [ ] Configure delivery email service
- [ ] Test full purchase flow
- [ ] Set up Stripe receipt emails

## Integration Options

### Option A: Hosted Page (Current)
- Simple Flask server
- Customer redirected to Stripe
- Minimal code required

### Option B: Embedded Checkout
- Stay on your site
- Requires JS integration
- More customizable

### Option C: Payment Links
- No code required
- Generate in Stripe Dashboard
- Share link directly

## Delivery Automation

### Webhook Integration Points
```python
# In webhook handler, add:

# 1. Email delivery via SendGrid
# 2. Customer database update
# 3. Analytics tracking
# 4. Slack notification
# 5. Tag customer in CRM
```

### Recommended Email Service
- SendGrid (free tier: 100 emails/day)
- AWS SES (cheap, reliable)
- Mailgun

## Pricing Strategy Note

Current price: **$47 USD**
- Positioned as premium guide
- A/B test: $37 vs $47 vs $67
- Consider: $97 with bonus templates

## Support & Troubleshooting

### Common Issues
1. **"No such price"** → Check PRICE_ID is correct
2. **"Invalid API key"** → Switch from test to live (or vice versa)
3. **Webhook failing** → Check webhook secret matches

### Testing Cards
```
Success: 4242 4242 4242 4242
Decline: 4000 0000 0000 0002
3D Secure: 4000 0027 6000 3184
```

## Next Steps

1. [ ] Set up Stripe account
2. [ ] Create product & price
3. [ ] Test in sandbox
4. [ ] Configure production
5. [ ] Deploy webhook endpoint
6. [ ] Test end-to-end flow
7. [ ] Launch!