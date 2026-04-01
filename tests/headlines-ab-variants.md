# A/B Headlines - Landing Page Variants

**Fecha:** 2026-04-01
**Estado:** ✅ COMPLETED
**Propósito:** 5 variantes de headline para split testing

---

## Current Headline (Control)

> **"Construye un Negocio Autónomo con Agentes IA"**

**Analysis:**
- ✅ Claro y directo
- ⚠️ Genérico (puede ser de cualquier curso)
- ⚠️ Sin diferenciación clara
- ⚠️ Sin urgency ni social proof

---

## Variant A: Urgency/Scarcity

> **"Tu CEO Que Nunca Duerme: Construye un Negocio Que Operó 24/7"**

**Psychological triggers:**
- "CEO" = authority/professionalism
- "Nunca duerme" = pain point solution
- "24/7" = continuous value

**Testing:** Mejor para urgency funnel, launch campaigns

---

## Variant B: Social Proof/Results

> **"El Framework Usado para Pasar de $0 a $1M MRR con Agentes IA"**

**Psychological triggers:**
- "Framework" = proven system, not theory
- "$0 a $1M" = aspirational results
- "$1M MRR" = specific, measurable

**Testing:** Mejor para credibility, warm traffic

---

## Variant C: Problem/Pain-Relief

> **"De Founder Agotado a Operator Estratégico: Sistema de Agentes IA"**

**Psychological triggers:**
- "Founder agotado" = immediate identification
- "Operator estratégico" = aspirational identity
- Contraste antes/después clear

**Testing:** Mejor para problem-aware audiences

---

## Variant D: Contrarian/Pattern Interrupt

> **"Ship or Shut Up. Construye con Agentes Que Decisionan Por Ti."**

**Psychological triggers:**
- "Ship or shut up" = brand voice, polarizing
- "Decisionan por ti" = autonomous, scary/exciting
- Challenge bravado

**Testing:** Mejor para brand-aligned audience, indie hackers

---

## Variant E: Benefit-Forward/Hook

> **"Escalar sin Contratar: Tu Equipo de IA Que Trabaja Mientras Duermes"**

**Psychological triggers:**
- "Escalar sin contratar" = unique mechanism
- "Equipo de IA" = product category
- "Mientras duermes" = dream outcome

**Testing:** Mejor for cold traffic, top of funnel

---

## Testing Framework

### Method A: Sequential Testing
```
Week 1: Variant A | Measure CTR
Week 2: Variant B | Measure CTR
Week 3: Variant C | Measure CTR
Winner: Highest CTR
```

### Method B: Google Optimize
```
50% traffic → Control
50% traffic → Variant (rotate weekly)
Track: CTR, Time on page, Conversion rate
```

### Method C: X Bio Testing
```
Rotate headline en bio cada 3 días
Track: Link clicks, followers, engagement
Winner: Clicks + engagement combination
```

---

## Implementation

### Local Testing
1. Copy variant HTML
2. Replace in `index.html`
3. Test locally
4. Push → GitHub Pages
5. Monitor 3-7 días

### UTM Tracking
```
https://alfredcamher.github.io/RelayLabs/?utm_campaign=landing-ab-test&utm_content=variant-a
```

---

## Predicted Winner Analysis

**Most likely:** Variant C (Problem/Pain-Relief)
- Indirect addressing of burnout
- Clear transformation promise
- Broader appeal than D

**Runner-up:** Variant B (Social Proof)
- Credibility driver
- Results-focused

**Wild card:** Variant D (Contrarian)
- Highest engagement polarization
- Might alienate but hook the right ones

---

## Next Variants to Test (Future)

### Price Anchoring:
> "$39 por un CEO Que Nunca Duerme (Valor Real: $538)"

### Skeptic:
> "Sigue Creyendo Que Necesitas Empleados para Escalar"

### Curiosity Gap:
> "El Último Framework de Productividad Que Necesitarás"

---

## Results Tracking Sheet

| Variant | Visitors | Clicks CTA | Conv Rate | Time on Page | Winner |
|---------|----------|------------|-----------|--------------|--------|
| Control | ___ | ___ | ___% | ___s | baseline |
| A | ___ | ___ | ___% | ___s | ___ |
| B | ___ | ___ | ___% | ___s | ___ |
| C | ___ | ___ | ___% | ___s | ___ |
| D | ___ | ___ | ___% | ___s | ___ |
| E | ___ | ___ | ___% | ___s | ___ |

**Update semanalmente**

---

## Notes

- Control está funcionando → No romper
- Test uno a la vez → Statistical significance
- Min 100 visitors per variant → Para tener data
- Emotional hooks > Logical features
- "Tu" y "Tú" > "Nosotros"

---

*Wireframe for Relay Labs landing A/B testing*
