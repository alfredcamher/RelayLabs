#!/usr/bin/env python3
"""
CEO Autónomo - Metrics Tracker
Tracks key business metrics from purchases.log and Stripe
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path


class MetricsTracker:
    """Track business metrics from logs."""
    
    def __init__(self, log_file='payment/purchases.log'):
        self.log_file = log_file
        self.purchases = []
        self.load_purchases()
    
    def load_purchases(self):
        """Load purchases from log file."""
        if not os.path.exists(self.log_file):
            return
        
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            purchase = json.loads(line)
                            self.purchases.append(purchase)
                        except json.JSONDecodeError:
                            continue
        except Exception as e:
            print(f"Error loading purchases: {e}")
    
    def get_metrics(self, days=7):
        """Get metrics for last N days."""
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        
        recent = [p for p in self.purchases if p.get('timestamp', '') > cutoff]
        
        return {
            'revenue': sum(p.get('amount', 0) / 100 for p in recent),
            'purchases': len(recent),
            'avg_value': sum(p.get('amount', 0) / 100 for p in recent) / len(recent) if recent else 0,
            'unique_customers': len(set(p.get('email', '') for p in recent))
        }
    
    def get_daily_breakdown(self, days=7):
        """Get daily breakdown."""
        cutoff = datetime.now() - timedelta(days=days)
        daily = {}
        
        for p in self.purchases:
            ts = datetime.fromisoformat(p.get('timestamp', '2000-01-01'))
            if ts < cutoff:
                continue
            
            date_str = ts.strftime('%Y-%m-%d')
            if date_str not in daily:
                daily[date_str] = {'revenue': 0, 'count': 0}
            
            daily[date_str]['revenue'] += p.get('amount', 0) / 100
            daily[date_str]['count'] += 1
        
        return daily
    
    def get_conversion_funnel(self,