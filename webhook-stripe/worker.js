/**
 * Cloudflare Worker - CEO Autónomo Delivery
 * Webhook: Stripe payment → Email with PDF attachment
 */

// Configuration (set via Cloudflare dashboard or wrangler secret)
const STRIPE_WEBHOOK_SECRET = "whsec_YOUR_WEBHOOK_SECRET_HERE";
const RESEND_API_KEY = "re_YOUR_RESEND_KEY_HERE";
const FROM_EMAIL = "alfred@relaylabs.com";

// PDF stored as base64 (8.7KB max for KV, inline here for MVP)
// REPLACE THIS with actual base64 of your PDF
const PDF_BASE64 = "PLACEHOLDER_PDF_BASE64";

export default {
  async fetch(request, env) {
    // Only accept POST requests
    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    try {
      // Get Stripe signature from headers
      const signature = request.headers.get('stripe-signature');
      if (!signature) {
        return new Response('No signature', { status: 400 });
      }

      // Get raw body
      const body = await request.text();
      
      // Verify webhook signature
      const isValid = await verifyStripeSignature(body, signature, env.STRIPE_WEBHOOK_SECRET || STRIPE_WEBHOOK_SECRET);
      if (!isValid) {
        return new Response('Invalid signature', { status: 400 });
      }

      // Parse event
      const event = JSON.parse(body);
      
      // Only handle checkout.session.completed
      if (event.type !== 'checkout.session.completed') {
        return new Response('Event type not handled', { status: 200 });
      }

      const session = event.data.object;
      const customerEmail = session.customer_details?.email;
      
      if (!customerEmail) {
        return new Response('No customer email', { status: 400 });
      }

      // Send email with PDF
      const emailSent = await sendEmailWithPDF(
        customerEmail,
        env.RESEND_API_KEY || RESEND_API_KEY,
        env.PDF_BASE64 || PDF_BASE64
      );

      if (emailSent) {
        return new Response('Success - Email sent', { status: 200 });
      } else {
        return new Response('Email failed', { status: 500 });
      }

    } catch (error) {
      console.error('Webhook error:', error);
      return new Response('Internal error', { status: 500 });
    }
  }
};

// Verify Stripe webhook signature
async function verifyStripeSignature(payload, signature, secret) {
  try {
    const encoder = new TextEncoder();
    const data = encoder.encode(payload);
    const sig = encoder.encode(signature);
    const key = await crypto.subtle.importKey(
      'raw',
      encoder.encode(secret),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['sign']
    );
    
    // Stripe signature format: t=timestamp,v1=signature
    const sigParts = signature.split(',');
    const sigHash = sigParts.find(p => p.startsWith('v1='))?.substring(3);
    
    if (!sigHash) return false;
    
    const computed = await crypto.subtle.sign('HMAC', key, data);
    const computedHex = Array.from(new Uint8Array(computed))
      .map(b => b.toString(16).padStart(2, '0'))
      .join('');
    
    return computedHex === sigHash;
  } catch (e) {
    console.error('Signature verification error:', e);
    return false;
  }
}

// Send email with PDF via Resend
async function sendEmailWithPDF(toEmail, apiKey, pdfBase64) {
  try {
    const emailHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8">
        <title>Tu CEO Autónomo está listo</title>
      </head>
      <body style="font-family: 'Space Grotesk', sans-serif; background: #0a0c0e; color: #f1f2ee; padding: 40px;">
        <div style="max-width: 600px; margin: 0 auto; background: #16191c; border: 1px solid #435058; border-radius: 16px; padding: 32px;">
          <h1 style="color: #dcf763; margin-bottom: 24px;">🎯 CEO Autónomo</h1>
          <p>Hola,</p>
          <p>Gracias por tu compra. Tu guía está adjunta.</p>
          <h3 style="color: #dcf763;">Contenido:</h3>
          <ul style="color: #848c8e;">
            <li>PDF Guía (120 páginas)</li>
            <li>Templates Notion</li>
            <li>50+ prompts probados</li>
            <li>Stack HKUDS completo</li>
          </ul>
          <p style="margin-top: 32px; padding: 16px; background: rgba(220, 247, 99, 0.1); border-left: 3px solid #dcf763;">
            <strong style="color: #dcf763;">🎯 Ship or shut up.</strong>
          </p>
          <p style="color: #848c8e; margin-top: 24px;">
            Alfred | Relay Labs<br>
            <a href="mailto:alfredcamher@gmail.com" style="color: #dcf763;">alfredcamher@gmail.com</a>
          </p>
          <p style="color: #848c8e; font-size: 12px; margin-top: 24px;">
            Garantía 30 días. Si no te sirve, devolución completa.
          </p>
        </div>
      </body>
      </html>
    `;

    // Decode base64 and create attachment
    const pdfBytes = Uint8Array.from(atob(pdfBase64), c => c.charCodeAt(0));
    
    // Create multipart form data
    const boundary = '----WebKitFormBoundary' + Math.random().toString(36).substring(2);
    
    const body = [
      `------${boundary}`,
      'Content-Disposition: form-data; name="from"',
      '',
      FROM_EMAIL,
      `------${boundary}`,
      'Content-Disposition: form-data; name="to"',
      '',
      toEmail,
      `------${boundary}`,
      'Content-Disposition: form-data; name="subject"',
      '',
      'Tu CEO Autónomo está listo 🎯',
      `------${boundary}`,
      'Content-Disposition: form-data; name="html"',
      '',
      emailHtml,
      `------${boundary}`,
      'Content-Disposition: form-data; name="attachments"; filename="CEO-Autonomo-Guia-Completo.pdf"',
      'Content-Type: application/pdf',
      '',
      pdfBytes,
      `------${boundary}--`
    ].join('\r\n');

    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': `multipart/form-data; boundary=----${boundary}`
      },
      body: body
    });

    if (response.ok) {
      console.log('Email sent successfully to:', toEmail);
      return true;
    } else {
      const error = await response.text();
      console.error('Resend error:', error);
      return false;
    }
  } catch (error) {
    console.error('Email send error:', error);
    return false;
  }
}