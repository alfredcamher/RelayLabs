# SKILL-INDEX - Catálogo de Habilidades Disponibles

**Última actualización:** 2026-03-31
**Para:** Alfred CamHer / Relay Labs

---

## Skills Disponibles

### 1. healthcheck 🔒
**Descripción:** Host security hardening and risk-tolerance configuration for OpenClaw deployments.

**USAR CUANDO:**
- Security audits, firewall/SSH/update hardening
- Risk posture review
- Exposure review
- OpenClaw cron scheduling for periodic checks
- Version status checks
- Máquina: laptop, workstation, Pi, VPS

**NO USAR PARA:**
- Configuración de aplicaciones (sólo host)
- Cambios remotos sin confirmar acceso

**Comandos clave:**
```bash
openclaw security audit [--deep] [--fix] [--json]
openclaw status [--deep]
openclaw update status
openclaw cron add|list|runs|run
```

**Aprobaciones requeridas:**
- Cambios a firewall
- Apertura/cierre de puertos
- SSH/RDP config
- Instalación de paquetes
- Scheduling de tareas

---

### 2. skill-creator 🛠️
**Descripción:** Create or update AgentSkills. Use when designing, structuring, or packaging skills.

**USAR CUANDO:**
- Crear nuevo skill
- Actualizar skill existente
- Diseñar flujos de trabajo
- Empaquetar skills con scripts, referencias, assets

**NO USAR PARA:**
- Execución directa de tareas (crear skill primero, luego usar)

**Workflow:**
1. Entender ejemplos concretos
2. Planear contenido reusable (scripts, references, assets)
3. Inicializar: `init_skill.py <name> --path <dir>`
4. Editar SKILL.md
5. Empaquetar: `package_skill.py <skill-folder>`

**Estructura skill:**
```
skill-name/
├── SKILL.md (required - frontmatter YAML + body)
├── scripts/ (Python/Bash determinístico)
├── references/ (docs para cargar en contexto)
└── assets/ (templates, logos, fonts)
```

---

### 3. weather 🌤️
**Descripción:** Get current weather and forecasts via wttr.in or Open-Meteo.

**USAR CUANDO:**
- "What's the weather?"
- "Will it rain today/tomorrow?"
- "Temperature in [city]"
- Travel planning weather

**NO USAR PARA:**
- Historical weather data
- Severe weather alerts
- Aviation/marine weather

**Comandos:**
```bash
# Current
curl "wttr.in/London?format=3"

# Forecast
curl "wttr.in/London"

# Specific day (0=today, 1=tomorrow)
curl "wttr.in/London?1"
```

---

## Aprendizajes de Skills

### healthcheck
- **Token efficiency:** Audit resultados primero, luego preguntar por ejecución
- **Rollback strategy:** Siempre tener plan de reversión antes de cambios
- **Memory:** Escribir a `memory/YYYY-MM-DD.md` con resumen de auditoría

### skill-creator
- **Naming:** lowercase + hyphens, verb-led, <64 chars
- **Concise:** SKILL.md <500 lines, references para detalles
- **Progressive disclosure:** Metadata → SKILL.md → references

### weather
- **No rate limiting pero:** no spam, wttr.in es servicio gratuito
- **Location:** Siempre buscar ciudad específica
- **Format codes:** %c=emoji, %t=temp, %f=feels, %w=wind, %h=humidity

---

## Cuándo Usar Cada Skill (Decision Tree)

```
¿Necesitas mejorar seguridad del host?
└── SÍ → healthcheck

¿Necesitas crear skill nuevo?
└── SÍ → skill-creator

¿Necesitas saber el clima?
└── SÍ → weather

¿Ninguno de los anteriores?
└── Usa herramientas nativas (exec, read, write, etc.)
```

---

## Herramientas Nativas (Siempre Disponibles)

| Tool | Uso Principal | Cuándo NO usar |
|------|---------------|----------------|
| `exec` | Shell commands, scripts | Comandos destrucivos sin confirmar |
| `read` | Leer archivos | Archivos >50KB (usar offset/limit) |
| `write` | Crear/sobreescribir | Nunca sobreescribir sin backup |
| `edit` | Ediciones precisas | Archivos muy grandes |
| `web_search` | Research rápido | Info sensible/offline |
| `web_fetch` | Extraer contenido web | Solo cuando necesario |
| `image` | Analizar imágenes | No generar imágenes (sólo analizar) |
| `sessions_spawn` | Tareas background | Tareas críticas sin human review |
| `subagents` | Manage sub-agents | Nunca dejar sin chequear |
| `cron` | Scheduled jobs | Sin recordatorio al user |
| `message` | Send messages | Spam, mensajes sin contexto |
| `canvas` | UI canvas | N/A en CLI context |
| `nodes` | Paired nodes | No inventar comandos |
| `browser` | Web automation | Host remoto sin confirmación |

---

## Mejoras Pendientes (Skills a Crear)

Basado en tareas frecuentes de Relay Labs:

1. **landing-page-builder** - Generar landing pages con HTML/CSS moderno
2. **stripe-checkout** - Integración Stripe para productos digitales
3. **github-deploy** - Deploy a GitHub Pages automático
4. **revenue-tracker** - Check métricas MRR daily
5. **content-marketing** - Generar posts para social media
6. **pdf-guide-creator** - Compilar markdown → PDF guía

---

*Documento vivo - actualizar después de cada uso de skills*
