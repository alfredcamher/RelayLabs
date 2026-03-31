#!/usr/bin/env python3
"""FastAPI web interface for Lead Research tool."""
import os
import sys
from pathlib import Path
from datetime import datetime
import json

# Add research module to path
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

from research.brave_client import BraveSearchClient
from research.analyzer import ResearchAnalyzer
from research.formatter import ReportFormatter


app = FastAPI(title="Lead Research API", version="0.1.0")

# Models
class ResearchRequest(BaseModel):
    company_name: str
    format: str = "all"  # md, html, json, all


class ResearchResponse(BaseModel):
    status: str
    company_name: str
    timestamp: str
    download_url: str = None


# Storage for reports
REPORTS_DIR = Path(__file__).parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the web interface."""
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Lead Research Tool</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            padding: 40px;
            max-width: 600px;
            width: 100%;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 0.95em;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }
        input, select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 1em;
            font-family: inherit;
        }
        input:focus, select:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 30px;
        }
        button {
            flex: 1;
            padding: 14px;
            border: none;
            border-radius: 6px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        .btn-primary:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        .status {
            margin-top: 20px;
            padding: 15px;
            border-radius: 6px;
            display: none;
        }
        .status.loading {
            background: #e3f2fd;
            color: #1976d2;
            display: block;
        }
        .status.success {
            background: #e8f5e9;
            color: #388e3c;
            display: block;
        }
        .status.error {
            background: #ffebee;
            color: #d32f2f;
            display: block;
        }
        .loader {
            display: inline-block;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: currentColor;
            margin-right: 8px;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 1; }
        }
        .download-link {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }
        .download-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Lead Research Tool</h1>
        <p class="subtitle">Generate comprehensive B2B research dossiers instantly</p>
        
        <form id="researchForm">
            <div class="form-group">
                <label for="company">Company Name</label>
                <input 
                    type="text" 
                    id="company" 
                    name="company" 
                    placeholder="e.g., Stripe, OpenAI, Figma"
                    required
                >
            </div>
            
            <div class="form-group">
                <label for="format">Output Format</label>
                <select id="format" name="format">
                    <option value="all">All (Markdown + HTML + JSON)</option>
                    <option value="md">Markdown</option>
                    <option value="html">HTML</option>
                    <option value="json">JSON</option>
                </select>
            </div>
            
            <div class="button-group">
                <button type="submit" class="btn-primary" id="submitBtn">
                    Generate Report
                </button>
            </div>
        </form>
        
        <div id="status" class="status"></div>
    </div>
    
    <script>
        document.getElementById('researchForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const company = document.getElementById('company').value;
            const format = document.getElementById('format').value;
            const statusDiv = document.getElementById('status');
            const submitBtn = document.getElementById('submitBtn');
            
            // Show loading
            statusDiv.innerHTML = '<span class="loader"></span> Researching ' + company + '...';
            statusDiv.className = 'status loading';
            submitBtn.disabled = true;
            
            try {
                const response = await fetch('/api/research', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ company_name: company, format: format })
                });
                
                if (!response.ok) {
                    throw new Error('Research failed');
                }
                
                const data = await response.json();
                
                statusDiv.className = 'status success';
                statusDiv.innerHTML = `
                    ✅ Report generated successfully!<br>
                    <a href="${data.download_url}" class="download-link">📥 Download Report</a>
                `;
            } catch (error) {
                statusDiv.className = 'status error';
                statusDiv.innerHTML = '❌ Error: ' + error.message;
            } finally {
                submitBtn.disabled = false;
            }
        });
    </script>
</body>
</html>
    """


@app.post("/api/research", response_model=ResearchResponse)
async def research_endpoint(request: ResearchRequest, background_tasks: BackgroundTasks):
    """API endpoint for research requests."""
    
    try:
        if not request.company_name or len(request.company_name.strip()) == 0:
            raise HTTPException(status_code=400, detail="Company name required")
        
        # Initialize clients
        brave = BraveSearchClient()
        analyzer = ResearchAnalyzer()
        
        # Gather data
        news_results = brave.search_news(request.company_name)
        funding_results = brave.search_funding(request.company_name)
        people_results = brave.search_people(request.company_name)
        job_results = brave.search_jobs(request.company_name)
        
        # Analyze
        research_data = {
            "overview": {
                "founded": "N/A",
                "size": "N/A",
                "location": "N/A",
                "industry": "B2B SaaS"
            },
            "funding": analyzer.analyze_funding(request.company_name, funding_results),
            "people": analyzer.analyze_people(request.company_name, people_results),
            "news": analyzer.analyze_news(request.company_name, news_results),
            "tech_stack": analyzer.infer_tech_stack(request.company_name, job_results),
            "pain_points": analyzer.infer_pain_points(
                request.company_name,
                news_results + people_results
            )
        }
        
        # Format
        formatter = ReportFormatter(request.company_name, research_data)
        
        # Save based on format
        timestamp = datetime.now().isoformat().replace(':', '-').split('.')[0]
        safe_name = request.company_name.lower().replace(' ', '_').replace('.', '')
        
        download_url = None
        
        if request.format in ['md', 'all']:
            md_file = REPORTS_DIR / f"{safe_name}_{timestamp}.md"
            with open(md_file, 'w') as f:
                f.write(formatter.to_markdown())
            download_url = f"/download/{md_file.name}"
        
        if request.format in ['html', 'all']:
            html_file = REPORTS_DIR / f"{safe_name}_{timestamp}.html"
            with open(html_file, 'w') as f:
                f.write(formatter.to_html())
            if not download_url:
                download_url = f"/download/{html_file.name}"
        
        if request.format in ['json', 'all']:
            json_file = REPORTS_DIR / f"{safe_name}_{timestamp}.json"
            formatter.save_json(str(json_file))
            if not download_url:
                download_url = f"/download/{json_file.name}"
        
        return ResearchResponse(
            status="success",
            company_name=request.company_name,
            timestamp=timestamp,
            download_url=download_url
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/download/{filename}")
async def download_report(filename: str):
    """Download a generated report."""
    filepath = REPORTS_DIR / filename
    
    if not filepath.exists():
        raise HTTPException(status_code=404, detail="Report not found")
    
    return FileResponse(filepath, filename=filename)


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
