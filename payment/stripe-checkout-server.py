#!/usr/bin/env python3
"""
Stripe Checkout Server for CEO Autónomo Guide
Version: 1.0.0
Created: 2026-04-02

Prerequisites:
- pip install stripe flask python-dotenv
- Stripe account with API keys
- Product configured in Stripe Dashboard

Environment Variables Required:
- STRIPE_SECRET_KEY: Your Stripe secret key (sk_live_... or sk_test_...)
- STRIPE_WEBHOOK_SECRET: Webhook endpoint secret (whsec_...)
- DOMAIN: Your domain (e.g., https://yoursite.com)
"""

import os
import stripe
from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask
app = Flask(__name__)

# Configure Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')
DOMAIN = os.getenv('DOMAIN', 'http://localhost:4242')

# Product Configuration
# Configure this in Stripe Dashboard: Products → Create Product
# Then copy the Price ID here
PRICE_ID = os.getenv('STRIPE_PRICE_ID', 'price_xxxxxxxxxxxxx')  # $47.00 USD

# Digital product delivery configuration
PRODUCT_DOWNLOAD_URL = os.getenv('PRODUCT_URL', 'https://your-storage.com/ceo-autonomo-guide.pdf')

@app.route('/')
def index():
    """Serve the checkout page."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CEO Autónomo Guide - Checkout</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            .product { border: 1px solid #e0e0e0; border-radius: 8px; padding: 30px; text-align: center; }
            h1 { color: #1a1a1a; margin-bottom: 10px; }
            .price { font-size: 48px; font-weight: bold; color: #635bff; margin: 20px 0; }
            .features { text-align: left; margin: 30px 0; }
            .features li { margin: 10px 0; }
            button { background: #635bff; color: white; border: none; padding: 15px 40px; font-size: 18px; border-radius: 6px; cursor: pointer; }
            button:hover { background: #4b3fd6; }
            .guarantee { font-size: 14px; color: #666; margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="product">
            <h1>CEO Autónomo Guide</h1>
            <p>Deja de trabajar EN tu negocio. Empieza a trabajar SOBRE tu negocio.</p>
            <div class="price">$47</div>
            <ul class="features">
                <li>✓ 41 páginas de frameworks probados</li>
                <li>✓ Sistemas > Esfuerzo (metodología)</li>
                <li>✓ Dashboard de métricas incluido</li>
                <li>✓ Templates de delegación y staging</li>
                <li>✓ Acceso de por vida + updates</li>
            </ul>
            <form action="/create-checkout-session" method="POST">
                <button type="submit">Comprar Ahora</button>
            </form>
            <p class="guarantee">Garantía de 30 días. Reembolso completo si no ves valor.</p>
        </div>
    </body>
    </html>
    """

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """Create Stripe Checkout session and redirect."""
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': PRICE_ID,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f"{DOMAIN}/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{DOMAIN}/cancel",
            automatic_tax={'enabled': True},
            customer_creation='always',  # Create customer for receipt
            # Optional: collect email for delivery
            billing_address_collection='auto',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return str(e), 400

@app.route('/success')
def success():
    """Handle successful payment."""
    session_id = request.args.get('session_id')
    
    try:
        # Retrieve session to verify payment
        session = stripe.checkout.Session.retrieve(session_id)
        
        if session.payment_status == 'paid':
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>¡Gracias por tu compra!</title>
                <style>
                    body {{ font-family: sans-serif; max-width: 600px; margin: 50px auto; text-align: center; padding: 20px; }}
                    .success {{ color: #00d26a; font-size: 72px; margin-bottom: 20px; }}
                    h1 {{ color: #1a1a1a; }}
                    .download {{ background: #635bff; color: white; padding: 15px 40px; text-decoration: none; border-radius: 6px; display: inline-block; margin: 20px 0; }}
                    .email {{ margin-top: 30px; padding: 20px; background: #f5f5f5; border-radius: 8px; }}
                </style>
            </head>
            <body>
                <div class="success">✓</div>
                <h1>¡Pago Completado!</h1>
                <p>Gracias por comprar el CEO Autónomo Guide.</p>
                <a href="{PRODUCT_DOWNLOAD_URL}" class="download">Descargar Guía PDF</a>
                <div class="email">
                    <p><strong>¿Problemas con la descarga?</strong></p>
                    <p>Contacta: support@yourdomain.com</p>
                </div>
            </body>
            </html>
            """
        else:
            return "Payment not completed. Please try again.", 400
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/cancel')
def cancel():
    """Handle cancelled checkout."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Checkout Cancelled</title>
        <style>
            body { font-family: sans-serif; max-width: 600px; margin: 50px auto; text-align: center; padding: 20px; }
            .message { margin: 30px 0; }
            a { color: #635bff; }
        </style>
    </head>
    <body>
        <h1>Checkout Cancelled</h1>
        <p class="message">No te preocupes, no se realizó ningún cargo.</p>
        <p><a href="/">Volver a intentar</a></p>
    </body>
    </html>
    """

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle Stripe webhooks for automated delivery."""
    payload = request.get_data()
    sig_header = request.headers.get('Stripe-Signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError:
        return 'Invalid signature', 400
    
    # Handle successful payment
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # TODO: Implement email delivery
        # - Send email with download link using SendGrid/AWS SES
        # - Log purchase to database
        # - Add to email sequences
        
        print(f"✅ Payment completed: {session['id']}")
        print(f"   Customer: {session['customer_details']['email']}")
        print(f"   Amount: ${session['amount_total']/100:.2f}")
    
    return jsonify({'status': 'success'}), 200

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok', 'stripe_configured': bool(stripe.api_key)}), 200

if __name__ == '__main__':
    print("=" * 60)
    print("CEO Autónomo - Stripe Checkout Server")
    print("=" * 60)
    print(f"Domain: {DOMAIN}")
    print(f"Price ID: {PRICE_ID}")
    print(f"Stripe Key configured: {'Yes'