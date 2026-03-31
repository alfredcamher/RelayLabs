"""Company research analysis and synthesis."""
from typing import Dict, List, Any
import json


class ResearchAnalyzer:
    """Analyzes search results and synthesizes insights."""
    
    def __init__(self):
        self.company_data = {}
    
    def analyze_funding(self, company_name: str, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract funding information from search results."""
        funding_info = {
            "latest_funding": None,
            "total_raised": None,
            "funding_rounds": [],
            "investors": []
        }
        
        # Parse funding text from descriptions
        for result in results:
            text = f"{result.get('title', '')} {result.get('description', '')}".lower()
            if any(word in text for word in ["series", "funding", "raised", "investment", "million", "billion"]):
                funding_info["funding_rounds"].append({
                    "source": result.get("title", ""),
                    "url": result.get("url", ""),
                    "snippet": result.get("description", "")[:200]
                })
        
        return funding_info
    
    def analyze_news(self, company_name: str, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract recent news."""
        news = []
        for result in results:
            news.append({
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "summary": result.get("description", "")[:300],
                "date_hint": self._extract_date_hint(result.get("description", ""))
            })
        return news[:5]  # Return top 5 news items
    
    def analyze_people(self, company_name: str, results: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Extract key people from search results."""
        people = {
            "ceo": None,
            "founders": [],
            "executives": []
        }
        
        # Simple extraction from titles
        for result in results:
            text = result.get("title", "").lower()
            if "ceo" in text:
                # Extract name before CEO
                parts = result.get("title", "").split("CEO")
                if parts:
                    people["ceo"] = parts[0].strip().replace("|", "").replace("-", "").strip()
            elif "founder" in text or "founder" in result.get("description", "").lower():
                people["founders"].append(result.get("title", "")[:100])
        
        return people
    
    def infer_tech_stack(self, company_name: str, job_results: List[Dict[str, Any]]) -> List[str]:
        """Infer technology stack from job postings."""
        tech_keywords = [
            "python", "javascript", "typescript", "java", "golang", "rust", "c++",
            "react", "vue", "angular", "node.js", "django", "fastapi", "spring",
            "postgresql", "mongodb", "redis", "elasticsearch", "kafka",
            "kubernetes", "docker", "aws", "gcp", "azure",
            "machine learning", "pytorch", "tensorflow", "llm", "ai"
        ]
        
        detected_tech = set()
        for result in job_results:
            text = f"{result.get('title', '')} {result.get('description', '')}".lower()
            for tech in tech_keywords:
                if tech in text:
                    detected_tech.add(tech.upper())
        
        return sorted(list(detected_tech))
    
    def infer_pain_points(self, company_name: str, all_results: List[Dict[str, Any]]) -> List[str]:
        """Infer pain points from news and search context."""
        pain_points = []
        
        # Common B2B pain points to infer
        pain_patterns = {
            "scaling": ["growth", "rapid expansion", "scale", "infrastructure"],
            "retention": ["churn", "retention", "customer success"],
            "competition": ["competitive", "market share", "competition"],
            "talent": ["hiring", "recruitment", "talent acquisition", "team growth"],
            "regulation": ["compliance", "regulatory", "gdpr", "law", "legal"]
        }
        
        all_text = " ".join([
            f"{r.get('title', '')} {r.get('description', '')}"
            for r in all_results
        ]).lower()
        
        for pain_type, keywords in pain_patterns.items():
            if any(kw in all_text for kw in keywords):
                pain_points.append(f"• {pain_type.title()}: {', '.join(keywords[:2])}")
        
        return pain_points[:3]  # Return top 3
    
    def _extract_date_hint(self, text: str) -> str:
        """Try to extract date from text."""
        if "2025" in text:
            return "2025"
        elif "2024" in text:
            return "2024"
        elif "2023" in text:
            return "2023"
        return "Recent"
