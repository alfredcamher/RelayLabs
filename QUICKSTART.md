# CEO Autónomo - Quick Start Guide

> Get your payment system running in 5 minutes.

## Prerequisites

- Python 3.11+
- Stripe account (free to create)
- Domain (optional for local testing)

## Step-by-Step Setup

### 1. Environment Setup (1 min)

```bash
cd payment
cp .env.example .env
```

Edit `.env`:
```bash
STRIPE_SECRET_KEY=sk_test_your_test_key_here
STRIPE_PUBLISHABLE_KEY=pk_test_your_test_key_here
DOMAIN=http://localhost:4242
```

### 2. Get Stripe Keys (2 min)

1. Go to [stripe.com](https://stripe.com) → Sign up → Developers → API Keys
2. Switch to "Test mode"
3. Copy `Secret key` → paste as `STRIPE_SECRET_KEY`
4. Copy `Publishable key` → paste as `STRIPE_PUBLISHABLE_KEY`

### 3. Install & Run (2 min)

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python stripe-checkout-server.py

# Server starts on http://localhost:4242
```

### 4. Test Purchase (30 sec)

1. Open http://localhost:4242
2. Click "