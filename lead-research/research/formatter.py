"""Report formatting and PDF generation."""
from datetime import datetime
from typing import Dict, List, Any
import json


class ReportFormatter:
    """Formats research data into markdown and HTML reports."""
    
    def __init__(self, company_name: str, research_data: Dict[str, Any]):
        self.company_name = company_name
        self.data = research_data
        self.timestamp = datetime.now().isoformat()
    
    def to_markdown(self) -> str:
        """Generate markdown report."""
        md = f"""# B2B Research Dossier: {self.company_name}

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Executive Summary

Comprehensive research dossier for {self.company_name}, including company overview, key personnel, funding history, technology stack, and identified pain points.

---

## Company Overview

"""
        
        if self.data.get("overview"):
            overview = self.data["overview"]
            md += f"""- **Founded:** {overview.get('founded', 'N/A')}
- **Size:** {overview.get('size', 'N/A')} employees
- **Headquarters:** {overview.get('location', 'N/A')}
- **Industry:** {overview.get('industry', 'N/A')}

"""
        
        # Funding Section
        md += "## Funding History\n\n"
        if self.data.get("funding"):
            funding = self.data["funding"]
            if funding.get("total_raised"):
                md += f"**Total Raised:** {funding['total_raised']}\n\n"
            
            if funding.get("funding_rounds"):
                md += "### Recent Funding Rounds\n\n"
                for round_info in funding["funding_rounds"][:3]:
                    md += f"- **{round_info.get('source', 'Unknown')}**\n"
                    md += f"  {round_info.get('snippet', 'N/A')[:150]}\n"
                    md += f"  [Source]({round_info.get('url', '#')})\n\n"
        
        # Key Personnel
        md += "## Key Personnel\n\n"
        if self.data.get("people"):
            people = self.data["people"]
            if people.get("ceo"):
                md += f"- **CEO:** {people['ceo']}\n"
            if people.get("founders"):
                md += f"- **Founders:** {', '.join(people['founders'][:2])}\n"
        
        # Recent News
        md += "\n## Recent News & Updates\n\n"
        if self.data.get("news"):
            for i, news in enumerate(self.data["news"][:5], 1):
                md += f"{i}. **{news.get('title', 'Unknown')}** ({news.get('date_hint', 'Recent')})\n"
                md += f"   {news.get('summary', 'N/A')[:150]}\n"
                md += f"   [Read More]({news.get('url', '#')})\n\n"
        
        # Technology Stack
        md += "## Inferred Technology Stack\n\n"
        if self.data.get("tech_stack"):
            tech = self.data["tech_stack"]
            if tech:
                md += "- " + "\n- ".join(tech[:10])
                md += "\n\n"
        
        # Pain Points & Opportunities
        md += "## Identified Pain Points & Opportunities\n\n"
        if self.data.get("pain_points"):
            for pain in self.data["pain_points"]:
                md += pain + "\n"
        
        md += f"""

---

## Research Methodology

This report was generated using:
- Brave Search API (web research)
- Automated content analysis
- Public data aggregation

**Data Sources:** Company websites, news outlets, job postings, funding databases

---

_End of Report_
"""
        return md
    
    def to_html(self) -> str:
        """Generate HTML report for PDF conversion."""
        md = self.to_markdown()
        
        # Simple markdown to HTML conversion
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{self.company_name} Research Dossier</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f9f9f9;
        }}
        h1 {{
            border-bottom: 3px solid #0066cc;
            padding-bottom: 10px;
            color: #0066cc;
        }}
        h2 {{
            border-left: 4px solid #0066cc;
            padding-left: 10px;
            margin-top: 30px;
        }}
        h3 {{
            color: #555;
        }}
        ul {{
            padding-left: 20px;
        }}
        li {{
            margin: 8px 0;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .meta {{
            color: #666;
            font-size: 0.9em;
            margin: 10px 0;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin: 30px 0;
        }}
    </style>
</head>
<body>
"""
        
        # Convert markdown to simple HTML
        for line in md.split('\n'):
            if line.startswith('# '):
                html += f"<h1>{line[2:]}</h1>\n"
            elif line.startswith('## '):
                html += f"<h2>{line[3:]}</h2>\n"
            elif line.startswith('### '):
                html += f"<h3>{line[4:]}</h3>\n"
            elif line.startswith('- '):
                html += f"<li>{line[2:]}</li>\n"
            elif line.startswith('**Generated'):
                html += f"<p class='meta'>{line}</p>\n"
            elif line.strip():
                html += f"<p>{line}</p>\n"
            elif html and not html.endswith('</ul>\n'):
                html += ""
        
        html += """</body>
</html>"""
        return html
    
    def save_json(self, filepath: str) -> None:
        """Save raw research data as JSON."""
        with open(filepath, 'w') as f:
            json.dump({
                "company": self.company_name,
                "timestamp": self.timestamp,
                "data": self.data
            }, f, indent=2)
