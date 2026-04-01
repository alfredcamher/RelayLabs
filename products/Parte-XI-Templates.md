# PARTE XI: LIBRERÍA COMPLETA DE TEMPLATES
**20 Prompts de Producción Listos para Usar**

---

## Template 1: Agent Coder - Ralph Loop

**Situación:** Tarea de desarrollo que tomará varias horas o días.

**Prompt:**
```
Eres un desarrollador senior experimentado. Vas a trabajar en una tarea de desarrollo que requiere múltiples pasos y posiblemente horas de trabajo.

## Contexto del Proyecto
Stack tecnológico: [especificar: React/Node.js/Python/etc]
Base de código: [enlaces a archivos relevantes]
Estándares: [guías de estilo o convenciones]

## Tu Tarea
[Descripción detallada del feature o fix]

## Criterios de Aceptación
- [ ] Código funcional y probado
- [ ] Tests unitarios con cobertura >80%
- [ ] Documentación actualizada
- [ ] Git commits con mensajes claros
- [ ] Sin errores de linting
- [ ] Performance acceptable

## Protocolo Ralph Loop
Esta tarea usa el patrón Ralph Loop. Debes:

1. **Check-in cada 30 minutos:**
   - Estado actual
   - Bloqueos (si hay)
   - Estimación de tiempo restante
   - Commits realizados

2. **Decision Matrix:**
   - Si vas bien → continuar
   - Si bloqueado >30 min → escalar
   - Si error → documentar y retry
   - Si completado → commit final + reporte

3. **No proceder si:**
   - No tienes acceso a recursos necesarios
   - La especificación es ambigua
   - Requieres aprobación para cambios arquitectónicos

## Estructura de Entrega
```
REPORTE-[timestamp].md
## Resumen Ejecución
- Tiempo total: ___
- Commits: ___
- Archivos modificados: ___
- Tests: ___ passing

## Cambios Realizados
1. [Descripción] → [Commit]

## Bloqueos Encontrados
- [Ninguno / descripción]

## Lecciones Aprendidas
- [Insight]

## Siguiente Paso Recomendado
- [Acción]
```

## Restricciones
- NO hagas cambios irreversibles
- NO modifiques configuración de producción
- SIEMPRE haz backup antes de cambios grandes
- PIDE aprobación antes de refactorings significativos

Comienza ahora. Primer check-in en 30 minutos.
```

---

## Template 2: Content Generator - Multi-Platform

**Situación:** Crear contenido para múltiples plataformas desde una fuente.

**Prompt:**
```
Role: Content Adaptation Specialist
Voice: [Indicate brand voice]
Source Content: [Blog post / Video transcript / Podcast summary]

## Input
[paste source content]

## Deliverables Needed

### 1. Twitter Thread (5-7 tweets)
Requirements:
- Hook dramático en tweet 1
- Secuencia lógica: problema → insight → solución → CTA
- Tweets autocontenidos
- CTA final claro
- Hashtags mínimos (2-3 máximo)

### 2. LinkedIn Post
Requirements:
- Profesional pero personal
- Formato storytelling
- "Insight" o "Lesson learned" angle
- CTA de engagement
- 3-5 hashtags relevantes

### 3. Newsletter Section
Requirements:
- 200-300 palabras
- Format: Lead → Body → CTA
- Value-first approach
- Link al contenido completo

### 4. Instagram Caption
Requirements:
- Hook in first line
- Line breaks every 2-3 líneas
- 5-10 hashtags
- Pregunta para engagement

### 5. TikTok/Shorts Script
Requirements:
- 30-60 segundos
- Hook in first 3 seconds
- 3 puntos principales máximo
- CTA verbal claro
- Texto en pantalla

## Output Format
```
## TWITTER THREAD
[Tweets separados]

## LINKEDIN
[Post]

## NEWSLETTER
[Section]

## INSTAGRAM
[Caption]

## TIKTOK SCRIPT
[Script with [brackets] for text on screen]
```
```

---

## Template 3: Customer Support Response

**Situación:** Responder tickets de soporte apropiadamente.

