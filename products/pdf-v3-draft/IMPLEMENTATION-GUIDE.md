# CEO Autónomo: PDF Design — Implementation Guide v1.0

**Purpose:** Step-by-step instructions to convert Markdown → Professional PDF  
**Date:** April 2, 2026  
**Status:** Complete Technical Specification  

---

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [File Structure](#file-structure)
4. [Markdown Formatting Guide](#markdown-formatting-guide)
5. [Pandoc Commands](#pandoc-commands)
6. [PDF Engine Options](#pdf-engine-options)
7. [Troubleshooting](#troubleshooting)
8. [Quality Assurance Checklist](#quality-assurance-checklist)

---

## System Requirements

### Essential
- **Pandoc** 2.18+ (markdown → PDF converter)
- **Python 3.8+** (for processing scripts)
- **Node.js 14+** (optional, for advanced tooling)

### Optional (Depends on PDF Engine)
- **WeasyPrint:** Python package (recommended for CSS styling)
- **XeLaTeX:** TeX Live installation (for advanced typography)
- **LuaLaTeX:** TeX Live installation (alternative to XeLaTeX)

### Storage
- **Disk space:** ~100MB for full TeX Live install (optional)
- **Output file:** ~5–8MB for 200-page PDF

---

## Installation Steps

### 1. Install Pandoc

**macOS:**
```bash
brew install pandoc
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install pandoc
```

**Windows:**
Download from https://pandoc.org/installing.html

**Verify installation:**
```bash
pandoc --version
```
Expected output: `pandoc 2.18` or higher

---

### 2. Install WeasyPrint (Recommended PDF Engine)

WeasyPrint converts HTML → PDF while respecting CSS, making it perfect for our design system.

**Install via pip:**
```bash
pip3 install --user weasyprint
```

**Verify installation:**
```bash
python3 -c "import weasyprint; print(weasyprint.__version__)"
```

**Note:** First run may take a minute as WeasyPrint downloads system dependencies.

---

### 3. Install Optional TeX Live (For XeLaTeX Option)

Only needed if using XeLaTeX as PDF engine. Skip if using WeasyPrint.

**macOS:**
```bash
brew install --cask mactex
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-latex-extra
```

---

### 4. Clone/Copy Design Files

All design files should be in the same directory:

```
pdf-v3-draft/
├── CEO-Autonomo-Guia-Master.md          (main content)
├── DESIGN-SYSTEM.md                      (reference only)
├── styles-pdf.css                        (essential)
├── pandoc-template.html                  (essential)
├── pandoc-config.yaml                    (essential)
├── SAMPLE-PAGES.md                       (reference only)
└── IMPLEMENTATION-GUIDE.md               (this file)
```

---

## File Structure

### Required Files for PDF Generation

#### 1. **CEO-Autonomo-Guia-Master.md**
The main content file. Must follow markdown conventions (see section below).

```markdown
# Chapter Title
## Section
### Subsection
Body text here.
```

#### 2. **styles-pdf.css**
CSS stylesheet defining all visual styles. Referenced by Pandoc template.

```css
h1 {
  font-family: Inter, sans-serif;
  font-size: 28pt;
  color: #0F172E;
}
```

#### 3. **pandoc-template.html**
Wrapper template that combines Markdown content with CSS.

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles-pdf.css">
</head>
<body>
$body$
</body>
</html>
```

#### 4. **pandoc-config.yaml**
Configuration file specifying all Pandoc options.

```yaml
from: markdown
to: pdf
template: pandoc-template.html
css: styles-pdf.css
```

#### 5. **Any images** (referenced in Markdown)
Save images in the same directory as markdown file.

---

## Markdown Formatting Guide

### Headings

```markdown
# H1 - Chapter Title
## H2 - Section Header
### H3 - Subsection
#### H4 - Minor Heading
```

**Styling:**
- H1: 28pt Navy, bold, page break before
- H2: 20pt Navy, bold
- H3: 16pt Electric Blue, bold
- H4: 13pt Charcoal, bold

---

### Body Text

```markdown
This is a normal paragraph. Write in sentences. 

This is another paragraph. Spacing is automatic (12pt before each paragraph).

You can use **bold** for emphasis and *italic* for secondary emphasis.
```

**Styling:**
- Font: Georgia 11pt
- Color: Charcoal (#2D3748)
- Line height: 1.6
- Text align: Justified

---

### Lists

#### Unordered Lists
```markdown
- First item
- Second item
  - Nested item
  - Another nested
- Third item
```

**Styling:**
- Bullets: Electric Blue circles
- Indent: 20pt
- Spacing: 6pt between items
- Nested bullets: Lighter blue, 8mm additional indent

#### Ordered Lists
```markdown
1. First step
2. Second step
   - Sub-item
   - Another sub-item
3. Third step
```

**Styling:**
- Numbers: Electric Blue, bold
- Indent: 20pt
- Same spacing as unordered lists

---

### Blockquotes (Quotations)

```markdown
> "The most important thing is not the tools, but the system that uses them."
> — Alfred CamHer
```

**Styling:**
- Left border: 4pt Electric Blue
- Background: Light Gray (#F5F5F5)
- Font: Italic Georgia 10pt
- Padding: 12pt all sides

---

### Code Blocks

Use triple backticks with optional language identifier:

````markdown
```python
def create_agent(name, role):
    """Create a new agent with given role."""
    return Agent(name=name, role=role)
```

```yaml
agent:
  id: "content-writer"
  role: "SEO Specialist"
  tasks_per_day: 10
```
````

**Styling:**
- Background: Light Gray (#F5F5F5)
- Font: Courier New 9pt
- Border: 1pt Charcoal
- Padding: 10pt
- Line height: 1.4
- No page break inside

#### Inline Code

```markdown
Use the `create_agent()` function to initialize new agents.
```

**Styling:**
- Font: Courier 9pt
- Background: Light Gray
- Padding: 2pt 4pt

---

### Tables

```markdown
| Agent Type | Cost/month | Tasks/day | Accuracy |
|---|---|---|---|
| Content Writer | $12 | 15–20 | 94% |
| Support Bot | $8 | 50–100 | 87% |
| Code Reviewer | $15 | 20–30 | 96% |
```

**Styling:**
- Header: Electric Blue background, white text, bold
- Rows: Alternating white/light gray
- Borders: 1pt Light Gray between rows
- Cell padding: 8pt
- Alignment: Left text, right numbers

---

### Info Boxes / Callouts

Use blockquote with inline formatting:

```markdown
**KEY INSIGHT:** This is critical information that stands out.
The reader should pause and absorb this.
```

Or with HTML classes (for CSS control):

```markdown
<div class="box-insight">
**Key Insight:** The agent framework reduces operational load by 80%.
</div>
```

**Styling options:**
- `.box-insight` — Navy label, Electric Blue border, Light Gray background
- `.box-warning` — Red label, red border, light red background
- `.box-success` — Green label, green border, light green background

---

### Horizontal Rules (Section Dividers)

```markdown
Some content above.

---

Content below on new section.
```

**Styling:**
- Height: 1pt
- Color: Light Gray (#E5E7EB)
- Margin: 24pt before/after

---

### Links

```markdown
[Click here to learn more](https://example.com)

Or reference-style:
[Learn more][1]

[1]: https://example.com
```

**Styling:**
- Color: Electric Blue (#0080FF)
- Underline: Yes
- Visited: Navy (#0F172E)

---

### Images

```markdown
![Alt text describing the image](./path/to/image.png)

Or with caption:
![Alt text](./path/to/image.png "Figure 1: Chart Title")
```

**Styling:**
- Max width: 100% of text column
- Margin: 12pt top/bottom
- Page break protection: Don't break inside
- Caption: 9pt italic gray, centered below image

---

### Special Markdown Extensions

#### Subscript & Superscript
```markdown
H~2~O (subscript)
x^2^ (superscript)
```

#### Strikethrough
```markdown
~~This text is struck through~~
```

#### Footnotes
```markdown
Here's a footnote reference[^1].

[^1]: And this is the footnote text at the bottom of the page.
```

#### Abbreviations
```markdown
The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
```

---

## Pandoc Commands

### Basic Command

Convert Markdown → PDF using the design system:

```bash
pandoc CEO-Autonomo-Guia-Master.md \
  --template=pandoc-template.html \
  --css=styles-pdf.css \
  --pdf-engine=weasyprint \
  -o CEO-Autonomo-Guia-Maestra-v3.pdf
```

### Using Configuration File (Recommended)

```bash
pandoc CEO-Autonomo-Guia-Master.md \
  --defaults=pandoc-config.yaml
```

This uses all settings from `pandoc-config.yaml`, making commands shorter.

### With Table of Contents

```bash
pandoc CEO-Autonomo-Guia-Master.md \
  --defaults=pandoc-config.yaml \
  --toc \
  --toc-depth=2
```

Generates a table of contents at the beginning. Adjust `--toc-depth`:
- `1`: Only H1 chapters
- `2`: H1 and H2 sections
- `3`: H1, H2, and H3 subsections

### Metadata Override

```bash
pandoc CEO-Autonomo-Guia-Master.md \
  --defaults=pandoc-config.yaml \
  --metadata title="Custom Title" \
  --metadata date="$(date +%B\ %d,\ %Y)"
```

Override metadata variables at runtime.

### Verbose Output (For Debugging)

```bash
pandoc CEO-Autonomo-Guia-Master.md \
  --defaults=pandoc-config.yaml \
  --verbose
```

Shows detailed processing steps. Useful for troubleshooting.

### Multiple Input Files

```bash
pandoc chapter1.md chapter2.md chapter3.md \
  --defaults=pandoc-config.yaml \
  --output=full-guide.pdf
```

Combine multiple markdown files into one PDF.

---

## PDF Engine Options

### 1. WeasyPrint (Recommended)

**Pros:**
- ✅ Excellent CSS support (our design system is CSS-based)
- ✅ Fast processing
- ✅ Lightweight, minimal dependencies
- ✅ Great for digital/print hybrid

**Cons:**
- ❌ Limited advanced typography control

**Command:**
```bash
pandoc input.md \
  --pdf-engine=weasyprint \
  --css=styles-pdf.css \
  -o output.pdf
```

**Install:**
```bash
pip3 install weasyprint
```

---

### 2. XeLaTeX

**Pros:**
- ✅ Professional typography, micro-level control
- ✅ Native Unicode support (Spanish special chars)
- ✅ Excellent for print-ready output

**Cons:**
- ❌ CSS support is limited (requires custom templates)
- ❌ Larger dependency footprint
- ❌ Slower processing

**Command:**
```bash
pandoc input.md \
  --pdf-engine=xelatex \
  -o output.pdf
```

**Install:**
```bash
# macOS
brew install --cask mactex

# Linux
sudo apt-get install texlive-xetex
```

---

### 3. LuaLaTeX

**Pros:**
- ✅ Modern TeX engine, good Unicode
- ✅ Balance between XeLaTeX and simplicity

**Cons:**
- ❌ CSS support limited
- ❌ Requires TeX Live installation

**Command:**
```bash
pandoc input.md \
  --pdf-engine=lualatex \
  -o output.pdf
```

---

### Recommendation

**Use WeasyPrint** for this project because:
1. Our design system is CSS-based
2. No complex typography requirements beyond our CSS
3. Faster, simpler, fewer dependencies
4. Perfect for digital publication and web-ready PDFs

---

## Troubleshooting

### Issue: "pandoc: command not found"

**Solution:**
```bash
# Check if installed
which pandoc

# If not found, install:
brew install pandoc  # macOS
sudo apt-get install pandoc  # Linux
```

---

### Issue: "Cannot find CSS file" or "styles-pdf.css not found"

**Solution:**
Ensure `styles-pdf.css` is in the same directory as the markdown file and config. Check paths in `pandoc-config.yaml`:

```yaml
css: styles-pdf.css  # Must be relative path or full path
template: pandoc-template.html  # Same directory
```

---

### Issue: WeasyPrint not found

**Solution:**
```bash
pip3 install weasyprint

# Or with system breakage (if needed):
pip3 install --user --break-system-packages weasyprint
```

---

### Issue: Spanish characters (á, é, ñ) appear as symbols

**Solution:**
Ensure the markdown file is saved as **UTF-8**. In your editor:
- VS Code: Bottom right → "UTF-8"
- Terminal: `file CEO-Autonomo-Guia-Master.md` should show "UTF-8"

Also ensure Pandoc config has:
```yaml
metadata:
  lang: es
```

---

### Issue: Images don't appear in PDF

**Solution:**
1. Check image format (PNG, JPG, SVG supported)
2. Use relative paths:
   ```markdown
   ![Alt](./images/diagram.png)  # Good
   ![Alt](/absolute/path/to/image.png)  # Avoid
   ```
3. Ensure image exists before running Pandoc
4. Check image file permissions

---

### Issue: Page numbers not showing

**Solution:**
Ensure footer is defined in CSS:
```css
@page {
  @bottom-right {
    content: counter(page);
  }
}
```

And verify PDF engine supports page counter (WeasyPrint does).

---

### Issue: Code blocks overflow the page

**Solution:**
Add to `styles-pdf.css`:
```css
pre {
  overflow-x: auto;
  word-wrap: break-word;
  white-space: pre-wrap;
}
```

Or manually break long code lines in markdown.

---

### Issue: Very slow PDF generation

**Solution:**
1. Check file size: `wc -l CEO-Autonomo-Guia-Master.md`
2. If > 500 lines, consider splitting into chapters
3. Try reducing image resolution
4. Disable unnecessary Pandoc filters

---

## Quality Assurance Checklist

### Before Final PDF

- [ ] **Content**
  - [ ] All chapters present
  - [ ] No placeholder text ([TODO], [FILL IN], etc.)
  - [ ] Spanish language verified (no encoding issues)
  - [ ] Typos checked (spell-checker)
  - [ ] Links verified (all URLs valid)

- [ ] **Formatting**
  - [ ] Headings hierarchy correct (H1 → H2 → H3)
  - [ ] Lists properly indented
  - [ ] Code blocks properly formatted
  - [ ] Tables render correctly
  - [ ] Images appear and are centered

- [ ] **Design**
  - [ ] Colors match spec (Navy, Electric Blue, White, Gray)
  - [ ] Fonts display correctly (Georgia, Inter)
  - [ ] Page numbers visible in footer
  - [ ] Chapter headers on right-facing pages
  - [ ] Margins consistent (20mm top/bottom, 18mm left/right)

- [ ] **Layout**
  - [ ] No orphan/widow lines
  - [ ] Page breaks logical (chapters start on right)
  - [ ] Table of contents matches content
  - [ ] No overflow text outside margins
  - [ ] Whitespace proportional and balanced

- [ ] **PDF Quality**
  - [ ] File size reasonable (~5–8MB)
  - [ ] Resolution adequate (150 DPI for digital)
  - [ ] Searchable text (not scanned image)
  - [ ] Links are clickable
  - [ ] Can be printed without issues

---

### Print Testing (Optional)

If printing professionally:

1. **Print preview:** Open PDF in Adobe Reader → Print preview
2. **Check margins:** All content within safe area
3. **Color check:** Colors appear as designed (CMYK-compatible)
4. **Text clarity:** Minimum 9pt readable at 100%
5. **Image quality:** No pixelation, sharp graphics

---

## Final Output

### Expected Results

**File:** `CEO-Autonomo-Guia-Maestra-v3.pdf`

**Size:** ~6–8 MB (200 pages, 150 DPI)

**Structure:**
- Page 1: Cover (full bleed)
- Page 2: Table of Contents
- Pages 3+: Main content
- Last page: Back matter / colophon

**Verification:**
```bash
# Check file stats
ls -lh CEO-Autonomo-Guia-Maestra-v3.pdf

# Verify PDF is valid
file CEO-Autonomo-Guia-Maestra-v3.pdf
# Should output: "PDF document, version 1.4"

# Check page count
pdfinfo CEO-Autonomo-Guia-Maestra-v3.pdf | grep Pages
```

---

## Automation Script (Optional)

Save as `generate-pdf.sh`:

```bash
#!/bin/bash

# Generate PDF from Markdown using design system

set -e  # Exit on error

SOURCE="CEO-Autonomo-Guia-Master.md"
OUTPUT="CEO-Autonomo-Guia-Maestra-v3.pdf"
CONFIG="pandoc-config.yaml"

echo "🎨 Generating PDF..."
echo "  Source: $SOURCE"
echo "  Output: $OUTPUT"
echo ""

pandoc "$SOURCE" \
  --defaults="$CONFIG" \
  --verbose \
  && echo "" \
  && echo "✅ PDF generated successfully!" \
  && echo "📄 File: $OUTPUT ($(ls -lh $OUTPUT | awk '{print $5}'))" \
  || echo "❌ PDF generation failed!"

exit 0
```

**Usage:**
```bash
chmod +x generate-pdf.sh
./generate-pdf.sh
```

---

**Implementation Guide Complete**  
**Date:** April 2, 2026  
**Status:** Ready for production use  
**Next:** Run Pandoc to generate final PDF
