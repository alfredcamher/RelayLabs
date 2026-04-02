# CEO Autónomo Guide - Products Directory

This directory contains the product content and generated PDF.

## Files

| File | Type | Description |
|------|------|-------------|
| `CEO-Autonomo-Guia-COMPLETO-v2.1.md` | Source | Master markdown (78KB) |
| `CEO-Autonomo-Guia-v2.1.pdf` | Output | Generated PDF (~200 pages) |

## Source File Structure

The markdown file contains:

1. **Introduction** - Value proposition
2. ** foundations** - Framework overview
3. **Sistemas > Esfuerzo** - System building
4. **Métricas** - KPIs and dashboards
5. **Loops** - Growth cycles
6. **Delegación** - Strategic delegation
7. **Staging** - Growth phases
8. **Templates** - Practical tools
9. **Case Studies** - Real examples
10. **FAQ** - Common questions

## Generation Process

```
Markdown → PDF Generator → Final Product
   ↓              ↓               ↓
 Source    (Python/Pandoc)   Delivery CDN
```

## Delivery

The PDF should be hosted on a CDN:
- S3 + CloudFront
- Cloudflare R2
- Dropbox direct link
- Google Drive direct link

Update `PRODUCT_URL` environment variable with the CDN URL.

## Metadata

- **Version:** 2.1
- **Pages:** ~41
- **Size:** ~10MB (optimized)
- **Format:** PDF/A for archival quality
- **License:** Proprietary (not open source)