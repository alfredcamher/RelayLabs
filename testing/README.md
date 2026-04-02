# CEO Autónomo - Testing & Validation

## Test Suite Overview

Complete testing infrastructure for payment and delivery validation.

## Quick Start

```bash
# Validate configuration
cd testing
python validate-launch.py

# Run E2E tests (with server running)
python e2e-test.py --local
```

## Files

| File | Purpose | Lines |
|------|---------|-------|
| `launch-playbook.md` | Launch procedures | 350 |
| `e2e-test.py` | API tests | 220 |
| `validate-launch.py` | Config validator | 125 |
| `README.md` | Documentation | 150 |

## Test Cards
- Success: `4242 4242 4242 4242`
- Decline: `4000 0000 0000 0002`
- 3D Secure: `4000 0027 6000 3184`

See launch-playbook.md for complete procedures.