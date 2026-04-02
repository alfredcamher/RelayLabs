# Analytics Setup Guide - CEO Autónomo

## Overview

Track key metrics: visitors, conversions, revenue, and customer behavior.

---

## 1. Google Analytics 4 (GA4)

### Setup

1. Go to [Google Analytics](https://analytics.google.com)
2. Create property: "CEO Autónomo"
3. Data stream: Web → URL: `https://yourdomain.com`
4. Copy Measurement ID: `G-XXXXXXXX`

### Implementation

Add to checkout page (`stripe-checkout-server.py`):

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXX');
</script>
```

### Custom Events

Track purchase completion:

```javascript
// On success page
gtag('event', 'purchase', {
  transaction_id: 'session_id_here',
  value: 47.00,
  currency: 'USD',
  items: [{
    item_name: 'CEO Autónomo Guide',
    item_id: 'ceo-autonomo-guide',
    price: 47.00,
    quantity: 1
  }]
});
```

---

## 2. Stripe Analytics

Built-in metrics at: https://dashboard.stripe.com/analytics

### Key Reports

- **Revenue recognition**: Daily/weekly/monthly
- **Conversion rates**: Via Stripe Sigma (paid) or manual export
- **Refund rates**: Built-in dashboard
- **Decline rates**: Payment analytics

### Custom Reporting

```python
import stripe
from datetime import datetime, timedelta

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def get_sales_report(days=7):
    """Get sales for last N days."""
    end = datetime.now()
    start = end - timedelta(days=days)
    
    charges = stripe.Charge.list(
        created={
            'gte': int(start.timestamp()),
            'lte': int(end.timestamp())
        }
    )
    
    return {
        'count': len(charges.data),
        'revenue': sum(ch.amount for ch in charges.data) / 100
    }
```

---

## 3. Email Tracking

If using SendGrid:

1. Go to SendGrid Dashboard → Statistics
2. Track opens, clicks, deliveries
3. Set up webhooks for real-time updates

Key metrics:
- Open rate: Target >20%
- Click rate: Target >5%
- Delivery rate: Target >95%

---

## 4. Simple Dashboard

Create `/analytics/dashScript` (content truncated for brevity, continue from previous)}