#!/usr/bin/env python3
"""
Claude Code Hook: Pre Tool Use

Triggered after Claude creates tool parameters and before processing the tool call.
Matches tools like Task, Bash, Glob, Grep, Read, Edit, Write, WebFetch.

Usage:
    uv run pre_tool_use.py

Input:
    Receives JSON input with session details and tool information.
"""

import json
import sys
from typing import Any, Dict

from common_functions import log_event


def validate_tool_use(tool_name: str, tool_params: Dict[str, Any]) -> bool:
    """
    Validate tool usage before execution.
    
    Args:
        tool_name: Name of the tool being called
        tool_params: Parameters being passed to the tool
        
    Returns:
        True if tool use should proceed, False to block
    """
    # Add custom validation logic here
    # For example, you might want to:
    # - Block certain file operations
    # - Validate file paths
    # - Check permissions
    # - Rate limit certain tools
    
    return True


def enhance_tool_params(tool_name: str, tool_params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Enhance or modify tool parameters before execution.
    
    Args:
        tool_name: Name of the tool being called
        tool_params: Original parameters
        
    Returns:
        Modified parameters (or original if no changes needed)
    """
    # Add parameter enhancement logic here
    # For example, you might want to:
    # - Add default parameters
    # - Modify file paths
    # - Add safety checks
    
    return tool_params


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event
        log_event("pre_tool_use", input_data)
        
        # Extract tool information
        tool_name = input_data.get("tool", {}).get("name", "")
        tool_params = input_data.get("tool", {}).get("parameters", {})
        
        # Validate tool use
        if not validate_tool_use(tool_name, tool_params):
            # Block the tool use by exiting with non-zero status
            sys.exit(1)
        
        # Enhance parameters if needed
        enhanced_params = enhance_tool_params(tool_name, tool_params)
        
        # If parameters were modified, output the updated tool call
        if enhanced_params != tool_params:
            output = {
                "tool": {
                    "name": tool_name,
                    "parameters": enhanced_params
                }
            }
            print(json.dumps(output))
        
    except Exception as e:
        # Log error but don't block execution
        error_data = {"error": str(e), "type": "pre_tool_use_error"}
        log_event("pre_tool_use", error_data)
        # Exit with 0 to allow tool execution to continue
        sys.exit(0)


if __name__ == "__main__":
    main()