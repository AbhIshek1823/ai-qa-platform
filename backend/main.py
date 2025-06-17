from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import numpy as np
import json
from datetime import datetime
import logging

app = FastAPI(title="AI QA Mock Backend")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock ML models
class MockLLM:
    def generate_response(self, prompt: str) -> Dict:
        """Simulate LLM response with varying accuracy"""
        response = {
            "text": f"Response to: {prompt}",
            "confidence": np.random.uniform(0.7, 0.95),
            "hallucination_score": np.random.uniform(0, 0.2),
            "timestamp": datetime.now().isoformat()
        }
        return response

mock_llm = MockLLM()

class PromptRequest(BaseModel):
    prompt: str
    context: Dict[str, Any] = {}
    temperature: float = 0.7

class ClassificationRequest(BaseModel):
    text: str
    categories: List[str]

class TestResult(BaseModel):
    prompt: str
    response: Dict
    accuracy: float
    latency: float
    hallucination_score: float

@app.post("/api/v1/llm/generate")
async def generate_llm_response(request: PromptRequest):
    """Generate LLM response with simulated metrics"""
    start_time = datetime.now()
    
    try:
        response = mock_llm.generate_response(request.prompt)
        latency = (datetime.now() - start_time).total_seconds()
        
        return {
            "response": response,
            "metrics": {
                "latency": latency,
                "accuracy": response["confidence"],
                "hallucination": response["hallucination_score"]
            }
        }
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        raise HTTPException(status_code=500, detail="Error generating response")

@app.post("/api/v1/classify")
async def classify_text(request: ClassificationRequest):
    """Simulate text classification with varying accuracy"""
    probabilities = np.random.dirichlet(np.ones(len(request.categories)))
    classification = {
        "category": request.categories[np.argmax(probabilities)],
        "probabilities": dict(zip(request.categories, probabilities.tolist())),
        "confidence": float(np.max(probabilities))
    }
    return classification

@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
