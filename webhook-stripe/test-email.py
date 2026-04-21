#!/usr/bin/env python3
"""
Test Resend email delivery
Sends CEO Autónomo PDF to test email
"""

import os
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# Load environment
env_path = Path.home() / '.openclaw/workspace/.env'
def load_env():
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val

load_env()

# Config
API_KEY = os.getenv('RESEND_API_KEY')
# Must use Resend-provided domain until custom domain is verified
# FROM_EMAIL = os.getenv('RESEND_FROM', 'alfredcamher@gmail.com')  # ❌ Can't use Gmail
FROM_EMAIL = 'onboarding@resend.dev'  # ✅ Resend default domain
PDF_PATH = '/home/alfredcamher/.openclaw/workspace/products/CEO-Autonomo-Guia-Maestra-v3.0.pdf'

# Test recipient
TEST_EMAIL = 'bcamarenaherrera10@gmail.com'

def send_test_email():
    """Send test email with PDF"""
    
    if not API_KEY:
        print("❌ RESEND_API_KEY not found in .env")
        return False
    
    if not Path(PDF_PATH).exists():
        print(f"❌ PDF not found: {PDF_PATH}")
        return False
    
    print(f"📧 Sending test email to: {TEST_EMAIL}")
    print(f"📎 Attaching: CEO-Autonomo-Guia-Maestra-v3.0.pdf")
    
    # Read PDF
    with open(PDF_PATH, 'rb') as f:
        pdf_content = f.read()
    
    pdf_b64 = base64.b64encode(pdf_content).decode('utf-8')
    
    # Build email
    payload = {
        'from': f"Relay Labs <{FROM_EMAIL}>",
        'to': [TEST_EMAIL],
        'subject': '🎉 Test: Tu CEO Autónomo - Acceso Inmediato',
        'html': '''
        <div style="font-family: 'Space Grotesk', sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
            <h2 style="color: #dcf763; background: #0a0c0e; padding: 20px; border-radius: 8px;">
                🎯 Bienvenido a CEO Autónomo
            </h2>
            
            <div style="background: #16191c; padding: 30px; border-radius: 8px; margin-top: 20px; border: 1px solid #435058;">
                <p style="color: #f1f2ee; font-size: 16px; line-height: 1.6;">
                    <strong>Esto es una prueba de entrega automática.</strong>
                </p>
                
                <p style="color: #bfb7b6; font-size: 14px; line-height: 1.6;">
                    Tu compra está confirmada. Aquí está tu guía completa para construir 
                    un negocio autónomo con agentes IA que operan 24/7.
                </p>
                
                <div style="background: rgba(220, 247, 99, 0.1); border: 1px solid #dcf763; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <h3 style="color: #dcf763; margin: 0 0 10px 0;">📚 CEO Autónomo - Guía Maestra v3.0</h3>
                    <p style="color: #848c8e; margin: 0; font-size: 13px;">
                        Incluye: Framework completo + Stack HKUDS + Templates + Scripts
                    </p>
                </div>
                
                <p style="color: #848c8e; font-size: 13px;">
                    PDF adjunto. Si no lo ves, revisa tu carpeta de spam.
                </p>
            </div>
            
            <hr style="border: none; border-top: 1px solid #435058; margin: 30px 0;">
            
            <p style="color: #848c8e; font-size: 12px;">
                ¿Preguntas? Responde a este email.<br>
                — Alfred @ <strong style="color: #dcf763;">Relay Labs</strong>
            </p>
        </div>
        ''',
        'attachments': [{
            'filename': 'CEO-Autonomo-Guia-Maestra-v3.0.pdf',
            'content': pdf_b64
        }]
    }
    
    # Send via Resend
    req = urllib.request.Request(
        'https://api.resend.com/emails',
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Authorization': f"Bearer {API_KEY}",
            'Content-Type': 'application/json'
        },
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"\n✅ Email enviado exitosamente!")
            print(f"   Email ID: {result.get('id')}")
            print(f"   Para: {TEST_EMAIL}")
            print(f"   Desde: {FROM_EMAIL}")
            return True
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        try:
            error_json = json.loads(error_body)
            print(f"\n❌ Error de Resend:")
            print(f"   Status: {e.code}")
            print(f"   Mensaje: {error_json.get('message', error_body)}")
        except:
            print(f"\n❌ Error HTTP {e.code}: {error_body}")
        return False
        
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("Relay Labs - Test de Email Auto-Delivery")
    print("=" * 50)
    print()
    
    success = send_test_email()
    
    print()
    print("=" * 50)
    if success:
        print("✅ Test completado - Sistema listo")
    else:
        print("❌ Test falló - Revisar configuración")
    print("=" * 50)
