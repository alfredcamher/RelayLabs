# SETUP WEBHOOK - Entrega Automática Stripe

**Objetivo:** Cuando cliente paga, recibe PDF automáticamente vía email
**Tiempo:** 20 minutos
**Costo:** $0 (Cloudflare free tier)

---

## Paso 1: Crear Cuentas (5 min)

### Cloudflare
1. Ve a https://dash.cloudflare.com/sign-up
2. Cuenta gratis (no necesitas dominio propio)
3. Verifica email

### Resend (Envío emails)
1. Ve a https://resend.com
2. Cuenta gratis (3000 emails/mes)
3. Verifica dominio o usa resend.dev
4. Copia API Key: `re_xxxxxxxxx`

---

## Paso 2: Instalar Wrangler CLI (3 min)

```bash
# Instalar wrangler global
npm install -g wrangler

# Login a Cloudflare
wrangler login

# Verificar
wrangler whoami
```

---

## Paso 3: Crear Worker (5 min)

```bash
# Crear proyecto
mkdir -p relaylabs-webhook
cd relaylabs-webhook

# Copiar archivos de este folder
cp /home/alfredcamher/.openclaw/workspace/webhook-stripe/worker.js .
cp /home/alfredcamher/.openclaw/workspace/webhook-stripe/wrangler.toml .

# Crear KV namespace para PDF
wrangler kv:namespace create "PDF_STORAGE"

# Output va a mostrar:
# "id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

**Copiar el ID** y pégalo en `wrangler.toml`:

```toml
[[kv_namespaces]]
binding = "PDF_STORAGE"
id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # <-- TU ID
```

---

## Paso 4: Subir PDF a KV (2 min)

```bash
# Codificar PDF a base64
base64 CEO-Autonomo-Guia-Completo.pdf > pdf_base64.txt

# Subir a KV
wrangler kv:key put --namespace-id=xxxxxxxxxxx "pdf-content" --path=pdf_base64.txt
```

---

## Paso 5: Secrets (2 min)

```bash
# Stripe Webhook Secret (lo obtienes en paso 6)
wrangler secret put STRIPE_WEBHOOK_SECRET
# Pegar: whsec_xxxxx

# Resend API Key
wrangler secret put RESEND_API_KEY
# Pegar: re_xxxxx
```

---

## Paso 6: Deploy Worker (2 min)

```bash
# Deploy
wrangler deploy

# Output:
# ✅ Published!
# https://relaylabs-stripe-webhook.tu-usuario.workers.dev
```

**Copiar URL** (la vas a pegar en Stripe)

---

## Paso 7: Configurar Webhook en Stripe (3 min)

1. Ve a https://dashboard.stripe.com/webhooks
2. Click "Add endpoint"
3. **Endpoint URL:** `https://relaylabs-stripe-webhook.tu-usuario.workers.dev`
4. **Events to listen to:**
   - ✅ `checkout.session.completed`
5. Click "Add endpoint"
6. **Copiar "Signing secret"** (empieza con `whsec_`)
7. Pegar en tu terminal:
   ```bash
   wrangler secret put STRIPE_WEBHOOK_SECRET
   # Pegar: whsec_xxxxx
   ```
8. Redeploy:
   ```bash
   wrangler deploy
   ```

---

## Paso 8: Test (1 min)

1. Ve a https://dashboard.stripe.com/test/webhooks
2. Click "Send test event"
3. Selecciona `checkout.session.completed`
4. Verificar en terminal de Cloudflare (Logs)

**O prueba real:**
- Compra tu propio producto ($39)
- Revisa email

---

## Troubleshooting

### "Webhook signature invalid"
- Verificar `STRIPE_WEBHOOK_SECRET` está correcto
- Webhook endpoint URL debe ser exacto (sin trailing slash)

### "Email not sent"
- Verificar `RESEND_API_KEY`
- Verificar `FROM_EMAIL` está verificado en Resend

### "PDF not attached"
- Verificar PDF subió a KV: `wrangler kv:key list --namespace-id=xxx`
- Verificar key name es `"pdf-content"`

---

## Costos

| Servicio | Free Tier | Costo real |
|----------|-----------|------------|
| Cloudflare Workers | 100k requests/día | $0 |
| Cloudflare KV | 1GB storage | $0 |
| Resend | 3000 emails/mes | $0 |
| **Total** | | **$0** hasta 3000 ventas/mes |

---

## Post-Setup

Una vez funcionando:
1. ✅ Checkout automático entrega PDF
2. ✅ Logs en Cloudflare dashboard
3. ✅ Escalable a 1000+ ventas/día
4. ✅ Código privado (no en GitHub público)

---

**Contacto:** alfredcamher@gmail.com
