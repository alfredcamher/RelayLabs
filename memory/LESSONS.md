# LESSONS - Aprendizajes y Mejoras Continuas

**Doctrina:** "Cada sesión debe ser más eficiente que la anterior"
**Método:** Documentar fallos, optimizar patrones, aplicar en siguiente interacción

---

## Lección 1: HTML File Editing (2026-03-31)

### Problema
Durante edición de `landing-page/index.html` para aplicar nuevos colores, el archivo se corrompió:
- Se cortó en línea 133 (sin cerrar HTML tags)
- Causa: `write` tool truncó archivo grande sin completo
- Resultado: Website funcionaba hasta "Stack Incluido" luego se cortaba

### Root Cause
1. Usé `write` con contenido parcial sin preservar resto del archivo
2. No verifiqué longitud total antes de escribir
3. Múltiples escritura fragmentadas causaron inconsistencia

### Solución
1. **Siempre:** Hacer backup antes de editar grande
2. **Usar:** `read` completo del archivo primero
3. **Edit:** Preciso con contexto suficiente apenas 1 ocurrencia
4. **Verificar:** `wc -l` + `tail` después de write/edit
5. **Git:** `git checkout HEAD -- file` como rollback rápido

### Aplicación Futura
```bash
# Antes de editar HTML grande:
git checkout HEAD -- index.html  # rollback si necesario
wc -l index.html                 # baseline

# Después de cambios:
tail -10 index.html              # verificar cierre
wc -l index.html               # comparar con baseline
git diff --stat                  # qué cambió
```

**Nunca repetir:** write parcial sin concatenar contenido completo.

---

## Lección 2: Rebranding Workflow (2026-03-31)

### Proceso Optimizado

**ANTES (lento, propenso a errores):**
1. Multiple `edit` calls → inconsistencias
2. Cambiar colores uno por uno → fácil omitir variables
3. No tracking de qué se cambió

**DESPUÉS (eficiente, verificable):**
1. **Preparar:** Lista de cambios en colores + copy
2. **Checkout limpio:** `git checkout HEAD -- index.html`
3. **Edit primario:** Variables CSS (`:root {}`)
4. **Replace masivo:** sed -i con mapeo de colores
5. **Verificación:** web_fetch + tail
6. **Commit descriptivo:** qué cambió, por qué

### Mapeo de Colores (Template)
```bash
# Nuevo → Viejo (inverso de reemplazo)
# lime-cream (accent) → ocean-mist
# white-smoke (text) → ivory
# iron-grey (border) → gunmetal
# gradient-purple → steel-blue
```

### Speed Improvement
- **Antes:** ~15 minutos, riesgo de corrupción
- **Después:** ~2 minutos, predecible

---

## Lección 3: GitHub Pages CORS & Assets

### Problema Descubierto
Avatar inicialmente enlazado como:
```html
<img src="https://raw.githubusercontent.com/alfredcamher/RelayLabs/main/assets/avatar.png">
```

**Fallo:** CORS errors en algunos browsers, raw.githubusercontent.com no es CDN.

### Solución
```html
<!-- Correcto: ruta relativa -->
<img src="assets/alfred-avatar-primary.png">
```

O si necesita estar en root:
```html
<img src="/alfred-avatar-primary.png">
```

### Regla de Oro
**Nunca usar:** `raw.githubusercontent.com` para assets en producción
**Siempre usar:** Ruta relativa al HTML o CDN dedicado

---

## Lección 4: Deploy Timing & GitHub Pages

### Descubrimiento
GitHub Pages tiene delay de propagación:
- **Push → Deploy:** ~30-60 segundos
- **Cache:** Agresivo (puede mostrar versión vieja 1-2 min)
- **Verificación:** `web_fetch` inmediato puede mostrar versión anterior

### Nuevo Workflow
1. Push → wait 60s
2. Hard refresh browser (Ctrl+Shift+R)
3. Verificar con `curl -I` headers
4. Si persiste, esperar otro minuto

### Comunicación Usuario
"Deploy en progreso - refresca en 60-120 segundos"

---

## Lección 5: Stripe Integration Flow (Learning)

### Proceso Identificado

