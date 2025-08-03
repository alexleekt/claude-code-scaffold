# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠️ IMPORTANT: This is a Template Repository

**This repository is a template and scaffold - not for storing actual project content.**

If you're working on an actual project or need to store real code/data:
1. **Clone this repository** to create your own project
2. **Use it as a starting point** for your specific project needs
3. **Do not commit project-specific content** to this template repository

This template provides the foundation - your real work should happen in a separate repository based on this template.

## Overview

Claude Code Scaffold is a starting template for projects that want to leverage Claude Code's powerful hook system. It provides a production-ready foundation with:

- **Complete Hook System**: All major Claude Code hooks implemented with extensible patterns
- **Specialized Sub-Agents**: Quality assurance, requirements clarity, documentation maintenance, UX differentiation, strategic visionary, and implementation standards agents
- **Centralized Logging**: Date-based logging system for all hook events
- **Permission Management**: Configurable security and permission controls
- **Project Context Awareness**: Automatic detection of project types and configurations
- **Session Management**: Track and manage Claude Code sessions with state persistence
- **Security Features**: Input validation, sensitive content detection, and audit trails

## Repository Structure

```
.claude/
├── settings.json          # Main Claude Code configuration
├── settings.local.json    # Local/user-specific overrides
├── hooks/                 # Hook implementations
│   ├── common_functions.py      # Shared logging utilities
│   ├── session_start.py         # Session initialization
│   ├── user_prompt_submit.py    # Prompt preprocessing
│   ├── pre_tool_use.py          # Tool validation/enhancement
│   ├── post_tool_use.py         # Tool result analysis
│   ├── notification.py          # Permission and idle handling
│   ├── stop.py                  # Session cleanup
│   └── subagent_stop.py         # Subagent completion
├── subagents/             # Specialized sub-agent documentation
│   ├── quality_assurance.md     # Software quality validation
│   ├── requirements_clarity.md  # Requirements analysis and clarification
│   ├── documentation_maintenance.md  # Documentation updates and maintenance
│   ├── ux_differentiation.md    # UX excellence and competitive differentiation
│   ├── strategic_visionary.md   # Future-thinking and architectural flexibility
│   └── implementation_standards.md  # Modern tooling and best practices
└── logs/                  # Date-based log files
    └── hooks_YYYYMMDD.log       # Daily hook event logs
```

## Hook System Architecture

This scaffold implements the complete Claude Code hook lifecycle:

### 1. Session Start (`session_start.py`)
- **Trigger**: When starting a new session or resuming
- **Features**:
  - Automatic project type detection (package.json, pyproject.toml, etc.)
  - System requirements checking (uv, git availability)
  - Previous session data recovery for resume operations
  - Project context setup and CLAUDE.md detection
  - Welcome message generation

### 2. User Prompt Submit (`user_prompt_submit.py`)
- **Trigger**: Before Claude processes user prompts
- **Features**:
  - Security validation (detects API keys, passwords, tokens)
  - Prompt enhancement with project context
  - Automatic injection of README.md and CLAUDE.md content
  - Content filtering and policy enforcement

### 3. Pre Tool Use (`pre_tool_use.py`)
- **Trigger**: After Claude creates tool parameters, before execution
- **Features**:
  - Tool usage validation and permission checking
  - Parameter enhancement and modification
  - Security checks for file operations
  - Rate limiting capabilities

### 4. Post Tool Use (`post_tool_use.py`)
- **Trigger**: Immediately after tool completion
- **Features**:
  - File modification tracking
  - Command execution auditing
  - Performance metrics collection
  - Security-relevant operation logging

### 5. Notification (`notification.py`)
- **Trigger**: Permission requests and idle timeouts
- **Features**:
  - Tool permission management
  - Idle session handling
  - External notification integration
  - Custom permission logic

### 6. Stop (`stop.py`)
- **Trigger**: When Claude finishes responding
- **Features**:
  - Session metrics generation
  - Resource cleanup
  - Session summary reporting
  - Analytics data collection

## Specialized Sub-Agents

This scaffold includes three specialized sub-agents that can be invoked using the Task tool to handle specific aspects of software development:

### 1. Quality Assurance Sub-Agent (`quality-assurance`)
- **Purpose**: Ensures code quality, testing coverage, and adherence to best practices
- **Capabilities**:
  - Automated code review and quality analysis
  - Test coverage verification and improvement suggestions
  - Security vulnerability scanning and remediation
  - Performance analysis and optimization recommendations
  - Coding standards and convention enforcement

