#!/usr/bin/env python3
"""Send cold outreach emails to high-priority leads"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# Load env
env_path = Path.home() / '.openclaw/workspace/.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ[k] = v

GMAIL_USER = 'alfredcamher@gmail.com'
GMAIL_PASS = os.getenv('GMAIL_APP_PASSWORD', '').replace(' ', '')

# Top 5 leads
LEADS = [
    {
        "name": "Mason Turner",
        "email": "mason.turner@example.com",  # Placeholder - would need real emails
        "type": "Marketing Ops",
        "hook": "Already understands automation"
    },
    {
        "name": "Ryan Hayes",
        "email": "ryan.hayes@example.com",
        "type": "Marketing Automation",
        "hook": "Uses tools, wants to scale"
    },
    {
        "name": "Julian Price",
        "email": "julian.price@example.com",
        "type": "AI Startup",
        "hook": "Builds automation products"
    },
    {
        "name": "Isabella Brown",
        "email": "isabella.brown@example.com",
        "type": "HR Tech SaaS",
        "hook": "Founder with workflow pain"
    },
    {
        "name": "Jackson Hall",
        "email": "jackson.hall@example.com",
        "type": "Sales Enablement",
        "hook": "Team scaling focus"
    }
]

def send_email(to, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = f"Alfred @ Relay Labs <{GMAIL_USER}>"
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Note: These are placeholder emails. Real outreach needs actual email addresses
# For now, log what WOULD be sent
print("=" * 60)
print("COLD OUTREACH - Ready to Send")
print("=" * 60)

for lead in LEADS[:3]:  # Top 3
    print(f"\nTo: {lead['name']} ({lead['email']})")
    print(f"Type: {lead['type']}")
    print(f"Hook: {lead['hook']}")
    print("-" * 40)

print("\n⚠️  NOTE: These are sample emails. Replace with real leads from research.")
print("✅ Gmail configured and ready to send when real emails obtained.")
