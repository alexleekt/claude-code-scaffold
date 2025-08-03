# 🚀 Claude Code Scaffold

[![Template Repository](https://img.shields.io/badge/Template-Repository-blue?style=flat-square)](https://github.com/alexleekt/claude-code-scaffold)
[![Claude Code](https://img.shields.io/badge/Claude-Code-orange?style=flat-square)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

> **🎯 Production-ready template for Claude Code projects with comprehensive hook system and specialized sub-agents**

## ⚠️ This is a Template Repository

**DO NOT use this repository directly for your projects!**

This is a template and scaffold designed to be cloned and customized. Follow the [Quick Start](#-quick-start) guide below to create your own project based on this template.

## 🌟 What's Included

### 🔧 Complete Hook System
- **Session Management** - Startup, resume, and cleanup hooks
- **Security & Validation** - Input validation and permission management
- **Tool Enhancement** - Pre/post tool execution hooks with logging
- **Notification System** - Permission requests and idle handling

### 🤖 Specialized Agents
- **Code Quality Guardian** (`code-quality-guardian`) - Comprehensive code quality assurance, test coverage, security scanning
- **Requirements Analyst** (`requirements-analyst`) - Requirement analysis, clarification, and validation
- **Documentation Maintenance** (`documentation-maintenance`) - Doc updates, auditing, and maintenance
- **UX Advantage Architect** (`ux-advantage-architect`) - Exceptional user experiences with competitive advantage
- **Strategic Visionary** (`strategic-visionary`) - Future-thinking and architectural flexibility
- **Modern Tooling Standards** (`modern-tooling-standards`) - Modern development setup with UV and Finch

### 📊 Advanced Features
- **Centralized Logging** - JSON Lines format with session tracking
- **Permission Management** - Granular tool and domain access controls
- **Zero Local Dependencies** - Container-first development with UV and Finch
- **Security by Design** - Input validation, audit trails, and compliance frameworks

## 🚀 Quick Start

### 1. Create Your Project
```bash
# Clone this template (replace with your project details)
git clone https://github.com/alexleekt/claude-code-scaffold.git my-project
cd my-project

# Remove template git history and start fresh
rm -rf .git
git init
git add .
git commit -m "Initial commit: Claude Code project from scaffold"

# Add your own remote
git remote add origin https://github.com/yourusername/your-project.git
git push -u origin main
```

### 2. Customize for Your Project
```bash
# Update project-specific files
vim CLAUDE.md          # Add your project context and instructions
vim README.md          # Replace with your project README
vim .claude/settings.json  # Configure permissions and hooks for your needs

# Customize agents (optional)
ls .claude/agents/  # Review and modify agent configurations
```

### 3. Start Using Claude Code
```bash
# Navigate to your project directory
cd /path/to/your-project

# Start Claude Code session (hooks will activate automatically)
claude code
```

## 🎯 Sub-Agent Usage Examples

### Code Quality Guardian
```python
Task(
    description="Quality audit after refactoring",
    prompt="Perform comprehensive quality assurance: analyze code quality, verify test coverage, check security issues, ensure standards compliance.",
    subagent_type="code-quality-guardian"
)
```

### Requirements Analyst
```python
Task(
    description="Clarify user story requirements",
    prompt="Analyze user request for clarity: break down into specific requirements, identify ambiguities, define acceptance criteria.",
    subagent_type="requirements-analyst"
)
```

### UX Advantage Architect
```python
Task(
    description="UX differentiation analysis",
    prompt="Identify competitive advantages, suggest innovative interactions, propose performance benefits, define success metrics.",
    subagent_type="ux-advantage-architect"
)
```

### Strategic Visionary
```python
Task(
    description="Future-proof architecture design",
    prompt="Design architecture for today's problem that can evolve into platform for tomorrow's unknown opportunities.",
    subagent_type="strategic-visionary"
)
```

### Modern Tooling Standards
```python
Task(
    description="Setup project with modern tooling",
    prompt="Set up Python project with UV, configure multi-stage Dockerfile, create development environment with Finch.",
    subagent_type="modern-tooling-standards"
)
```

## 📁 Repository Structure

```
.claude/
├── settings.json              # Main Claude Code configuration
├── settings.local.json        # Local/user-specific overrides
├── hooks/                     # Hook implementations
│   ├── common_functions.py    # Shared logging utilities
│   ├── session_start.py       # Session initialization
│   ├── user_prompt_submit.py  # Prompt preprocessing
│   ├── pre_tool_use.py        # Tool validation/enhancement
│   ├── post_tool_use.py       # Tool result analysis
│   ├── notification.py        # Permission and idle handling
│   ├── stop.py                # Session cleanup
│   └── subagent_stop.py       # Subagent completion
├── agents/                    # Specialized agent documentation
│   ├── code-quality-guardian.md
│   ├── requirements-analyst.md
│   ├── documentation-maintenance.md
│   ├── ux-advantage-architect.md
│   ├── strategic-visionary.md
│   └── modern-tooling-standards.md
└── logs/                      # Date-based log files
    └── hooks_log_YYYYMMDD_sessionid.jsonl
```

## 🔧 Configuration

### Hook System
- **Automatic Activation** - Hooks activate when Claude Code starts in your project
- **Session Tracking** - Logs include session IDs for better organization
- **Permission Control** - Configurable tool and domain access
- **Error Handling** - Graceful degradation when hooks encounter issues

### Sub-Agents
- **On-Demand Usage** - Invoke with `Task` tool using `subagent_type` parameter
- **Specialized Expertise** - Each agent focuses on specific development aspects
- **Composable Workflows** - Combine multiple agents for complex tasks
- **Extensible Design** - Add custom agents by creating new documentation files

## 🛠 Development Workflow

### Modern Tooling (Zero Local Dependencies)
- **UV (Astral)** - Ultra-fast Python package management
- **Finch** - Efficient container runtime
- **Container-First** - All development in containers
- **Quality Tools** - Ruff, mypy, pytest via UV

### Best Practices Enforced
- **Pre-commit Hooks** - Automated quality checks
- **Multi-stage Builds** - Optimized Docker images
- **Security Scanning** - Dependency and code vulnerability checks
- **Performance Focus** - Fast builds, tests, and deployments

## 📊 Logging and Monitoring

### Centralized Logging
- **JSON Lines Format** - Structured, parseable logs
- **Session Tracking** - Logs organized by date and session ID
- **Hook Events** - Complete audit trail of all hook executions
- **Error Tracking** - Detailed error information and context

### Log Location
```bash
# View today's logs
cat .claude/logs/hooks_log_$(date +%Y%m%d)_*.jsonl

# Monitor real-time activity
tail -f .claude/logs/hooks_log_$(date +%Y%m%d)_*.jsonl
```

## 🔒 Security Features

### Input Validation
- **Sensitive Content Detection** - API keys, passwords, tokens
- **Prompt Security** - Validation before processing
- **Audit Trails** - Complete logging of security events

### Permission Management
- **Tool Access Control** - Granular permissions for Claude Code tools
- **Domain Restrictions** - Control web access and external integrations
- **Configurable Policies** - Customizable security rules

## 📚 Documentation

### Getting Started
- [`CLAUDE.md`](CLAUDE.md) - Complete project documentation and configuration guide
- [`MCP.md`](MCP.md) - Model Context Protocol servers and integrations
- [`.claude/agents/`](.claude/agents/) - Individual agent documentation
- [`.claude/settings.json`](.claude/settings.json) - Configuration reference

### Advanced Usage
- **Hook Customization** - Modify existing hooks for project-specific needs
- **Sub-Agent Development** - Create custom agents for domain-specific tasks
- **Integration Patterns** - CI/CD, monitoring, and external tool integration

## 🤝 Contributing

This is a template repository. Contributions should focus on:
- **Hook System Improvements** - Enhanced functionality and reliability
- **New Agents** - Additional specialized agents for common development tasks
- **Documentation** - Better examples and usage patterns
- **Security Enhancements** - Improved validation and audit capabilities

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Claude Code Documentation** - [docs.anthropic.com/claude-code](https://docs.anthropic.com/en/docs/claude-code)
- **Issues** - Report template issues in this repository
- **Project-Specific Help** - Use your project repository for project-specific questions

---

**Remember**: This is a template! Clone it, customize it, and build amazing things with Claude Code. 🚀