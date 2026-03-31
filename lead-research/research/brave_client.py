"""Brave Search API client for research queries."""
import os
import requests
import time
from typing import List, Dict, Any


class BraveSearchClient:
    """Wrapper for Brave Search API."""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("BRAVE_API_KEY")
        if not self.api_key:
            raise ValueError("BRAVE_API_KEY not set in environment")
        self.base_url = "https://api.search.brave.com/res/v1/web/search"
    
    def search(self, query: str, count: int = 10) -> List[Dict[str, Any]]:
        """
        Execute a web search via Brave API.
        
        Args:
            query: Search query string
            count: Number of results to return (max 10)
        
        Returns:
            List of result dicts with 'title', 'url', 'description'
        """
        headers = {
            "Accept": "application/json",
            "X-Subscription-Token": self.api_key
        }
        params = {
            "q": query,
            "count": min(count, 10)
        }
        
        try:
            # Rate limiting: add delay between requests
            time.sleep(0.5)
            
            resp = requests.get(self.base_url, headers=headers, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            
            results = []
            if "web" in data and "results" in data["web"]:
                for item in data["web"]["results"]:
                    results.append({
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "description": item.get("description", "")
                    })
            return results
        except requests.exceptions.RequestException as e:
            print(f"Error querying Brave API: {e}")
            return []
    
    def search_funding(self, company_name: str) -> List[Dict[str, Any]]:
        """Search for funding information."""
        query = f"{company_name} funding rounds investment"
        return self.search(query, count=10)
    
    def search_news(self, company_name: str) -> List[Dict[str, Any]]:
        """Search for recent news about company."""
        query = f"{company_name} news 2024 2025"
        return self.search(query, count=10)
    
    def search_people(self, company_name: str) -> List[Dict[str, Any]]:
        """Search for key people."""
        query = f"{company_name} CEO founder executives leadership"
        return self.search(query, count=10)
    
    def search_jobs(self, company_name: str) -> List[Dict[str, Any]]:
        """Search for job postings to infer tech stack."""
        query = f"{company_name} job postings careers hiring"
        return self.search(query, count=10)
