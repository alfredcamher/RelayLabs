#!/usr/bin/env python3
"""
CEO Autónomo PDF Generator
Converts Markdown to Professional PDF using WeasyPrint
"""

import re
import os
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def markdown_to_html(md_content):
    """Basic Markdown to HTML converter"""
    html = md_content
    
    # Escape HTML special chars
    html = html.replace('&', '&amp;')
    html = html.replace('<', '&lt;')
    html = html.replace('>', '&gt;')
    
    # Headers
    html = re.sub(r'^###### (.+)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold and Italic
    html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Code blocks
    html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code class="language-\1">\2</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Unordered lists
    def process_ul(match):
        items = match.group(1)
        items = re.sub(r'^[\*\-] (.+)$', r'<li>\1</li>', items, flags=re.MULTILINE)
        return f'<ul>{items}</ul>'
    html = re.sub(r'((?:^[\*\-] .+\n?)+)', process_ul, html, flags=re.MULTILINE)
    
    # Ordered lists
    def process_ol(match):
        items = match.group(1)
        items = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', items, flags=re.MULTILINE)
        return f'<ol>{items}</ol>'
    html = re.sub(r'((?:^\d+\. .+\n?)+)', process_ol, html, flags=re.MULTILINE)
    
    # Tables (basic)
    def process_table(match):
        lines = match.group(0).strip().split('\n')
        if len(lines) < 2:
            return match.group(0)
        
        # Header
        header_cells = lines[0].split('|')[1:-1]
        header_html = '<tr>' + ''.join(f'<th>{c.strip()}</th>' for c in header_cells) + '</tr>'
        
        # Separator line - skip
        # Data rows
        data_html = ''
        for line in lines[2:]:
            cells = line.split('|')[1:-1]
            data_html += '<tr>' + ''.join(f'<td>{c.strip()}</td>' for c in cells) + '</tr>'
        
        return f'<table><thead>{header_html}</thead><tbody>{data_html}</tbody></table>'
    
    html = re.sub(r'(\|[^\n]+\|\n)+', process_table, html)
    
    # Horizontal rules
    html = re.sub(r'^---+$', r'<hr>', html, flags=re.MULTILINE)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Paragraphs (simple - wrap remaining text)
    lines = html.split('\n')
    result = []
    in_paragraph = False
    current_para = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current_para:
                result.append('<p>' + ' '.join(current_para) + '</p>')
                current_para = []
            result.append('')
        elif stripped.startswith('<') and stripped.endswith('>'):
            if current_para:
                result.append('<p>' + ' '.join(current_para) + '</p>')
                current_para = []
            result.append(line)
        else:
            current_para.append(stripped)
    
    if current_para:
        result.append('<p>' + ' '.join(current_para) + '</p>')
    
    html = '\n'.join(result)
    
    return html

def generate_pdf():
    """Generate PDF from Markdown"""
    
    # Read markdown content
    md_path = Path('CEO-Autonomo-FINAL-v3.md')
    if not md_path.exists():
        print(f"Error: {md_path} not found")
        return
    
    md_content = md_path.read_text(encoding='utf-8')
    
    # Convert to HTML
    body_html = markdown_to_html(md_content)
    
    # Wrap in template
    full_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Alfred CamHer">
    <meta name="date" content="Abril 2026">
    <title>CEO Autónomo: Guía Maestra v3.0</title>
    <link rel="stylesheet" href="styles-pdf.css" type="text/css">
    <style>
        html {{
            font-size: 12pt;
            width: 8.27in;
        }}
        body {{
            width: 100%;
            margin: 0;
            padding: 0;
            font-family: Georgia, 'Times New Roman', serif;
            line-height: 1.6;
            color: #2D3748;
        }}
    </style>
</head>
<body>
    <div class="cover">
        <div class="chapter-number">✦</div>
        <h1>CEO Autónomo</h1>
        <div class="cover-divider"></div>
        <p class="subtitle">El Sistema de Agentes IA que Multiplica tu Productividad por 10x</p>
        <div class="cover-meta">
            <span class="cover-author">Por: Alfred CamHer</span>
            <span class="cover-date">Abril 2026</span>
            <span class="cover-version">Versión 3.0</span>
        </div>
    </div>
    <div class="page-break-before"></div>
    <div class="main-content">
        {body_html}
    </div>
</body>
</html>'''
    
    # Write HTML for debugging (optional)
    html_path = Path('CEO-Autonomo-FINAL-v3.html')
    html_path.write_text(full_html, encoding='utf-8')
    print(f"HTML generated: {html_path}")
    
    # Generate PDF
    pdf_path = Path('CEO-Autonomo-Guia-Maestra-v3.pdf')
    
    font_config = FontConfiguration()
    html_doc = HTML(string=full_html, base_url=str(Path.cwd()))
    
    # Load CSS
    css_path = Path('styles-pdf.css')
    if css_path.exists():
        css = CSS(filename=str(css_path), font_config=font_config)
        html_doc.write_pdf(str(pdf_path), stylesheets=[css], font_config=font_config)
    else:
        html_doc.write_pdf(str(pdf_path), font_config=font_config)
    
    print(f"PDF generated: {pdf_path}")
    file_size = pdf_path.stat().st_size / 1024 / 1024
    print(f"File size: {file_size:.2f} MB")

if __name__ == '__main__':
    os.chdir('/home/alfredcamher/.openclaw/workspace/products/pdf-v3-draft')
    generate_pdf()