# PARTE XIII: GUÍA COMPLETA DE TROUBLESHOOTING
**Resolución de Problemas Comunes y No Tan Comunes**

---

## 13.1 Diagnóstico Rápido: Árbol de Decisiones

### Mi agente no responde

```
¿El agente no responde?
    │
    ├─► ¿Gateway está corriendo?
    │       ├─ NO → sudo openclaw gateway start
    │       └─ SÍ → Verificar en localhost:18789
    │
    ├─► ¿Modelo tiene acceso?
    │       ├─ NO → Verificar API keys en .env
    │       └─ SÍ → Probar prompt simple
    │
    └─► ¿El agente está "stalled"?
            ├─ SÍ (>30 min sin output)
            │   ├─ ¿Proceso activo? → pgrep agent-name
            │   ├─ ¿Tmux session? → tmux list-sessions
            │   └─ ¿Logs? → tail -f ~/.openclaw/logs/*
            │
            └─ NO → Tarea posiblemente completó sin notificar
```

### Gateway no inicia

**Síntomas:**
```
$ openclaw gateway start
Error: Port 18789 already in use
```

**Diagnóstico:**
```bash
# ¿Proceso Ocupando el puerto?
sudo lsof -i :18789

# Si hay proceso, matarlo
sudo kill -9 [PID]

# O reiniciar limpio
openclaw gateway restart --force
```

**Prevención:**
```bash
# Agregar antes de iniciar
pkill -f "openclaw.*gateway" 2>/dev/null
sleep 2
openclaw gateway start
```

---

## 13.2 Errores Comunes y Soluciones

### Error Type 1: Rate Limiting

**Symptom:**
```json
{
  "error": "Rate limit exceeded",
  "retry_after": 60
}
```

**Causas:**
- Demasiadas requests en poco tiempo
- Plan gratuito con límites bajos
- API key compartida

**Soluciones inmediatas:**
```python
# Implementar exponential backoff
def call_with_retry(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError as e:
            wait = (2 ** attempt) * 10  # 10s, 20s, 40s
            time.sleep(wait)
    raise MaxRetriesExceeded()
```

**Soluciones permanentes:**
```yaml
# Implementar circuit breaker
rate_limit_config:
  requests_per_minute: 20
  burst_allowance: 5
  on_limit: 
    action: switch_to_backup_model
    backup: ollama_local
```

---

### Error Type 2: Context Window Exceeded

**Symptom:**
```
Error: Input too long (tokens: 298432, limit: 256000)
```

**Causas:**
- Historial de mensajes muy largo
- Contexto acumulado sin resumen
- File attachments grandes

**Solución inmediata:**
```python
# Truncar mensajes antiguos
def truncate_context(messages, keep_last=10):
    if len(messages) > keep_last:
        # Mantener system prompt + últimos N
        return [messages[0]] + messages[-keep_last:]
    return messages
```

**Solución permanente:**
```python
# Implementar memory management
class ContextManager:
    def __init__(self, max_tokens=200000):
        self.max_tokens = max_tokens
        
    def add_message(self, role, content):
        # Si excedería, resumir historia
        if self.projected_tokens() > self.max_tokens * 0.9:
            self.summarize_history()
        
        self.messages.append({"role": role, "content": content})
    
    def summarize_history(self):
        # Crear summary de mensajes antiguos
        pass
```

---

### Error Type 3: Agent Stuck in Loop

**Symptom:**
```
[10:00:00] Starting task...
[10:00:05] Retrying...
[10:00:10] Retrying...
[10:00:15] Retrying...  # Infinite loop
```

**Causas:**
- Error handling sin límites
- Condición terminal mal definida
- Feedback loop:
- Prompt ambiguo causando misinterpretación

**Detección:**
```python
class LoopDetector:
    def __init__(self, max_iterations=5, similarity_threshold=0.9):
        self.max_iterations = max_iterations
        self.threshold = similarity_threshold
        self.previous_states = []
        
    def check_progress(self, current_state):
        if len(self.previous_states) >= self.max_iterations:
            # Calcular similitud con estados anteriores
            for old_state in self.previous_states:
                if self.similarity(current_state, old_state) > self.threshold:
                    return "LOOP_DETECTED"
            
            # Shift window
            self.previous_states.pop(0)
        
        self.previous_states.append(current_state)
        return "PROGRESS_OK"
    
    def similarity(self, a, b):
        # Implementar similitud de cadenas
        return SequenceMatcher(None, a, b).ratio()
```

