import pytest
import requests
from datetime import datetime
import logging
from defect_logger import DefectLogger

BASE_URL = "http://localhost:8000/api/v1"
logger = logging.getLogger(__name__)
defect_logger = DefectLogger()

def test_classification_endpoint():
    """
    Test the classification endpoint with multiple test cases
    """
    test_cases = [
        {
            "text": "This is a technical article about AI",
            "categories": ["technology", "business", "entertainment"],
            "expected_category": "technology"
        },
        {
            "text": "Financial news about stock market",
            "categories": ["finance", "healthcare", "education"],
            "expected_category": "finance"
        },
        {
            "text": "Healthcare policy update",
            "categories": ["healthcare", "politics", "sports"],
            "expected_category": "healthcare"
        }
    ]

    for case in test_cases:
        response = requests.post(
            f"{BASE_URL}/classify",
            json={
                "text": case["text"],
                "categories": case["categories"]
            }
        )

        assert response.status_code == 200, f"Failed to classify text: {response.text}"
        
        result = response.json()
        
        # Verify category is in the provided list
        assert result["category"] in case["categories"], \
            f"Category {result['category']} not in {case['categories']}"
            
        # Log low confidence predictions
        if result["confidence"] < 0.3:
            defect_logger.log_defect(
                test_name="Low Confidence Classification",
                error=f"Low confidence prediction: {result['confidence']}",
                severity="Medium"
            )

def test_classification_with_invalid_input():
    """
    Test classification with invalid input
    """
    invalid_cases = [
        {"text": "", "categories": ["test"]},  # Empty text
        {"text": "test", "categories": []},    # Empty categories
        {"text": "test", "categories": None},  # None categories
    ]

    for case in invalid_cases:
        response = requests.post(
            f"{BASE_URL}/classify",
            json=case
        )
        
        assert response.status_code == 400, f"Expected 400 for invalid input: {case}"

if __name__ == "__main__":
    pytest.main(["-v", "test_classify.py"])
