# AI Quality Assurance Platform

[![Build Status](https://github.com/your-org/ai-qa-platform/workflows/AI%20QA%20CI/CD%20Pipeline/badge.svg)](https://github.com/your-org/ai-qa-platform/actions)
[![Coverage Status](https://coveralls.io/repos/github/your-org/ai-qa-platform/badge.svg)](https://coveralls.io/github/your-org/ai-qa-platform)
[![Defects](https://img.shields.io/badge/defects-0-brightgreen.svg)](defects_log.json)

A comprehensive ML Quality Assurance platform that simulates enterprise-grade AI testing workflows. This project follows Agile practices and provides a complete test automation solution for AI/ML systems.

## Project Structure

```
ai-qa-platform/
├── backend/              # FastAPI ML backend
│   ├── main.py          # Main API endpoints
│   └── tests/           # Backend unit tests
├── frontend/            # React dashboard
│   ├── src/            # Source code
│   └── package.json    # Frontend dependencies
├── qa/                  # Quality Assurance modules
│   ├── python/         # Python test suite
│   │   ├── unit/      # Unit tests
│   │   ├── integration/ # Integration tests
│   │   └── performance/ # Performance tests
│   └── java/           # Java UI test suite
├── synthetic-data/     # Data generation
│   └── generate.py     # Synthetic data generator
├── ci/                 # CI/CD configurations
│   └── ci.yml          # GitHub Actions workflow
└── docs/               # Documentation
```

## Prerequisites

- Python 3.11+
- pip
- Node.js 18+
- npm
- Selenium WebDriver (for UI tests)

## Manual Setup Instructions

1. **Backend Setup**
   ```bash
   # Install dependencies
   cd backend
   pip install -r requirements.txt
   
   # Start the backend server
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   
   The backend will be available at: http://localhost:8000
   API documentation: http://localhost:8000/docs

2. **Frontend Setup**
   ```bash
   # Install dependencies
   cd frontend
   npm install
   
   # Start the development server
   npm start
   ```
   
   The frontend will be available at: http://localhost:3000

3. **Running Tests**
   ```bash
   # Run Python tests
   cd backend
   pytest tests/
   
   # Run UI tests (requires Selenium WebDriver)
   cd qa/java
   mvn test
   ```

## Key Features

1. **Mock ML Backend**
   - FastAPI-based mock ML endpoints
   - Simulated LLM and classification responses
   - Response metrics (accuracy, latency, hallucination)
   - Health check endpoints

2. **Frontend Dashboard**
   - React-based UI for AI testing
   - Real-time response visualization
   - Performance metrics display
   - Interactive prompt testing

3. **Test Automation**
   - Python test suite with:
     - Unit tests for core functionality
     - Integration tests for API endpoints
     - Performance tests for response times
   - Java Selenium UI test suite
   - Synthetic data generation
   - Automated prompt evaluation

4. **Quality Assurance**
   - Prompt consistency testing
   - Safety checks for responses
   - Hallucination detection
   - Performance benchmarking

5. **CI/CD Pipeline**
   - Separate test stages:
     - Unit tests
     - Integration tests
     - Performance tests
   - Automated test reporting
   - Defect tracking
   - Slack notifications

## Prerequisites

- Python 3.9+
- Java 17+
- Node.js 18+
- Docker
- Git

## Setup Instructions

### Traditional Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   # Backend
   cd backend
   pip install -r requirements.txt
   
   # Frontend
   cd frontend
   npm install
   
   # Python QA
   cd qa/python
   pip install -r requirements.txt
   
   # Java QA
   cd qa/java
   mvn install
   ```

3. Run the application:
   ```bash
   # Start backend
   cd backend
   uvicorn main:app --reload
   
   # Start frontend
   cd frontend
   npm run dev
   ```

### Docker Setup (Recommended)

1. Install Docker and Docker Compose
2. Build and run containers:
   ```bash
   # Build and run containers
   docker-compose up --build
   
   # Run in detached mode
   docker-compose up -d --build
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - API Docs: http://localhost:8000/docs
   - API Swagger UI: http://localhost:8000/redoc

4. Stop containers:
   ```bash
   docker-compose down
   ```

5. View logs:
   ```bash
   docker-compose logs -f
   ```

6. Rebuild containers:
   ```bash
   docker-compose up --build --force-recreate
   ```

4. Run tests:
   ```bash
   # Python tests
   cd qa/python
   pytest tests/unit/    # Unit tests
   pytest tests/integration/  # Integration tests
   pytest tests/performance/  # Performance tests
   
   # Java tests
   cd qa/java
   mvn test
   ```

## Test Organization

Tests are organized into three main categories:

1. **Unit Tests**
   - Core functionality verification
   - Response validation
   - Edge case testing

2. **Integration Tests**
   - API endpoint testing
   - End-to-end workflows
   - Response consistency

3. **Performance Tests**
   - Response time benchmarks
   - Load testing
   - Resource utilization

## Defect Management

The project includes a mock Jira integration that:
- Logs failed test cases
- Tracks defect severity
- Maintains defect status
- Generates defect reports

## CI/CD Pipeline

The CI pipeline runs:
1. Unit tests
2. Integration tests
3. Performance tests
4. Java UI tests
5. Defect analysis
6. Report generation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## License

MIT License - see LICENSE file for details
