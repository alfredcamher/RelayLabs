#!/usr/bin/env python3
"""
Webhook Handlers for CEO Autónomo Guide
Version: 1.0.0
Email delivery automation for Stripe webhooks
"""

import os
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PURCHASES_LOG = os.getenv('PURCHASES_LOG', 'purchases.log')


class PurchaseLogger:
    """Log purchases to local file for backup."""
    
    @staticmethod
    def log_purchase(session_id: str, email: str, amount: int, currency: str) -> None:
        """Log successful purchase to file."""
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'session_id': session_id,
            'email': email,
            'amount': amount,
            'currency': currency,
            'status': 'completed'
        }
        
        with open(PURCHASES_LOG, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        logger.info(f"✅ Purchase logged: {email} - ${amount/100:.2f} {currency}")


class EmailDeliverer:
    """Handle email delivery to customers."""
    
    def __init__(self):
        self.provider = os.getenv('EMAIL_PROVIDER', 'none')
        self.from_email = os.getenv('FROM_EMAIL', 'noreply@example.com')
        self.product_name = "CEO Autónomo Guide"
        self.download_url = os.getenv('PRODUCT_URL', 'https://example.com/download')
    
    def send_delivery_email(self, to_email: str, customer_name: str = "") -> bool:
        """Send product delivery email."""
        if self.provider == 'sendgrid':
            return self._send_sendgrid(to_email, customer_name)
        elif self.provider == 'ses':
            return self._send_ses(to_email, customer_name)
        elif self.provider == 'smtp':
            return self._send_smtp(to_email, customer_name)
        else:
            self._log_manual_delivery(to_email, customer_name)
            return True
    
    def _send_sendgrid(self, to_email: str, customer_name: str) -> bool:
        """Send via SendGrid."""
        try:
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            
            message = Mail(
                from_email=self.from_email,
                to_emails=to_email,
                subject=f"Tu {self.product_name} está listo",
                html_content=self._email_template(customer_name),
                plain_text_content=self._email_text(customer_name)
            )
            
            response = sg.send(message)
            logger.info(f"📧 SendGrid: {to_email} (Status: {response.status_code})")
            return response.status_code == 202
        except Exception as e:
            logger.error(f"SendGrid error: {str(e)}")
            return False
    
    def _send_ses(self, to_email: str, customer_name: str) -> bool:
        """Send via AWS SES."""
        try:
            import boto3
            
            client = boto3.client('ses',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION', 'us-east-1')
            )
            
            response = client.send_email(
                Source=self.from_email,
                Destination={'ToAddresses': [to_email]},
                Message={
                    'Subject': {'Data': f"Tu {self.product_name} está listo"},
                    'Body': {
                        'Text': {'Data': self._email_text(customer_name)},
                        'Html': {'Data': self._email_template(customer_name)}
                    }
                }
            )
            
            logger.info(f"📧 SES: {to_email} (ID: {response['MessageId']})")
            return True
        except Exception as e:
            logger.error(f"SES error: {str(e)}")
            return False
    
    def _send_smtp(self, to_email: str, customer_name: str) -> bool:
        """Send via SMTP."""
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"Tu {self.product_name} está listo"
            msg['From'] = self.from_email
            msg['To'] = to_email
            
            msg.attach(MIMEText(self._email_text(customer_name), 'plain'))
            msg.attach(MIMEText(self._email_template(customer_name), 'html'))
            
            server = smtplib.SMTP(os.getenv('SMTP_HOST'), int(os.getenv('SMTP_PORT', 587)))
            server.starttls()
            server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))
            server.sendmail(self.from_email, [to_email], msg.as_string())
            server.quit()
            
            logger.info(f"📧 SMTP: {to_email}")
            return True
        except Exception as e:
            logger.error(f"SMTP error: {str(e)}")
            return False
    
    def _log_manual_delivery(self, to_email: str, customer_name: str) -> None:
        """Log email for manual delivery."""
        logger.warning(f"📋 MANUAL DELIVERY: {to_email}")
        logger.warning(f"   Download: {self.download_url}")
    
    def _email_template(self, name: str) -> str:
        """HTML email template."""
        name = name or "Emprendedor"
        return f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenido</title>
</head>
<body style="font-family: sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
    <div style="text-align: center; padding: 30px 0;">
        <h1 style="color: #1a1a1a;">¡Bienvenido! 🚀</h1>
        <p style="font-size: 18px; color: #666;">Tu CEO Autónomo Guide está listo</p>
    </div>
    
    <div style="background: #f8f9fa; border-radius: 8px; padding: 30px;">
        <p>Hola {name},</p>
        <p>Gracias por unirte al CEO Autónomo. Ya has tomado la decisión más importante: <strong>operar como inversionista, no como empleado.</strong></p>
        
        <p>Esto es lo que viene ahora:</p>
        <ol>
            <li><strong>Descarga tu guía:</strong> El botón de abajo</li>
            <li><strong>Lee en este orden:</strong> Sistemas → Métricas → Loops</li>
            <li><strong>Toma acción:</strong> ¿Qué sistema implementarás esta semana?</li>
        </ol>
        
        <div style="text-align: center; margin: 30px 0;">
            <a href="{self.download_url}" style="background: #635bff; color: white; padding: 15px 40px; text-decoration: none; border-radius: 6px; display: inline-block; font-size: 18px;">Descargar CEO Autónomo Guide</a>
        </div>
    </div>
    
    <div style="margin-top: 30px; padding: 20px; background: #fff3cd; border-radius: 8px; border: 1px solid #ffeaa7;">
        <p><strong>📧 Lo que sigue:</strong></p>
        <p>Recibirás 3 emails en los próximos días con consejos para maximizar tu guía. Responde a cualquiera si tienes preguntas.</p>
    </div>
    
    <p style="margin-top: 30px; text-align: center; color: #666;">
        ¿Problemas? Responde a este email.<br>
        <small>Garantía de 30 días. Reembolso completo si no ves valor.</small>
    </p>
</body>
</html>
'''
    
    def _email_text(self, name: str) -> str:
        """Plain text email."""
        return f'''
¡Bienvenido al CEO Autónomo Guide!

Hola {name or "Emprendedor"},

Gracias por tu compra. Aquí está tu descarga:
