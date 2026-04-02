#!/bin/bash
# generate-pdf.sh
# Script para generar PDF desde markdown

set -e

echo "=== Generando PDF CEO Autónomo v2.1 ==="

# Verificar dependencias
if ! command -v pandoc &> /dev/null; then
    echo "Instalando pandoc..."
    sudo apt-get update
    sudo apt-get install -y pandoc
fi

if ! command -v xelatex &> /dev/null; then
    echo "Instalando LaTeX..."
    sudo apt-get install -y texlive-xetex texlive-fonts-recommended
fi

# Directorio de trabajo
WORKDIR="/home/alfredcamher/.openclaw/workspace"
PRODUCTS="$WORKDIR/products"
OUTPUT="$PRODUCTS/CEO-Autonomo-Guia-v2.1.pdf"

# Archivos en orden
cd "$PRODUCTS"

echo "=== Concatenando archivos ==="

# Crear documento unificado
cat CEO-Autonomo-Guia-v1.md \
    EXPANSION-v2.md \
    Parte-VIII-Implementation.md \
    Parte-IX-Patterns.md \
    Parte-X-Scale.md \
    Parte-XI-Templates.md \
    Parte-XII-Case-Studies.md \
    Parte-XIII-Troubleshooting.md \
    Parte-XIV-Integrations.md \
    Parte-XV-FAQ.md \
    > CEO-Autonomo-Guia-COMPLETO-v2.1-for-pdf.md

echo "=== Generando PDF ==="

# Opción 1: Con xelatex (mejor calidad)
pandoc CEO-Autonomo-Guia-COMPLETO-v2.1-for-pdf.md \
    -o "$OUTPUT" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V mainfont="Liberation Serif" \
    -V sansfont="Liberation Sans" \
    --toc \
    --toc-depth=2 \
    -V colorlinks=true \
    -V linkcolor=blue \
    -V urlcolor=blue \
    -V toccolor=black

# Opción 2: Sin LaTeX (más simple, menos formato)
# pandoc CEO-Autonomo-Guia-COMPLETO-v2.1.md \
#     -o "$OUTPUT" \
#     --template=default

echo "=== PDF Generado ==="
echo "Ubicación: $OUTPUT"
echo "Tamaño: $(du -h "$OUTPUT")"

# Limpiar archivo temporal
rm CEO-Autonomo-Guia-COMPLETO-v2.1-for-pdf.md

echo "=== Proceso completado ==="