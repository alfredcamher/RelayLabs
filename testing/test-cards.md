# Stripe Test Cards Reference

## Standard Test Cards

| Card Number | Brand | Scenario |
|-------------|-------|----------|
| `4242 4242 4242 4242` | Visa | **Success** - Use for happy path testing |
| `4000 0000 0000 0002` | Visa | **Declined** - Generic decline |
| `4000 0000 0000 9995` | Visa | **Insufficient funds** |
| `4000 0000 0000 9987` | Visa | **Lost card** |
| `4000 0000 0000 9979` | Visa | **Stolen card** |
| `4000 0000 0000 0069` | Visa | **Expired card** |
| `4000 0000 0000 0127` | Visa | **Incorrect CVC** |
| `4000 0000 0000 0119` | Visa | **Processing error** |
| `4242 4242 4242 4241` | Visa | **Incorrect number** (fails Luhn) |

## 3D Secure Authentication

| Card Number | Scenario |
|-------------|----------|
| `4000 0025 0000 3155` | 3DS2 - Frictionless (no auth) |
| `4000 0027 6000 3184` | 3DS2 - Challenge (requires auth) |
| `4000 0000 0000 3220` | 3DS2 - Challenge with specific exit |

## International Cards

| Card Number | Brand | Country |
|-------------|-------|---------|
| `4000 0000 0000 0010` | Visa | Argentina (AR) |
| `4000 0000 0000 0036` | Visa | Brazil (BR) |
| `4000 0000 0000 0051` | Visa | Canada (CA) |
| `4000 0000 0000 0077` | Visa | Mexico (MX) |

## Usage Instructions

For all test cards:
- **Expiry**: Any future date (e.g., 12/30)
- **CVC**: Any 3 digits
- **ZIP**: Any 5 digits (e.g., 12345)
- **Name**: Any name

## SCA (Strong Customer Authentication)

For cards requiring 3D Secure:
1. Complete checkout
2. When Stripe shows authentication modal, click "Complete"
3. Payment completes successfully

## Webhook Testing

Use Stripe CLI to receive webhooks locally:
```bash
stripe listen --forward-to localhost:4242/webhook
```

Test events:
- `payment_intent.succeeded`
- `checkout.session.completed`
- `invoice.payment_succeeded`