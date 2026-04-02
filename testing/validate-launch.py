#!/usr/bin/env python3
"""
CEO Autónomo - Launch Validation Script
Validates all pre-launch requirements are met
"""

import os
import sys

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'

REQUIRED_VARS = [
    'STRIPE_SECRET_KEY',
    'STRIPE_WEBHOOK_SECRET',
    'STRIPE_PRICE_ID',
    'DOMAIN',
    'PRODUCT_URL'
]

OPTIONAL_VARS = [
    'EMAIL_PROVIDER',
    'FROM_EMAIL',
    'SENDGRID_API_KEY'
]

def check_env_vars():
    print("\n📋 Environment Variables Check")
    print("-" * 40)
    
    all_good = True
    
    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value and not value.startswith('xxxxx'):
            print(f"✓ {var}: Set")
        else:
            print(f"✗ {var}: NOT SET")
            all_good = False
    
    print("\nOptional:")
    for var in OPTIONAL_VARS:
        value = os.getenv(var)
        status = "Set" if value else "Not set"
        print(f"• {var}: {status}")
    
    return all_good

def check_files():
    print("\n📁 Required Files Check")
    print("-" * 40)
    
    files = [
        ('../payment/.env', '.env file'),
        ('../payment/stripe-checkout-server.py', 'Payment server'),
        ('../payment/webhook_handlers.py', 'Email handlers'),
    ]
    
    all_exist = True
    for filepath, desc in files:
        full = os.path.join(os.path.dirname(__file__), filepath)
        if os.path.exists(full):
            print(f"✓ {desc}")
        else:
            print(f"✗ {desc} - MISSING")
            all_exist = False
    
    return all_exist

def check_stripe_key():
    print("\n💳 Stripe Key Check")
    print("-" * 40)
    
    key = os.getenv('STRIPE_SECRET_KEY', '')
    
    if not key:
        print("✗ STRIPE_SECRET_KEY not set")
        return False
    
    if key.startswith('sk_test_'):
        print("⚠️  TEST keys (ok for testing)")
        return True
    elif key.startswith('sk_live_'):
        print("✓ LIVE keys (production)")
        return True
    else:
        print("✗ Invalid format")
        return False

def check_domain():
    print("\n🌐 Domain Check")
    print("-" * 40)
    
    domain = os.getenv('DOMAIN', '')
    
    if not domain:
        print("✗ DOMAIN not set")
        return False
    
    if 'localhost' in domain:
        print("⚠️  localhost (testing only)")
        return True
    elif domain.startswith('https://'):
        print(f"✓ {domain}")
        return True
    else:
        print("⚠️  should use HTTPS")
        return False

def main():
    print("=" * 50)
    print("CEO AUTÓNOMO - Launch Validator")
    print("=" * 50)
    
    results = [
        ("Environment", check_env_vars()),
        ("Files", check_files()),
        ("Stripe", check_stripe_key()),
        ("Domain", check_domain()),
    ]
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    for name, passed in results:
        status = f"{Colors.GREEN}✓ PASS{Colors.END}" if passed else f"{Colors.RED}✗ FAIL{Colors.END}"
        print(f"{name}: {status}")
    
    all_passed = all(r[1] for r in results)
    
    print("\n" + "=" * 50)
    if all_passed:
        print(f"{Colors.GREEN}🚀 READY FOR LAUNCH!{Colors.END}")
    else:
        print(f"{Colors.RED}⚠️  FIX BLOCKERS BEFORE LAUNCH{Colors.END}")
    print("=" * 50)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())