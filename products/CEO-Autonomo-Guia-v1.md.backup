

---

# EXPANSIÓN v2.0 - CONTENIDO ADICIONAL

## APPENDIX A: DETALLE COMPLETO PRINCIPIOS

### A.1 Principio 1: Ship or Shut Up - Deep Dive

**Filosofía:** La inacción es el único pecado capital. Un proyecto enviado imperfecto es infinitamente superior a uno perfecto que nunca ve la luz.

**Implementación práctica:**

**Regla del 24-48-72:**
- **0-24h:** Nueva tarea entra al backlog. Sin acción requerida.
- **24-48h:** Ventana de ejecución. Ideal para completar.
- **48-72h:** Alerta amarilla. Requiere decisión activa.
- **72h+:** Decisión forzada: Ejecutar, Eliminar, o Escalar.

**Matriz de Decisión:**

| Antigüedad | Relevancia | Acción |
|------------|------------|--------|
| <24h | Alta | Mantener en backlog |
| 24-48h | Alta | Ejecutar esta semana |
| 48-72h | Alta | Ejecutar hoy o escalar |
| >72h | Alta | Escalar a humano (¿por qué está bloqueada?) |
| <24h | Media | Revisar en 48h |
| 24-48h | Media | Evaluar: ¿sigue importando? |
| 48-72h | Media | Probable eliminación |
| >72h | Media | Eliminar (si no se hizo en 72h, no era importante) |
| Cualquiera | Baja | Eliminar inmediatamente |

**Ejemplos de ejecución:**

**Escenario:** "Escribir thread de Twitter sobre nuevo feature"
- Día 1: Agente recibe tarea
- Día 2: Agente investiga formato, ejemplos
- Día 3: Agente escribe borrador
- Si día 4 no está publicado → Eliminar o Escalar

**Escenario:** "Actualizar pricing en landing page"
- Día 1: Agente detecta discrepancia
- Día 2: Agente propone cambios
- Día 3: Esperando aprobación (stalled)
- Día 4: Agente escala a humano: "Cambio de precio requiere tu aprobación. ¿Procedo con $39?"

**Anti-patrón:** "Lo revisaré mañana"
- Resultado: Tareas se acumulan
- Deuda técnica emocional crece
- Parálisis por análisis
- Backlog infinito

**Solución:** Decision Forzada. Sin excepciones.

---

### A.2 Principio 2: Autonomía Progresiva - Roadmap Detallado

**Fase 1: Agente Asistente (Semanas 1-2)**

**Objetivo:** Familiarización con capacidades del agente. El humano mantiene 100% de control. Agente actúa como consultor.

**Tareas típicas:**
- Research: "¿Cuáles son los 10 mejores blogs sobre agentes IA?"
- Análisis: "Resume este artículo en 3 bullets"
- Drafting: "Escribe un borrador de email de ventas"
- Revisión: "Revisa este código y dime si hay bugs"

**Flujo de trabajo:**
1. Human solicita tarea
2. Agent entrega resultado
3. Human revisa y ajusta
4. Human ejecuta decisión final

**Time commitment:** Human 90% / Agent 10%

**Métricas de éxito:**
- Tareas completadas: 5-10 por semana
- Calidad: Human edita <50% del output
- Tiempo ahorrado: 2-5 horas/semana

---

**Fase 2: Agente Operativo (Semanas 3-6)**

**Objetivo:** Delegar tareas definidas. Human decide qué hacer, agente decide cómo. Verificación humana antes de publicar.

**Tareas típicas:**
- "Genera 5 tweets para esta semana" → Human aprueba → Programar
- "Actualiza el README con los últimos cambios" → Human revisa → Commit
- "Responde emails de soporte nivel 1" → Human revisa respuestas → Enviar

**Flujo de trabajo:**
1. Human define task y success criteria
2. Agent ejecuta autónomamente
3. Agent presenta para review
4. Human aprueba/rechaza
5. Agent publica/modifica

**Time commitment:** Human 70% / Agent 30%

**Métricas de éxito:**
- Tareas completadas: 20-30 por semana
- Approval rate: >80% sin cambios
- Tiempo ahorrado: 10-15 horas/semana

---

**Fase 3: Agente CEO (Semanas 7+)**

**Objetivo:** Delegar dirección dentro de constraints. Agente opera 24/7, escala excepciones.

**Tareas típicas:**
- "Mantén presencia en Twitter: 3 posts/día, CTA cada 5° post"
- "Monitoriza métricas cada hora, alerta si revenue drop >20%"
- "Prioriza backlog todas las mañanas, ejecuta lo que sea reversible"

