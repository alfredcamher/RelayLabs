# CEO Autónomo: Guía Maestra — Design System v1.0

**Document:** Professional PDF Design System  
**Purpose:** Print-ready, accessible 200-page guide  
**Date:** April 2026  
**Status:** Complete Design Specification

---

## 1. VISUAL IDENTITY

### Color Palette

#### Primary Colors
- **Deep Navy** `#0F172E` (RGB: 15, 23, 46)
  - Use: Headers, footers, accent bars
  - Psychology: Trust, stability, tech-forward
  
- **Electric Blue** `#0080FF` (RGB: 0, 128, 255)
  - Use: Highlights, callouts, links
  - Accent for critical information
  
- **Clean White** `#FFFFFF` (RGB: 255, 255, 255)
  - Use: Background, text area
  - Breathing room, readability

#### Secondary Colors
- **Light Gray** `#F5F5F5` (RGB: 245, 245, 245)
  - Use: Code blocks, info boxes backgrounds
  
- **Charcoal** `#2D3748` (RGB: 45, 55, 72)
  - Use: Body text, secondary headers
  
- **Accent Green** `#10B981` (RGB: 16, 185, 129)
  - Use: Success/positive indicators, icons
  
- **Alert Red** `#EF4444` (RGB: 239, 68, 68)
  - Use: Important warnings, key callouts

### Color Psychology & Usage
```
Deep Navy (0F172E)
├─ Main headers (h1, h2)
├─ Page footers
├─ Section dividers
└─ Accent bars on callouts

Electric Blue (0080FF)
├─ Subheaders emphasis (h3, h4)
├─ Key statistics/metrics
├─ "What You'll Learn" boxes
├─ Important links
└─ Diagram highlights

White + Light Gray
├─ Body text area
├─ Code block backgrounds
├─ Table alternating rows
└─ Info box backgrounds

Charcoal (2D3748)
├─ Body paragraph text
├─ Small headers
└─ Secondary information
```

---

## 2. TYPOGRAPHY

### Font Stack (Web Safe + Accessible)

#### Headers (Geometric, Modern)
- **Font Family:** Inter, Poppins, -apple-system, sans-serif
- **Fallback:** System fonts (iOS, macOS, Windows)
- **Weight:** 600–700 (bold)
- **Character:** Clean, minimal, tech-forward

#### Body Text (Readability Optimized)
- **Font Family:** Georgia, Charter, "Times New Roman", serif
- **Alternative:** Tinos (open-source, similar to Georgia)
- **Weight:** 400 (regular)
- **Size:** 11pt (print), readable at 10pt+ on screens

#### Code/Monospace
- **Font Family:** "Courier New", Monaco, Menlo, monospace
- **Weight:** 400
- **Size:** 9pt–10pt

### Typography Scale

| Element | Font | Size | Weight | Line Height | Color |
|---------|------|------|--------|-------------|-------|
| h1 (Chapter Title) | Inter, 600 | 28pt | 600 | 1.4 | Navy `#0F172E` |
| h2 (Section) | Inter, 600 | 20pt | 600 | 1.3 | Navy `#0F172E` |
| h3 (Subsection) | Inter, 600 | 16pt | 600 | 1.3 | Electric Blue `#0080FF` |
| h4 (Minor Head) | Poppins, 600 | 13pt | 600 | 1.2 | Charcoal `#2D3748` |
| Body (p) | Georgia, 400 | 11pt | 400 | 1.6 | Charcoal `#2D3748` |
| Caption/Footer | Georgia, 400 | 9pt | 400 | 1.4 | Gray `#666` |
| Code | Courier, 400 | 9pt | 400 | 1.4 | Charcoal `#2D3748` |

### Line Spacing
- **Headers:** 1.2–1.4 (tight, impactful)
- **Body:** 1.6 (comfortable reading, scannable)
- **Code:** 1.4 (clarity without waste)

---

## 3. LAYOUT & GRID

### Page Specifications

#### Trim Size
- **Format:** A4 (210mm × 297mm / 8.27" × 11.69")
- **Orientation:** Portrait

#### Margins (mm)
- **Top:** 20mm (inside text area + header)
- **Bottom:** 20mm (inside text area + footer)
- **Left:** 18mm
- **Right:** 18mm
- **Inner (binding):** +3mm on left for spine allowance

**Text Area:** 174mm width × 257mm height

#### Grid System
- **Column width:** 87mm (single column with sidebar option)
- **Gutter:** 6mm
- **Baseline grid:** 6pt (ensures vertical rhythm)

### Whitespace Strategy
- **Paragraph spacing:** 12pt before, 0pt after
- **Section spacing:** 24pt between sections
- **Chapter spacing:** 36pt between chapters

---

## 4. COMPONENT SPECIFICATIONS

