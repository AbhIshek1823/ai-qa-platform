import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_llm_generation():
    """Test LLM response generation"""
    response = client.post(
        "/api/v1/llm/generate",
        json={
            "prompt": "Test prompt",
            "context": {},
            "temperature": 0.7
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "metrics" in data
    assert "latency" in data["metrics"]
    assert "accuracy" in data["metrics"]

def test_classification():
    """Test text classification"""
    response = client.post(
        "/api/v1/classify",
        json={
            "text": "Test text",
            "categories": ["category1", "category2", "category3"]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "category" in data
    assert "probabilities" in data
    assert "confidence" in data

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