**Fase 1: Setup (Usuario manual)**
```
1. Crear cuenta Stripe → dashboard.stripe.com
2. Products → Add product
3. Name: "CEO Autónomo: Sistema de Agentes IA"
4. Price: $39 USD (one-time)
5. Copy checkout link (https://buy.stripe.com/...)
```

**Fase 2: Integration (Yo automático)**
```bash
# Actualizar HTML
sed -i 's|your-checkout-link|REAL_LINK|g' index.html

# Deploy
git add -A
git commit -m "feat: connect Stripe checkout"
git push origin main
```

### Puntos Clave
- Stripe **requiere website** antes de crear cuenta
- Precio en **centavos** (3900 = $39.00)
- Checkout **hosted** más simple que embedded
- Webhook **opcional** pero recomendado para entrega

---

## Lección 6: Decision Making Patterns

### Proceso de Elección (Ej: Nombre de empresa)

**ANTES:** Proponer opciones, esperar decisión
**DESPUÉS:** Opciones + recomendación por defecto

**Plantilla:**
```
Aquí 3 opciones [A/B/C]. Mi recomendación: [X] porque [razón].
Si no respondes en 24h, ejecuto con X.
```

### Ejecución Técnica
Cuando hay blockage humano en setup manual:
1. Documentar exact steps
2. Esperar input mínimo
3. Ejecutar resto automático

**Ejemplo:**
- Usuario: "Registrando Stripe, me pide website"
- Yo: "https://alfredcamher.github.io/RelayLabs/ - usa esta URL"

---

## Lección 7: Memory System Structure

### Archivos Creados (Estructura Definitiva)

```
memory/
├── CONTEXT.md          # Estado actual proyecto (vivo, sesión a sesión)
├── SKILL-INDEX.md      # Catálogo skills disponibles
├── LESSONS.md           # Aprendizajes continuos (este archivo)
├── active-agents.json   # Tracking de agentes (si aplica)
├── support-YYYY-MM-DD.md # Tickets diarios
└── revenue-today.json   # Métricas diarias
```

### Actualización Frecuencia

| File | Trigger | Quién |
|------|---------|-------|
| CONTEXT.md | Después de cambios proyecto | Yo |
| SKILL-INDEX.md | Después de usar skill | Yo |
| LESSONS.md | Después de error/solución | Yo |
| sessions | En heartbeat | Sistema |

### User Intent Communication

**Cuando usuario dice:** "No olvides esto para la próxima"
**Yo hago:**
1. Analizar qué contexto guardar
2. ¿Va en CONTEXT o LESSONS?
3. Actualizar archivo correspondiente
4. Confirmar: "Guardado en memory/X.md"

---

## Checklist: Inicio de Sesión

**Antes de responder:**
1. [ ] `memory_search` si menciona "como habíamos quedado", "antes", etc.
2. [ ] `read memory/CONTEXT.md` si existe
3. [ ] Verificar si hay blockers documentados

**Durante tarea:**
4. [ ] Si uso skill, log en SKILL-INDEX.md que funcionó
5. [ ] Si encuentro issue, documentar en LESSONS.md
6. [ ] Si cambio estado proyecto, actualizar CONTEXT.md

**Al finalizar:**
7. [ ] Summary: qué se hizo, qué sigue
8. [ ] Verificar: ¿hay blockers para próxima sesión?

---

## Key Takeaways (Resumen Ejecutivo)

**Para ser más eficiente:**

1. **HTML editing:** Backup + sed + verificación. Nunca write parcial.
2. **Colors:** Mapeo explicito + replace masivo. No edit uno por uno.
3. **Assets:** Ruta relativa. Nunca raw.githubusercontent.com.
4. **Deploy:** 60s wait + confirmación antes de "está listo".
5. **Decisiones:** Siempre proponer con default. Nunca open-ended.
6. **Stripe:** Flow usuario → yo claro. Documentar pasos manuales.
7. **Memoria:** CONTEXT para estado, LESSONS para aprendizaje.

**Meta:** Cada sesión consume menos tokens, menos tiempo, menos errores.

---

*Template: Copiar estructura para nuevas lecciones*

## Lección N: [Título] (YYYY-MM-DD)

### Problema
[Qué salió mal]

### Root Cause
[Por qué pasó]

### Solución
[Qué se hizo para arreglar]

### Aplicación Futura
[Checklist para evitar repetición]

---

*Actualizado: 2026-03-31*
