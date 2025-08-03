#!/usr/bin/env python3
"""
Claude Code Hook: Stop

Triggered when the main Claude Code agent has finished responding.
Excludes user interruptions.

Usage:
    uv run stop.py

Input:
    Receives JSON input with session details and response completion information.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from common_functions import log_event


def analyze_session_completion(session_data: Dict[str, Any]) -> None:
    """
    Analyze the completed session for insights and metrics.
    
    Args:
        session_data: Session completion data
    """
    # Add session analysis logic here
    # For example, you might want to:
    # - Calculate response time metrics
    # - Count tools used
    # - Analyze task completion
    # - Track user satisfaction patterns
    # - Generate session summaries
    
    pass


def cleanup_session_resources() -> None:
    """Clean up any temporary resources from the session."""
    # Add cleanup logic here
    # For example, you might want to:
    # - Clean temporary files
    # - Close database connections
    # - Save session state
    # - Archive logs
    # - Reset rate limiters
    
    pass


def generate_session_summary(session_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a summary of the session for reporting.
    
    Args:
        session_data: Session data
        
    Returns:
        Session summary dictionary
    """
    summary = {
        "session_end": datetime.now().isoformat(),
        "tools_used": session_data.get("tools_used", []),
        "duration": session_data.get("duration"),
        "tasks_completed": session_data.get("tasks_completed", 0),
        "errors_encountered": session_data.get("errors", [])
    }
    
    return summary


def save_session_metrics(session_data: Dict[str, Any]) -> None:
    """
    Save session metrics for analytics.
    
    Args:
        session_data: Session data to save
    """
    # Add metrics saving logic here
    # For example, you might want to:
    # - Save to analytics database
    # - Send to monitoring service
    # - Update usage statistics
    # - Generate reports
    
    summary = generate_session_summary(session_data)
    log_event("stop", {
        "session_summary": summary,
        "type": "session_metrics"
    })


def notify_session_completion(session_data: Dict[str, Any]) -> None:
    """
    Send notifications about session completion.
    
    Args:
        session_data: Session completion data
    """
    # Add notification logic here
    # For example, you might want to:
    # - Send completion notifications
    # - Update external systems
    # - Trigger follow-up actions
    # - Save session reports
    
    pass


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event
        log_event("stop", input_data)
        
        # Extract session data
        session_data = input_data.get("session", {})
        
        # Analyze the completed session
        analyze_session_completion(session_data)
        
        # Save session metrics
        save_session_metrics(session_data)
        
        # Clean up resources
        cleanup_session_resources()
        
        # Send completion notifications
        notify_session_completion(session_data)
        
    except Exception as e:
        # Log error
        error_data = {"error": str(e), "type": "stop_error"}
        log_event("stop", error_data)


if __name__ == "__main__":
    main()