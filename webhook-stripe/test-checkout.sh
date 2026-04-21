#!/bin/bash
# Test Stripe Checkout - CEO Autónomo
# Creates a test checkout session

PRODUCT_ID="prod_UFoP8JQIWob942"
PRICE_ID="price_1THImVJP2vdPzDc4ZE98yzyh"

echo "=== Relay Labs - Test Checkout ==="
echo "Product: CEO Autónomo"
echo ""

# Create test checkout session
echo "Creating test checkout session..."

stripe checkout sessions create \
    --line-items="price=${PRICE_ID},quantity=1" \
    --success-url="https://alfredcamher.github.io/RelayLabs/success.html" \
    --cancel-url="https://alfredcamher.github.io/RelayLabs/cancel.html" \
    --customer-email="test@relaylabs.com" \
    --mode=payment \
    --print-json 2>&1 | tee /tmp/test-checkout.json

SESSION_URL=$(cat /tmp/test-checkout.json | grep -o '"url": "[^"]*"' | head -1 | cut -d'"' -f4)

echo ""
echo "Test checkout created!"
echo "URL: $SESSION_URL"
echo ""
echo "To test webhook:"
echo "1. Open URL in browser"
echo "2. Use test card: 4242 4242 4242 4242"
echo "3. Complete purchase"
echo "4. Check webhook-logs/ for event"
