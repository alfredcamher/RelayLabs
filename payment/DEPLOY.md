# CEO Autónomo - Deployment Guide

## Quick Deploy Options

### Option 1: Render (Easiest - Free Tier)

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. New → Web Service → Connect your repo
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -w 4 -b 0.0.0.0:$PORT stripe-checkout-server:app`
   - Python 3.11
5. Add environment variables from `.env`
6. Deploy

**Cost:** Free tier: 512MB RAM, sleeps after 15 min inactivity

---

### Option 2: Railway (Easy - Free Tier)

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. Select repo
5. Configure environment variables
6. Deploy

**Cost:** Free: $5 credit/month, generous limits

---

### Option 3: Fly.io (Production-Ready)

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Launch app
fly launch --name ceo-autonomo-payment

# Set secrets
fly secrets set STRIPE_SECRET_KEY=sk_live_xxxxx
fly secrets set STRIPE_WEBHOOK_SECRET=whsec_xxxxx
fly secrets set STRIPE_PRICE_ID=price_xxxxx
fly secrets set DOMAIN=https://ceo-autonomo-payment.fly.dev
fly secrets set PRODUCT_URL=https://your-cdn.com/ceo-autonomo-guide.pdf

# Deploy
fly deploy
```

**Cost:** Free allowance: 2340 hours/month, 1GB RAM, 3GB storage

---

### Option 4: VPS (DigitalOcean, Hetzner, etc.)

```bash
# SSH to your server
ssh user@your-server.com

# Clone and setup
git clone https://github.com/yourusername/ceo-autonomo.git
cd ceo-autonomo/payment

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install gunicorn
pip install gunicorn

# Create .env file (see SETUP.md)
nano .env

# Test run
python stripe-checkout-server.py &

# Set up systemd service
sudo nano /etc/systemd/system/stripe-server.service
```

**systemd service:**
```ini
[Unit]
Description=CEO Autonomo Payment Server
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/user/ceo-autonomo/payment
ExecStart=/home/user/ceo-autonomo/payment/venv/bin/gunicorn -w 4 -b 0.0.0.0:4242 stripe-checkout-server:app
Restart=always
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start
sudo systemctl enable stripe-server
sudo systemctl start stripe-server

# Check status
sudo systemctl status stripe-server
```

---

### Option 5: Docker (Any Platform)

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## Webhook Configuration

After deployment, configure Stripe webhook:

1. Go to Stripe Dashboard → Developers → Webhooks
2. Add endpoint: `https://your-domain.com/webhook`
3. Select events:
   - `checkout.session.completed`
   - `checkout.session.async_payment_succeeded`
4. Copy webhook secret to env var `STRIPE_WEBHOOK_SECRET`

---

## SSL/HTTPS Setup

### With Nginx (VPS option):

```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renew
sudo certbot renew --dry-run
```

### With Nginx config:

```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:4242;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}
```

---

## Post-Deploy Checklist

- [ ] Health check passes: `curl https://your-domain.com/health`
- [ ] Checkout page loads: `curl https://your-domain.com/`
- [ ] Stripe webhook configured and verified
- [ ] Test payment completes successfully
- [ ] Email delivery works (if configured)
- [ ] PDF is accessible from success page
- [ ] SSL certificate valid
- [ ] Analytics tracking enabled

---

## Monitoring

### Health Endpoint
```bash
curl https://your-domain.com/health
# Expected: {"status": "ok", "stripe_configured": true}
```

### View Logs

**Fly.io:**
```bash
fly logs
```

**Railway:**
Dashboard → Logs tab

**VPS:**
```bash
sudo journalctl -u stripe-server -f
```

**Docker:**
```bash
docker-compose logs -f
```

---

## Cost Comparison

| Platform | Free Tier | Production | Best For |
|----------|-----------|------------|----------|
| Render | Yes | $7/mo | Simplicity |
| Railway | Yes ($5 credit) | Pay as you go | Flexibility |
| Fly.io | Yes (generous) | Cheap scales | Production |
| Railway VPS | $5/mo | $5-10/mo | Full control |

---

## Troubleshooting

**Webhook "No signature" error:**
- Verify `STRIPE_WEBHOOK_SECRET` is set correctly
- Check webhook URL matches deployment URL

**"No such price" error:**
- Price ID must match environment (test vs live)
- Create product in correct Stripe account

**CORS errors:**
- Domain must match `DOMAIN` env var exactly
- Include https:// in domain

**Email not sending:**
- Check `EMAIL_PROVIDER` is set correctly
- Verify API keys for SendGrid/SES
- Check spam folders