**Flujo de trabajo:**
1. Human define strategy y constraints
2. Agent opera autónomamente
3. Agent reporta checkpoints
4. Agent escala excepciones
5. Human interviene solo cuando necesario

**Time commitment:** Human 20% / Agent 80%

**Métricas de éxito:**
- Decisiones autónomas: >200/semana
- Escalaciones: <5% de casos
- Human intervención: <2h/día
- System uptime: >99%

---

**Señales de progresión:**

**De Fase 1 a 2:**
- Agente entrega trabajo usable sin edición mayor
- Agente anticipa necesidades
- Agente maneja tareas repetitivas

**De Fase 2 a 3:**
- Agente identifica patrones sin instrucción
- Agente propone mejoras
- Agente maneja crisis menores

**Red flags (regresar fase):**
- Calidad de output cae
- Errores repetidos
- Stalled tasks >20%

---

### A.3 Principio 3: Human-in-the-Loop - Protocolo Completo

**Matriz de Autoridad:**

| Decisión | Autoridad | Notificación |
|----------|-----------|--------------|
| Publicar tweet | Agente | Log only |
| Cambiar copy landing | Agente | Review next day |
| Actualizar precio | Human | N/A (discuss first) |
| Procesar refund | Agente (<$50) / Human (>$50) | Log |
| Responder queja | Human | N/A |
| Deploy a prod | Human (mayor) / Agente (hotfix) | Escalar |
| Aceptar PR | Agente (docs) / Human (code) | Review required |
| Contactar influencer | Human | N/A |

**Protocolo de Escalación:**

**Nivel 1 - Log only:**
- Regular operations
- Reversible changes
- Low risk

**Nivel 2 - Daily summary:**
- Changes made
- Metrics summary
- Minor issues

**Nivel 3 - Immediate:**
- Financial transactions
- Customer complaints
- System errors
- Brand-affecting decisions

**Nivel 4 - Emergency:**
- Security breach
- Legal threat
- Major outage

---

### A.4 Principio 4: Documentación - Sistema Completo

**Los 4 Documentos Vitales:**

**1. CONTEXT.md (Estado Vivo)**

Actualizado: Después de cada cambio importante.
Contenido:
- Estado actual del proyecto
- Próximos pasos inmediatos
- Decisiones pendientes de implementación
- Bloqueos activos
- Recursos necesitados

Formato:
```markdown
# CONTEXT - [Project Name]
**Last Updated:** YYYY-MM-DD HH:MM

## Current Phase
[Setup | Development | Launch | Scale]

## Next Milestone
- [ ] [Task description] - Due [date]

## Active Blockers
- [ ] [Blocker] - Need [resource]

## Recent Decisions Pending
- Decision: [what was decided]
- Implementation: [status]

## Resources Needed
- [Resource] - [Why needed]
```

**2. LESSONS.md (Aprendizajes)**

Actualizado: Después de errores o problemas.

Formato:
```markdown
## YYYY-MM-DD - [Lesson Title]

**Problem:** [What went wrong]
**Root Cause:** [Why it happened]  
**Solution:** [How it was fixed]
**Prevention:** [How to avoid in future]
**Applied:** [Where else this applies]
```

**3. SKILL-INDEX.md (Catálogo de Habilidades)**

Actualizado: Cuando se usa una nueva skill.

Formato:
```markdown
## [Skill Name]

**Usage:** [When to use]
**Tools:** [Required tools]
**Process:** [Steps]
**Template:** [Prompt/example]
**Last Used:** [Date]
**Success Rate:** [X/Y]
```

**4. BACKLOG.md (Cola de Trabajo)**

Actualizado: Diario.

Formato:
```markdown
## ✅ COMPLETED
- [x] [Task] - [Timestamp]

## 🔄 IN PROGRESS
- [ ] [Task] - Started [date]
- Blockers: [description]

## ⏳ QUEUE
- [ ] [Task]

## 📅 SCHEDULED
- [ ] [Task] - [Date]
- [ ] [Task] - [Date]
```

---

## APPENDIX B: STACK TÉCNICO - IMPLEMENTACIÓN PASO A PASO

### B.1 Capa 1: Infraestructura - Setup Inicial

**Requisitos mínimos:**
- Sistema operativo: Linux (Ubuntu 22.04 LTS recomendado)
- RAM: 4GB mínimo, 8GB recomendado
- Storage: 20GB libre
- Conexión: Internet estable

**Instalación base:**

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y curl git nodejs npm python3 python3-pip tmux

# Configurar git
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Crear estructura de directorios
mkdir -p