# Secrets Management Guide

## Required Secrets

### For GitHub Actions (`.github/workflows/deploy.yml`)

Add these in GitHub: Settings → Secrets and variables → Actions

| Secret | Description | How to Get |
|--------|-------------|------------|
| `FLY_API_TOKEN` | Deploy to Fly.io | `fly auth token` |
| `RENDER_API_KEY` | Deploy to Render | Render Dashboard → API |
| `RENDER_SERVICE_ID` | Service identifier | From Render URL |
| `STRIPE_PRICE_ID` | Product price ID | Stripe Dashboard |

### For Stripe (Product Setup)

These come from your Stripe Dashboard:

1. **Product Creation**
   - Products → Create Product
   - Name: "CEO Autónomo Guide"
   - Price: $47 USD (One-time)
   - Copy `price_xxxxx` ID

2. **Webhook Endpoint**
   - Developers → Webhooks → Add endpoint
   - URL: `https://yourdomain.com/webhook`
   - Events: `checkout.session.completed`
   - Copy signing secret: `whsec_xxxxx`

## Setting Secrets by Platform

### GitHub Actions
```bash
# Using gh CLI
gh secret set FLY_API_TOKEN --body "your-token"
gh secret set STRIPE_PRICE_ID --body "price_xxxxx"
```

### Fly.io
```bash
flyctl secrets set STRIPE_SECRET_KEY=sk_live_xxxxx
flyctl secrets set STRIPE_WEBHOOK_SECRET=whsec_xxxxx
```

### Render Dashboard
Web UI: Settings → Environment Variables

### Local Development
```bash
cp deploy/.env.staging payment/.env
echo "sk_test_xxxxx" > payment/.stripe_key
chmod 600 payment/.env payment/.stripe_key
```

## Security Best Practices

1. **Never commit secrets**
   - `.gitignore` includes `.env` and `*.key`

2. **Rotate regularly**
   - Stripe: Can rotate in dashboard
   - SendGrid: API keys can be regenerated

3. **Use least privilege**
   - Stripe: Restricted API keys for webhooks only
   - SendGrid: Limited scope API keys

4. **Monitor usage**
   - Check Stripe Dashboard for unexpected calls
   - Review webhook delivery logs

## Testing Secrets

### Stripe Test Mode
```bash
# Verify key works
curl https://api.stripe.com/v1/account \
  -u sk_test_xxxxx:
```

### Webhook Secret
```bash
# Test locally
stripe listen --forward-to localhost:4242/webhook
```

## Recovery

If secrets are exposed:
1. Revoke immediately in respective dashboards
2. Generate new keys
3. Update all deployed environments
4. Check logs for unauthorized usage