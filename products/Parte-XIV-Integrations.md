# PARTE XIV: INTEGRACIONES AVANZADAS
**Conectando tu Sistema con el Mundo**

---

## 14.1 Stripe Integration - Automatización Completa

### Setup Inicial

**Paso 1: Configuración de Producto**

```javascript
// stripe-product-setup.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

async function setupProduct() {
  // Crear producto
  const product = await stripe.products.create({
    name: 'CEO Autónomo - Sistema de Agentes IA',
    description: 'Guía completa + templates + stack tecnológico',
    images: ['https://relaylabs.com/product-image.jpg'],
    metadata: {
      category: 'digital-product',
      version: '1.0'
    }
  });
  
  // Crear precio
  const price = await stripe.prices.create({
    product: product.id,
    unit_amount: 3900, // $39.00 USD
    currency: 'usd',
    metadata: {
      original_price: '25000', // $250 for anchoring
      savings: '84%'
    }
  });
  
  console.log('Price ID:', price.id);
  console.log('Product ID:', product.id);
  return { product, price };
}

module.exports = { setupProduct };
```

**Paso 2: Checkout Link**

```javascript
// checkout-link.js
async function createCheckoutSession(priceId) {
  const session = await stripe.checkout.sessions.create({
    line_items: [{
      price: priceId,
      quantity: 1,
    }],
    mode: 'payment',
    success_url: 'https://relaylabs.com/thank-you?session_id={CHECKOUT_SESSION_ID}',
    cancel_url: 'https://relaylabs.com/canceled',
    customer_email: true,
    automatic_tax: { enabled: true },
    invoice_creation: {
      enabled: true,
      invoice_data: {
        description: 'CEO Autónomo - Digital Product',
        footer: 'Gracias por tu compra. Acceso enviado por email.',
      }
    },
  });
  
  return session.url;
}
```

---

### Webhook Automation

**Cloudflare Worker para Delivery Automático:**

```javascript
// worker.js
export default {
  async fetch(request, env) {
    // Validar método
    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }
    
    // Validar signature
    const sig = request.headers.get('stripe-signature');
    const event = await validateStripeWebhook(request, sig, env.STRIPE_WEBHOOK_SECRET);
    
    // Procesar evento
    switch (event.type) {
      case 'checkout.session.completed':
        await handleSuccessfulPayment(event.data.object, env);
        break;
      
      case 'invoice.payment_failed':
        await handleFailedPayment(event.data.object, env);
        break;
      
      case 'charge.refunded':
        await handleRefund(event.data.object, env);
        break;
    }
    
    return new Response('OK');
  }
}

async function handleSuccessfulPayment(session, env) {
  const customerEmail = session.customer_email;
  const customerId = session.customer;
  
  // Generar access token único
  const accessToken = generateToken(customerId);
  
  // Guardar orden en KV
  await env.ORDERS.put(customerId, JSON.stringify({
    email: customerEmail,
    purchased_at: new Date().toISOString(),
    token: accessToken,
    status: 'active'
  }));
  
  // Enviar email de acceso
  await sendDeliveryEmail(customerEmail, accessToken, env.RESEND_API_KEY);
  
  // Log para analytics
  await logEvent('purchase', {
    customer_id: customerId,
    amount: session.amount_total,
    currency: session.currency
  });
}

async function sendDeliveryEmail(email, token, apiKey) {
  const response = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      from: 'Alfred <alfred@relaylabs.com>',
      to: email,
      subject: 'Tu CEO Autónomo está listo 🎯',
      html: `
        <h1>Bienvenido al sistema de agentes IA</h1>
        <p>Tu acceso:</p>
        <a href="https://relaylabs.com/download?token=${token}">
          Descargar Guía
        </a>
        <p>O usa este link: https://relaylabs.com/download?token=${token}</p>
        <p>Guarda este email - tu link es único.</p>
      `
    })
  });
  
  return response.ok;
}
```

---

### Dashboard de Revenue

**Script para métricas diarias:**

```python
# revenue_tracker.py
import stripe
from datetime import datetime, timedelta

stripe.api_key = process.env.STRIPE_SECRET_KEY

def get_daily_metrics(date=None):
    if date is None:
        date = datetime.now()
    
    start = int(date.replace(hour=0, minute=0, second=0).timestamp())
    end = int(date.replace(hour=23, minute=59, second=59).timestamp())
    
    # Obtener charges
    charges = stripe.Charge.list(
        created={'gte': start, 'lte': end},
        limit=100
    )
    
    metrics = {
        'date': date.strftime('%Y-%m-%d'),
        'revenue': sum(c.amount for c in charges if c.paid) / 100,
        'refunds': sum(c.amount_refunded for c in charges) / 100,
        'net': 0,
        'successful': len([c for c in charges if c.paid]),
        'failed': len([c for c in charges if not c.paid and c.status != 'refunded']),
        'refunded': len([c for c in charges if c.refunded]),
    }
    metrics['net'] = metrics['revenue'] - metrics['refunds']
    
    return metrics

def save_metrics(metrics, path='memory/revenue-daily.json'):
    import json
    
    # Cargar existente
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    # Agregar nuevo
    data.append(metrics)
    
    # Guardar
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def generate_report(days=7):
    from datetime import timedelta
    
    report = []
    for i in range(days-1, -1, -1):
        date = datetime.now() - timedelta(days=i)
        metrics = get_daily_metrics(date)
        report.append(metrics)
    
    return report

# Ejecutar diariamente
if __name__ == '__main__':
    metrics = get_daily_metrics()
    save_metrics(metrics)
    print(f"Revenue today: ${metrics['revenue']:.2f}")
```

---

## 14.2 Email Automation con Resend

### Setup Transaccional

**Email Templates:**

```javascript
// emails/welcome.js
module.exports = {
  subject: 'Bienvenido a CEO Autónomo, {{name}}',
  html: `
    <html>
    <body style="font-family: sans-serif; max-width: 600px;">
      <h1 style="color: #333;">¡Hola {{name}}!</h1>
      
      <p>Gracias por adquirir CEO Autónomo.</p>
      
      <div style="background: #f5f5f5; padding: 20px; margin: 20px 0;">
        <h2>Tu acceso:</h2>
        <ul>
          <li>📄 Guía PDF: <a href="{{download_link}}">Descargar</a></li>
          <li>📝 Templates: <a href="{{templates_link}}">Ver</a></li>
          <li>💻 Stack Scripts: <a href="{{scripts_link}}">Instalar</a></li>
        </ul>
      </div>
      
      <p>Próximos pasos:</p>
      <ol>
        <li>Lee <strong>Parte I: Introducción</strong></li>
        <li>Configura tu entorno (Semana 1)</li>
        <li>Crea tu primer agente (Semana 2)</li>
      </ol>
      
      <p>¿Preguntas? Responde a este email.</p>
      
      <p>Ship or shut up,<br>Alfred</p>
    </body>
    </html>
  `
};
```

**Agente de Email:**

```python
# email_agent.py
import os
import resend

resend.api_key = os.getenv('RESEND_API_KEY')

class EmailAgent:
    def __init__(self):
        self.sent_emails = []
    
    def send_welcome(self, customer):
        email = resend.Emails.send({
            "from": "Alfred <alfred@relaylabs.com>",
            "to": customer.email,
            "subject": f"Bienvenido, {customer.name}",
            "html": self.render_template('welcome', customer)
        })
        
        self.log_sent('welcome', customer.email)
        return email
    
    def send_followup_sequence