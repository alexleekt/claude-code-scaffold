#!/usr/bin/env python3
"""
Claude Code Hook: Subagent Stop

Triggered when a Claude Code subagent (Task tool call) has finished responding.

Usage:
    uv run subagent_stop.py

Input:
    Receives JSON input with session details and subagent completion information.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from common_functions import log_event


def analyze_subagent_performance(subagent_data: Dict[str, Any]) -> None:
    """
    Analyze subagent performance and results.
    
    Args:
        subagent_data: Subagent completion data
    """
    # Add subagent analysis logic here
    # For example, you might want to:
    # - Track subagent execution time
    # - Analyze task completion success
    # - Monitor resource usage
    # - Evaluate result quality
    # - Track error patterns
    
    subagent_type = subagent_data.get("type", "unknown")
    task_description = subagent_data.get("task", "")
    execution_time = subagent_data.get("execution_time")
    
    # Log performance metrics
    performance_data = {
        "subagent_performance": {
            "type": subagent_type,
            "task": task_description[:100] if task_description else "",
            "execution_time": execution_time,
            "success": subagent_data.get("success", True)
        }
    }
    log_event("subagent_stop", performance_data)


def track_subagent_usage(subagent_data: Dict[str, Any]) -> None:
    """
    Track subagent usage patterns for optimization.
    
    Args:
        subagent_data: Subagent data
    """
    # Add usage tracking logic here
    # For example, you might want to:
    # - Count subagent invocations by type
    # - Track most common tasks
    # - Monitor success/failure rates
    # - Identify optimization opportunities
    
    pass


def validate_subagent_results(subagent_data: Dict[str, Any]) -> bool:
    """
    Validate subagent results for quality assurance.
    
    Args:
        subagent_data: Subagent completion data
        
    Returns:
        True if results are valid, False otherwise
    """
    # Add result validation logic here
    # For example, you might want to:
    # - Check for expected outputs
    # - Validate against requirements
    # - Ensure security compliance
    # - Verify data integrity
    
    return True


def process_subagent_artifacts(subagent_data: Dict[str, Any]) -> None:
    """
    Process any artifacts created by the subagent.
    
    Args:
        subagent_data: Subagent data containing artifact information
    """
    # Add artifact processing logic here
    # For example, you might want to:
    # - Save generated files
    # - Archive search results
    # - Process analysis outputs
    # - Update documentation
    
    artifacts = subagent_data.get("artifacts", [])
    if artifacts:
        log_event("subagent_stop", {
            "subagent_artifacts": {
                "count": len(artifacts),
                "types": [artifact.get("type") for artifact in artifacts]
            }
        })


def escalate_subagent_issues(subagent_data: Dict[str, Any]) -> None:
    """
    Escalate any issues found in subagent execution.
    
    Args:
        subagent_data: Subagent data
    """
    # Add issue escalation logic here
    # For example, you might want to:
    # - Alert on failures
    # - Report security issues
    # - Flag quality problems
    # - Trigger human review
    
    if not subagent_data.get("success", True):
        error_info = subagent_data.get("error", {})
        log_event("subagent_stop", {
            "subagent_error": {
                "type": subagent_data.get("type", "unknown"),
                "error": error_info,
                "escalated": True
            }
        })


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event
        log_event("subagent_stop", input_data)
        
        # Extract subagent data
        subagent_data = input_data.get("subagent", {})
        
        # Analyze subagent performance
        analyze_subagent_performance(subagent_data)
        
        # Track usage patterns
        track_subagent_usage(subagent_data)
        
        # Validate results
        results_valid = validate_subagent_results(subagent_data)
        
        # Process any artifacts
        process_subagent_artifacts(subagent_data)
        
        # Escalate issues if needed
        if not results_valid or not subagent_data.get("success", True):
            escalate_subagent_issues(subagent_data)
        
    except Exception as e:
        # Log error
        error_data = {"error": str(e), "type": "subagent_stop_error"}
        log_event("subagent_stop", error_data)


if __name__ == "__main__":
    main()