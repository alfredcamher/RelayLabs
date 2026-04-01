# PARTE VIII: IMPLEMENTACIÓN SEMANA A SEMANA
**Guía Completa: De Setup a 100 Agentes en 8 Semanas**

---

## Semana 1: Fundamentos y Primeros Pasos

### Día 1: Visión y Alcance (3-4 horas)

**Mañana - Clarificación de Objetivos (2h):**

Antes de escribir una línea de código o configurar cualquier herramienta, necesitas claridad absoluta sobre qué problema estás resolviendo. Este es el paso más crítico y más ignorado.

**Ejercicio de Clarificación:**

Pregunta 1: ¿Cuál es tu mayor dolor operativo actual?
- [ ] Tengo demasiadas tareas repetitivas que consumen mi tiempo
- [ ] No tengo tiempo para pensar en estrategia porque estoy apagando incendios
- [ ] Quiero escalar pero contratar es caro/complicado
- [ ] Mi backlog de ideas nunca se ejecuta
- [ ] Estoy agotado trabajando 60+ horas semanales

Pregunta 2: ¿Qué resultado quieres lograr en 90 días?
- Reducir horas de trabajo a la mitad
- Automatizar el 70% de tareas operativas
- Tener un sistema que opere mientras duermo
- Liberar tiempo para trabajo estratégico

Pregunta 3: ¿Cuál es tu presupuesto para herramientas?
- Menos de $50/mes
- $50-100/mes
- $100-200/mes
- Lo que sea necesario

**Documentación inicial:**

Crea un archivo `VISION.md` con esto:

```markdown
# Visión - CEO Autónomo Implementation
**Fecha:** YYYY-MM-DD
**Revisión:** Cada 30 días

## Mi Situación Actual
- Horas trabajadas/semana: ___
- Tareas repetitivas identificadas: ___
- Principal bloqueo: ___

## Mi Objetivo a 90 días
- Horas/semana objetivo: ___
- % de tareas automatizadas: ___
- Primer agente operativo: Semana ___

## Métricas de Éxito
- [ ] Semana 2: Primer agente funcional
- [ ] Semana 4: 3 agentes operativos
- [ ] Semana 6: Sistema de monitoreo
- [ ] Semana 8: Operaciones 24/7
```

**Output del Día 1:**
- [ ] Documento de visión completado
- [ ] Prioridades identificadas (máximo 3)
- [ ] Línea base de métricas registrada

---

### Día 2: Setup de Infraestructura - Git y GitHub (3-4 horas)

**La infraestructura es el cimiento.** Si no tienes un sistema robusto de versionado y deploy, todo lo demás será frágil.

**Paso 1: Configuración de Git (30 min):**

```bash
# Instalar Git si no lo tienes
sudo apt install git

# Configurar identidad
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Configurar editor por defecto
git config --global core.editor nano

# Configurar diff más legible
git config --global core.pager "less -F -X"
```

**Verifica:** `git config --list` debe mostrar tu nombre y email.

**Paso 2: Generación de SSH Keys (15 min):**

```bash
# Generar clave SSH
ssh-keygen -t ed25519 -C "tu@email.com"

# Presiona Enter 3 veces para aceptar defaults

# Mostrar clave pública
cat ~/.ssh/id_ed25519.pub
```

**Copia la salida** (comienza con `ssh-ed25519` y termina con tu email).

**Paso 3: GitHub (30 min):**

1. Ve a github.com → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Pega tu clave pública
4. Click "Add SSH key"

**Prueba:**
```bash
ssh -T git@github.com
```

Deberías ver: "Hi username! You've successfully authenticated..."

**Paso 4: Crear Repositorio (20 min):**

```bash
# Crear directorio
mkdir -p ~/workspace/RelayLabs
cd ~/workspace/RelayLabs

# Inicializar
git init

# Crear estructura base
mkdir -p {memory,content/{threads,tweets,newsletters},products,tools,tests}

# Crear README
cat > README.md << 'EOF'
# Relay Labs - CEO Autónomo

Sistema de agentes IA para escalar negocios sin contratar.

## Estructura
- `/memory/` - Documentación y contexto
- `/content/` - Contenido para redes
- `/products/` - Productos y entregables
- `/tools/` - Scripts y utilidades
- `/tests/` - Experimentos y tests

## Quick Start
1. Leer `memory/CONTEXT.md`
2. Configurar agente heartbeat
3. Iniciar primera tarea

---
Built with OpenClaw + Kimi K2.5
EOF

# Commit inicial
git add .
git commit -m "Initial commit: Project structure"
```

**Paso 5: GitHub Pages Setup (45 min):**

