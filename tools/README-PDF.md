# PDF Generation Tools

## Option 1: Python Script (Recommended)

### Install Dependencies
```bash
cd tools
pip install -r requirements-pdf.txt
```

### Generate PDF
```bash
python generate-pdf-python.py -i products/CEO-Autonomo-Guia-COMPLETO-v2.1.md -o products/CEO-Autonomo-Guia-v2.1.pdf
```

**Pros:**
- No system dependencies
- Works on any platform
- Customizable styling
- Fast generation

**Cons:**
- Simpler formatting than LaTeX
- Tables may need manual work

---

## Option 2: Pandoc + LaTeX (Higher Quality)

### Install On Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y pandoc texlive-xetex texlive-fonts-recommended
```

### Install On macOS
```bash
brew install pandoc
brew install --cask mactex
```

### Generate PDF
```bash
./tools/generate-pdf.sh
```

**Pros:**
- Professional typography
- Better table formatting
- Native PDF features
- Industry standard

**Cons:**
- Large install (~1GB)
- Complex dependencies
- Slower generation

---

## Option 3: Online Services

Use pandoc online:
1. Go to https://pandoc.org/try/
2. Paste markdown content
3. Export as PDF

Or use cloud tools:
- CloudConvert: https://cloudconvert.com/md-to-pdf
- Markdown to PDF: https://www.markdowntopdf.com/

---

## Option 4: WeasyPrint (Alternative)

### Install
```bash
pip install markdown weasyprint
```

### Generate
```bash
python -c "
import markdown
from weasyprint import HTML

with open('products/CEO-Autonomo-Guia-COMPLETO-v2.1.md') as f:
    html = markdown.markdown(f.read())
    
HTML(string=html).write_pdf('products/CEO-Autonomo-Guia-v2.1.pdf')
"
```

**Note:** WeasyPrint requires additional system libraries on Linux.

---

## Verification

After PDF generation, verify:

```bash
# Check file exists
ls -lh products/CEO-Autonomo-Guia-v2.1.pdf

# Check page count
pdfinfo products/CEO-Autonomo-Guia-v2.1.pdf | grep Pages

# Open sample page
# macOS:
open products/CEO-Autonomo-Guia-v2.1.pdf
# Linux:
xdg-open products/CEO-Autonomo-Guia-v2.1.pdf
```

---

## Recommended Workflow

1. **Edit content** in `products/*.md``
2. **Generate PDF:** `python tools/generate-pdf-python.py`
3. **Validate:** Check page count, formatting
4. **Upload:** Place PDF in CDN/S3 for delivery
5. **Update:** Change PRODUCT_URL in environment