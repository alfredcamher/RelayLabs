#!/usr/bin/env python3
"""Webhook Handlers for CEO Autónomo Guide - Email delivery automation"""

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
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'session_id': session_id,
            'email': email,
            'amount': amount,
            'currency': currency,
            'status': 'completed'
        }
        with open(PURCHASES_LOG, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        logger.info(f"Purchase logged: {email} - ${amount/100:.2f} {currency}")


class EmailDeliverer:
    """Handle email delivery to customers."""
    
    def __init__(self):
        self.provider = os.getenv('EMAIL_PROVIDER', 'none')
        self.from_email = os.getenv('FROM_EMAIL', 'noreply@example.com')
        self.download_url = os.getenv('PRODUCT_URL', 'https://example.com/download')
    
    def send_delivery_email(self, to_email: str, customer_name: str = "") -> bool:
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
        try:
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            message = Mail(
                from_email=self.from_email,
                to_emails=to_email,
                subject="Tu CEO Autónomo Guide está listo",
                html_content=self._email_template(customer_name),
                plain_text_content=self._email_text(customer_name)
            )
            response = sg.send(message)
            logger.info(f"SendGrid: {to_email}")
            return response.status_code == 202
        except Exception as e:
            logger.error(f"SendGrid error: {str(e)}")
            return False
    
    def _send_ses(self, to_email: str, customer_name: str) -> bool:
        try:
            import boto3
            client = boto3.client('ses',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION', 'us-east-1'))
            client.send_email(
                Source=self.from_email,
                Destination={'ToAddresses': [to_email]},
                Message={
                    'Subject': {'Data': "Tu CEO Autónomo Guide está listo"},
                    'Body': {
                        'Text': {'Data': self._email_text(customer_name)},
                        'Html': {'Data': self._email_template(customer_name)}
                    }
                })
            logger.info(f"SES: {to_email}")
            return True
        except Exception as e:
            logger.error(f"SES error: {str(e)}")
            return False
    
    def _send_smtp(self, to_email: str, customer_name: str) -> bool:
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Tu CEO Autónomo Guide está listo"
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg.attach(MIMEText(self._email_text(customer_name), 'plain'))
            msg.attach(MIMEText(self._email_template(customer_name), 'html'))
            server = smtplib.SMTP(os.getenv('SMTP_HOST'), int(os.getenv('SMTP_PORT', 587)))
            server.starttls()
            server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))
            server.sendmail(self.from_email, [to_email], msg.as_string())
            server.quit()
            logger.info(f"SMTP: {to_email}")
            return True
        except Exception as e:
            logger.error(f"SMTP error: {str(e)}")
            return False
    
    def _log_manual_delivery(self, to_email: str, customer_name: str) -> None:
        logger.warning(f"MANUAL DELIVERY: {to_email}")
        logger.warning(f"Download: {self.download_url}")
    
    def _email_template(self, name: str) -> str:
        name = name or "Emprendedor"
        return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Bienvenido</title></head>
<body style="font-family: sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
<div style="text-align: center; padding: 30px 0;">
<h1 style="color: #1a1a1a;">¡Bienvenido!</h1>
<p style="font-size: 18px; color: #666;">Tu CEO Autónomo Guide está listo</p>
</div>
<div style="background: #f8f9fa; border-radius: 8px; padding: 30px;">
<p>Hola {name},</p>
<p>Gracias por unirte al CEO Autónomo.</p>
<ol>
<li><strong>Descarga tu guía:</strong> <a href="{self.download_url}">Descargar aquí</a></li>
<li><strong>Lee en orden:</strong> Sistemas → Métricas → Loops</li>
<li><strong>Toma acción:</strong> ¿Qué implementarás esta semana?</li>
</ol>
</div>
<p style="text-align: center; color: #666; margin-top: 30px;">
¿Problemas? Responde a este email.<br>
<small>Garantía de 30 días.</small>
</p>
</body></html>"""
    
    def _email_text(self, name: str) -> str:
        return f"""¡Bienvenido al CEO Autónomo Guide!

Hola {name or "Emprendedor"},

Gracias por tu compra. Descarga: {self.download_url}

Pasos:
1. Lee la introducción (páginas 1-3)
2. Identifica tu mayor dolor operativo
3. Aplica UN framework esta semana

¿Preguntas? Responde a este email.

Saludos,
CEO Autónomo"""