# Analytics - CEO Autónomo

## Files

| File | Purpose |
|------|---------|
| `SETUP.md` | Analytics configuration guide |
| `dashboard.html` | Visual metrics dashboard |
| `metrics-tracker.py` | CLI metrics from purchases.log |
| `README.md` | This file |

## Quick Start

### View Dashboard

Open `dashboard.html` in browser or host it:

```bash
# Local viewing
open analytics/dashboard.html

# Simple server
python -m http.server 8080
# Visit: http://localhost:8080/dashboard.html
```

### Track Metrics

From purchases:

```bash
# Show last 7 days
python analytics/metrics-tracker.py --days 7

# Show last 30 days  
python analytics/metrics-tracker.py --days 30
```

## Integration

### Connect to Live Data

The dashboard currently shows placeholder data. To make it live:

1. **Option A**: Read from purchases.log directly (static)
2. **Option B**: Create `/api/metrics` endpoint in Flask
3. **Option C**: Export to Google Sheets via webhook

### Webhook Integration

Add to `payment/stripe-checkout-server.py` webhook handler:

```python
# After logging purchase, update metrics
import json
metrics = {
    'timestamp': datetime.now().isoformat(),
    'revenue': session['amount_total'] / 100
}
# Send to metrics service or log file
```

## Key Metrics

| Metric | Source | Target |
|--------|--------|--------|
| Revenue | Stripe/purchases.log | $470+ (Week 1) |
| Conversion | GA4 + Stripe | >2% |
| AOV | Stripe | $47 |
| Refund Rate | Stripe | <5% |
| Email Open | SendGrid | >20% |

## External Analytics

- **Stripe Dashboard**: https://dashboard.stripe.com/analytics
- **GA4**: https://analytics.google.com
- **SendGrid Stats**: https://app.sendgrid.com/statistics