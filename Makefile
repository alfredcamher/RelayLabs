# CEO Autónomo - Makefile
# Common tasks for development and deployment

.PHONY: help install test run deploy clean

help: ## Show this help menu
	@echo "CEO Autónomo - Available Commands"
	@echo "=================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies
	cd payment && pip install -r requirements.txt
	@echo "✓ Dependencies installed"

test: ## Run validation suite
	@echo "Running validation..."
	cd testing && ./validation-suite.sh

test-e2e: ## Run end-to-end tests (requires server running)
	@echo "Running E2E tests..."
	cd testing && python e2e-test.py --local

test-full: ## Run all tests
	@echo "Running full test suite..."
	make test && make test-e2e

run: ## Start development server
	@echo "Starting server on http://localhost:4242"
	cd payment && python stripe-checkout-server.py

run-docker: ## Start with Docker Compose
	@echo "Starting with Docker..."
	cd payment && docker-compose up -d
	@echo "Server running on http://localhost:4242"

stop-docker: ## Stop Docker containers
	cd payment && docker-compose down

logs: ## Show server logs
	cd payment && docker-compose logs -f

build: ## Build Docker image
	cd payment && docker build -t ceo-autonomo-payment .

format: ## Format Python code
	cd payment && python -m black *.py

check: ## Run Python syntax checks
	cd payment && python -m py_compile *.py
	@echo "✓ Syntax valid"

clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete
	@echo "✓ Cleaned up"

env: ## Copy environment template
	cd payment && cp .env.example .env
	@echo "✓ Created .env from template"
	@echo "⚠️  Remember to edit .env with your keys"

stripe-test: ## Test Stripe configuration
	@echo "Testing Stripe keys..."
	@cd payment && python -c "import os; from dotenv import load_dotenv; load_dotenv(); import stripe; stripe.api_key = os.getenv('STRIPE_SECRET_KEY'); print('✓ Secret key works' if stripe.api_key else '✗ No key set')" 2>/dev/null || echo "✗ Check your .env file"

status: ## Check project status
	@echo "CEO Autónomo Status"
	@echo "==================="
	@echo "Git branch: $$(git branch --show-current 2>/dev/null || echo 'N/A')"
	@echo "Last commit: $$(git log -1 --format='%h %s' 2>/dev/null || echo 'N/A')"
	@echo "Working directory: $$(git status --porcelain 2>/dev/null | wc -l) uncommitted changes"
	@echo "Python version: $$(python3 --version)"
	@echo "Stripe server: $$(curl -s http://localhost:4242/health 2>/dev/null | grep -o 'ok' || echo 'not running')"

count-lines: ## Count lines of code
	@echo "Code Statistics"
	@echo "==============="
	@find . -name "*.py" -not -path "./venv/*" -exec wc -l {} + | tail -1 | awk '{print "Python lines: " $$1}'
	@find . -name "*.md" -not -path "./venv/*" -exec wc -l {} + | tail -1 | awk '{print "Markdown lines: " $$1}'
	@find . -name "*.sh" -not -path "./venv/*" -exec wc -l {} + | tail -1 | awk '{print "Bash lines: " $$1}'

.DEFAULT_GOAL := help