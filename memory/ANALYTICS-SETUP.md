# ANALYTICS SETUP - Tracking Guide
**Proyecto:** Relay Labs / CEO Autónomo  
**Fecha:** 2026-04-01  
**Status:** ✅ IMPLEMENTADO

---

## Resumen

Analytics simple implementado en landing page usando **Plausible** (privacy-friendly, no cookies, GDPR compliant).

---

## Configuración Actual

### Script Principal
```html
<!-- En <head> de index.html -->
<script defer data-domain="alfredcamher.github.io" src="https://plausible.io/js/script.js"></script>
```

### Event Tracking

**Checkout Clicks:**
```html
<a href="https://buy.stripe.com/..." data-analytics="checkout-click">
```

```javascript
<!-- Event tracking script -->
<script>
  document.querySelectorAll("[data-analytics=checkout-click]").forEach((element) => {
    element.addEventListener("click", () => {
      if (typeof plausible !== "undefined") plausible("Checkout Click");
    });
  });
</script>
```

---

## Métricas Track

| Métrica | Evento Plausible | Descripción |
|---------|------------------|-------------|
| Page Views | Auto | Visitas a landing |
| Checkout Clicks | "Checkout Click" | Clicks en botón compra |
| Conversion Rate | (Calcular) | Clicks / Page Views |

---

## Dashboard

**Plausible:** https://plausible.io/
- Configurar cuenta con dominio
- Agregar sitio: alfredcamher.github.io
- View stats en tiempo real

---

## Configuración Post-Setup (Manual)

1. Crear cuenta en plausible.io
2. Agregar sitio con dominio
3. Verificar script está cargando (network tab)
4. Probar evento de checkout

### Costo: $9/mes (primer 30K views/mes)
- Alternativa gratuita: Cloudflare Web Analytics (no tiene event tracking)

---

## Eventos Futuros a Agregar

Cuando tengamos más interacción:
- [ ] Scroll depth (75% page)
- [ ] Time on page > 2 min
- [ ] Outbound link clicks (docs, github)
- [ ] Email click (mailto)

---

*Implementado por Alfred - Autonomous Work Cycle*
