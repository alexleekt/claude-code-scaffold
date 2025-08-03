# MCP Servers

This document tracks Model Context Protocol (MCP) servers installed and configured for use with Claude Code in this project.

## What is MCP?

Model Context Protocol (MCP) is an open standard that enables secure connections between Claude Code and external data sources, tools, and services. MCP servers provide additional capabilities like database access, API integrations, and specialized tools.

## Installed MCP Servers

### Serena
- **Server**: `serena`
- **Transport**: Stdio (uvx)
- **Command**: `uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project /Users/alexleekt/git/claude-code-scaffold`
- **Purpose**: Professional coding agent with semantic coding tools, symbol-based code navigation, intelligent file operations, and memory management
- **Status**: ✅ Active
- **Key Features**:
  - Symbol-based code navigation and editing
  - Intelligent file search and pattern matching
  - Project memory management
  - Context-aware code analysis
  - IDE integration support

### Context7
- **Server**: `context7`
- **Transport**: HTTP
- **URL**: `https://mcp.context7.com/mcp`
- **Purpose**: Up-to-date documentation and code examples for libraries and frameworks
- **Status**: ✅ Active
- **Key Features**:
  - Library documentation retrieval
  - Code examples and snippets
  - API reference lookup
  - Framework-specific guidance

## MCP Server Management

### Adding New Servers
```bash
# General syntax
claude mcp add --transport <transport> <name> <url_or_path>

# HTTP transport example
claude mcp add --transport http server-name https://example.com/mcp

# Stdio transport example  
claude mcp add --transport stdio server-name /path/to/server
```

### Listing Servers
```bash
claude mcp list
```

### Removing Servers
```bash
claude mcp remove <server-name>
```

## Server Categories

### Development Tools
- **Serena**: Professional coding agent with semantic tools, symbol navigation, and intelligent code operations

### Context & Retrieval
- **Context7**: Library documentation and code examples retrieval

### Database & Storage
- *None currently installed*

### API Integrations  
- *None currently installed*

### Custom Servers
- *None currently installed*

## Available Tools

### Serena Tools
- **Code Navigation**: `find_symbol`, `get_symbols_overview`, `find_referencing_symbols`
- **File Operations**: `list_dir`, `find_file`, `search_for_pattern`
- **Code Editing**: `replace_symbol_body`, `insert_after_symbol`, `insert_before_symbol`, `replace_regex`
- **Memory Management**: `write_memory`, `read_memory`, `list_memories`, `delete_memory`
- **Project Analysis**: `check_onboarding_performed`, `onboarding`
- **Utilities**: `restart_language_server`, `think_about_*` tools

### Context7 Tools
- **Library Resolution**: `resolve-library-id` - Find Context7-compatible library IDs
- **Documentation**: `get-library-docs` - Retrieve up-to-date library documentation

## Configuration Notes

- MCP servers are configured globally for Claude Code, not per-project
- All servers listed here are available across all Claude Code sessions
- Server availability depends on network connectivity and server status
- Some servers may require authentication or API keys

## Security Considerations

- Only install MCP servers from trusted sources
- Review server permissions and capabilities before installation
- Monitor server access logs if available
- Remove unused servers to minimize attack surface

## Troubleshooting

### Common Issues
- **Connection timeouts**: Check network connectivity and server status
- **Authentication errors**: Verify API keys and credentials
- **Permission denied**: Check server access permissions
- **Server not found**: Verify server URL and transport type

### Debug Commands
```bash
# Check MCP server status
claude mcp list

# Test server connectivity (if available)
claude mcp test <server-name>
```

## Updates and Maintenance

- Regularly review installed servers and remove unused ones
- Update server URLs when they change
- Monitor server deprecation notices
- Keep this documentation updated when adding/removing servers

---

**Last Updated**: 2025-08-03  
**Next Review**: 2025-09-03