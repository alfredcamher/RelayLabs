# Lead Research Agent MVP

**Purpose:** Generate comprehensive B2B research dossiers for any company in <60 seconds.

**Input:** Company name (e.g., "Stripe")  
**Output:** Markdown/HTML/JSON report + optional PDF

---

## Features

✅ **Company Overview** — Size, founding date, location, industry  
✅ **Funding History** — Recent rounds, total raised, investor names  
✅ **Key Personnel** — CEO, founders, executives from public data  
✅ **Recent News** — Last 12 months via Brave Search  
✅ **Tech Stack Signals** — Inferred from job postings  
✅ **Pain Points** — Derived from news, reviews, context  
✅ **Multiple Formats** — Markdown, HTML, JSON, PDF  
✅ **Web Interface** — FastAPI form + instant download  
✅ **CLI Tool** — Batch research capability  

---

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

**Note:** Requires `BRAVE_API_KEY` environment variable set.

### CLI Usage

```bash
# Generate all formats
python main.py Stripe --output reports --format all

# Markdown only
python main.py "OpenAI" -f md

# With PDF
python main.py Figma -f all --pdf
```

### Web Interface

```bash
python web.py
# Open http://localhost:8000
```

---

## Project Structure

```
lead-research/
├── main.py                 # CLI entry point (click)
├── web.py                  # FastAPI web interface
├── research/
│   ├── brave_client.py    # Brave Search API wrapper
│   ├── analyzer.py        # Data analysis & synthesis
│   ├── formatter.py       # Markdown/HTML/JSON formatting
│   └── __init__.py
├── templates/
│   └── report.html        # HTML template (optional)
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker containerization
└── README.md             # This file
```

---

## API Reference

### POST /api/research

**Request:**
```json
{
  "company_name": "Stripe",
  "format": "all"
}
```

**Response:**
```json
{
  "status": "success",
  "company_name": "Stripe",
  "timestamp": "2025-03-31T16:45:00",
  "download_url": "/download/stripe_2025-03-31T16-45-00.md"
}
```

### GET /download/{filename}

Download a generated report file.

### GET /health

Health check endpoint.

---

## Environment Variables

```bash
export BRAVE_API_KEY="your-api-key-here"
```

---

## Success Criteria (MVP)

- [x] Can input "Stripe" → generates full dossier in <60 seconds
- [x] Report includes: funding rounds, CEO name, employee count, recent news, 3 pain points
- [x] Markdown output clean, professional format
- [x] Code committed to git with clear README
- [x] Web interface loads, accepts input, displays/downloads report
- [ ] Docker image builds and runs

---

## Roadmap

**Phase 2:**
- [ ] LinkedIn scraper for deeper personnel research
- [ ] Enhanced tech stack detection (GitHub, npm, PyPI)
- [ ] Sentiment analysis on news
- [ ] Email generation for outreach
- [ ] CRM integration (Pipedrive, HubSpot)

**Phase 3:**
- [ ] Bulk research (CSV upload)
- [ ] Research history & comparison
- [ ] AI-powered insights (LLM synthesis)
- [ ] Custom report templates

---

## Deployment

### Docker

```bash
docker build -t lead-research .
docker run -e BRAVE_API_KEY=xxx -p 8000:8000 lead-research
```

### Cloud

- **Heroku:** Procfile ready
- **AWS Lambda:** Serverless adaptation possible
- **Railway/Render:** Zero-config deployment

---

## Troubleshooting

### "BRAVE_API_KEY not set"
```bash
export BRAVE_API_KEY="your-key"
# Then run again
```

### PDF generation fails
```bash
pip install weasyprint
# Requires system deps: cairo, pango
# macOS: brew install weasyprint
# Ubuntu: apt-get install python3-weasyprint
```

### Rate limit errors
Brave API allows 5 req/sec by default. Reduce concurrent requests.

---

## License

MIT — Use freely for commercial or personal projects.

---

## Contact

Built by Alfred CamHer | Maintained by Bernardo (facilitator)

_Version 0.1.0-MVP | Last updated 2026-03-31_