**Acción ante loop:**
```python
if loop_detected:
    # Estrategia: Reset con contexto limpio
    agent.clear_context()
    agent.add_context("Previous attempt failed with infinite loop. 
                       Approaching differently.")
    agent.set_strategy("alternative_approach")
    agent.retry()
```

---

### Error Type 4: Authentication Failures

**Síntomas:**
- "Authentication failed"
- "Invalid API key"
- "401 Unauthorized"

**Causas:**
1. API key expirada
2. Key formateada incorrectamente
3. Variable de entorno no cargada
4. Key revocada

**Diagnóstico sistemático:**

**Paso 1: Verificar variable**
```bash
echo $KIMI_API_KEY
# Si vacío → no cargada

# Cargar manualmente
export KIMI_API_KEY=$(cat ~/.secrets/kimi_key)
```

**Paso 2: Verificar formato**
```bash
# Key válida Kimi: sk-xxxxxxxxxxxxxxxx
# Si tiene espacios o newlines:
echo "$KIMI_API_KEY" | xxd | head
```

**Paso 3: Probar con curl**
```bash
curl -H "Authorization: Bearer $KIMI_API_KEY" \
     https://api.moonshot.cn/v1/models
```

**Paso 4: Si falla → regenerar key**
1. Ir a dashboard de API
2. Revocar key vieja
3. Generar nueva
4. Actualizar .env
5. Reiniciar agente

---

### Error Type 5: Disk Space Full

**Symptom:**
```
Error: No space left on device
IOError: [Errno 28]
```

**Impacto:**
- Heartbeats no se guardan
- Logs corrompidos
- Git operations fallan
- Agente no puede escribir output

**Diagnóstico:**
```bash
# Verificar espacio
df -h

# Encontrar archivos grandes
du -sh /home/user/.openclaw/* | sort -hr | head -20

# Archivos problemáticos comunes:
# - Logs antiguos
# - Heartbeat files acumulados
# - Git objects
# - Model caches
```

**Clean up script:**
```bash
#!/bin/bash
# cleanup.sh

# Limpiar heartbeats viejos (>30 días)
find ~/workspace/RelayLabs/memory/heartbeat-* \ 
    -mtime +30 -delete

# Limpiar logs
find ~/.openclaw/logs/*.log -mtime +7 -delete

# Limpiar git

cd ~/workspace/RelayLabs

git gc --aggressive

# Limpiar cache
rm -rf ~/.cache/pip/*

# Reporte
echo "Cleanup complete. Space freed:"
du -sh ~/.local/share/Trash/files 2>/dev/null || echo "0B"
```

**Prevención - cron:**
```bash
# Agregar a crontab
0 2 * * 0 ~/workspace/RelayLabs/tools/cleanup.sh
```

---

## 13.3 Debugging Avanzado

### Técnica 1: Step-by-Step Execution

Cuando un agente falla consistentemente:

```python
# Descomponer en pasos debuggeables
def task_debug_mode():
    # Paso 1: Verificar inputs
    print("Step 1: Input validation")
    print(f"Input: {input_data}")
    
    # Paso 2: Transformación
    print("Step 2: Data transformation")
    intermediate = transform(input_data)
    print(f"Intermediate: {intermediate}")
    
    # Paso 3: Procesamiento principal
    print("Step 3: Core processing")
    result = process(intermediate)
    print(f"Result type: {type(result)}")
    print(f"Result size: {len(result)}")
    
    # Paso 4: Transformación de salida
    print("Step 4: Output formatting")
    output = format(result)
    
    return output
```

### Técnica 2: Búsqueda Diferencial

Cuando "funcionaba ayer pero hoy no":

```bash
# Qué cambió?
git log --since="24 hours ago" --oneline

# Qué archivos modificados?
git diff --name-only HEAD~1

# Ver diferencias específicas
git diff HEAD~1 path/to/file

# Rollback si necesario
git checkout HEAD~1 -- path/to/file
```

### Técnica