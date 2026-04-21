#!/bin/bash
# Stripe Webhook Listener - Auto-delivery System
# Usage: ./start-webhook.sh [forward-url]

WEBHOOK_SECRET=""
PORT=4242

echo "=== Relay Labs - Stripe Webhook Listener ==="
echo "Product: CEO Autónomo (prod_UFoP8JQIWob942)"
echo "PDF: products/CEO-Autonomo-Guia-Maestra-v3.0.pdf"
echo ""

# Check if stripe is authenticated
if ! stripe config --list > /dev/null 2>&1; then
    echo "Error: Stripe CLI not authenticated"
    echo "Run: stripe login"
    exit 1
fi

echo "Stripe CLI authenticated ✓"

# Forward to local endpoint or just log
echo ""
echo "Starting webhook listener for 'checkout.session.completed'..."
echo "Events will be logged to: ./webhook-logs/"
echo ""

# Create logs directory
mkdir -p ~/workspace/webhook-stripe/webhook-logs

# Listen and log
echo "Listening... Press Ctrl+C to stop"

stripe listen \
    --events checkout.session.completed \
    --print-json | while read line; do
    # Log with timestamp
    TIMESTAMP=$(date +%Y%m%d-%H%M%S)
    echo "$line" > ~/workspace/webhook-stripe/webhook-logs/event-${TIMESTAMP}.json
    
    # Extract customer email and log
    echo "[$(date +%H:%M:%S)] Event received, saved to webhook-logs/event-${TIMESTAMP}.json"
    
    # TODO: Add PDF delivery integration here
    # When ready, integrate with Resend API for auto-delivery
    echo "[$(date +%H:%M:%S)] PDF delivery: READY (manual process until Resend configured)"
done
