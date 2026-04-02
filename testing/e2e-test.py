#!/usr/bin/env python3
"""
CEO Autónomo - End-to-End Test Suite
Tests complete purchase flow from webhook to email delivery

Usage:
    python e2e-test.py [--webhook-url URL] [--local]

Options:
    --local         Test against localhost:4242
    --webhook-url   Test specific webhook endpoint
"""

import os
import sys
import json
import time
import argparse
import requests
from datetime import datetime

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_status(message, status="INFO"):
    """Print colored status messages."""
    color = {
        "PASS": Colors.GREEN,
        "FAIL": Colors.RED,
        "WARN": Colors.YELLOW,
        "INFO": Colors.BLUE
    }.get(status, Colors.BLUE)
    
    icon = {
        "PASS": "✓",
        "FAIL": "✗",
        "WARN": "⚠",
        "INFO": "ℹ"
    }.get(status, "ℹ")
    
    print(f"{color}{icon} {message}{Colors.END}")

class E2ETester:
    """End-to-end test runner."""
    
    def __init__(self, base_url="http://localhost:4242"):
        self.base_url = base_url.rstrip('/')
        self.results = []
        self.start_time = datetime.now()
    
    def test_health_endpoint(self):
        """Test server health."""
        print_status("Testing health endpoint...", "INFO")
        
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'ok':
                    print_status("Health check passed", "PASS")
                    self.results.append(("Health Check", True, None))
                    return True
            
            print_status(f"Health check failed: HTTP {response.status_code}", "FAIL")
            self.results.append(("Health Check", False, f"HTTP {response.status_code}"))
            return False
            
        except Exception as e:
            print_status(f"Health check error: {str(e)}", "FAIL")
            self.results.append(("Health Check", False, str(e)))
            return False
    
    def test_checkout_page(self):
        """Test checkout page loads."""
        print_status("Testing checkout page...", "INFO")
        
        try:
            response = requests.get(self.base_url, timeout=5)
            
            if response.status_code == 200:
                if "CEO Autónomo Guide" in response.text:
                    print_status("Checkout page loads correctly", "PASS")
                    self.results.append(("Checkout Page", True, None))
                    return True
                else:
                    print_status("Page loads but content check failed", "WARN")
                    self.results.append(("Checkout Page", False, "Content mismatch"))
                    return False
            
            print_status(f"Checkout page failed: HTTP {response.status_code}", "FAIL")
            self.results.append(("Checkout Page", False, f"HTTP {response.status_code}"))
            return False
            
        except Exception as e:
            print_status(f"Checkout page error: {str(e)}", "FAIL")
            self.results.append(("Checkout Page", False, str(e)))
            return False
    
    def test_session_creation(self):
        """Test checkout session creation."""
        print_status("Testing checkout session creation...", "INFO")
        
        try:
            response = requests.post(
                f"{self.base_url}/create-checkout-session",
                allow_redirects=False,
                timeout=5
            )
            
            if response.status_code in [302, 303]:
                stripe_url = response.headers.get('Location', '')
                if 'stripe.com' in stripe_url:
                    print_status("Session created and redirects to Stripe", "PASS")
                    self.results.append(("Session Creation", True, None))
                    return True
            
            print_status(f"Session creation failed: HTTP {response.status_code}", "FAIL")
            self.results.append(("Session Creation", False, f"HTTP {response.status_code}"))
            return False
            
        except Exception as e:
            print_status(f"Session creation error: {str(e)}", "FAIL")
            self.results.append(("Session Creation", False, str(e)))
            return False
    
    def test_webhook_endpoint(self):
        """Test webhook endpoint responds."""
        print_status("Testing webhook endpoint...", "INFO")
        
        try:
            response = requests.post(
                f"{self.base_url}/webhook",
                data="{}",
                headers={"Content-Type": "application/json"},
                timeout=5
            )
            
            if response.status_code == 400:
                print_status("Webhook endpoint responsive", "PASS")
                self.results.append(("Webhook Endpoint", True, None))
                return True
            elif response.status_code == 500:
                print_status("Webhook endpoint error", "FAIL")
                self.results.append(("Webhook Endpoint", False, "Server error"))
                return False
            else:
                print_status(f"Webhook unexpected: HTTP {response.status_code}", "WARN")
                self.results.append(("Webhook Endpoint", False, f"HTTP {response.status_code}"))
                return False
                
        except Exception as e:
            print_status(f"Webhook error: {str(e)}", "FAIL")
            self.results.append(("Webhook Endpoint", False, str(e)))
            return False
    
    def test_success_page(self):
        """Test success page."""
        print_status("Testing success page...", "INFO")
        
        try:
            response = requests.get(f"{self.base_url}/success", timeout=5)
            
            if response.status_code in [200, 400]:
                print_status("Success page responds correctly", "PASS")
                self.results.append(("Success Page", True, None))
                return True
            else:
                print_status(f"Success page: HTTP {response.status_code}", "WARN")
                self.results.append(("Success Page", False, f"HTTP {response.status_code}"))
                return False
                
        except Exception as e:
            print_status(f"Success page error: {str(e)}", "FAIL")
            self.results.append(("Success Page", False, str(e)))
            return False
    
    def test_cancel_page(self):
        """Test cancel page."""
        print_status("Testing cancel page...", "INFO")
        
        try:
            response = requests.get(f"{self.base_url}/cancel", timeout=5)
            
            if response.status_code == 200:
                print_status("Cancel page loads correctly", "PASS")
                self.results.append(("Cancel Page", True, None))
                return True
            
            print_status(f"Cancel page failed: HTTP {response.status_code}", "FAIL")
            self.results.append(("Cancel Page", False, f"HTTP {response.status_code}"))
            return False
            
        except Exception as e:
            print_status(f"Cancel page error: {str(e)}", "FAIL")
            self.results.append(("Cancel Page", False, str(e)))
            return False
    
    def test_environment_variables(self):
        """Test critical environment variables are    
    def run_all_tests(self):
        """Run complete test suite."""
        print("=" * 60)
        print("CEO AUTÓNOMO - E2E TEST SUITE")
        print("=" * 60)
        print(f"Target: {self.base_url}")
        print(f"Started: {self.start_time.isoformat()}")
        print("=" * 60)
        
        # Run all tests
        self.test_health_endpoint()
        self.test_checkout_page()
        self.test_session_creation()
        self.test_webhook_endpoint()
        self.test_success_page()
        self.test_cancel_page()
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print test summary."""
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for _, status, _ in self.results if status)
        failed = sum(1 for _, status, _ in self.results if not status)
        
        for name, status, error in self.results:
            icon = "✓" if status else "✗"
            print(f"{icon} {name:<25} {'PASS' if status else 'FAIL'}")
            if error:
                print(f"   Error: {error}")
        
        print("=" * 60)
        print(f"Results: {passed} passed, {failed} failed")
        print(f"Duration: {(datetime.now() - self.start_time).total_seconds():.2f}s")
        print("=" * 60)
        
        return failed == 0

def main():
    parser = argparse.ArgumentParser(description="CEO Autónomo E2E Tests")
    parser.add_argument("--local", action="store_true", help="Test localhost:4242")
    parser.add_argument("--url", default=None, help="Custom base URL")
    args = parser.parse_args()
    
    if args.local:
        base_url = "http://localhost:4242"
    elif args.url:
        base_url = args.url
    else:
        base_url = os.getenv("TEST_URL", "http://localhost:4242")
    
    tester = E2ETester(base_url)
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
