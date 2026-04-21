/**
 * Stripe Webhook Handler - Auto-delivery CEO Autónomo PDF
 * Trigger: checkout.session.completed
 */

// Config
const CONFIG = {
  productId: 'prod_UFoP8JQIWob942',
  pdfPath: '/home/alfredcamher/.openclaw/workspace/products/CEO-Autonomo-Guia-Maestra-v3.0.pdf',
  fromEmail: 'hola@relaylabs.com',
};

// Mock handlers for different email providers
async function deliverPDF(customerEmail, customerName) {
  // This would integrate with Resend/SendGrid/Postmark
  // For now, log the delivery
  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    event: 'PDF_DELIVERY',
    customer: customerEmail,
    name: customerName,
    product: CONFIG.productId,
    pdf: CONFIG.pdfPath,
    status: 'queued'
  }));
  
  // Delivery will be implemented via Resend or similar
  return { success: true, queued: true };
}

// Main handler
module.exports = async (payload) => {
  const { data } = payload;
  const session = data.object;
  
  // Verify it's our product
  const lineItems = session.line_items?.data || [];
  const isOurProduct = lineItems.some(item => 
    item.price?.product === CONFIG.productId
  );
  
  if (!isOurProduct) {
    return { status: 'ignored', reason: 'not_our_product' };
  }
  
  // Extract customer info
  const customerEmail = session.customer_email || 
    session.customer?.email || 
    'unknown@customer.com';
  const customerName = session.customer_details?.name || 'Cliente';
  
  // Deliver PDF
  const result = await deliverPDF(customerEmail, customerName);
  
  return {
    status: 'success',
    customer: customerEmail,
    delivered: result.success,
    sessionId: session.id
  };
};

// Log completion
console.log('PDF Auto-delivery handler loaded for product:', CONFIG.productId);
