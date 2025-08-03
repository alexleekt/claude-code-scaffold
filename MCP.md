# MCP Servers

This document tracks Model Context Protocol (MCP) servers installed and configured for use with Claude Code in this project.

## What is MCP?

Model Context Protocol (MCP) is an open standard that enables secure connections between Claude Code and external data sources, tools, and services. MCP servers provide additional capabilities like database access, API integrations, and specialized tools.

## Installed MCP Servers

### Context7
- **Server**: `context7`
- **Transport**: HTTP
- **URL**: `https://mcp.context7.com/mcp`
- **Purpose**: Enhanced context management and retrieval capabilities
- **Status**: ✅ Active
- **Installation Date**: 2025-08-03

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

### Context & Retrieval
- **Context7**: Advanced context management and document retrieval

### Database & Storage
- *None currently installed*

### API Integrations  
- *None currently installed*

### Development Tools
- *None currently installed*

### Custom Servers
- *None currently installed*

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