**Usage Example**:
```python
Task(
    description="Quality audit after refactoring",
    prompt="Perform comprehensive quality assurance on recent changes: analyze code quality, verify test coverage, check for security issues, and ensure standards compliance.",
    subagent_type="quality-assurance"
)
```

### 2. Requirements Clarity Sub-Agent (`requirements-clarity`)
- **Purpose**: Ensures project requirements are clear, complete, and well-documented
- **Capabilities**:
  - Requirement decomposition and analysis
  - Ambiguity detection and resolution
  - Completeness validation and gap identification
  - Stakeholder alignment facilitation
  - Acceptance criteria definition

**Usage Example**:
```python
Task(
    description="Clarify user story requirements",
    prompt="Analyze the user request for clarity: break down into specific requirements, identify ambiguities, define acceptance criteria, and suggest clarification questions.",
    subagent_type="requirements-clarity"
)
```

### 3. Documentation Maintenance Sub-Agent (`documentation-maintenance`)
- **Purpose**: Ensures project documentation remains current, comprehensive, and useful
- **Capabilities**:
  - Documentation auditing and gap analysis
  - Automated updates synchronized with code changes
  - Quality assessment and improvement recommendations
  - Structure optimization and consistency enforcement
  - Link validation and reference checking

**Usage Example**:
```python
Task(
    description="Update documentation for new feature",
    prompt="Review and update documentation following recent changes: update API docs, verify code examples, check for broken links, and ensure completeness.",
    subagent_type="documentation-maintenance"
)
```

### 4. UX Differentiation Sub-Agent (`ux-differentiation`)
- **Purpose**: Ensures exceptional, differentiated user experiences that create competitive advantage
- **Capabilities**:
  - Competitive differentiation analysis and market positioning
  - Value proposition optimization and unique benefit identification
  - User journey innovation and friction point elimination
  - Micro-interaction excellence and performance-as-UX optimization
  - Accessibility leadership and inclusive design advancement

**Usage Example**:
```python
Task(
    description="UX differentiation analysis for new feature",
    prompt="Analyze the proposed feature for differentiation opportunities: identify competitive advantages, suggest innovative interactions, propose performance benefits, and define success metrics.",
    subagent_type="ux-differentiation"
)
```

### 5. Strategic Visionary Sub-Agent (`strategic-visionary`)
- **Purpose**: Challenges conventional thinking by envisioning future possibilities and building architectural flexibility
- **Capabilities**:
  - Future scenario planning and technology trend anticipation
  - Use case expansion and adjacent market opportunity discovery
  - Architecture future-proofing for evolving requirements
  - Platform thinking and ecosystem development strategies
  - Long-term value creation through network effects and community building

**Usage Example**:
```python
Task(
    description="Visionary analysis for new product concept",
    prompt="Analyze this concept through a strategic lens: identify alternative use cases, design scalable architecture, predict evolution paths, suggest platform capabilities, and plan for unknown future requirements.",
    subagent_type="strategic-visionary"
)
```

### 6. Implementation Standards Sub-Agent (`implementation-standards`)
- **Purpose**: Ensures consistent implementation using modern tooling with zero local dependencies
- **Capabilities**:
  - Dependency-free development with UV and Finch
  - Modern Python tooling and container-first architecture
  - Development environment standardization across teams
  - Performance optimization through efficient build patterns
  - Security best practices and quality tool integration

**Usage Example**:
```python
Task(
    description="Setup project with implementation standards",
    prompt="Set up new Python project with UV, configure Dockerfile with multi-stage builds, create development environment with Finch, and ensure zero local dependencies.",
    subagent_type="implementation-standards"
)
```

### Proactive Sub-Agent Usage

These sub-agents should be used proactively during development:

- **Quality Assurance**: After significant code changes, before commits/PRs, during code reviews
- **Requirements Clarity**: Before starting new features, when user requests are ambiguous, during planning
- **Documentation Maintenance**: After feature implementation, before releases, during onboarding
- **UX Differentiation**: During feature design, before competitive launches, when seeking market advantage
- **Strategic Visionary**: During project planning, before architectural decisions, when exploring new markets
- **Implementation Standards**: During project setup, when establishing development workflows, for tooling audits

