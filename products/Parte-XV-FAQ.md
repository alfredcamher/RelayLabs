# PARTE XV: FAQ - PREGUNTAS FRECUENTES
**Respuestas a las Dudas Más Comunes**

---

## Sección 1: Sobre el Sistema

### ¿Esto realmente funciona o es hype?

**Respuesta corta:** Funciona, pero requiere trabajo inicial.

**Realidad:**
Los agentes IA no son magia. Son herramientas poderosas que amplifican tu capacidad, pero necesitan:
- Setup inicial de 10-20 horas
- Entrenamiento durante 2-4 semanas
- Iteración constante
- Supervisión humana

**Expectativa realista:**
- Mes 1: 5-10 horas semanales ahorradas
- Mes 3: 15-25 horas semanales
- Mes 6: 40+ horas semanales (1 FTE)

**No esperes:** "Instalar y olvidar"
**Sí espera:** "Inversión que paga dividendos exponenciales"

---

### ¿Cuánto cuesta realmente?

**Costos directos mensuales:**

| Componente | Costo |
|------------|-------|
| LLM API (Kimi) | $15-50 |
| Ollama (local) | $0 |
| OpenClaw | $0 |
| GitHub Pages | $0 |
| Plausible Analytics | $0-9 |
| Stripe fees | 2.9% + $0.30/transacción |
| **Total típico** | **$15-75/mes** |

**Costo indirecto (tu tiempo):**
- Setup: 10-20h inicial
- Training: 5-10h/semana primer mes
- Optimización: 2-5h/semana meses 2-3
- Management: 2-3h/semana mes 6+

**Comparativa:**
- Contratista: $3,000-8,000/mes
- Empleado: $5,000-15,000/mes + beneficios
- Sistema de agentes: $50/mes + 5h/semana

---

### ¿Necesito saber programar?

**Nivel técnico mínimo:**
- Copiar/pegar comandos
- Editar archivos de texto
- Usar terminal básica
- Entender conceptos de folders

**Si sabes programar:**
- Setup: Más rápido
- Debugging: Más fácil
- Customization: Ilimitada

**Si no sabes programar:**
- Setup: ~20h vs ~10h
- Puedes usar no-code tools
- Comunidad ayuda
- 90% funciona sin código

**Veredicto:** No es requisito, pero ayuda.

---

### ¿Es seguro poner mi negocio en manos de IA?

**Seguridad por diseño:**

1. **Human-in-the-loop:** Decisiones críticas requieren aprobación
2. **Reversible:** La mayoría de cambios se pueden deshacer
3. **Rollback:** Git permite volver atrás siempre
4. **Monitoreo:** Alertas por comportamiento anómalo

**Lo que EL AGENTE NO hace solo:**
- Cambios irreversibles
- Gastos >$100
- Decisiones legales
- Comunicaciones sensibles

**Tu control:** 100% en puntos críticos

---

## Sección 2: Sobre el Setup

### ¿Cuánto tiempo lleva tener el sistema operativo?

**Timeline realista:**

**Semana 1:** Fundamentos
- Infraestructura: 8-12h
- Primer heart: 2-4h
- Total: 10-16h

**Semana 2:** Primeras automatizaciones
- Primer agente: 4-8h
- Ajustes: 4-6h
- Total: 8-14h

**Semana 3-4:** Refinamiento
- Expansion: 5-10h/semana
- Optimización: continua

**Total mes 1:** 40-60h
**ROI:** Ahorro de 20h+/mes desde mes 2

---

### ¿Puedo usar otro modelo que no sea Kimi?

**Sí, pero:**

| Modelo | Pros | Contras |
|--------|------|---------|
| **Kimi K2.5** | Costo óptimo, bueno en español | Menos conocido |
| **GPT-4** | Más documentado | 2x costo |
| **Claude 3** | Excelente para código | Más lento |
| **Local (Ollama)** | Gratis, privado | Menos capaz |

**Recomendación:**
- Start con Kimi
- Ollama como backup
- Subir a GPT-4 si necesitas más capacidad

---

### ¿Qué hago si OpenClaw no funciona en mi sistema?

**Alternativas:**

1. **LangChain** (Python)
   - Más establecido
   - Más documentación
   - Más complejo

2. **Autogen** (Microsoft)
   - Multi-agent nativo
   - Más experimental
   - Potente

3. **CrewAI**
   - Especializado para equipos
   - Menos flexible
   - Más opinionated

4. **Build your own**
   - Llamadas directas a API
   - Más control
   - Más trabajo

