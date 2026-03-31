#!/usr/bin/env python3
"""CLI entry point for Lead Research tool."""
import sys
import os
from pathlib import Path
import time

# Add research module to path
sys.path.insert(0, str(Path(__file__).parent))

import click
from research.brave_client import BraveSearchClient
from research.analyzer import ResearchAnalyzer
from research.formatter import ReportFormatter


def load_env():
    """Load environment variables from .env if present."""
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        from dotenv import load_dotenv
        load_dotenv(env_file)


@click.command()
@click.argument('company_name')
@click.option('--output', '-o', default='reports', help='Output directory for reports')
@click.option('--format', '-f', type=click.Choice(['md', 'html', 'json', 'all']), 
              default='all', help='Output format')
@click.option('--pdf', is_flag=True, help='Generate PDF (requires weasyprint)')
def research(company_name: str, output: str, format: str, pdf: bool):
    """
    Generate comprehensive B2B research dossier for a company.
    
    Example:
        python main.py Stripe --output reports --format all --pdf
    """
    
    load_env()
    
    # Create output directory
    output_dir = Path(output)
    output_dir.mkdir(exist_ok=True)
    
    click.echo(f"🔍 Researching {company_name}...")
    click.echo("")
    
    try:
        # Initialize clients
        brave = BraveSearchClient()
        analyzer = ResearchAnalyzer()
        
        # Gather data
        click.echo("📰 Fetching news...")
        news_results = brave.search_news(company_name)
        
        click.echo("💰 Fetching funding info...")
        funding_results = brave.search_funding(company_name)
        
        click.echo("👥 Fetching people data...")
        people_results = brave.search_people(company_name)
        
        click.echo("💻 Searching job postings...")
        job_results = brave.search_jobs(company_name)
        
        # Analyze
        click.echo("🧠 Analyzing results...")
        
        research_data = {
            "overview": {
                "founded": "N/A",
                "size": "N/A",
                "location": "N/A",
                "industry": "B2B SaaS"
            },
            "funding": analyzer.analyze_funding(company_name, funding_results),
            "people": analyzer.analyze_people(company_name, people_results),
            "news": analyzer.analyze_news(company_name, news_results),
            "tech_stack": analyzer.infer_tech_stack(company_name, job_results),
            "pain_points": analyzer.infer_pain_points(
                company_name, 
                news_results + people_results
            )
        }
        
        # Format and save
        click.echo("📝 Generating report...")
        formatter = ReportFormatter(company_name, research_data)
        
        # Determine formats to generate
        formats_to_gen = []
        if format in ['md', 'all']:
            formats_to_gen.append('md')
        if format in ['html', 'all']:
            formats_to_gen.append('html')
        if format in ['json', 'all']:
            formats_to_gen.append('json')
        
        # Save files
        timestamp = int(time.time())
        safe_name = company_name.lower().replace(' ', '_').replace('.', '')
        
        for fmt in formats_to_gen:
            if fmt == 'md':
                filepath = output_dir / f"{safe_name}_dossier_{timestamp}.md"
                with open(filepath, 'w') as f:
                    f.write(formatter.to_markdown())
                click.echo(f"✅ Markdown: {filepath}")
            
            elif fmt == 'html':
                filepath = output_dir / f"{safe_name}_dossier_{timestamp}.html"
                with open(filepath, 'w') as f:
                    f.write(formatter.to_html())
                click.echo(f"✅ HTML: {filepath}")
            
            elif fmt == 'json':
                filepath = output_dir / f"{safe_name}_dossier_{timestamp}.json"
                formatter.save_json(str(filepath))
                click.echo(f"✅ JSON: {filepath}")
        
        # PDF generation (optional)
        if pdf and 'html' in formats_to_gen:
            try:
                from weasyprint import HTML
                pdf_path = output_dir / f"{safe_name}_dossier_{timestamp}.pdf"
                html_file = output_dir / f"{safe_name}_dossier_{timestamp}.html"
                
                if html_file.exists():
                    HTML(str(html_file)).write_pdf(str(pdf_path))
                    click.echo(f"✅ PDF: {pdf_path}")
            except ImportError:
                click.echo("⚠️  PDF requires weasyprint: pip install weasyprint")
        
        click.echo("")
        click.echo(f"✨ Research complete for {company_name}!")
        click.echo(f"📂 Reports saved to: {output_dir.absolute()}")
        
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    research()
