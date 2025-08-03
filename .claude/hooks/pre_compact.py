#!/usr/bin/env python3
"""
Claude Code Hook: Pre Compact

Triggered before Claude Code runs a compact operation.
Matchers: "manual" (from /compact) or "auto" (full context window).

Usage:
    uv run pre_compact.py

Input:
    Receives JSON input with session details and compact operation information.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from common_functions import log_event


def backup_session_state(session_data: Dict[str, Any]) -> None:
    """
    Backup current session state before compacting.
    
    Args:
        session_data: Current session data
    """
    # Add backup logic here
    # For example, you might want to:
    # - Save current conversation state
    # - Backup important context
    # - Archive session logs
    # - Store user preferences
    
    backup_dir = Path(__file__).parent.parent / "logs" / "backups"
    backup_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_dir / f"session_backup_{timestamp}.json"
    
    try:
        with open(backup_file, "w") as f:
            json.dump(session_data, f, indent=2)
        
        log_event("pre_compact", {
            "session_backup": {
                "file": str(backup_file),
                "timestamp": timestamp
            }
        })
    except Exception as e:
        log_event("pre_compact", {
            "backup_error": str(e)
        })


def analyze_context_usage(session_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze context usage patterns before compacting.
    
    Args:
        session_data: Session data
        
    Returns:
        Context usage analysis
    """
    analysis = {
        "total_messages": session_data.get("message_count", 0),
        "context_size": session_data.get("context_size", 0),
        "tools_used": session_data.get("tools_used", []),
        "files_accessed": session_data.get("files_accessed", []),
        "compact_trigger": session_data.get("compact_trigger", "unknown")
    }
    
    return analysis


def suggest_compact_strategy(compact_type: str, session_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Suggest optimal compacting strategy based on session analysis.
    
    Args:
        compact_type: Type of compact operation ("manual" or "auto")
        session_data: Session data
        
    Returns:
        Compact strategy recommendations
    """
    strategy = {
        "preserve_recent": True,
        "keep_important_context": True,
        "suggested_retention": "last_10_messages"
    }
    
    # Customize strategy based on compact type
    if compact_type == "auto":
        # More aggressive compacting for auto-triggered compacts
        strategy["suggested_retention"] = "last_5_messages"
    elif compact_type == "manual":
        # More conservative for manual compacts
        strategy["suggested_retention"] = "last_15_messages"
    
    # Analyze session patterns
    analysis = analyze_context_usage(session_data)
    
    # Adjust strategy based on tool usage
    if len(analysis["tools_used"]) > 10:
        strategy["preserve_tool_context"] = True
    
    # Adjust for file operations
    if len(analysis["files_accessed"]) > 5:
        strategy["preserve_file_context"] = True
    
    return strategy


def validate_compact_safety(session_data: Dict[str, Any]) -> bool:
    """
    Validate that it's safe to perform compacting operation.
    
    Args:
        session_data: Session data
        
    Returns:
        True if safe to compact, False to block
    """
    # Add safety validation logic here
    # For example, you might want to:
    # - Check for ongoing operations
    # - Verify critical context preservation
    # - Ensure user consent for important data
    # - Validate backup completion
    
    # Example: Don't compact if there are unsaved changes
    unsaved_changes = session_data.get("unsaved_changes", False)
    if unsaved_changes:
        log_event("pre_compact", {
            "compact_blocked": True,
            "reason": "Unsaved changes detected"
        })
        return False
    
    return True


def prepare_compact_metadata(compact_type: str, session_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Prepare metadata for the compact operation.
    
    Args:
        compact_type: Type of compact operation
        session_data: Session data
        
    Returns:
        Compact metadata
    """
    metadata = {
        "compact_timestamp": datetime.now().isoformat(),
        "compact_type": compact_type,
        "session_id": session_data.get("session_id"),
        "pre_compact_stats": analyze_context_usage(session_data),
        "strategy": suggest_compact_strategy(compact_type, session_data)
    }
    
    return metadata


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event
        log_event("pre_compact", input_data)
        
        # Extract compact information
        compact_type = input_data.get("type", "unknown")  # "manual" or "auto"
        session_data = input_data.get("session", {})
        
        # Validate safety
        if not validate_compact_safety(session_data):
            # Block the compact operation
            sys.exit(1)
        
        # Backup session state
        backup_session_state(session_data)
        
        # Prepare compact metadata
        metadata = prepare_compact_metadata(compact_type, session_data)
        
        # Log compact preparation
        log_event("pre_compact", {
            "compact_preparation": metadata
        })
        
        # Optional: Output compact configuration
        # This could modify how the compact operation works
        # if Claude Code supports it in the future
        
    except Exception as e:
        # Log error but don't block compacting
        error_data = {"error": str(e), "type": "pre_compact_error"}
        log_event("pre_compact", error_data)
        # Exit with 0 to allow compact to continue
        sys.exit(0)


if __name__ == "__main__":
    main()