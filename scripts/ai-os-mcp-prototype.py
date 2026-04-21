#!/usr/bin/env python3
"""
AI OS - MCP Server Prototype
Model Context Protocol server for agent coordination
"""

import json
import os
from datetime import datetime
from pathlib import Path

class MCPServer:
    """MCP Server for AI OS - provides context to agents"""
    
    def __init__(self, company_id="relay-labs"):
        self.company_id = company_id
        self.context_dir = Path(f"~/.openclaw/mcp/{company_id}").expanduser()
        self.context_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize knowledge stores
        self.knowledge = {
            "company": {
                "name": "Relay Labs",
                "mission": "Build autonomous AI systems for businesses",
                "products": ["CEO Autónomo", "AI OS"],
                "tone": "Direct, anti-bullshit, execution-focused"
            },
            "agents": {},
            "skills": self._load_skills(),
            "memory": self._load_memory()
        }
    
    def _load_skills(self):
        """Load available skills for agents"""
        skills_path = Path("/usr/lib/node_modules/openclaw/skills")
        skills = {}
        if skills_path.exists():
            for skill_dir in skills_path.iterdir():
                if skill_dir.is_dir():
                    skill_md = skill_dir / "SKILL.md"
                    if skill_md.exists():
                        with open(skill_md) as f:
                            content = f.read()
                            # Parse frontmatter
                            if "---" in content:
                                skills[skill_dir.name] = {
                                    "path": str(skill_dir),
                                    "available": True
                                }
        return skills
    
    def _load_memory(self):
        """Load company memory"""
        memory_file = self.context_dir / "company_memory.json"
        if memory_file.exists():
            with open(memory_file) as f:
                return json.load(f)
        return {
            "created": datetime.now().isoformat(),
            "milestones": [],
            "patterns": [],
            "anti_patterns": []
        }
    
    def query(self, agent_id, query_type, params=None):
        """Agent queries MCP server for context"""
        params = params or {}
        
        if query_type == "skill":
            # Agent asks which skill to use
            task = params.get("task", "")
            return self._recommend_skill(task)
        
        elif query_type == "company":
            # Agent asks for company context
            return self.knowledge["company"]
        
        elif query_type == "memory":
            # Agent asks for historical context
            topic = params.get("topic", "")
            return self._search_memory(topic)
        
        elif query_type == "agent_status":
            # Check other agent status
            return self.knowledge["agents"]
        
        return {"error": "Unknown query type"}
    
    def _recommend_skill(self, task):
        """Recommend skill based on task"""
        task_lower = task.lower()
        
        skill_mapping = {
            "code": ["coding-agent", "github"],
            "write": ["coding-agent"],
            "tweet": ["browser"],
            "post": ["browser"],
            "notify": ["discord", "slack"],
            "kanban": ["trello"],
            "visual": ["canvas"],
            "health": ["healthcheck"],
            "search": ["web_search"]
        }
        
        for keyword, skills in skill_mapping.items():
            if keyword in task_lower:
                available = [s for s in skills if s in self.knowledge["skills"]]
                if available:
                    return {
                        "recommended": available[0],
                        "alternatives": available[1:] if len(available) > 1 else [],
                        "reason": f"Task '{task}' requires {keyword} capability"
                    }
        
        return {
            "recommended": "web_search",
            "reason": "Research first, then execute"
        }
    
    def _search_memory(self, topic):
        """Search company memory"""
        results = []
        for pattern in self.knowledge["memory"].get("patterns", []):
            if topic.lower() in pattern.get("tags", []):
                results.append(pattern)
        return results[:5]  # Top 5
    
    def update_agent_status(self, agent_id, status, task=None):
        """Update agent status"""
        self.knowledge["agents"][agent_id] = {
            "status": status,  # running, completed, failed
            "task": task,
            "last_update": datetime.now().isoformat()
        }
        self._save_memory()
    
    def _save_memory(self):
        """Persist memory to disk"""
        memory_file = self.context_dir / "company_memory.json"
        with open(memory_file, 'w') as f:
            json.dump(self.knowledge["memory"], f, indent=2)
    
    def log_pattern(self, pattern_type, description, tags=None):
        """Log learned pattern"""
        self.knowledge["memory"]["milestones"].append({
            "timestamp": datetime.now().isoformat(),
            "type": pattern_type,
            "description": description,
            "tags": tags or []
        })
        self._save_memory()

# Demo
if __name__ == "__main__":
    mcp = MCPServer()
    
    # Test query
    print("MCP Server Status: ONLINE")
    print(f"Skills available: {len(mcp.knowledge['skills'])}")
    print()
    
    # Simulate agent asking for skill
    result = mcp.query("agent-1", "skill", {"task": "build landing page"})
    print(f"Skill recommendation: {result}")
    
    # Company context
    result = mcp.query("agent-1", "company")
    print(f"Company context: {result['name']}")
    
    print("\nMCP Server ready for agent coordination")
