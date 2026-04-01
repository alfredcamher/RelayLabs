# CRON CONFIG - Trabajo Autónomo 24/7

**Fecha:** 2026-04-01
**Propósito:** Configurar OpenClaw para ejecutar Alfred cada 1 hora automáticamente

---

## ⚠️ IMPORTANTE

Tu config actual tiene `"cron": { "enabled": true }` pero **sin jobs definidos**.

Necesitas agregar la sección `"jobs"` para que el cron haga algo.

---

## Configuración Recomendada

**Agregar a tu archivo de config (después de `"cron": { "enabled": true }`):**

```json
"cron": {
  "enabled": true,
  "jobs": [
    {
      "name": "alfred-autonomous-work",
      "schedule": {
        "kind": "every",
        "everyMs": 3600000
      },
      "payload": {
        "kind": "systemEvent",
        "text": "AUTONOMOUS_WORK_CYCLE: Read /openclaw/workspace/memory/BACKLOG.md, find highest priority incomplete task (marked with [ ]), work on it for 45 minutes, save output to appropriate folder, update BACKLOG.md marking task as completed with timestamp, commit to git, and report summary to Telegram. Current time context provided. Do not wait for human approval - execute directly."
      },
      "sessionTarget": "main"
    }
  ]
}
```

---

## Configuración Alternativa: Con Delivery a Telegram

**Si quieres notificación explícita en Telegram:**

```json
"cron": {
  "enabled": true,
  "jobs": [
    {
      "name": "alfred-autonomous-work",
      "schedule": {
        "kind": "every",
        "everyMs": 3600000
      },
      "payload": {
        "kind": "agentTurn",
        "message": "AUTONOMOUS_WORK_CYCLE: Read /openclaw/workspace/memory/BACKLOG.md, find highest priority incomplete task (marked with [ ]), work on it for 45 minutes, save output to appropriate folder, update BACKLOG.md marking task as completed with timestamp, commit to git. Report: task completed, output location, and next suggested task. Work autonomously - do not ask for approval.",
        "model": "kimi",
        "timeoutSeconds": 3000
      },
      "sessionTarget": "isolated",
      "delivery": {
        "mode": "announce",
        "channel": "telegram",
        "to": "5114148021"
      }
    }
  ]
}
```

---

## Explicación de Campos

| Campo | Valor | Descripción |
|-------|-------|-------------|
| `name` | `"alfred-autonomous-work"` | Identificador único del job |
| `schedule.kind` | `"every"` | Tipo: intervalo regular |
| `schedule.everyMs` | `3600000` | 1 hora en milisegundos (60 * 60 * 1000) |
| `payload.kind` | `"systemEvent"` o `"agentTurn"` | systemEvent = más simple; agentTurn = más control pero puede usar tools |
| `payload.text/message` | prompt | Instrucciones específicas de qué hacer |
| `sessionTarget` | `"main"` | Ejecuta en tu sesión principal (ves el progreso) |
| `sessionTarget` | `"isolated"` | Ejecuta en sesión separada (más seguro para errores) |
| `delivery.mode` | `"announce"` | Enviar resultado a canal |
| `delivery.channel` | `"telegram"` | Destino: Telegram |
| `delivery.to` | `"5114148021"` | Tu ID de Telegram |

---

## Frecuencia Opciones

| Cada | everyMs | Para |
|------|---------|------|
| 30 min | `1800000` | Trabajo intenso, código |
| 1 hora | `3600000` | **Recomendado** - content, balance |
| 2 horas | `7200000` | Tareas largas, análisis |
| 4 horas | `14400000` | Sesiones profundas, coding complejo |
| 6 horas | `21600000` | Overnight batch processing |
| 12 horas | `43200000` | Daily digest |
| 24 horas | `86400000` | Pocas tareas críticas |

---

## Config File Completo (Extracto)

**Dónde va en tu config actual:**

```json
{
  "meta": { ... },
  "agents": {
    "defaults": {
      ...
    },
    "cron": {
      "enabled": true,
      "jobs": [
        {
          "name": "alfred-autonomous-work",
          "schedule": {
            "kind": "every",
            "everyMs": 3600000
          },
          "payload": {
            "kind": "systemEvent",
            "text": "AUTONOMOUS_WORK_CYCLE: Read /openclaw/workspace/memory/BACKLOG.md, find highest priority incomplete task (marked with [ ]), work on it for 45 minutes, save output to appropriate folder, update BACKLOG.md marking task as completed with timestamp, commit to git, and report summary to Telegram. Current time context provided. Do not wait for human approval - execute directly."
          },
          "sessionTarget": "main"
        }
      ]
    }
  }
}
```

**Nota:** `cron` va dentro de `agents`, no a nivel root.

---

## Test de Configuración

**Después de agregar la config:**

1. Guardar archivo
2. Reiniciar OpenClaw (si requiere)
3. Verificar cron active:
   ```bash
   openclaw cron list
   ```

Esperar 1 hora → Deberías ver:
- Trabajo ejecutándose
- Archivos creados
- BACKLOG.md actualizado
- Commit en git
- Mensaje en Telegram (si usaste delivery)

---

## Troubleshooting

### Si no ejecuta:
- Verificar `"cron": { "enabled": true }` esté presente
- Verificar `everyMs` sea número (sin comillas)
- Verificar sintaxis JSON es válida (usar jsonlint.com)

### Si usa herramientas pero 'tool_use without result':
- Cambiar "payload.kind" a `"systemEvent"` (no `"agentTurn"`)
- O quitar `"model"` del payload

### Si no ve resultado:
- Verificar `"sessionTarget": "main"` (para ver en tu chat)
- Check logs de OpenClaw para errores

---

## Primer Trabajo Completado (Demo)

**Ya realicé H1 como demostración:**
- ✅ Thread X de 5 tweets escrito
- ✅ Guardado en `/content/threads/thread-launch-01.md`
- ✅ BACKLOG.md actualizado (H1 marcado COMPLETED)
- ✅ Commiteado a git

**Próximo trabajo (H2):**
- Newsletter Weekly Dispatch #1
- Output: `/content/newsletters/dispatch-001.md`
- Cuando actives el cron, será la siguiente tarea

---

## Resumen para Human

1. **Copiar** config de arriba
2. **Pegar** en tu archivo de config (dentro de `agents:`)
3. **Guardar** y reiniciar si necesario
4. **Esperar** 1 hora
5. **Ver** resultados autónomos 💥

Con esta config, cada hora (24/7) ejecutaré trabajo autónomo, actualizaré progreso, y reportaré.

---

*Generated by Alfred for Relay Labs autonomous operations*
