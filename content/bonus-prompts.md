# Bonus Prompts - 10 Extra Prompts CEO Autónomo
**Extra jugoso: Prompts de alta conversión**

---

## Prompt B1: Autonomous Task Detection

**Use case:** Detectar si una tarea puede ser automatizada

```
Eres un analizador de task automation. Tu trabajo:

1. ANALIZA esta tarea: [INSERT TASK]

2. EVALÚA en 5 dimensiones:
   - Repetitividad (1-5): ¿Se repite >3x/semana?
   - Complejidad (1-5): ¿Requiere juicio humano complejo?
   - Reversibilidad (1-5): ¿Se puede deshacer fácilmente?
   - Tiempo manual promedio: ___ minutos
   - Costo del error: Bajo/Medio/Alto/Irreversible

3. VEREDICTO:
   [ ] AUTOMATIZABLE AHORA (score 25-30)
   [ ] AUTOMATIZABLE CON HUMAN-IN-THE-LOOP (score 15-24)
   [ ] HUMAN-ONLY (score <15)

4. SI es automatizable, propón:
   - Herramienta/método óptimo
   - Prompt template para el agente
   - Checkpoints humanos necesarios

FORMATO: Tabla + decisión clara + ejemplos
```

---

## Prompt B2: Crisis Communication Protocol

**Use case:** Responder a quejas/escalaciones

```
SITUACIÓN EXTREMA: [baja calificación/refund request/complaint]

1. ANÁLISIS RÁPIDO (<5 min):
   - ¿Se puede solucionar con refund?
   - ¿Es un edge case válido?
   - ¿Hay screenshots/logs?

2. TONE SELECTION:
   [ ] Servicial (minor complaint)
   [ ] Empático (frustrated customer)
   [ ] Firm-friendly (unreasonable demands)
   [ ] Escalar humano (legal/threats)

3. RESPUESTA ESTRUCTURADA:
   - Empathy acknowledgment
   - Solution offered
   - Compensation (si aplica)
   - Next steps (monitoring)
   - Human escalation (si necesario)

4. TEXTO FINAL: [Respuesta lista para enviar]

5. ESCALAR A HUMANO SI:
   - Legal threats
   - Requests >$100
   - Complex edge case
   - Negative sentiment crossing threshold
```

---

## Prompt B3: Content Gap Analysis

**Use case:** Identificar qué contenido falta en tu estrategia

```
Industria: [tu industria]
Competidores: 5 handles X
Tu ICP: [descripción]

1. SCRAPE competidores (último mes):
   - Tópicos más mencionados
   - Formatos con mejor engagement
   - Sentimiento de comentarios
   - Gaps en cobertura

2. ANALYSIS:
   - Keyword overlap
   - Unique positioning opportunities
   - Formatos no usados por nadie
   - Contenido bajo pero valor alto

3. CONTENT CALENDAR (30 días):
| Día | Formato | Tópico | Hook | CTA |
|-----|---------|--------|------|-----|
| L1 | Thread | X | Y | landing |
| M1 | Tweet | A | B | newsletter |

4. PRIORIDAD: High/Med/Low con justificación
```

---

## Prompt B4: Pricing Psychology Optimizer

**Use case:** Encontrar tu precio óptimo

```
Producto: [descripción]
ICP: [persona]
Valor percibido: [outcomes]

1. ANCHOR OPTIONS:
   - Precio aspiracional: $_____
   - Precio actual/expected: $_____
   - Precio anchoring bundle: $_____

2. PSYCHOLOGY TESTS:
   a) Ending in 7: $47 vs $49 vs $50
   b) Bundle friction: Enseñar savings vs hidden savings
   c) Decoy effect: Añadir tier ultra-premium
   d) Annual discount: 20% vs "2 months free"

3. RECOMMENDED PRICE:
   - Main offering: $_____
   - Justification: [emotional + logical]
   - Launch discount: $_____ (40-60% off)

4. COPY PARA CHECKOUT:
   - Strikethrough original
   - "Los early believers..."
   - Scarcity: "Solo 50 spots a este precio"
   - Guarantee: "30 días garantía"
```

---

## Prompt B5: Daily Standup Report

**Use case:** Generar reporte diario automático

```
Generar DAILY STANDUP para [FECHA]:

1. COMPLETED YESTERDAY:
   [Del BACKLOG ayer: what got done]
   - Commit ID: ___
   - Output file: ___

2. IN PROGRESS TODAY:
   [Lo que está en trabajo ahora]
   - Blockers: ___
   - ETA: ___
   - Resources needed: ___

3. BLOCKERS:
   - Need human approval: ___
   - External dependency: ___
   - Technical issue: ___

4. METRICS:
   - Tasks completed: ___
   - Commits: ___
   - Files modified: ___
   - Lines changed: ___

5. INSIGHTS:
   - Efficiency: up/down stable
   - Quality: good/warning
   - Next sprint priority: ___

FORMATO: Markdown tabla + bullet points. Listo para human review.
```

