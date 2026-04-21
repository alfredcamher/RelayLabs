# Relay Labs - GitHub Deploy Configuration
**Date:** 2026-04-20 21:24 CDT
**Status:** DEPLOYED ✅

## Company Identity
- **Name:** Relay Labs (not alfredcamher.github.io)
- **Product:** CEO Autónomo - Sistema de Agentes IA
- **Price:** $47 USD
- **Stripe Link:** https://buy.stripe.com/aFabJ28NrfiHdFl3jfcMM00

## GitHub Configuration
- **Repo:** github.com/alfredcamher/RelayLabs
- **SSH Auth:** ✅ Configured (id_ed25519_github)
- **Remote:** git@github.com:alfredcamher/RelayLabs.git
- **Branch:** master
- **Landing Page:** /index.html (deployed 2026-04-20)

## Deploy Commands
```bash
cd /home/alfredcamher/.openclaw/workspace
git remote set-url origin git@github.com:alfredcamher/RelayLabs.git
git add index.html
git commit -m "deploy: update landing"
git push origin master
```

## GitHub Pages Status
- URL: https://alfredcamher.github.io/RelayLabs/
- Custom domain: Pending (purchase after first revenue)

## Critical Reminder
**The company is Relay Labs, NOT alfredcamher.github.io.**
Use RelayLabs repo for all deployments.
