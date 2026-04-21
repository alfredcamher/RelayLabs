#!/usr/bin/env python3
"""Send CEO Autónomo PDF via Gmail SMTP"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

# Config
GMAIL_USER = 'alfredcamher@gmail.com'
GMAIL_PASS = os.getenv('GMAIL_APP_PASSWORD', '').replace(' ', '')  # Remove spaces
PDF_PATH = '/home/alfredcamher/.openclaw/workspace/products/CEO-Autonomo-Guia-Maestra-v3.0.pdf'
TO_EMAIL = 'bcamarenaherrera10@gmail.com'

def send_pdf():
    if not GMAIL_PASS:
        print("❌ GMAIL_APP_PASSWORD not set")
        return False
    
    if not Path(PDF_PATH).exists():
        print(f"❌ PDF not found: {PDF_PATH}")
        return False
    
    print(f"📧 Sending from: {GMAIL_USER}")
    print(f"📧 Sending to: {TO_EMAIL}")
    print(f"📎 Attaching: CEO-Autonomo-Guia-Maestra-v3.0.pdf")
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = f"Relay Labs <{GMAIL_USER}>"
    msg['To'] = TO_EMAIL
    msg['Subject'] = '🎯 CEO Autónomo - Tu Guía Maestra v3.0'
    
    # HTML body
    html = '''
    <div style="font-family: 'Space Grotesk', sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px; background: #0a0c0e; color: #f1f2ee;">
        <h2 style="color: #dcf763; text-align: center;">
            🎯 Bienvenido a CEO Autónomo
        </h2>
        
        <div style="background: #16191c; padding: 30px; border-radius: 8px; margin-top: 20px; border: 1px solid #435058;">
            <p style="color: #f1f2ee; font-size: 16px; line-height: 1.6;">
                <strong>Gracias por tu compra.</strong>
            </p>
            
            <p style="color: #bfb7b6; font-size: 14px; line-height: 1.6;">
                Aquí está tu Guía Maestra completa para construir un negocio autónomo 
                con agentes IA que operan 24/7 sin tu intervención constante.
            </p>
            
            <div style="background: rgba(220, 247, 99, 0.1); border: 1px solid #dcf763; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;">
                <h3 style="color: #dcf763; margin: 0 0 10px 0; font-size: 18px;">📚 CEO Autónomo - Guía Maestra v3.0</h3>
                <p style="color: #848c8e; margin: 0; font-size: 13px;">
                    Framework + Stack HKUDS + Templates + Scripts
                </p>
            </div>
            
            <p style="color: #848c8e; font-size: 13px;">
                <strong>Contenido:</strong><br>
                • Parte I-XV: Fundamentos a Escala<br>
                • Stack HKUDS completo (Playwright, LightRAG, CLI-Anything, RAG-Anything)<br>
                • Scripts y templates listos para usar<br>
                • Arquitectura de agentes autónomos 24/7
            </p>
        </div>
        
        <hr style="border: none; border-top: 1px solid #435058; margin: 30px 0;">
        
        <p style="color: #848c8e; font-size: 12px; text-align: center;">
            ¿Preguntas? Responde a este email.<br><br>
            — Alfred @ <strong style="color: #dcf763;">Relay Labs</strong>
        </p>
    </div>
    '''
    msg.attach(MIMEText(html, 'html'))
    
    # Attach PDF
    with open(PDF_PATH, 'rb') as f:
        pdf = MIMEBase('application', 'octet-stream')
        pdf.set_payload(f.read())
        encoders.encode_base64(pdf)
        pdf.add_header('Content-Disposition', 'attachment; filename="CEO-Autonomo-Guia-Maestra-v3.0.pdf"')
        msg.attach(pdf)
    
    # Send via Gmail SMTP
    try:
        print("\n🔗 Connecting to smtp.gmail.com...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        print("🔐 Authenticating...")
        server.login(GMAIL_USER, GMAIL_PASS)
        print("📤 Sending email...")
        server.send_message(msg)
        server.quit()
        
        print("\n" + "="*50)
        print("✅ EMAIL ENVIADO EXITOSAMENTE")
        print("="*50)
        print(f"📧 To: {TO_EMAIL}")
        print(f"📎 PDF: CEO-Autonomo-Guia-Maestra-v3.0.pdf")
        print(f"⏰ Sent: {os.popen('date').read().strip()}")
        print("="*50)
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == '__main__':
    load_env = lambda: None
    env_path = Path.home() / '.openclaw/workspace/.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val
    
    success = send_pdf()
    exit(0 if success else 1)
