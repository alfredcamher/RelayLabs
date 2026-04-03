# Deploy Landing Page to Static Hosting

## Overview
Deploy `marketing/seo-landing-page.html` to a live static hosting platform.

## Options

### Option 1: Vercel (Recommended)
**Why:** Free, fast, automatic HTTPS, custom domain
**Steps:**
1. Sign up at vercel.com (GitHub login)
2. Import repository
3. Configure:
   - Framework: Other
   - Build Command: (none - static HTML)
   - Output Directory: ./marketing
4. Deploy
5. Add custom domain (optional)

### Option 2: Netlify
**Why:** Free tier generous, drag & drop
**Steps:**
1. Sign up at netlify.com
2. Drag `marketing/` folder to deploy area
3. Site live instantly
4. Add custom domain in settings

### Option 3: GitHub Pages
**Why:** Free, integrated with repo
**Steps:**
1. Go to repo Settings → Pages
2. Source: Deploy from a branch
3. Branch: main / Folder: /marketing
4. Wait 2-3 minutes
5. Site at: username.github.io/repo-name/

### Option 4: Render Static Sites
Already configured in `deploy/render.yaml`
1. Create account at render.com
2. Click "New Static Site"
3. Connect GitHub repo
4. Build settings:
   - Publish directory: ./marketing
5. Deploy

## Recommended: Vercel (Fastest)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy (from repo root)
vercel --prod

# Follow prompts, select:
# - Scope: your account
# - Project settings: confirm

# Output: https://your-project.vercel.app
```

## Custom Domain Setup

### If you bought ceoautonomo.com:
1. In Vercel dashboard: Project → Settings → Domains
2. Add: ceoautonomo.com
3. Vercel shows DNS records
4. Add to your domain registrar
5. Wait for propagation (minutes to hours)

### DNS Records Example (Cloudflare/Namecheap):
```
Type: A
Name: @
Value: 76.76.21.21 (or Vercel's IP)

Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

## Post-Deploy Checklist

- [ ] Site loads at custom URL
- [ ] All images load
- [ ] Form submission works
- [ ] Links work correctly
- [ ] Mobile responsive
- [ ] HTTPS certificate active
- [ ] Analytics tracking active
- [ ] Twitter cards valid
- [ ] Facebook debugger valid

## Email Integration

Update `payment/` server to use live domain:
```
DOMAIN=https://ceoautonomo.com
WEBHOOK_URL=https://api.ceoautonomo.com/webhook
```

## Analytics Setup

Add to deployed HTML:
```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## Cost Breakdown

| Platform | Cost | Limits |
|----------|------|--------|
| Vercel | $0 | 100GB bandwidth/mo |
| Netlify | $0 | 100GB bandwidth/mo |
| GitHub Pages | $0 | 1GB storage, 100GB traffic |
| Render | $0 | 100GB bandwidth/mo |

All sufficient for launch.

## Timeline

- Deployment: 5 minutes
- Custom domain: 15 minutes
- SSL propagation: 5-60 minutes
- Total: Under 30 minutes to live

## Success

Site URL: _________________
Status: 🟢 LIVE

---

*Deploy guide ready*
*Created: 2026-04-03 06:47 CDT*