```bash
# Crear conexión remota
git remote add origin git@github.com:username/RelayLabs.git

# Push inicial
git push -u origin main

# Crear rama gh-pages
git checkout -b gh-pages
git push origin gh-pages

# Volver a main
git checkout main
```

**Configura GitHub Pages:**
1. Repo → Settings → Pages
2. Source: Deploy from a branch
3. Branch: gh-pages, / (root)
4. Save

**Crea landing básica:**

```bash
mkdir -p landing-page/assets
cat > landing-page/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Relay Labs - CEO Autónomo</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Relay Labs</h1>
    <h2>CEO Autónomo: Sistema de Agentes IA</h2>
    <p>Próximamente...</p>
</body>
</html>
EOF

# Deploy
git checkout gh-pages
git checkout main -- landing-page/
mv landing-page/* .
git add .
git commit -m "Landing page v0.1"
git push origin gh-pages
git checkout main
```

**Verifica:** En 2-5 minutos, `https://username.github.io/RelayLabs/` debe mostrar tu landing.

**Output Día 2:**
- [ ] Git configurado
- [ ] SSH funcionando
- [ ] Repo creado y push
- [ ] GitHub Pages enabled
- [ ] Landing page viva

---

### Día 3-4: OpenClaw Gateway (4-6 horas)

**Paso 1: Instalación OpenClaw (1h):**

```bash
# Instalar Node.js si no lo tienes
sudo apt install -y nodejs npm

# Instalar OpenClaw
npm install -g @openclaw/gateway

# Verificar
openclaw --version
```

**Paso 2: Configuración Inicial (1h):**

```bash
# Crear directorio de configuración
mkdir -p ~/.openclaw
cd ~/.openclaw

# Crear config base
cat > config.json << 'EOF'
{
  "gateway": {
    "port": 18789,
    "host": "127.0.0.1"
  },
  "models": {
    "default": "kimi-k2.5",
    "backup": "ollama-llama3.2:3b"
  },
  "memory": {
    "enabled": true,
    "path": "~/workspace/RelayLabs/memory"
  },
  "cron": {
    "enabled": true,
    "heartbeatInterval": 600000
  }
}
EOF

# Crear .env (NUNCA comitear esto!)
cat > .env << 'EOF'
# API Keys
KIMI_API_KEY=your_key_here
OPENCLAW_TOKEN=vault

# Config
TIMEZONE=America/Mexico_City
EOF

chmod 600 .env
```

**Paso 3: Primer Heartbeat (2h):**

```bash
# Script de heartbeat
cat > ~/workspace/RelayLabs/tools/heartbeat.sh << 'EOF'
#!/bin/bash
TIMESTAMP=$(date '+%Y-%m-%d-%H%M')
LOG_FILE="~/workspace/RelayLabs/memory/heartbeat-${TIMESTAMP}.json"

# Check OpenClaw status
if curl -s http://localhost:18789/status > /dev/null 2>&1; then
    STATUS="active"
else
    STATUS="stopped"
fi

# Create log
cat > "${LOG_FILE}" << LOG
{
  "timestamp": "$(date -Iseconds)",
  "status": "${STATUS}",
  "checks": {
    "openclaw": "${STATUS}",
    "ollama": "$(pgrep -c ollama || echo '0')",
    "disk": "$(df -h / | awk 'NR==2{print $5}')",
    "memory": "$(free -m | awk 'NR==2{print $3"/"$2}')"
  },
  "cycle": $(basename $(ls ~/workspace/RelayLabs/memory/heartbeat-*.json 2>/dev/null | wc -l))
}
LOG

echo "Heartbeat logged: ${TIMESTAMP}"
EOF

chmod +x ~/workspace/RelayLabs/tools/heartbeat.sh

# Test
~/workspace/RelayLabs/tools/heartbeat.sh
```

**Paso 4: Configurar Cron (30 min):**

```bash
# Editar crontab
crontab -e

# Añadir:
*/10 * * * * ~/workspace/RelayLabs/tools/heartbeat.sh
```

**Paso 5: Verificación (30 min):**

```bash
# Verificar heartbeats están llegando
ls -la ~/workspace/RelayLabs/memory/heartbeat-*.json | tail -5

# Leer último heartbeat
cat ~/workspace/RelayLabs/memory/heartbeat-$(date +%Y-%m-%d)-* | tail -1 | jq .
```

**Output Días 3-4:**
- [ ] OpenClaw instalado
- [ ] Configuración lista
- [ ] Heartbeat automatizado
- [ ] Logs funcionando

---

### Día 5-7: Modelos LLM y Primer Agente

**Día 5: Configuración Kimi K2.5 (3h):**

O