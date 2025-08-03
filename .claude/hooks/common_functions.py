#!/usr/bin/env python3
"""
Common logging utility for Claude Code hooks.

Provides centralized logging functionality with date-based log files.
All hook events are logged to hooks_yyyymmdd.log files.
"""

import fcntl
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def log_event(hook_name: str, event_data: Dict[str, Any], use_separate_files: bool = False) -> None:
    """
    Log a hook event to the date-based log file with file locking.
    
    Args:
        hook_name: Name of the hook generating the event
        event_data: Event data to log
        use_separate_files: If True, create separate log files per hook (reduces contention)
    """
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    # Create date-based log filename
    date_str = datetime.now().strftime("%Y%m%d")
    if use_separate_files:
        # Separate file per hook: hooks_notification_20250802.log
        log_file = log_dir / f"hooks_{hook_name}_{date_str}.log"
    else:
        # Single combined file: hooks_20250802.log
        log_file = log_dir / f"hooks_{date_str}.log"
    
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "hook": hook_name,
        "data": event_data,
        "pid": os.getpid()  # Add process ID for debugging
    }
    
    # Use file locking to prevent race conditions
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            # Acquire exclusive lock
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            try:
                f.write(json.dumps(log_entry) + "\n")
                f.flush()  # Force write to disk
            finally:
                # Lock is automatically released when file is closed
                pass
    except Exception as e:
        # Fallback: write to stderr if logging fails
        import sys
        fallback_entry = {
            "error": "logging_failed",
            "original_hook": hook_name,
            "exception": str(e),
            "timestamp": timestamp
        }
        print(json.dumps(fallback_entry), file=sys.stderr)