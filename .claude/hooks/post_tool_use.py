#!/usr/bin/env python3
"""
Claude Code Hook: Post Tool Use

Triggered immediately after a tool completes successfully.
Matches tools like Task, Bash, Glob, Grep, Read, Edit, Write, WebFetch.

Usage:
    uv run post_tool_use.py

Input:
    Receives JSON input with session details, tool information, and tool results.
"""

import json
import sys
from typing import Any, Dict

from common_functions import log_event


def analyze_tool_result(tool_name: str, tool_params: Dict[str, Any], result: Any) -> None:
    """
    Analyze tool execution results.
    
    Args:
        tool_name: Name of the tool that was executed
        tool_params: Parameters that were passed to the tool
        result: Result returned by the tool
    """
    # Add result analysis logic here
    # For example, you might want to:
    # - Track file modifications
    # - Monitor command execution
    # - Collect performance metrics
    # - Detect errors or warnings
    # - Log security-relevant operations
    
    pass


def process_file_operations(tool_name: str, tool_params: Dict[str, Any]) -> None:
    """
    Process file-related operations for tracking changes.
    
    Args:
        tool_name: Name of the tool
        tool_params: Tool parameters
    """
    if tool_name in ["Edit", "Write", "MultiEdit"]:
        file_path = tool_params.get("file_path")
        if file_path:
            # Track file modifications
            log_data = {
                "file_operation": {
                    "tool": tool_name,
                    "file": file_path,
                    "action": "modified"
                }
            }
            log_event("post_tool_use", log_data)


def track_command_execution(tool_name: str, tool_params: Dict[str, Any], result: Any) -> None:
    """
    Track command execution for audit purposes.
    
    Args:
        tool_name: Name of the tool
        tool_params: Tool parameters
        result: Command result
    """
    if tool_name == "Bash":
        command = tool_params.get("command", "")
        # Track potentially sensitive commands
        sensitive_commands = ["rm", "mv", "git", "curl", "wget", "ssh"]
        
        if any(cmd in command for cmd in sensitive_commands):
            log_data = {
                "command_execution": {
                    "command": command,
                    "sensitive": True
                }
            }
            log_event("post_tool_use", log_data)


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event
        log_event("post_tool_use", input_data)
        
        # Extract tool information
        tool_name = input_data.get("tool", {}).get("name", "")
        tool_params = input_data.get("tool", {}).get("parameters", {})
        result = input_data.get("result")
        
        # Analyze the tool result
        analyze_tool_result(tool_name, tool_params, result)
        
        # Process specific operation types
        process_file_operations(tool_name, tool_params)
        track_command_execution(tool_name, tool_params, result)
        
    except Exception as e:
        # Log error
        error_data = {"error": str(e), "type": "post_tool_use_error"}
        log_event("post_tool_use", error_data)


if __name__ == "__main__":
    main()