#!/usr/bin/env python3
"""
CEO Autónomo Guide - PDF Generator (Python Edition)
Generates PDF from markdown without system dependencies

Requires: pip install markdown reportlab beautifulsoup4
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Convert markdown to HTML first
import markdown
from bs4 import BeautifulSoup

# PDF generation
from reportlab.lib.colors import HexColor, black
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class MarkdownToPDF:
    """Convert markdown to PDF directly."""
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.styles = getSampleStyleSheet()
        self.setup_styles()
        
    def setup_styles(self):
        """Configure paragraph styles."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            fontSize=24,
            textColor=HexColor('#1a1a1a'),
            spaceAfter=30,
            alignment=1,  # Center
            fontName='Helvetica-Bold'
        ))
        
        # Heading styles
        self.styles.add(ParagraphStyle(
            name='CustomH1',
            fontSize=18,
            textColor=HexColor('#1a1a1a'),
            spaceAfter=20,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomH2',
            fontSize=14,
            textColor=HexColor('#333333'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomH3',
            fontSize=12,
            textColor=HexColor('#444444'),
            spaceAfter=8,
            spaceBefore=8,
            fontName='Helvetica-Bold'
        ))
        
        # Body text
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            fontSize=10,
            textColor=black,
            spaceAfter=6,
            leading=14,
            fontName='Helvetica'
        ))
        
        # Bullet points
        self.styles.add(ParagraphStyle(
            name='CustomBullet',
            fontSize=10,
            textColor=black,
            spaceAfter=4,
            leftIndent=20,
            bulletIndent=10,
            leading=12,
            fontName='Helvetica'
        ))
        
        # Code blocks
        self.styles.add(ParagraphStyle(
            name='CustomCode',
            fontSize=8,
            textColor=HexColor('#666666'),
            spaceAfter=6,
            leftIndent=20,
            backColor=HexColor('#f5f5f5'),
            fontName='Courier'
        ))
    
    def read_markdown(self):
        """Read markdown file."""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def parse_markdown(self, md_text):
        """Parse markdown to structured elements."""
        # Simple line-by-line parsing
        elements = []
        lines = md_text.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Skip empty lines
            if not line.strip():
                i += 1
                continue
            
            # H1: # Title
            if re.match(r'^#\s', line):
                title = re.sub(r'^#\s*', '', line)
                elements.append(('h1', title))
                i += 1
                continue
            
            # H2: ## Subtitle
            if re.match(r'^##\s', line):
                title = re.sub(r'^##\s*', '', line)
                elements.append(('h2', title))
                i += 1
                continue
            
            # H3: ### Sub-subtitle
            if re.match(r'^###\s', line):
                title = re.sub(r'^###\s*', '', line)
                elements.append(('h3', title))
                i += 1
                continue
            
            # Bullet points: - item or * item
            if re.match(r'^[-*]\s', line):
                items = []
                while i < len(lines) and re.match(r'^[-*]\s', lines[i]):
                    item = re.sub(r'^[-*]\s*', '', lines[i])
                    items.append(item)
                    i += 1
                elements.append(('bullets', items))
                continue
            
            # Code block: ``` or indented
            if line.strip() == '```':
                code_lines = []
                i += 1
                while i < len(lines) and lines[i].strip() != '```':
                    code_lines.append(lines[i])
                    i += 1
                elements.append(('code', '\n'.join(code_lines)))
                i += 1
                continue
            
            # Regular paragraph
            para = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('#') and not lines[i].startswith('-') and not lines[i].startswith('*'):
                para.append(lines[i])
                i += 1
            
            if para:
                elements.append(('p', ' '.join(para)))
            else:
                i += 1
        
        return elements
    
    def build_pdf(self, elements):
        """Build PDF from parsed elements."""
        # Create document
        doc = SimpleDocTemplate(
            self.output_file,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        story = []
        
        # Add title page
        story.append(Paragraph("CEO Autónomo Guide", self.styles['CustomTitle']))
        story.append(Paragraph("Versión 2.1", self.styles['CustomH2']))
        story.append(Spacer(1, 0.5*inch))
        story.append(Paragraph(
            "Deja de trabajar EN tu negocio. Empieza a trabajar SOBRE tu negocio.",
            self.styles['CustomBody']
        ))
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph(
            f"Generado: {datetime.now().strftime('%Y-%m-%d')}",
            self.styles['CustomBody']
        ))
        story.append(PageBreak())
        
        # Process content
        for elem_type, content in elements:
            if elem_type == 'h1':
                story.append(Paragraph(content, self.styles['CustomH1']))
            elif elem_type == 'h2':
                story.append(Paragraph(content, self.styles['CustomH2']))
            elif elem_type == 'h3':
                story.append(Paragraph(content, self.styles['CustomH3']))
            elif elem_type == 'p':
                # Clean up markdown links [text](url) -> text
                content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
                content = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', content)
                content = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', content)
                story.append(Paragraph(content, self.styles['CustomBody']))
            elif elem_type == 'bullets':
                for item in content:
                    story.append(Paragraph(f"• {item}", self.styles['CustomBullet']))
            elif elem_type == 'code':
                for line in content.split('\n')[:5]:  # Limit code display
                    story.append(Paragraph(line, self.styles['CustomCode']))
            
            # Add spacing
            if elem_type != 'h1':  # Don't add space after title (already has spaceAfter)
                story.append(Spacer(1, 0.1*inch))
        
        # Build PDF
        try:
            doc.build(story)
            return True
        except Exception as e:
            print(f"Error building PDF: {e}")
            return False
    
    def generate(self):
        """Main generation workflow."""
        print(f"=== CEO Autónomo PDF Generator ===")
        print(f"Input: {self.input_file}")
        print(f"Output: {self.output_file}")
        
        # Read markdown
        print("Reading markdown...")
        md_text = self.read_markdown()
        
        # Parse
        print("Parsing markdown...")
        elements = self.parse_markdown(md_text)
        print(f"Found {len(elements)} elements")
        
        # Build PDF
        print("Building PDF...")
        success = self.build_pdf(elements)
        
        if success:
            print(f"\n✓ PDF generated successfully!")
            print(f"  File: {self.output_file}")
            try:
                size = os.path.getsize(self.output_file)
                print(f"  Size: {size:,} bytes ({size/1024:.1f} KB)")
            except:
                pass
            return 0
        else:
            print("\n✗ PDF generation failed")
            return 1


def main():
    """Command line interface."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate PDF from markdown')
    parser.add_argument('-i', '--input', default='products/CEO-Autonomo-Guia-COMPLETO-v2.1.md',
                       help='Input markdown file (default: products/CEO-Autonomo-Guia-COMPLETO-v2.1.md)')
    parser.add_argument('-o', '--output', default='products/CEO-Autonomo-Guia-v2.1.pdf',
                       help='Output PDF file (default: products/CEO-Autonomo-Guia-v2.1.pdf)')
    args = parser.parse_args()
    
    # Validate input
    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}")
        print(f"Run from project root: {os.getcwd()}")
        return 1
    
    # Generate
    converter = MarkdownToPDF(args.input, args.output)
    return converter.generate()


if __name__ == '__main__':
    sys.exit(main())
