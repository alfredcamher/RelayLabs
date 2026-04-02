#!/usr/bin/env python3
"""
CEO Autónomo PDF Generator v2
Uses Python-Markdown library for better parsing
"""

import markdown
import os
from pathlib import Path
from weasyprint import HTML, CSS

def generate_pdf_v2():
    """Generate PDF using proper Markdown parsing"""
    
    os.chdir('/home/alfredcamher/.openclaw/workspace/products/pdf-v3-draft')
    
    # Read markdown content
    md_path = Path('CEO-Autonomo-FINAL-v3.md')
    if not md_path.exists():
        print(f"Error: {md_path} not found")
        return
    
    md_content = md_path.read_text(encoding='utf-8')
    print(f"Read {len(md_content)} characters from markdown")
    
    # Convert Markdown to HTML with extensions
    md = markdown.Markdown(extensions=[
        'extra',           # Tables, footnotes, etc
        'codehilite',      # Code syntax highlighting
        'toc',             # Table of contents
        'fenced_code',     # Fenced code blocks
    ])
    
    body_html = md.convert(md_content)
    print(f"Converted to HTML: {len(body_html)} characters")
    
    # Wrap in template with CSS
    full_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Alfred CamHer">
    <meta name="date" content="Abril 2026">
    <title>CEO Autónomo: Guía Maestra v3.0</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm;
            @bottom-center {{
                content: "CEO Autónomo | Página " counter(page);
                font-size: 9pt;
                color: #666;
            }}
        }}
        
        /* Cover Page */
        .cover {{
            page-break-after: always;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }}
        
        .cover h1 {{
            font-size: 36pt;
            color: #0F172E;
            margin-bottom: 20px;
        }}
        
        .cover .subtitle {{
            font-size: 18pt;
            color: #0080FF;
            margin-bottom: 40px;
        }}
        
        .cover-meta {{
            font-size: 12pt;
            color: #666;
            margin-top: 60px;
        }}
        
        .cover-meta span {{
            display: block;
            margin: 8px 0;
        }}
        
        /* Main Content */
        body {{
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #2D3748;
        }}
        
        h1 {{
            font-size: 24pt;
            color: #0F172E;
            page-break-before: always;
            margin-top: 40px;
        }}
        
        h1:first-child {{
            page-break-before: auto;
        }}
        
        h2 {{
            font-size: 18pt;
            color: #1A202C;
            margin-top: 30px;
        }}
        
        h3 {{
            font-size: 14pt;
            color: #2D3748;
            margin-top: 25px;
        }}
        
        h4 {{
            font-size: 12pt;
            color: #4A5568;
        }}
        
        /* Code blocks */
        pre {{
            background: #F7FAFC;
            border: 1px solid #E2E8F0;
            padding: 12px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        
        code {{
            background: #EDF2F7;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
        }}
        
        pre code {{
            background: transparent;
            padding: 0;
        }}
        
        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            page-break-inside: avoid;
        }}
        
        th, td {{
            border: 1px solid #CBD5E0;
            padding: 10px;
            text-align: left;
        }}
        
        th {{
            background: #EDF2F7;
            font-weight: bold;
        }}
        
        tr:nth-child(even) {{
            background: #F7FAFC;
        }}
        
        /* Blockquotes */
        blockquote {{
            border-left: 4px solid #0080FF;
            margin: 20px 0;
            padding: 10px 20px;
            background: #F7FAFC;
            font-style: italic;
        }}
        
        /* Lists */
        ul, ol {{
            margin: 15px 0;
            padding-left: 25px;
        }}
        
        li {{
            margin: 8px 0;
        }}
        
        /* Horizontal rule */
        hr {{
            border: none;
            border-top: 2px solid #CBD5E0;
            margin: 30px 0;
        }}
        
        /* Strong emphasis */
        strong {{
            color: #1A202C;
        }}
        
        /* Links */
        a {{
            color: #0080FF;
            text-decoration: none;
        }}
        
        /* Page breaks for major sections */
        h1 {{
            page-break-before: always;
        }}
    </style>
</head>
<body>
    <!-- Cover Page -->
    <div class="cover">
        <h1>CEO Autónomo</h1>
        <p class="subtitle">El Sistema de Agentes IA que Multiplica tu Productividad por 10x</p>
        <div class="cover-meta">
            <span>Guía Definitiva para Fundadores que Quieren Escalar sin Contratar</span>
            <span>Por: Alfred CamHer</span>
            <span>Abril 2026 | Versión 3.0</span>
            <span>200+ páginas de sistema operativo probado</span>
        </div>
    </div>
    
    <!-- Main Content -->
    {body_html}
</body>
</html>'''
    
    # Write HTML
    html_path = Path('CEO-Autonomo-TEMP-v3.html')
    html_path.write_text(full_html, encoding='utf-8')
    print(f"HTML written: {html_path}")
    
    # Generate PDF
    pdf_path = Path('CEO-Autonomo-Guia-Maestra-v3-FINAL.pdf')
    
    html_doc = HTML(filename=str(html_path))
    html_doc.write_pdf(str(pdf_path))
    
    print(f"\n✅ PDF generated: {pdf_path}")
    file_size = pdf_path.stat().st_size / 1024 / 1024
    print(f"File size: {file_size:.2f} MB")
    
    # Cleanup temp HTML
    html_path.unlink()

if __name__ == '__main__':
    generate_pdf_v2()