---

## Prompt B6: Cold Outreach Generator

**Use case:** Generar outbound messages a influencers/targets

```
TARGET: [handle/profile link]
ICP: [type]
Product: [CEO Autónomo]
Goal: [familiarity/mention/partnership]

1. RESEARCH TARGET (<2 min):
   - Recent content themes
   - Engagement patterns
   - Pain points mentioned
   - Communication style

2. MESSAGE OPTIONS:

   a) WARM (mutual connection):
   "[Connection] me habló de tu trabajo en [topic]. Como también estoy en [space], quisiera..."

   b) VALUE-FIRST (no connection):
   "Vi tu thread sobre [topic]. Estoy trabajando en [project] y creé [resource] que te podría interesar..."

   c) COMPLIMENT-SPECIFIC:
   "Tu approach a [specific thing] es único. ¿Te open a una convo sobre [mutual interest]?"

3. SELECTED MESSAGE:
   [Full text ready to send]

4. FOLLOW-UP SEQUENCE (si no responde):
   - Día 3: Gentle reminder
   - Día 7: Value-add
   - Día 14: Final check

5. ESCALATE: Wait for human before sending DM
```

---

## Prompt B7: Landing Page Heatmap Review

**Use case:** Simular análisis de página

```
SITE: [URL]
Tool: Mock eye-tracking / Hotjar-style analysis

1. VISUAL HIERARCHY:
   - What catches eye first? [chronological order]
   - What do they miss completely?
   - Where does attention drop?

2. FRICTION POINTS:
   - Confusing sections
   - Unclear CTAs
   - Missing trust signals
   - Information overload

3. CONVERSION ANALYSIS:
   - CTA prominence: visible/subtle/hidden
   - Value prop clarity: clear/muddy/absent
   - Trust indicators: sufficient/missing
   - Pricing transparency: good/opaque

4. RECOMMENDATIONS:
   - Quick wins (implement today)
   - A/B tests to run
   - Copy changes suggested
   - Visual improvements

5. PRIORITIZED ACTION:
   - Priority 1: ___
   - Priority 2: ___
   - Priority 3: ___
```

---

## Prompt B8: Decision Fatigue Reducer

**Use case:** Cuando hay muchas tareas y no sabes por dónde empezar

```
BACKLOG ACTUAL:
[List all pending tasks]

1. MATRIX EISENHOWER:
| Urgent/Important | Not Urgent/Important |
| Urgent/Not Imp   | Not Urgent/Not Imp   |
[Classificar cada task]

2. ENERGY ASSESSMENT:
   - Mi energía: High/Med/Low
   - Tiempo disponible: ___ minutos
   - Modalidad: Focused/Distracted/On-the-go

3. NEXT ACTION SELECTION:
   CRITERIOS (in order):
   ✓ Quick win possible? (<30 min)
   ✓ Unblocks others? (dependency)
   ✓ Strategic value? (ROI)
   ✓ My energy match? (cognitive load)

4. RECOMENDACIÓN:
   "Haz _____ AHORA porque ______"

5. IF ENERGY LOW:
   - Suggest "energy recharge" task
   - Or minimal viable version
   - Or defer with specific reason
```

---

## Prompt B9: Viral Content Reverse Engineer

**Use case:** Aprender de contenido viral en tu espacio

```
CONTENT: [link/screenshot]
Platform: [X/LinkedIn/TikTok/etc]
Engagement: [views/likes/shares]
Author: [handle]

1. ANATOMY:
   | Element | Implementation |
   | Hook | |
   | Structure | |
   | Pattern Interrupt | |
   | Story Arc | |
   | CTA | |

2. PSYCHOLOGY TRIGGERS:
   [ ] FOMO
   [ ] Curiosity Gap
   [ ] Social Proof
   [ ] Status Signaling
   [ ] Pattern Recognition
   [ ] Contrarian

3. REMIXES:
   Básico: [Aplicar a tu contexto]
   Intermedio: [Añadir tu twist]
   Avanzado: [Subvert expectation]

4. IMPLEMENTATION:
   Draft: [Tu versión]
   Predicted engagement: [+/-]
   Best platform: ___
   Best time: ___
```

---

## Prompt B10: Agent Self-Improvement Loop

**Use case:** El agente evalúa su propio rendimiento

```
SESION ANTERIOR: [ID/commit/summary]

1. COMPLETADO:
   - Tasks finished: ___/___
   - Quality: 1-10
   - Human interventions needed: ___
   - Time spent: ___

2. METRICS:
   - Success rate: ___%
   - Error rate: