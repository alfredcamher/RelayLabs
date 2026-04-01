# PARTE IX: PATRONES AVANZADOS
**Arquitecturas para Agentes de Producción**

---

## 9.1 Patrón: Agent Swarms (Enjambres de Agentes)

### Concepto
Un solo agente tiene limitaciones. Un enjambre de agentes especializados, orquestados por un coordinador central, puede resolver problemas complejos mediante división y paralelización.

### Arquitectura Básica

```
┌─────────────────────────────────────┐
│      ORCHESTRATOR AGENT             │
│  (Coordinación y síntesis)           │
└──────────────┬──────────────────────┘
               │
       ┌───────┼───────┬──────────┐
       │       │       │          │
┌──────▼──┐ ┌──▼───┐ ┌─▼─────┐ ┌─▼─────┐
│Research │ │Writer│ │ Code  │ │ Review│
│  Agent  │ │ Agent│ │ Agent │ │ Agent │
└────┬────┘ └─┬────┘ └──┬────┘ └──┬────┘
     │        │         │         │
     └────────┴────┬────┴────┬────┘
                  │         │
           ┌──────▼─────────▼───────┐
           │     MERGE & SYNC       │
           │   (Result integration) │
           └────────────────────────┘
```

### Implementación Práctica

**Caso: Generar Reporte Mensual**

```python
# Ejemplo conceptual
swarm_tasks = {
    "data_collection": {
        "agent": "research_agent",
        "task": "Collect metrics from APIs",
        "output_format": "json",
        "timeout": 600
    },
    "analysis": {
        "agent": "analytics_agent",
        "task": "Analyze trends and anomalies",
        "depends_on": ["data_collection"],
        "output_format": "markdown"
    },
    "narrative": {
        "agent": "writer_agent",
        "task": "Write executive summary",
        "depends_on": ["analysis"],
        "output_format": "markdown"
    },
    "visualization": {
        "agent": "design_agent",
        "task": "Generate charts and graphs",
        "depends_on": ["data_collection"],
        "output_format": "images"
    }
}

# Orchestration
orchestrator = Swarm_Orchestrator()
result = orchestrator.execute_parallel(swarm_tasks)
```

### Casos de Uso

1. **Content Factory:** 5+ agents (research, writer, editor, SEO, formatter)
2. **Code Review:** Code analyzer, security scanner, performance profiler, style checker
3. **Customer Success:** Ticket classifier, response drafter, escalation detector, satisfaction tracker

### Consideraciones

- **Overhead:** Coordination adds 10-20% overhead
- **Cuándo usar:** Tareas >2h, múltiples sub-problemas
- **Cuándo NO usar:** Tareas simples que un solo agente maneje en <30 min

---

## 9.2 Patrón: Multi-Modal Chain

### Concepto
Pipeline donde la salida de un agente es entrada del siguiente, con transformación de formato (texto → código → visualización → publicación).

### Ejemplo: Text to Deployed Feature

```
USER REQUEST
     │
     ▼
┌─────────────┐
│  REQUIREMENT │ Text → Structured JSON
│   ANALYZER   │
└──────┬──────┘
       │ JSON
       ▼
┌─────────────┐
│   ARCHITECT  │ JSON → Architecture spec
│   DESIGNER   │
└──────┬──────┘
       │ Architecture
       ▼
┌─────────────┐
│    CODER     │ Spec → Code
└──────┬──────┘
       │ Code
       ▼
┌─────────────┐
│    TESTER    │ Code → Test results
└──────┬──────┘
       │ Pass/Fail
       ▼
┌─────────────┐
│   DEPLOYER   │ → Staging/Production
└─────────────┘
```

### Gate de Calidad Cada Etapa

```python
quality_gates = {
    "requirement_analyzer": {
        "check": "ambiguity_score < 0.3",
        "action_on_fail": "request_clarification"
    },
    "architect": {
        "check": "security_review_passed",
        "action_on_fail": "escalate_to_human"
    },
    "coder": {
        "check": "linting_passes AND tests_pass",
        "action_on_fail": "auto_fix OR human_review"
    },
    "tester": {
        "check": "coverage > 80%",
        "action_on_fail": "request_more_tests"
    }
}
```

