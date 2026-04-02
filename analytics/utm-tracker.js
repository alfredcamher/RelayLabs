// UTM Parameter Tracker
// Captures marketing source for conversion attribution

(function() {
    'use strict';
    
    // Parse UTM parameters from URL
    function getUTMParams() {
        const urlParams = new URLSearchParams(window.location.search);
        return {
            source: urlParams.get('utm_source'),
            medium: urlParams.get('utm_medium'),
            campaign: urlParams.get('utm_campaign'),
            content: urlParams.get('utm_content'),
            term: urlParams.get('utm_term')
        };
    }
    
    // Store UTM params in localStorage
    function storeUTM() {
        const params = getUTMParams();
        
        // Only store if UTM params exist
        if (params.source) {
            const data = {
                ...params,
                timestamp: new Date().toISOString(),
                landing_page: window.location.pathname
            };
            localStorage.setItem('utm_data', JSON.stringify(data));
        }
    }
    
    // Get stored UTM params
    function getStoredUTM() {
        try {
            return JSON.parse(localStorage.getItem('utm_data')) || {};
        } catch {
            return {};
        }
    }
    
    // Send to analytics on purchase
    function trackPurchase(price, currency) {
        const utm = getStoredUTM();
        
        // Send to GA4
        if (typeof gtag !== 'undefined') {
            gtag('event', 'purchase', {
                transaction_id: Date.now().toString(),
                value: price,
                currency: currency,
                items: [{
                    item_name: 'CEO Autónomo Guide',
                    item_id: 'ceo-autonomo-guide',
                    price: price,
                    quantity: 1
                }],
                // Include UTM data
                campaign_source: utm.source,
                campaign_medium: utm.medium,
                campaign_name: utm.campaign
            });
        }
        
        // Clear stored UTM after purchase
        localStorage.removeItem('utm_data');
    }
    
    // Initialize on page load
    document.addEventListener('DOMContentLoaded', storeUTM);
    
    // Expose tracking function globally
    window.trackCEOAutonomoPurchase = trackPurchase;
    window.getUTMData = getStoredUTM;
    
})();

// Usage in checkout:
// <script src="/analytics/utm-tracker.js"></script>
// <script>
//   document.getElementById('checkout-form').addEventListener('submit', function() {
//     trackCEOAutonomoPurchase(47.00, 'USD');
//   });
// </script>