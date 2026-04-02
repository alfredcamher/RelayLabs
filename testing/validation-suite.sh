#!/bin/bash
# CEO Autónomo - Complete Validation Suite
# Run before any launch

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASSED=0
FAILED=0

check_pass() {
    echo -e "${GREEN}✓${NC} $1"
    ((PASSED++))
}

check_fail() {
    echo -e "${RED}✗${NC} $1"
    ((FAILED++))
}

check_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

echo "=================================================="
echo "  CEO AUTÓNOMO - LAUNCH VALIDATION SUITE"
echo "=================================================="
echo ""

# 1. Environment validation
echo "1. Checking environment files..."
if [ -f "payment/.env" ]; then
    check_pass ".env file exists"
    
    # Check required vars
    source payment/.env 2>/dev/null || true
    
    [ -n "$STRIPE_SECRET_KEY" ] && check_pass "STRIPE_SECRET_KEY set" || check_fail "STRIPE_SECRET_KEY missing"
    [ -n "$STRIPE_PRICE_ID" ] && check_pass "STRIPE_PRICE_ID set" || check_fail "STRIPE_PRICE_ID missing"
    [ -n "$DOMAIN" ] && check_pass "DOMAIN set" || check_fail "DOMAIN missing"
else
    check_fail ".env file missing (copy from .env.example)"
fi

# 2. File structure
echo ""
echo "2. Validating file structure..."
[ -f "products/CEO-Autonomo-Guia-COMPLETO-v2.1.md" ] && check_pass "Product markdown exists" || check_fail "Product markdown missing"
[ -f "marketing/landing-page-copy.md" ] && check_pass "Landing copy exists" || check_fail "Landing copy missing"
[ -f "payment/stripe-checkout-server.py" ] && check_pass "Payment server exists" || check_fail "Payment server missing"
[ -f "payment/webhook_handlers.py" ] && check_pass "Webhook handlers exist" || check_fail "Webhook handlers missing"

# 3. Dependencies
echo ""
echo "3. Checking dependencies..."
python3 -c "import stripe" 2>/dev/null && check_pass "stripe package installed" || check_fail "stripe package missing"
python3 -c "import flask" 2>/dev/null && check_pass "flask package installed" || check_fail "flask package missing"

# 4. Git status
echo ""
echo "4. Checking git repository..."
git diff --quiet 2>/dev/null && check_pass "Working directory clean" || check_warn "Uncommitted changes present"

# 5. Python syntax
echo ""
echo "5. Validating Python syntax..."
python3 -m py_compile payment/stripe-checkout-server.py 2>/dev/null && check_pass "Server syntax valid" || check_fail "Server has syntax errors"
python3 -m py_compile payment/webhook_handlers.py 2>/dev/null && check_pass "Handlers syntax valid" || check_fail "Handlers have syntax errors"

# 6. Docker (optional)
echo ""
echo "6. Checking Docker (optional)..."
if command -v docker &> /dev/null; then
    check_pass "Docker available"
    [ -f "payment/Dockerfile" ] && check_pass "Dockerfile exists" || check_fail "Dockerfile missing"
else
    check_warn "Docker not installed (optional)"
fi

# 7. Summary
echo ""
echo "=================================================="
echo "  VALIDATION SUMMARY"
echo "=================================================="
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo "=================================================="

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed! Ready for launch.${NC}"
    exit 0
else
    echo -e "${RED}✗ $FAILED checks failed. Fix before launching.${NC}"
    exit 1
fi