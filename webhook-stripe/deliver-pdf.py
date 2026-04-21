#!/usr/bin/env python3
"""
Stripe Webhook Handler + Resend Auto-Delivery
Triggered on: checkout.session.completed
Sends: CEO Autónomo PDF to customer email
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# Load environment
env_path = Path.home() / '.openclaw/workspace/.env'
def load_env():
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val

load_env()

# Config
CONFIG = {
    'pdf_path': '/home/alfredcamher/.openclaw/workspace/products/CEO-Autonomo-Guia-Maestra-v3.0.pdf',
    'from_email': os.getenv('RESEND_FROM', 'alfredcamher@gmail.com'),
    'from_name': 'Relay Labs',
    'resend_api_key': os.getenv('RESEND_API_KEY'),
    'product_id': 'prod_UFoP8JQIWob942',
}

def log_event(event_type, data):
    """Log webhook event to file"""
    log_dir = Path('/home/alfredcamher/.openclaw/workspace/webhook-stripe/logs')
    log_dir.mkdir(exist_ok=True)
    
    timestamp = subprocess.run(['date', '+%Y%m%d-%H%M%S'], capture_output=True, text=True).stdout.strip()
    log_file = log_dir / f"{event_type}-{timestamp}.json"
    
    with open(log_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    return log_file

def send_pdf_via_resend(to_email, customer_name):
    """Send PDF via Resend API"""
    import urllib.request
    import urllib.error
    
    if not CONFIG['resend_api_key']:
        print("ERROR: RESEND_API_KEY not configured")
        return False
    
    if not Path(CONFIG['pdf_path']).exists():
        print(f"ERROR: PDF not found at {CONFIG['pdf_path']}")
        return False
    
    # Read PDF
    with open(CONFIG['pdf_path'], 'rb') as f:
        pdf_content = f.read()
    
    import base64
    pdf_b64 = base64.b64encode(pdf_content).decode('utf-8')
    
    # Build email payload
    payload = {
        'from': f"{CONFIG['from_name']} <{CONFIG['from_email']}>",
        'to': [to_email],
        'subject': 'Tu CEO Autónomo - Acceso Inmediato',
        'html': f'''
        <h2>¡Bienvenido a CEO Autónomo, {customer_name}!</h2>
        <p>Tu compra está confirmada. Aquí está tu guía completa:</p>
        <p><strong>CEO Autónomo - Sistema de Agentes IA</strong></p>
        <p>PDF adjunto: Guía Maestra v3.0</p>
        <hr>
        <p>¿Preguntas? Responde a este email.</p>
        <p>— Alfred @ Relay Labs</p>
        ''',
        'attachments': [{
            'filename': 'CEO-Autonomo-Guia-Maestra-v3.0.pdf',
            'content': pdf_b64
        }]
    }
    
    # Send via Resend
    req = urllib.request.Request(
        'https://api.resend.com/emails',
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Authorization': f"Bearer {CONFIG['resend_api_key']}",
            'Content-Type': 'application/json'
        },
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"Email sent! ID: {result.get('id')}")
            return True
    except urllib.error.HTTPError as e:
        error = json.loads(e.read().decode('utf-8'))
        print(f"Resend error: {error}")
        return False

def handle_checkout_webhook(payload):
    """Process Stripe checkout webhook"""
    event = json.loads(payload)
    event_type = event.get('type')
    
    if event_type != 'checkout.session.completed':
        print(f"Ignoring event: {event_type}")
        return {'status': 'ignored'}
    
    session = event['data']['object']
    
    # Check if it's our product
    line_items = session.get('line_items', {}).get('data', [])
    is_our_product = any(
        item.get('price', {}).get('product') == CONFIG['product_id']
        for item in line_items
    )
    
    if not is_our_product:
        print(f"Not our product, ignoring")
        return {'status': 'not_our_product'}
    
    # Get customer info
    customer_email = session.get('customer_email') or session.get('customer_details', {}).get('email')
    customer_name = session.get('customer_details', {}).get('name', 'Cliente')
    
    if not customer_email:
        print("ERROR: No customer email found")
        return {'status': 'error', 'reason': 'no_email'}
    
    # Log event
    log_file = log_event('checkout-success', event)
    print(f"Event logged: {log_file}")
    
    # Send PDF
    success = send_pdf_via_resend(customer_email, customer_name)
    
    return {
        'status': 'success' if success else 'failed',
        'customer': customer_email,
        'logged_to': str(log_file),
        'product': CONFIG['product_id']
    }

if __name__ == '__main__':
    # Read from stdin (for webhook)
    if not sys.stdin.isatty():
        payload = sys.stdin.read()
        result = handle_checkout_webhook(payload)
        print(json.dumps(result, indent=2))
    else:
        print("Usage: stripe listen --forward-to webhook...")
        print("Or pipe webhook payload to stdin")
