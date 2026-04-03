# Implementacion Tracking Afiliados

## Arquitectura

```
Afiliado → Link (?ref=AFF_ID) → Landing Page → Stripe Checkout → Purchase + Webhook
   ↓                                               ↓
   ↓ Cookie (60 dias)                            Guarda ref en txn
   ↓                                             Email confirmacion
   ↓ UTM params                                  Calculo comision
```

## Implementacion en Stripe

### 1. Agregar metadata en Checkout

```python
# Modificar stripe-checkout-server.py
session = stripe.checkout.Session.create(
    line_items=[...],
    mode='payment',
    success_url=...,
    cancel_url=...,
    metadata={
        'affiliate_id': request.args.get('ref', ''),
        'utm_source': request.args.get('utm_source', ''),
        'utm_campaign': request.args.get('utm_campaign', ''),
    }
)
```

### 2. Guardar en webhook

```python
# webhook_handlers.py
if event['type'] == 'checkout.session.completed':
    session = event['data']['object']
    affiliate_id = session.get('metadata', {}).get('affiliate_id')
    
    if affiliate_id:
        # Guardar en log separado para afiliados
        affiliate_log = {
            'timestamp': datetime.now().isoformat(),
            'affiliate_id': affiliate_id,
            'customer_email': session['customer_details']['email'],
            'amount': session['amount_total'],
            'commission': session['amount_total'] * 0.30,  # 30%
            'status': 'pending'  # 30 dias garantia
        }
        # Append to affiliates.log
```

## Calculo Comision

```python
def calculate_commission(amount_cents, tax_rate=0):
    """Calculate affiliate commission (30%)"""
    amount_usd = amount_cents / 100
    # Subtract tax if applicable
    net_amount = amount_usd * (1 - tax_rate)
    commission = net_amount * 0.30
    return round(commission, 2)

# Ejemplo:
# Venta: $47 USD
# Comision: $47 * 0.30 = $14.10 USD
```

## Cookie Tracking (Client-side)

```javascript
// Agregar a utm-tracker.js
// Set cookie when ref parameter present
const urlParams = new URLSearchParams(window.location.search);
const ref = urlParams.get('ref');

if (ref) {
    // Cookie 60 dias
    const sixtyDays = 60 * 24 * 60 * 60 * 1000;
    const expires = new Date(Date.now() + sixtyDays).toUTCString();
    document.cookie = `aff_ref=${ref}; expires=${expires}; path=/; domain=.ceoautonomo.com`;
}

// Pasar referral a checkout
function getAffiliateCookie() {
    return document.cookie.match(/aff_ref=([^;]+)/)?.[1] || '';
}

// En boton "Comprar"
const buyButton = document.getElementById('buy-now');
buyButton.href = buyButton.href + '&ref=' + getAffiliateCookie();
```

## Dashboard Afiliados

### API endpoints necesarios:

```python
# GET /api/affiliate/dashboard
# Requiere: affiliate_id en header o token

{
    "affiliate_id": "AFF001",
    "total_clicks": 150,
    "total_sales": 12,
    "conversion_rate": "8%",
    "revenue": 564.00,  # $47 * 12
    "commission": 169.20,  # 30%
    "pending_payouts": 169.20,
    "paid_payouts": 0.00,
    "transactions": [
        {
            "date": "2026-04-15",
            "customer": "maria@email.com",
            "amount": 47.00,
            "commission": 14.10,
            "status": "pending"  // o "paid"
        }
    ]
}
```

## Payout Automation

### Cron job mensual:

```python
# affiliate-payouts.py
# Ejecutar dia 15 de cada mes

def process_payouts():
    # 1. Lee affiliates.log
    # 2. Filtra transacciones >30 dias (garantia vencida)
    # 3. Calcula comisiones
    # 4. Genera CSV para bulk payout
    # 5. Transfiere via Stripe Connect o PayPal API
    # 6. Actualiza estado a "paid"
    pass
```

## Seguridad

### Validations:
- - [ ] Affiliate ID exists in whitelist
- - [ ] Transaction not duplicate
- - [ ] Self-referral prevention (email != affiliate_email)
- - [ ] 30-day hold for refunds

### Anti-fraud:
- - [ ] IP tracking
- - [ ] Device fingerprinting  
- - [ ] Rate limiting (max X clicks/hour per affiliate)
- - [ ] Manual review for suspicious patterns

## Integracion con Email

### Email de confirmacion para afiliados:

```
Asunto: Nueva venta generada (+$14.10)

Hola [Nombre],

Excelentes noticias:

Un comprador hizo click en tu link y compro CEO Autonomo.

Detalles de la venta:
- Monto: $47.00 USD
- Tu comision (30%): $14.10 USD
- Estado: Pendiente (30 dias garantia)
- Pago esperado: 15 mayo 2026

Total acumulado este mes: $X.XX USD

Dashboard: [LINK]
```

## Costos

- Stripe Connect: $0 (solo transacciones)
- Comision promedio: $14.10 por venta
- Target: 10 afiliados activos generando 5 ventas/mes c/u
- Costo mensual estimado: $705 USD
- Ingresos generados: $2,350 USD
- ROI: 3.3x

## Timeline

| Task | Duracion | Status |
|------|----------|--------|
| Implementar tracking cookie | 1 dia | Pendiente |
| Modificar webhook Stripe | 2 horas | Pendiente |
| Crear dashboard afiliados | 1 dia | Pendiente |
| Sistema pagos automaticos | 1 dia | Pendiente |
| Onboarding primeros 5 afiliados | 1 semana | Pendiente |
| Launch oficial programa | Semana 2 | Pendiente |

---

*Sistema listo para implementacion*  
*Creado: 2026-04-03 05:47 CDT*