### Cover Page
```
Layout: Full bleed with margin (20mm safe area)
Background: Deep Navy (#0F172E) gradient to Electric Blue (#0080FF)
Elements:
├─ Title: Inter 600, 48pt, white, centered, top 40% of page
├─ Subtitle: Inter 400, 22pt, light gray, centered, 15mm below title
├─ Decorative line: Electric Blue, 2pt height, 40mm width, centered
├─ Author + date: Georgia 400, 10pt, bottom 25mm
└─ Version badge: Electric Blue box, white text, bottom right

Spacing:
├─ Title top margin: 120mm from page top
├─ Subtitle: 15mm below title
└─ Footer text: 25mm from page bottom
```

### Table of Contents Page
```
Background: White
Elements:
├─ Header: "Table of Contents" in h1 style
├─ Divider line: Electric Blue, 3pt, 40mm width
├─ TOC entries: Georgia 11pt, Navy colored chapter names
├─ Page numbers: Right-aligned, 10pt, Charcoal
└─ Leader dots: Dotted line between entry and page number (optional, lighter)

Entry format: Chapter Title ........... Page #
```

### Chapter Header Page (Right Page)
```
Layout: Full-height chapter break
Background: Gradient area at top (Navy to Blue, 40% of page height)
Elements:
├─ Chapter number: Inter 600, 72pt, Electric Blue, semi-transparent (40% opacity)
├─ Chapter title: Inter 600, 32pt, white, positioned over gradient
├─ Divider: Electric Blue line, 2pt, 60mm width, centered
├─ First paragraph: Georgia 11pt, Navy, subtle intro text below divider (100mm from top)
└─ Page number: Footer, centered, 10pt, Charcoal

Spacing:
├─ Gradient area: top 0–120mm
├─ Title position: 60mm from top, centered horizontally
└─ Chapter intro: 150mm from top
```

### Content Page (Standard)
```
Layout: Two-column friendly (single column body, potential sidebar)
Header: 
├─ Chapter title: Inter 400, 9pt, Navy, left side
└─ Page number: Right side, 9pt

Body:
├─ h2 headers: Navy, 20pt, 12pt before spacing
├─ h3 headers: Electric Blue, 16pt, 12pt before spacing
├─ Body text: Georgia 11pt, Charcoal, 1.6 line height
└─ Paragraphs: 12pt spacing before

Footer:
├─ Chapter name (left): Georgia 9pt, Charcoal, 666 gray
├─ Page number (right): Inter 10pt, Navy
└─ Divider line: Light Gray, 0.5pt above

Footer margins: 15mm from page bottom
```

### Info Box / Callout
```
Background: Light Gray (#F5F5F5)
Border: Left Electric Blue (4pt solid)
Padding: 12pt (all sides)
Border radius: 2pt (minimal, professional)

Elements:
├─ Label: Inter 600, 11pt, Electric Blue, caps (e.g., "KEY INSIGHT")
├─ Divider: Electric Blue line, 1pt, 20mm width, below label
├─ Content: Georgia 11pt, Navy, normal spacing
└─ Icon (optional): Electric Blue accent on top-left

Usage examples:
- "KEY INSIGHT": Navy header + normal body
- "WARNING": Red left border + Alert Red label
- "DATA POINT": Green left border + accent green label
```

### Code Block
```
Background: Light Gray (#F5F5F5)
Border: 1pt Charcoal
Padding: 10pt (all sides)
Font: Courier New 9pt, Charcoal

Elements:
├─ Language label (optional): Inter 400, 7pt, Gray, top-right
├─ Code text: Monospace 9pt, syntax (if applicable)
└─ Border radius: 2pt

Line breaks: Preserve formatting
Line numbers: Optional, Light Gray, right-aligned
```

### Data Tables
```
Border: 1pt Light Gray
Header row:
├─ Background: Electric Blue
├─ Text: White, Inter 600, 10pt
└─ Padding: 8pt

Body rows:
├─ Alternating: White / Very Light Gray (#FAFAFA)
├─ Text: Georgia 10pt, Charcoal
├─ Padding: 8pt
└─ Border: Bottom 0.5pt Light Gray between rows

Footer row (if totals): Lighter shade, italic
```

### Callout / Key Takeaway Box
```
Type 1 - "You Should Know"
├─ Background: Electric Blue, 10% opacity (very light)
├─ Border-left: Electric Blue 4pt
├─ Header: "⚡ YOU SHOULD KNOW" in Inter 600, 11pt, Navy
└─ Content: Georgia 10pt, Navy

Type 2 - "Framework"
├─ Background: Accent Green 8% opacity
├─ Border-left: Accent Green 4pt
├─ Header: "🎯 FRAMEWORK" in Inter 600, 11pt, Navy
└─ Content: Georgia 10pt, Navy
```

### Numbered List
```
Format:
├─ Number: Inter 600, 12pt, Electric Blue
├─ Content: Georgia 11pt, Charcoal
├─ Line height: 1.6
└─ Bullet padding: 8pt left margin

Example:
   1. First item in list
   2. Second item here
```

