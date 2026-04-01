# Stripe Checkout Integration Guide

## Configuración de Pagos

### Paso 1: Crear Cuenta Stripe
- URL: https://stripe.com
- Email: alfredcamher@gmail.com
- Verificar cuenta con datos bancarios

### Paso 2: Producto en Stripe Dashboard

**Producto:** CEO Autónomo Guía PDF
**Precio:** $39 USD (one-time)

```json
{
  "name": "CEO Autónomo: Sistema de Agentes IA",
  "description": "Guía completa + Templates + Stack HKUDS",
  "price": 3900,
  "currency": "usd",
  "type": "one_time"
}
```

### Paso 3: Checkout Session

```javascript
const session = await stripe.checkout.sessions.create({
  payment_method_types: ['card'],
  line_items: [{
    price_data: {
      currency: 'usd',
      product_data: {
        name: 'CEO Autónomo',
      },
      unit_amount: 3900,
    },
    quantity: 1,
  }],
  mode: 'payment',
  success_url: 'https://alfredcamher.com/success',
  cancel_url: 'https://alfredcamher.com/cancel',
});
```

### Paso 4: Webhook para Entrega

```javascript
// Endpoint: /webhook
stripe.webhooks.constructEvent(
  payload,
  signature,
  webhookSecret
);

// On payment success:
// - Send email with PDF link
// - Grant Notion access
// - Log to revenue tracker
```

### Paso 5: Email de Confirmación

**From:** alfredcamher@gmail.com  
**Subject:** Tu CEO Autónomo está listo 🎯

```
Hola,

Gracias por adquirir CEO Autónomo.

Tu acceso:
- PDF: [Link descarga]
- Templates: [Link Notion]
- Stack HKUDS: [Instrucciones]

¿Preguntas? Responde a este email.

Alfred CamHer
```

---

## Deploy Opciones (Gratuitas)

### Opción A: GitHub Pages
1. Push `landing-page/` a repo GitHub
2. Settings → Pages → Source: main
3. URL: `alfredcamher.github.io/ceo-autonomo`

### Opción B: Cloudflare Pages
1. Fork repo
2. Connect to Cloudflare Pages
3. Build command: none (static)
4. URL: `ceo-autonomo.pages.dev`

### Opción C: Netlify (Free)
1. Drag & drop folder
2. Automatic URL
3. Custom domain: optional

---

## Dominio Recomendado

**Opciones:**
- `alfredcamher.com` (~$12/año)
- `ceoautonomo.com` (~$12/año)
- `agenteceo.com` (~$12/año)

**DNS:** A record → hosting provider
