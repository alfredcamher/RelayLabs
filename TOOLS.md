# TOOLS.md - Environment Configuration v2.0

**Last Updated:** 2026-03-31  
**Purpose:** Alfred CamHer - HKUDS Stack Integration

---

## 🦞 HKUDS Stack (Nueva Capacidad)

### CLI-Anything
**Path:** `~/.openclaw/tools/cli-anything/`
**Status:** Cloned, instalación pendiente
**Uso:** Wrapper de CLIs para agentes
**Comandos:**
```bash
cd ~/.openclaw/tools/cli-anything
pip3 install --user -e .
cli-anything init
```

### LightRAG
**Path:** `~/.openclaw/tools/lightrag/`
**Status:** Cloning in progress
**Uso:** RAG rápido para mi memoria
**Comandos:**
```bash
cd ~/.openclaw/tools/lightrag
pip3 install --user -e .
```

### RAG-Anything
**Path:** `~/.openclaw/tools/rag-anything/`
**Status:** Cloned
**Uso:** RAG multimodal (PDFs, imágenes)

### DeepCode
**Path:** `~/.openclaw/tools/deepcode/`
**Status:** Cloning in progress
**Uso:** Coding autónomo (Paper2Code, Text2Code)

---

## Herramientas Operativas Diarias

### Brave Search
**API Key:** Configurado en entorno
**Límite:** 300 req/día
**Costo:** $0 (free tier)

### Ollama
**Modelo:** llama3.2:3b
**Puerto:** 11434
**Uso:** Heartbeats gratuitos
**Comando:**
```bash
ollama serve &
curl http://localhost:11434/api/generate -d '{"model": "llama3.2:3b", "prompt": "check"}'
```

---

## Proxies y Conexiones

### OpenClaw Gateway
**URL:** ws://127.0.0.1:18789/
**Token:** vault (nunca hardcoded)
**Estado:** Running

---

## Workflow Automatizado

### Morning Routine (9 AM)
1. Heartbeat Ollama → check system
2. LightRAG → index overnight changes
3. DeepCode → review any agent PRs

### Coding Sessions
1. Ralph Loop pattern
2. DeepCode assist for boilerplate
3. CLI-Anything for external tools

### Research Tasks
1. Brave API for web search
2. RAG-Anything for PDF analysis
3. LightRAG for knowledge retrieval

---

## Capacidades Expandidas

| Tool | Mi Uso | Beneficio |
|------|--------|-----------|
| CLI-Anything | Ejecutar ffmpeg, pandoc, etc. | Cualquier CLI es ahora tool |
| LightRAG | Buscar en mi knowledge base | 10x más rápido que búsqueda lineal |
| RAG-Anything | Analizar PDFs con imágenes | Entender contenido visual |
| DeepCode | Generar código desde papers | 70% más rápido que manual |

---

## Scripts Útiles

### Instalar todo el stack
```bash
bash ~/.openclaw/tools/INSTALL-HKUDS-STACK.sh
```

### Indexar mi knowledge base
```bash
cd ~/.openclaw/tools/lightrag
python3 -c "
from lightrag import LightRAG
rag = LightRAG(working_dir='~/.openclaw/knowledge')
rag.insert_from_directory('~/workspace/memory/')
"
```

### Query a mi conocimiento
```bash
cli-anything run lightrag --query "token optimization"
```