## Configuration

### Main Settings (`settings.json`)

The main configuration defines:

- **Permissions**: Granular tool and domain access controls
- **Hook Mappings**: Associates hooks with trigger events
- **Tool Integration**: Uses `uv run` for Python hook execution

### Local Overrides (`settings.local.json`)

User-specific settings that override main configuration:
- Additional permissions
- Custom hook parameters
- Development-specific settings

## Security Features

### Input Validation
- Automatic detection of sensitive content in prompts
- Configurable pattern matching for API keys, passwords, tokens
- Prompt blocking with detailed audit logging

### File Operation Tracking
- Complete audit trail of file modifications
- Command execution monitoring for sensitive operations
- Real-time security event logging

### Permission System
- Fine-grained tool access controls
- Domain-specific web access restrictions
- Configurable allow/deny lists

## Logging System

### Centralized Logging (`common_functions.py`)
- **Format**: JSON-structured logs with timestamps
- **Organization**: Date-based files (`hooks_YYYYMMDD.log`)
- **Content**: Complete hook events, errors, and security incidents
- **Simple Design**: No file locking, straightforward append operations

### Log Structure
```json
{
  "timestamp": "2025-08-02T19:17:58.221554",
  "hook": "hook_name",
  "data": {
    "event_specific_data": "value"
  }
}
```

## Development Workflow

### Prerequisites
- **uv**: Python package manager (recommended for hook execution)
- **Python 3.11+**: Required for hook scripts
- **Git**: For version control and project detection

### Setup
1. Clone this scaffold repository
2. Customize `.claude/settings.json` for your project needs
3. Modify hook implementations in `.claude/hooks/`
4. Configure local overrides in `.claude/settings.local.json`

### Common Commands
```bash
# View hook logs
cat .claude/logs/hooks_$(date +%Y%m%d).log

# Test hook execution
echo '{"test": "data"}' | uv run .claude/hooks/session_start.py

# Monitor real-time hook activity
tail -f .claude/logs/hooks_$(date +%Y%m%d).log
```

## Customization Guide

### Adding Custom Hooks
1. Create new Python script in `.claude/hooks/`
2. Import `common_functions` for logging
3. Implement main() function with JSON stdin/stdout
4. Add hook configuration to `settings.json`

### Extending Validation
- Modify `user_prompt_submit.py` for custom prompt validation
- Update `pre_tool_use.py` for tool-specific security checks
- Extend `post_tool_use.py` for custom result analysis

### Project Context Integration
- Add project type detection in `session_start.py`
- Customize context injection in `user_prompt_submit.py`
- Implement project-specific workflows

## Integration Patterns

### CI/CD Integration
- Hook logs provide audit trails for automated processes
- Security validation prevents unauthorized operations
- Session metrics enable performance monitoring

### Team Collaboration
- Shared settings ensure consistent Claude Code behavior
- Audit logs provide transparency for team activities
- Permission system enables role-based access control

### Project Templates
- Use as base template for new Claude Code projects
- Customize hooks for domain-specific requirements
- Extend logging for project-specific metrics

## Best Practices

### Security
- Regularly review permission configurations
- Monitor logs for suspicious activity
- Keep sensitive patterns updated in validation
- Use local settings for user-specific permissions

### Performance
- Optimize hook execution for minimal latency
- Use efficient logging patterns
- Implement graceful error handling
- Monitor session metrics for bottlenecks

### Maintenance
- Rotate log files periodically
- Update hook implementations for new requirements
- Test hook modifications in isolation
- Document custom extensions thoroughly

## Troubleshooting

### Common Issues
- **Hook execution failures**: Check uv installation and Python compatibility
- **Permission denied**: Verify settings.json and settings.local.json permissions
- **Missing logs**: Ensure .claude/logs directory exists and is writable
- **Context injection failures**: Check file paths and permissions

### Debug Mode
Enable detailed logging by modifying hook scripts to include debug information in log events.

## Advanced Features

### Session State Management
- Automatic session backup and recovery
- Cross-session context preservation
- User preference persistence

### Analytics Integration
- Custom metrics collection
- Performance monitoring
- Usage pattern analysis

### External Integrations
- Webhook notifications
- Slack/Discord alerts
- Monitoring system integration

This scaffold provides a robust foundation for Claude Code projects with enterprise-grade features while remaining highly customizable for specific use cases.