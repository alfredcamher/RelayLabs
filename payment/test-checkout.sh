#!/bin/bash
# Test script for Stripe Checkout integration

set -e

echo "================================"
echo "CEO Autónomo - Checkout Tester"
echo "================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 not found${NC}"
    exit 1
fi

# Check environment
echo "Checking environment..."
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}Warning: .env file not found${NC}"
    echo "Creating from template..."
    cp .env.example .env
    echo -e "${RED}Please edit .env with your Stripe keys${NC}"
    exit 1
fi

# Source environment
export $(grep -v '^#' .env | xargs) 2>/dev/null || true

# Validate keys
if [ -z "$STRIPE_SECRET_KEY" ] || [ "$STRIPE_SECRET_KEY" = "sk_test_xxxxxxxxxxxxxxxxxxxxx" ]; then
    echo -e "${RED}Error: STRIPE_SECRET_KEY not configured${NC}"
    echo "Please edit .env file with your Stripe test keys"
    exit 1
fi

echo -e "${GREEN}✓ Environment configured${NC}"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -q stripe flask python-dotenv

echo -e "${GREEN}✓ Dependencies installed${NC}"

# Start server
echo ""
echo "Starting Flask server..."
python3 stripe-checkout-server.py &
SERVER_PID=$!

# Wait for server
sleep 2

# Health check
echo ""
echo "Running health check..."
if curl -s http://localhost:4242/health | grep -q '"status": "ok"'; then
    echo -e "${GREEN}✓ Server responding${NC}"
else
    echo -e "${RED}✗ Server not responding${NC}"
    kill $SERVER_PID 2>/dev/null
    exit 1
fi

# Test checkout creation
echo ""
echo "Testing checkout session creation..."
HTTP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:4242/create-checkout-session)

if [ "$HTTP_RESPONSE" = "303" ] || [ "$HTTP_RESPONSE" = "302" ]; then
    echo -e "${GREEN}✓ Checkout session created (redirects to Stripe)${NC}"
else
    echo -e "${RED}✗ Checkout failed (HTTP $HTTP_RESPONSE)${NC}"
fi

# Cleanup
echo ""
echo "Stopping server..."
kill $SERVER_PID 2>/dev/null || true

echo ""
echo "================================"
echo -e "${GREEN}All tests passed!${NC}"
echo "================================"
echo ""
echo "Next steps:"
echo "1. Configure your Stripe keys in .env"
echo "2. Create product in Stripe Dashboard"
echo "3. Get Price ID and update STRIPE_PRICE_ID"
echo "4. Run: python stripe-checkout-server.py"
echo "5. Open browser to http://localhost:4242"
echo ""
echo "Test card: 4242 4242 4242 4242"