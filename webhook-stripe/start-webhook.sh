#!/bin/bash
# Stripe Webhook Listener - Auto-delivery System with Resend
# Usage: ./start-webhook.sh

echo "=== Relay Labs - Stripe Webhook Listener ==="
echo "Product: CEO Autónomo (prod_UFoP8JQIWob942)"
echo "PDF Delivery: Resend API (auto)"
echo ""

# Check dependencies
if ! stripe config --list > /dev/null 2>&1; then
    echo "❌ Stripe CLI not authenticated"
    echo "Run: stripe login"
    exit 1
fi

echo "✓ Stripe CLI authenticated"

# Check Python script exists
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DELIVERY_SCRIPT="$SCRIPT_DIR/deliver-pdf.py"

if [[ ! -f "$DELIVERY_SCRIPT" ]]; then
    echo "❌ Delivery script not found: $DELIVERY_SCRIPT"
    exit 1
fi

echo "✓ Delivery script ready"

# Create logs directory
mkdir -p "$SCRIPT_DIR/logs"

echo ""
echo "Starting webhook listener..."
echo "Events: checkout.session.completed"
echo "Logs: $SCRIPT_DIR/logs/"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Listen and pipe to Python handler
stripe listen \
    --events checkout.session.completed \
    --print-json | while read -r line; do
    
    # Skip empty lines
    [[ -z "$line" ]] && continue
    
    echo "$line" | python3 "$DELIVERY_SCRIPT"
done