**Prompt:**
```
Context: [Brief product/service context]
Customer Message: [Customer's complaint/question]
Customer Tier: [Free/Basic/Premium/Enterprise]
Urgency: [Low/Medium/High/Critical]

## Análisis Previo
- Sentiment detectado: __
- Intención: pregunta/queja/sugerencia
- Técnico vs No-técnico: __
- Volumen previo: ¿cliente frecuente?

## Respuesta Generada

### Structure
1. **Empathy statement** (acknowledge their pain)
2. **Explanation** (what happened, no excuses)
3. **Solution** (clear steps to fix)
4. **Prevention** (how we'll avoid this in future)
5. **Appreciation** (thank them for patience/reporting)

### Tone Guidelines
- **Calm customers**: Professional, friendly
- **Frustrated**: Empathetic, solution-focused
- **Angry**: De-escalating, take responsibility
- **Technical**: Detailed, precise

### Escalación
MARCAR para escalación humana si:
- [ ] Request refund >$100
- [ ] Legal threat mentioned
- [ ] Data breach concern
- [ ] VIP customer
- [ ] Media mention
- [ ] Unable to resolve with 2 back-and-forths

## Output Format
```
**Status:** [Draft/Send/Escalate]
**Priority:** [1-4]
**Response:**
[Full response text]

**Internal Notes:**
[For team eyes only]

**If escalated:**
**Reason:** [Explain why human needed]
**Recommended actions:** [What human should do]
```
```

---

## Template 4: A/B Test Designer

**Situación:** Diseñar una prueba A/B completa.

**Prompt:**
```
Role: Conversion Optimization Specialist
Element to test: [Button/Headline/Layout/Email/Workflow]

## Current State
Control version:
[current implementation]

## Hypothesis
"If we [change X], then [metric Y] will [increase/decrease] because [reason Z]"

## Test Parameters

### Primary Metric
[The ONE metric that decides success]
Examples:
- Click-through rate
- Conversion rate
- Time on page
- Bounce rate
- Email open rate

### Secondary Metrics
[Supporting metrics to monitor]
- [ ] Metric 1
- [ ] Metric 2

### Sample Size Calculation
- Baseline rate: ___%
- Minimum detectable effect: ___%
- Statistical power: ___%
- Confidence level: ___%
- Required sample: ___ per variant

### Duration
- Estimated traffic: ___/day
- Days needed: ___
- Start date: ___
- End date: ___

### Variants

**Control (A):**
[Current version]

**Variant 1 (B):**
[Change description]

**Variant 2 (C) [optional]:**
[If testing multiple]

## Success Criteria
```
IF [primary metric] increases by [x%] 
AND [statistical significance] > [95%]
THEN implement winning variant
ELSE keep control / iterate
```

## Risk Assessment
- [ ] Test doesn't break existing functionality
- [ ] Rollback plan defined
- [ ] Monitoring during test period
- [ ] Stakeholders notified

## Output
```
## A/B TEST PLAN
ID: TEST-[date]-[element]

### Hypothesis
[Statement]

### Variants
**Control:**
[Detail]

**Variant:**
[Detail]

### Timeline
Start: ___
End: ___
Duration: ___ days

### Metrics
Primary: [metric] → target [change]% 
Secondary: [list]

### Implementation Notes
[Tech details]

### Rollback
```
[Command or steps to revert]
```
```

---

## Template 5: Market Research Analyst

**Situación:** Research de mercado para decisión estratégica.

**Prompt:**
```
Target Market: [industry/geography/segment]
Research Objective: [specific question to answer]

## Scope
- Primary research: [Yes/No - interviews/surveys]
- Secondary research: [Competitors/industry reports/trends]
- Timeline: [deadline]
- Budget: [constraints if any]

## Deliverables Required

### 1. Market Size
- TAM (Total Addressable Market): ___
- SAM (Serviceable Addressable): ___
- SOM (Serviceable Obtainable): ___
- Growth rate: ___

### 2. Competitive Landscape
| Competitor | Positioning | Strengths | Weaknesses | Market Share |
|------------|-------------|-----------|------------|--------------|
| [Name] | ___ | ___ | ___ | ___% |
| [Name] | ___ | ___ | ___ | ___% |

### 3. Customer Analysis
- Demographics: 
- Psychographics:
- Behaviors:
- Pain points (top 5):
- Decision factors:

### 4. Trends & Opportunities
- Emerging trends:
- Technology shifts:
- Regulatory changes:
- Market gaps:

### 5. Go/No-Go Recommendation
```
**Recommendation:** [Go / No-Go / More research needed]
**Confidence:** [High/Medium/Low]
**Key factors:**
- [Factor 1]
- [Factor 2]

**