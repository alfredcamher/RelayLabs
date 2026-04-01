# CONTEXT - Estado Actual del Proyecto Relay Labs

**Fecha:** 2026-03-31
**Proyecto:** CEO Autónomo / Relay Labs
**Estado:** Pre-launch, Landing page ready, Stripe pendiente
**URL:** https://alfredcamher.github.io/RelayLabs/

---

## Proyecto Overview

### Nombre Empresa
**Relay Labs** - Una iniciativa que enseña a construir negocios con agentes IA

### Producto Principal
**CEO Autónomo** - Guía PDF + Templates + Stack HKUDS
- Precio: $39 USD (launch), precio original $250
- Contenido: 120 páginas, templates Notion, 50+ prompts, cheat sheets

### Stack Tecnológico
| Herramienta | Propósito | Estado |
|-------------|-----------|--------|
| OpenClaw | Orchestration | ✅ Activo |
| Kimi K2.5 | Modelo principal | ✅ 100% uso |
| GitHub Pages | Hosting landing | ✅ Deployed |
| GitHub | Repo + CI/CD | ✅ RelayLabs repo |
| Stripe | Pagos | ⏳ Pendiente checkout link |
| Cloudflare Pages | Opcional migración | ⏳ Futuro |

### Estructura Repositorio
```
RelayLabs/
├── index.html (landing page)
├── assets/
│   └── alfred-avatar-primary.png (White Walker pixel art)
└── .git/
```

---

## Estado Componentes

### Landing Page ✅✅ LIVE
**URL:** https://alfredcamher.github.io/RelayLabs/

**Features implementadas:**
- ✅ HTML/CSS vanilla, responsive
- ✅ Secciones: Hero, Features, Stack, Includes, CTA, Creator, Footer
- ✅ Badge "Ahorro 87% en costos de API"
- ✅ Precio tachado $250 → $39 USD
- ✅ Botón checkout ✅✅ **STRIPE CONECTADO** - https://buy.stripe.com/aFabJ28NrfiHdFl3jfcMM00
- ✅ Avatar Alfred (White Walker pixel art, redondeado)
- ✅ Sección "Conoce a Alfred" - OpenClaw IA config
- ✅ Relay Labs branding

**ESTADO:** LIVE - Listo para recibir pagos

**Paleta actual:**
- `--bg-dark: #0a0c0e` (casi negro)
- `--bg-card: #16191c` (gris oscuro)
- `--lime-cream: #dcf763` (acento verde lima)
- `--grey-olive: #848c8e` (texto mutado)
- `--iron-grey: #435058` (bordes)
- `--gradient-purple: #6a5acd` (púrpura gradiente)

**Tipografías:**
- Body: Space Grotesk
- Técnico/Mono: IBM Plex Mono

**Pendiente:**
- ⏳ Checkout link de Stripe
- ⏳ Formato conversión optimizado
- ⏳ Analytics (?)

---

### Stripe Integration ✅✅ LIVE
**Estado:** PRODUCTO CREADO Y LINK ACTIVO

**Checkout Link:** `https://buy.stripe.com/aFabJ28NrfiHdFl3jfcMM00`

**Configuración:**
- Producto: "CEO Autónomo. Sistema de Agentes de IA."
- Precio: $39 USD one-time
- Product ID: `prod_UFoP8JQIWob942`
- Price ID: `price_1THImVJP2vdPzDc4ZE98yzyh`

**ESTADO:** ✅✅ LIVE - Pagos activos

---

## Estado Actual Post-Restart

**Sistema operativo:** 100%
- ✅ Landing page live con checkout
- ✅ Stripe connected y funcionando
- ⏳ Esperando primera venta
- ⏳ Delivery manual activado (revisaría email Stripe 2-3x/día)
- ⏳ GTM strategy lista para ejecutar tras primera venta
- ⏳ PDF guía pendiente de crear

---

### Avatar ✅
**Estado:** Aprobado

**Descripción:** White Walker pixel art
- Ojos cyan brillantes
- Bigote
- Vestimenta ejecutiva oscura
- Fondo espacial con partículas
- Estilo pixel art 8/16-bit

**Variantes:**
- ✅ Primary: Guardado en `assets/alfred-avatar-primary.png`
- ⏳ Working: Pendiente
- ⏳ Success: Pendiente
- ⏳ X/Twitter: Pendiente
- ⏳ Favicon: Pendiente

---

### GitHub Setup ✅
**Repositorio:** https://github.com/alfredcamher/RelayLabs

**Config:**
- SSH access configurado
- Pages: branch main, source root
- URL: https://alfredcamher.github.io/RelayLabs/
- Repo público (requerido para Pages free)

**SSH Key:**
```
~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP2pXXAxU1GpVdMf5Dvm3bqtdxccvv/P4CQs4Nt1VnNl alfredcamher@gmail.com
```

---

## Aprendizajes Clave (Contexto Operacional)

### GitHub Pages
- **Repo público obligatorio** para free tier
- **CORS issues** con raw.githubusercontent.com - usar ruta relativa
- **Deploy delay** ~1-2 minutos después de push
- **Files sensibles:** NUNCA pushear tokens, .env, archivos internos

### HTML/CSS Simple
- **Vanilla > Framework** para landing estática - más rápido deploy
- **CSS variables** para fácil rebranding
- **Responsive:** Mobile-first con `@media (max-width: 768px)`
- **Grid + Flexbox:** Mejor que Bootstrap para control total

### Stripe Integration
- **Website requerido** para crear cuenta
- **Checkout hosted** es más fácil que embedded (menos código)
- **Webhook opcional** para entrega automática

### Proceso Colaborativo (Bernardo + Alfred)
- **Bernardo:** Facilitador, decisiones estratégicas, token humano
- **Alfred:** Ejecutor técnico, daily ops, agent management
- **Comunicación:** Async, Telegram
- **Urgencia:** Tag "URGENT" en mensaje

---

## Métricas objetivo

| Métrica | Target | Actual |
|---------|--------|--------|
| MRR | $1M | $0 |
| Precio | $39 | ✅ Configurado |
| Landing | Deployed | ✅ GitHub Pages |
| Ventas | 10-50/mes | 0 |
| CAC | <$50 | N/A |
| Autonomy ratio | 80%+ | Estableciendo |

---

## Blockers Actuales

1. **Stripe checkout link** - Esperando usuario
2. **Testing completo** - Sin checkout link, no se puede probar flujo
3. **Analytics** - No configurado

---

## Decisiones Recientes

| Fecha | Decisión | Razón |
|-------|----------|-------|
| 2026-03-31 | Nombre "Relay Labs" vs CEO Autónomo | Más escalable, marca empresa |
| 2026-03-31 | Paleta grey-olive/lime-cream | Más oscuro, profesional |
| 2026-03-31 | Avatar White Walker | Aprobado por Bernardo |
| 2026-03-31 | $39 precio launch | $250 original más creíble que $538 |
| 2026-03-31 | GitHub Pages vs Cloudflare | Gratuito, rápido, conocido |

---

## Contactos

- **Alfred:** alfredcamher@gmail.com
- ** marca:** 🎯 (bullseye)
- **Tone:** Ship or shut up. Time is non-renewable.

---

*Actualizar después de cada milestone*
