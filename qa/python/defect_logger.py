import json
from datetime import datetime
from typing import Dict, List
import os
import logging

logger = logging.getLogger(__name__)

class Severity:
    """Severity levels for defects"""
    BLOCKER = "Blocker"
    CRITICAL = "Critical"
    MAJOR = "Major"
    MINOR = "Minor"
    TRIVIAL = "Trivial"

class Status:
    """Status states for defects"""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    FIXED = "Fixed"
    REOPENED = "Reopened"
    CLOSED = "Closed"

class DefectLogger:
    """
    Mock Jira defect logger that logs test failures to a JSON file
    """
    def __init__(self, log_file: str = "defects_log.json"):
        self.log_file = log_file
        self._ensure_log_file_exists()

    def _ensure_log_file_exists(self):
        """Ensure the log file exists and has correct structure"""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)

    def log_defect(self, test_name: str, error: str, confidence: float = None, severity: str = Severity.CRITICAL):
        """
        Log a new defect
        Args:
            test_name: Name of the failed test
            error: Error message or description
            confidence: Confidence score of the prediction
            severity: Severity level of the defect
        """
        defect = {
            "id": str(datetime.now().timestamp()),
            "test_name": test_name,
            "error": error,
            "confidence": confidence,
            "timestamp": datetime.now().isoformat(),
            "severity": severity,
            "status": Status.OPEN,
            "created_by": "AI-QA-System"
        }

        # Read existing defects
        with open(self.log_file, 'r') as f:
            defects = json.load(f)

        # Add new defect
        defects.append(defect)

        # Write back to file
        with open(self.log_file, 'w') as f:
            json.dump(defects, f, indent=2)

        logger.info(f"Logged defect: {test_name} - {severity}")

    def get_open_defects(self) -> List[Dict]:
        """Get all open defects"""
        with open(self.log_file, 'r') as f:
            defects = json.load(f)
        return [d for d in defects if d["status"] == Status.OPEN]

    def update_defect_status(self, defect_id: str, status: str):
        """
        Update the status of a defect
        Args:
            defect_id: ID of the defect to update
            status: New status
        """
        with open(self.log_file, 'r') as f:
            defects = json.load(f)

        for defect in defects:
            if defect["id"] == defect_id:
                defect["status"] = status
                defect["updated_at"] = datetime.now().isoformat()
                break

        with open(self.log_file, 'w') as f:
            json.dump(defects, f, indent=2)

    def get_defect_report(self) -> Dict:
        """Generate a report of all defects"""
        with open(self.log_file, 'r') as f:
            defects = json.load(f)

        report = {
            "total_defects": len(defects),
            "by_severity": {
                Severity.BLOCKER: 0,
                Severity.CRITICAL: 0,
                Severity.MAJOR: 0,
                Severity.MINOR: 0,
                Severity.TRIVIAL: 0
            },
            "by_status": {
                Status.OPEN: 0,
                Status.IN_PROGRESS: 0,
                Status.FIXED: 0,
                Status.REOPENED: 0,
                Status.CLOSED: 0
            }
        }

        for defect in defects:
            report["by_severity"][defect["severity"]] += 1
            report["by_status"][defect["status"]] += 1

        return report
