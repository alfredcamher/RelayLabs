# Domain Setup Guide

## Step 1: Choose a Domain

### Domain Options

| Provider | Price | Best For |
|----------|-------|----------|
| Namecheap | ~\$12/year | Privacy included |
| Cloudflare | Wholesale | DNS + CDN included |
| Porkbun | ~\$12/year | Low renewals |
| GoDaddy | ~\$18/year | Support |

### Recommended Domain Patterns
- `ceoguide.com` (premium, expensive)
- `ceoautonomo.com`
- `yourname.guide`
- `buildasaceo.com`
- `operateasaceo.com`

## Step 2: DNS Configuration

### For Fly.io
```dns
Type    Name                Value
A       @                   66.241.124.248
AAAA    @                   2a09:8280:1:3565:5afe:46d4:55fc:f567
CNAME   *                   your-app.fly.dev.
```

### For Render
```dns
Type    Name                Value
CNAME   @                   ceo-autonomo-payment.onrender.com
```

### For VPS (Custom Server)
```dns
Type    Name                Value
A       @                   YOUR_SERVER_IP
A       www                 YOUR_SERVER_IP
```

## Step 3: SSL Certificate (Let's Encrypt)

### Using Certbot

```bash
# Install certbot
sudo apt update
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal test
sudo certbot renew --dry-run
```

### SSL Renewal
```bash
# Add to crontab
0 3 * * * certbot renew --quiet
```

## Step 4: Webhook URL Update

After setting up domain:

1. Update `DOMAIN` env var: `https://yourdomain.com`
2. Update Stripe webhook endpoint: `https://yourdomain.com/webhook`
3. Test webhook delivery in Stripe Dashboard

## Step 5: Health Check

```bash
# Test domain
curl -I https://yourdomain.com/health

# Expected: HTTP 200 with JSON response
```

## Troubleshooting

### DNS not propagating
- Check: `dig +short yourdomain.com`
- Wait: Up to 48 hours (usually minutes)
- Clear local DNS: `sudo killall -HUP mDNSResponder`

### SSL errors
- Check certificate: `openssl s_client -connect yourdomain.com:443`
- Verify renewal: `certbot certificates`

### Webhook failures
- Verify `DOMAIN` matches exactly (with https://)
- Check webhook secret matches
- Test manually: `curl -X POST https://yourdomain.com/webhook`