---

## 9.3 Patrón: Recursive Self-Improvement

### Concepto
El agente mide su propio desempeño y sugiere mejoras al sistema.

### Feedback Loop

```
        ┌────────────────┐
        │   EXECUTE      │
        │    TASK        │
        └───────┬────────┘
                │
                ▼
        ┌──────────────┐
        │  MEASURE     │
        │ PERFORMANCE  │
        └───────┬──────┘
                │ metrics
                ▼
        ┌──────────────┐
        │   ANALYZE    │
        │   vs BASE    │
        └───────┬──────┘
                │
           > threshold?
                │
        ┌───────┴──────┐
        │              │
        ▼              ▼
   ┌────────┐    ┌──────────┐
   │CONTINUE│    │ IDENTIFY │
   │NORMAL  │    │ BOTTLENECK│
   └────────┘    └────┬─────┘
                       │
                       ▼
              ┌──────────────┐
              │ PROPOSE      │
              │ IMPROVEMENT  │
              │  (to LESSONS)│
              └──────────────┘
```

### Implementación

```markdown
## Post-Task Analysis Template

**Task ID:** [ID]
**Completed:** [Timestamp]
**Agent:** [Name]

### Performance Metrics
- Time allocated: ___ min
- Time taken: ___ min
- Variance: ___%
- Quality score: ___/10
- Success: [Yes/No]

### Analysis
**What went well:**
- 

**What went wrong:**
- 

**Root cause:**
- 

### Improvement Proposal
**Category:** [Prompt/Tool/Process/Architecture]

**Current:**
- 

**Proposed:**
- 

**Expected impact:**
- Time: ___%
- Quality: ___%
- Cost: ___%

**applied_in:** [Future tasks this applies to]
```

---

## 9.4 Patrón: Context Window Management

### El Problema

Modelos LLM tienen límites de contexto (Kimi: 256K tokens). Documentos largos, historiales extensos, o múltiples fuentes pueden exceder esto.

### Solución: Chunking Inteligente

```
┌────────────────────────────────────┐
│      DOCUMENTO ORIGINAL             │
│  (100K palabras = 150K tokens)     │
└────────────┬───────────────────────┘
             │
    ┌────────┴────────┐
    │  CLASSIFIER     │ ¿Qué secciones necesito?
    │                 │ Marcar relevantes
    └────────┬────────┘
             │
    ┌────────┴────────┐
    │  SUMMARIZER   │ Para secciones no-críticas
    │               │ Crear summaries
    └────────┬────────┘
             │
    ┌────────┴────────┐
    │   COMPILER    │ Reconstruir contexto
    │               │ <256K tokens
    └────────┬────────┘
             │
             ▼
┌──────────────────────────────────┐
│  CONTEXT OPTIMIZED FOR QUERY    │
└──────────────────────────────────┘
```

### Estrategias de Reducción

1. **Hierarchical Summarization:**
   - Nivel 1: Summary de párrafo
   - Nivel 2: Summary de sección
   - Nivel 3: Summary de documento

2. **Relevance Filtering:**
   ```python
   scores = [
       (chunk, relevance_score(chunk, query))
       for chunk in document
   ]
   top_chunks = sorted(scores, key=lambda x: x[1], reverse=True)[:N]
   ```

3. **Progressive Disclosure:**
   - Iteración 1: Solo summaries
   - Completar → Done
   - Ambiguo → Expandir chunks específicos

---

## 9.5 Patrón: Circuit Breaker

### Problema

Agente entra en loop infinito o produce output degradado.

### Implementación

```python
class CircuitBreaker:
    def __init__(self, threshold=3, timeout=300):
        self.failure_count = 0
        self.threshold = threshold
        self.timeout = timeout
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def call(self, function, *args):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.timeout:
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit OPEN - Service unavailable")
        
        try:
