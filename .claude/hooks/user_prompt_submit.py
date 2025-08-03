#!/usr/bin/env python3
"""
Claude Code Hook: User Prompt Submit

Triggered when the user submits a prompt, before Claude processes it.
Allows context addition, prompt validation, or blocking.

Usage:
    uv run user_prompt_submit.py

Input:
    Receives JSON input with session details and user prompt.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from common_functions import log_event


def validate_prompt(prompt: str) -> bool:
    """
    Validate user prompt for security or policy compliance.
    
    Args:
        prompt: The user's prompt text
        
    Returns:
        True if prompt is valid, False to block
    """
    # Add prompt validation logic here
    # For example, you might want to:
    # - Check for sensitive information
    # - Validate against company policies
    # - Block certain types of requests
    # - Rate limit based on content
    
    # Example: Block prompts that might contain API keys
    sensitive_patterns = [
        "api_key",
        "secret_key",
        "password",
        "token"
    ]
    
    prompt_lower = prompt.lower()
    for pattern in sensitive_patterns:
        if pattern in prompt_lower:
            # Log the blocked attempt
            log_event("user_prompt_submit", {
                "blocked_prompt": True,
                "reason": f"Contains sensitive pattern: {pattern}"
            })
            return False
    
    return True


def enhance_prompt(prompt: str, context: Dict[str, Any]) -> str:
    """
    Enhance user prompt with additional context or instructions.
    
    Args:
        prompt: Original user prompt
        context: Session context information
        
    Returns:
        Enhanced prompt (or original if no changes needed)
    """
    # Add prompt enhancement logic here
    # For example, you might want to:
    # - Add project-specific context
    # - Include coding standards
    # - Add security reminders
    # - Inject common patterns or templates
    
    enhanced_prompt = prompt
    
    # Example: Add project context for certain types of requests
    if any(keyword in prompt.lower() for keyword in ["implement", "create", "add"]):
        project_context = "\n\nProject Context: This is a Claude Code boilerplate repository. Please follow existing patterns and conventions."
        enhanced_prompt = prompt + project_context
    
    return enhanced_prompt


def add_context_from_files() -> str:
    """
    Add relevant context from project files.
    
    Returns:
        Additional context string to append to prompt
    """
    context_parts = []
    
    # Check for project documentation
    docs_path = Path.cwd() / "README.md"
    if docs_path.exists():
        try:
            with open(docs_path, "r") as f:
                readme_content = f.read()[:500]  # First 500 chars
            context_parts.append(f"README excerpt: {readme_content}")
        except Exception:
            pass
    
    # Check for Claude configuration
    claude_md_path = Path.cwd() / "CLAUDE.md"
    if claude_md_path.exists():
        try:
            with open(claude_md_path, "r") as f:
                claude_content = f.read()[:300]  # First 300 chars
            context_parts.append(f"CLAUDE.md excerpt: {claude_content}")
        except Exception:
            pass
    
    return "\n\n".join(context_parts) if context_parts else ""


def main() -> None:
    """Main hook function."""
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the event (with truncated prompt for privacy)
        log_data = input_data.copy()
        if "prompt" in log_data and len(log_data["prompt"]) > 100:
            log_data["prompt"] = log_data["prompt"][:100] + "..."
        log_event("user_prompt_submit", log_data)
        
        # Extract prompt and context
        prompt = input_data.get("prompt", "")
        context = input_data.get("context", {})
        
        # Validate the prompt
        if not validate_prompt(prompt):
            # Block the prompt by exiting with non-zero status
            sys.exit(1)
        
        # Enhance the prompt
        enhanced_prompt = enhance_prompt(prompt, context)
        
        # Add context from project files
        additional_context = add_context_from_files()
        if additional_context:
            enhanced_prompt += f"\n\n{additional_context}"
        
        # If prompt was modified, output the updated prompt
        if enhanced_prompt != prompt:
            output = {
                "prompt": enhanced_prompt
            }
            print(json.dumps(output))
        
    except Exception as e:
        # Log error but don't block execution
        error_data = {"error": str(e), "type": "user_prompt_submit_error"}
        log_event("user_prompt_submit", error_data)
        # Exit with 0 to allow prompt processing to continue
        sys.exit(0)


if __name__ == "__main__":
    main()