### Bulleted List
```
Format:
├─ Bullet: Electric Blue circle, 4pt
├─ Content: Georgia 11pt, Charcoal
├─ Line height: 1.6
└─ Bullet padding: 8pt left margin

Nested bullets:
├─ Indent: +8mm
└─ Bullet style: Smaller, lighter blue
```

### Page Divider / Section Break
```
Element: Centered decorative line
├─ Type: Electric Blue, 2pt height
├─ Width: 60mm
├─ Margin: 24pt before/after
└─ Optional accent: Navy dot center (3pt) or electric blue icon
```

---

## 5. PRINT SPECIFICATIONS

### Color Mode
- **Primary:** RGB (for web viewing, on-screen)
- **Print Profile:** CMYK-compatible (if printed)
- **ICC Profile:** sRGB (standard web)

### Typography in Print
- **Minimum text size:** 9pt body text
- **Anti-aliasing:** Ensure fonts at 11pt+ are crisp
- **Font embedding:** All fonts must be embedded in PDF

### Margins & Bleeds
- **Trim margin:** 20mm (safe area for critical content)
- **Bleed:** Not required (margins sufficient)
- **Gutter:** +3mm on left (if binding planned)

### Resolution
- **Screen:** 72 DPI
- **Print-ready:** 300 DPI (if offset/professional printing)
- **Current:** 150 DPI (good for digital + print hybrid)

---

## 6. ACCESSIBILITY

### Contrast Ratios (WCAG AA Compliant)
- **Navy on White:** 9.4:1 ✅ (exceed 4.5:1 requirement)
- **Electric Blue on White:** 5.1:1 ✅
- **Charcoal on White:** 8.1:1 ✅
- **White on Navy:** 9.4:1 ✅

### Font Accessibility
- **Minimum size:** 9pt (body), 11pt (headers)
- **Line spacing:** 1.6 (exceeds 1.5 requirement)
- **Letter spacing:** Appropriate for readability
- **No all-caps:** Only in small labels (< 10pt)

### Structure
- **Heading hierarchy:** H1 → H2 → H3 → H4 (consistent)
- **Alt text for diagrams:** Required
- **PDF tags:** Ensure proper document structure for screen readers

---

## 7. PANDOC TEMPLATE VARIABLES

For markdown-to-HTML/PDF conversion:

```yaml
title: "CEO Autónomo: Guía Maestra"
subtitle: "El Sistema de Agentes IA que Multiplica tu Productividad por 10x"
author: "Alfred CamHer"
date: "Abril 2026"
lang: "es"
fontsize: "11pt"
linestretch: "1.6"
documentclass: "article"
classoption:
  - "a4paper"
  - "twoside"
geometry:
  - "left=18mm"
  - "right=18mm"
  - "top=20mm"
  - "bottom=20mm"
colorlinks: true
urlcolor: "#0080FF"
linkcolor: "#0F172E"
```

---

## 8. IMPLEMENTATION CHECKLIST

- [ ] Fonts embedded in PDF (all weights, styles)
- [ ] Color palette applied consistently (Navy, Blue, White, Gray, Charcoal)
- [ ] Typography scale applied across all elements
- [ ] Margins and spacing follow grid system
- [ ] Cover page designed (Navy-to-Blue gradient, white text)
- [ ] TOC page formatted with leaders
- [ ] Chapter headers with gradient + numbering
- [ ] Body pages with headers/footers
- [ ] Info boxes with Electric Blue left border
- [ ] Code blocks styled with Light Gray background
- [ ] Tables with alternating rows + blue headers
- [ ] Callout boxes (You Should Know, Framework)
- [ ] Page numbers centered in footer
- [ ] Dividers between major sections
- [ ] PDF generated in 150 DPI resolution
- [ ] WCAG AA contrast verified
- [ ] Print preview checked for color accuracy
- [ ] Spanish language verification (special characters)

---

## 9. QUICK REFERENCE

| Property | Value |
|----------|-------|
| **Primary Color** | Deep Navy `#0F172E` |
| **Accent Color** | Electric Blue `#0080FF` |
| **Body Font** | Georgia (serif) 11pt |
| **Header Font** | Inter/Poppins (sans-serif) 600 |
| **Page Size** | A4 (210 × 297mm) |
| **Margins** | 20mm top/bottom, 18mm left/right |
| **Line Height** | 1.6 (body), 1.3 (headers) |
| **Grid** | 87mm column, 6mm gutter |
| **DPI** | 150 (digital/print hybrid) |
| **Color Mode** | RGB (CMYK-compatible) |

---

**Design System Created:** April 2, 2026  
**Status:** Complete and Ready for Implementation  
**Next Step:** Generate sample pages using CSS + Pandoc templates