**MVP sin OpenClaw:**
```python
import requests

def chat_with_model(prompt):
    response = requests.post(
        "https://api.moonshot.cn/v1/chat/completions",
        headers={"Authorization": "Bearer KEY"},
        json={
            "model": "kimi-k2.5",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()['choices'][0]['message']['content']

# Tu loop manual
while True:
    task = get_next_task()
    prompt = create_prompt(task)
    result = chat_with_model(prompt)
    save_result(result)
```

---

## Sección 3: Sobre Agentes

### ¿Cómo sé si mi agente está funcionando bien?

**Métricas clave:**

1. **Success Rate:** % de tareas completadas exitosamente
   - Target: >80%
   - Revisar si <70%

2. **Approval Rate:** % de outputs aceptados sin cambios
   - Target: >70%
   - Indica calidad del prompt

3. **Cycle Time:** Tiempo promedio por tarea
   - Necesita baseline
   - Alerta si >2x baseline

4. **Stall Rate:** % de tareas que se bloquean
   - Target: <5%
   - Revisar si >10%

**Dashboard simple:**
```json
{
  "agent_name": "content_agent",
  "period": "2026-04-01 to 2026-04-07",
  "tasks_completed": 45,
  "success_rate": "88%",
  "approval_rate": "75%",
  "avg_cycle_time": "25m",
  "stall_rate": "4%",
  "status": "HEALTHY"
}
```

---

### ¿Qué hago si el agente comete el mismo error repetidamente?

**Diagnóstico:**

1. ¿Está en el prompt? → Agregar constraint explícito
2. ¿Está en los examples? → Añadir ejemplo positivo/negativo
3. ¿Es un edge case? → Documentar en LESSONS.md

**Fix pattern:**
```markdown
# Prompt - Tarea X

## Context
[...]

## ⚠️ LESSON LEARNED
Previous attempts failed because of Y.
DO NOT: [acción que falla]
DO: [acción correcta]

## Examples
### ✓ Correct
Input: [...]
Output: [...]

### ✗ Incorrect (why it fails)
Input: [...]
Output: [...]
Reason: [...]
```

---

### ¿Puedo confiar en el agente para código en producción?

**Niveles de confianza:**

**Nivel 1 - Nunca (0%):**
- Core business logic
- Security-critical code
- Financial calculations

**Nivel 2 - Con review (requieres):**
- Database migrations
- API contracts
- Tests

**Nivel 3 - Probado (80%+):**
- Scripts internos
- Documentation
- UI components

**Nivel 4 - Automatizado (95%+):**
- Boilerplate
- Lint fixes
- Formatting

**Estrategia recomendada:**
- Mes 1-3: Nivel 2 (todo revisado)
- Mes 4-6: Nivel 3 (confianza construida)
- Mes 7+: Nivel 4 para código mundano

---

## Sección 4: Sobre Escalabilidad

### ¿Hasta cuántos agentes puedo tener?

**Límites prácticos:**

| Factor | Límite | Workaround |
|--------|--------|------------|
| Gateway | ~100 agents concurrentes | Shard por dominio |
| Memoria | ~1M documentos RAG | Archivar viejos |
| API costs | $500/mes razonable | Optimizar prompts |
| Human mgmt | ~20 swarms | Documentar procesos |

**Números reales:**
- @levelsio: Reporta 50+ procesos automatizados
- @marc_lou: 100+ micro-agentes para product suites
- Típico: 10-20 agentes cubren 80% de operaciones

**Veredicto:** Los límites son económicos y de gestión, no técnicos.

---

### ¿Qué pasa si el agente "se sale de control"?

**Prevention:**

1. **Circuit breakers:**
   ```python
   if error_count > 3:
       pause_agent()
       notify_human()
   ```

2. **Rate limiting:**
   ```python
   if changes_per_hour > 10:
       require_approval()
   ```

3. **Escalation levels:**
   - L1: Agent handles
   - L2: Daily review
   - L3: Immediate stop

**Recovery:**

```bash
# Parar inmediatamente
tmux kill-session -t agent-name

# Rollback
git checkout HEAD -- affected/files

# Fix
git commit -m "Fix: Agent error recovery"

# Restart (con más supervisión)
# Añadir debug logging
# Reducir scope
```

**Realidad:** En 3 meses de operación 24/7, zero incidents graves.

---

## Sección 5: Sobre el Negocio

### ¿El sistema de agentes reemplaza contratar?

**Comparativa:**

| Aspecto | Empleado | Agentes IA |
|---------|----------|------------|
| Costo/mes | $5K-15K | $50-100 |
| Onboarding | 2-3 meses | 2-4 semanas |
| Disponibilidad |