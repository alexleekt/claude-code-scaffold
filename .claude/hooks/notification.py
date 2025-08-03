#!/usr/bin/env python3
"""
Claude Code Hook: Notification

Triggered when:
- Claude needs permission to use a tool
- Prompt input has been idle for 60+ seconds

Usage:
    uv run notification.py

Input:
    Receives JSON input with session details and notification information.
"""

import json
import sys
from typing import Any, Dict

from common_functions import log_event


def handle_permission_request(notification_data: Dict[str, Any]) -> None:
    """
    Handle tool permission requests.
    
    Args:
        notification_data: Notification data containing permission request details
    """
    # Add permission handling logic here
    # For example, you might want to:
    # - Auto-approve certain tools
    # - Log permission requests for audit
    # - Implement custom permission logic
    # - Send notifications to external systems
    
    pass


def handle_idle_timeout(notification_data: Dict[str, Any]) -> None:
    """
    Handle idle timeout notifications.
    
    Args:
        notification_data: Notification data containing idle timeout details
    """
    # Add idle timeout handling logic here
    # For example, you might want to:
    # - Save session state
    # - Send reminder notifications
    # - Clean up temporary resources
    # - Log session activity patterns
    
    pass


def send_external_notification(notification_type: str, details: Dict[str, Any]) -> None:
    """
    Send notifications to external systems.
    
    Args:
        notification_type: Type of notification
        details: Notification details
    """
    # Add external notification logic here
    # For example, you might want to:
    # - Send to Slack/Discord
    # - Write to monitoring systems
    # - Send email alerts
    # - Push to webhook endpoints
    
    pass


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event
        log_event("notification", input_data)
        
        # Extract notification information
        notification_type = input_data.get("type", "")
        notification_data = input_data.get("data", {})
        
        # Handle different notification types
        if notification_type == "permission_request":
            handle_permission_request(notification_data)
        elif notification_type == "idle_timeout":
            handle_idle_timeout(notification_data)
        
        # Send external notifications if configured
        send_external_notification(notification_type, notification_data)
        
    except Exception as e:
        # Log error
        error_data = {"error": str(e), "type": "notification_error"}
        log_event("notification", error_data)


if __name__ == "__main__":
    main()