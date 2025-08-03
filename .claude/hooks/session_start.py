#!/usr/bin/env python3
"""
Claude Code Hook: Session Start

Triggered when starting a new session or resuming.
Matchers: "startup", "resume", or "clear".

Usage:
    uv run session_start.py

Input:
    Receives JSON input with session details and startup information.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from common_functions import log_event


def initialize_session_state(session_type: str) -> Dict[str, Any]:
    """
    Initialize session state based on session type.
    
    Args:
        session_type: Type of session start ("startup", "resume", "clear")
        
    Returns:
        Initial session state
    """
    state = {
        "session_id": f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "start_time": datetime.now().isoformat(),
        "session_type": session_type,
        "tools_used": [],
        "files_accessed": [],
        "tasks_completed": 0
    }
    
    return state


def load_previous_session_data(session_type: str) -> Dict[str, Any]:
    """
    Load previous session data if resuming.
    
    Args:
        session_type: Type of session start
        
    Returns:
        Previous session data or empty dict
    """
    if session_type != "resume":
        return {}
    
    # Add logic to load previous session data
    # For example, you might want to:
    # - Load from session cache
    # - Restore user preferences
    # - Recover interrupted tasks
    # - Load project context
    
    backup_dir = Path(__file__).parent.parent / "logs" / "backups"
    if not backup_dir.exists():
        return {}
    
    # Find the most recent backup
    backup_files = list(backup_dir.glob("session_backup_*.json"))
    if not backup_files:
        return {}
    
    latest_backup = max(backup_files, key=lambda p: p.stat().st_mtime)
    
    try:
        with open(latest_backup, "r") as f:
            return json.load(f)
    except Exception:
        return {}


def setup_project_context() -> Dict[str, Any]:
    """
    Set up project-specific context for the session.
    
    Returns:
        Project context information
    """
    context = {}
    
    # Check for project configuration files
    project_files = [
        "package.json",
        "pyproject.toml",
        "Cargo.toml",
        "go.mod",
        "composer.json",
        "pom.xml"
    ]
    
    for file_name in project_files:
        file_path = Path.cwd() / file_name
        if file_path.exists():
            context["project_type"] = file_name
            break
    
    # Check for Claude-specific configuration
    claude_md = Path.cwd() / "CLAUDE.md"
    if claude_md.exists():
        context["has_claude_config"] = True
    
    # Check for git repository
    git_dir = Path.cwd() / ".git"
    if git_dir.exists():
        context["is_git_repo"] = True
    
    return context


def check_system_requirements() -> Dict[str, Any]:
    """
    Check system requirements and tool availability.
    
    Returns:
        System status information
    """
    status = {
        "python_available": True,  # We're running Python
        "uv_available": False,
        "git_available": False
    }
    
    # Check for uv (since we're using it for hook execution)
    import subprocess
    
    try:
        subprocess.run(["uv", "--version"], capture_output=True, check=True)
        status["uv_available"] = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        status["git_available"] = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    return status


def configure_session_settings(session_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Configure session settings based on project and user preferences.
    
    Args:
        session_data: Session data
        
    Returns:
        Session configuration
    """
    settings = {
        "logging_enabled": True,
        "backup_enabled": True,
        "security_checks": True,
        "performance_monitoring": True
    }
    
    # Customize settings based on project context
    project_context = session_data.get("project_context", {})
    
    if project_context.get("is_git_repo"):
        settings["git_integration"] = True
    
    if project_context.get("has_claude_config"):
        settings["claude_config_detected"] = True
    
    return settings


def send_welcome_message(session_type: str, session_data: Dict[str, Any]) -> None:
    """
    Send welcome message or status update.
    
    Args:
        session_type: Type of session start
        session_data: Session data
    """
    # Add welcome message logic here
    # For example, you might want to:
    # - Display project status
    # - Show available commands
    # - Alert about system issues
    # - Display recent activity
    
    welcome_data = {
        "welcome": {
            "session_type": session_type,
            "project_context": session_data.get("project_context", {}),
            "system_status": session_data.get("system_status", {}),
            "message": f"Session started: {session_type}"
        }
    }
    
    log_event("session_start", welcome_data)


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event
        log_event("session_start", input_data)
        
        # Extract session information
        session_type = input_data.get("type", "startup")  # "startup", "resume", or "clear"
        
        # Initialize session state
        session_state = initialize_session_state(session_type)
        
        # Load previous session data if resuming
        if session_type == "resume":
            previous_data = load_previous_session_data(session_type)
            session_state.update(previous_data)
        
        # Set up project context
        project_context = setup_project_context()
        session_state["project_context"] = project_context
        
        # Check system requirements
        system_status = check_system_requirements()
        session_state["system_status"] = system_status
        
        # Configure session settings
        settings = configure_session_settings(session_state)
        session_state["settings"] = settings
        
        # Log session initialization
        log_event("session_start", {
            "session_initialized": session_state
        })
        
        # Send welcome message
        send_welcome_message(session_type, session_state)
        
    except Exception as e:
        # Log error
        error_data = {"error": str(e), "type": "session_start_error"}
        log_event("session_start", error_data)


if __name__ == "__main__":
    main()