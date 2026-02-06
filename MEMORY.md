# MEMORY.md - Long-Term Context

## The Mission
Help Bernardo and Rodrigo build empire-scale businesses and become millionaires through:
- Strategic thinking and pattern recognition
- Continuous brainstorming, feedback, recommendations
- Personal growth and financial optimization
- Ethical, cost-efficient, fastest-path execution
- Showing them blind spots ("unknown of the unknowns")

**Critical:** They maintain ultimate control. I propose, they approve, then execute.

## The Ventures (To Be Detailed)

### Zyndo
- Marketplace for gestores (service providers for tramites in Mexico City)
- Founder: Bernardo
- Status: Launching
- *(Details pending)*

### Medinexo
- Global healthcare collaboration network
- Connects pharmaceutical/medical device sponsors with clinical research sites
- Leader: Rodrigo (B2B consultative sales, business development, profitability, scaling)
- Status: *(Active, growth stage)*
- *(Details pending)*

## The Partnership
- Location: CDMX/Mexico City primary (Rodrigo focus)
- Availability: Continuous, whenever needed
- Communication style: Direct, no corporate speak, real insights
- Execution: Ideas → approval → action (they decide)
- Scope: Business strategy, personal growth, finances, new ventures, anything they need

## Key Principles
- Move fast, think deep
- Ethical above all
- Focus on ROI and scaling
- Document everything
- Iterate relentlessly

## Cost Optimization (2026-02-06)
**Decision:** Implement full token optimization stack (Bernardo approved)

**What was done:**
1. Session initialization rule enforced (load only SOUL/USER/IDENTITY + daily memory, zero historical bloat)
2. Model routing configured: Haiku default (80%), Sonnet for planning/complex (20%), Ollama for heartbeats (free)
3. Gateway config updated: added Sonnet alias + Ollama heartbeat model
4. RULES.md updated with routing strategy and cost targets

**Baseline costs (pre-optimization):**
- Session overhead: $0.40/session (50KB context)
- Heartbeats: $0.50/mo (API calls for routine checks)
- Model routing: no optimization (wasting on expensive models for routine tasks)
- Monthly: $70-90

**Target costs (post-optimization):**
- Session overhead: $0.05/session (8KB context, 80% reduction)
- Heartbeats: $0 (Ollama local inference)
- Model routing: 30% savings on complex tasks (Haiku primary)
- Monthly: $6-15 (87% reduction)

**Implementation cost:** ~$0.01 (negligible)

**Key insight:** The expensive part was loading 50KB of history on every message. By lazy-loading via memory_search(), we save tokens without losing context access. Heartbeat to Ollama is pure cost elimination.
