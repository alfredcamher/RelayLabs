# CONFIGURACIÓN DE SEGURIDAD - OpenClaw

## Resumen de Healthcheck 2026-04-01

**Estado General:** ✅ Bueno con mejoras aplicables

### Hallazgos Críticos
| Item | Estado | Acción |
|------|--------|--------|
| Gateway Loopback | ✅ | Seguro (127.0.0.1:18789) |
| Trusted Proxies | ⚠️ | Vacío - ok para local-only |
| Modelos Haiku | ⚠️ | En fallbacks - recomendado remover |
| Updates | ⚠️ | npm 2026.4.1 disponible |
| UFW Firewall | ✅ | Activo |
| Attack Surface | ✅ | Mínimo (0 open, 1 allowlist) |

---

## Modelos Actualizados (Seguridad)

**ANTES (Vulnerable):**
```json
"fallbacks": [
  "anthropic/claude-haiku-4-5"  // ❌ Haiku tier - propensa a injection
]
```

**DESPUÉS (Recomendado):**
```json
"fallbacks": [
  "nvidia-nim/moonshotai/kimi-k2.5",
  "anthropic/claude-sonnet-4-20250514",
  "anthropic/claude-opus-4-20250514"
]
```

**Razón:** Haiku tier = menor resistencia a prompt injection y tool misuse.

---

## Gateway Security Config

```json
{
  "gateway": {
    "port": 18789,
    "bind": "loopback",           // ✅ Solo acceso local
    "mode": "local",
    "trustedProxies": [],            // ✅ Vacío = sin reverse proxy
    "auth": {
      "mode": "token"              // ✅ Token-based
    }
  }
}
```

**Nota:** Si expones Control UI vía reverse proxy, configura `trustedProxies` con IPs específicas.

---

## Firewall UFW Status

```bash
sudo ufw status
# Estado: active
# 18789/tcp ALLOW IN Loopback-only
# 11434/tcp ALLOW IN Loopback-only  // Ollama
```

---

## Próximos Pasos Recomendados

### Prioridad ALTA (Esta semana)
- [ ] `openclaw update` → npm 2026.4.1
- [ ] Verificar backup automático de configuración
- [ ] Documentar valores secretos en vault

### Prioridad MEDIA (Este mes)
- [ ] Verificar encriptación de disco: `sudo lsblk -f | grep crypt`
- [ ] Configurar backup diario de workspace
- [ ] Revisar logs de seguridad semanalmente

### Prioridad BAJA (Opcional)
- [ ] Setup fail2ban para intentos SSH sospechosos
- [ ] Configurar SSH key-only auth
- [ ] Documentar disaster recovery plan

---

## Comandos Rápidos

```bash
# Ver estado
openclaw security audit

# Actualizar
openclaw update

# Verificar firewall
sudo ufw status verbose

# Ver repositorios
ls ~/.openclaw/workspace/.git
```

---

**Healthcheck completado:** 2026-04-01 17:30 CDT
**Próxima revisión:** 2026-04-08
**Responsable:** Alfred | Relay Labs
