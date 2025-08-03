# Documentation Maintenance Sub-Agent

## Purpose
Ensures project documentation remains current, comprehensive, and useful throughout the development lifecycle.

## Agent Type: `documentation-maintenance`

## Capabilities
- **Documentation Auditing**: Analysis of existing documentation for completeness and accuracy
- **Automated Updates**: Synchronization of documentation with code changes
- **Gap Identification**: Detection of missing or outdated documentation sections
- **Quality Assessment**: Evaluation of documentation clarity and usefulness
- **Structure Optimization**: Organization and formatting improvements

## Trigger Conditions
- After significant code changes
- Before releases or deployments
- During onboarding or knowledge transfer
- On scheduled documentation reviews
- When new features are implemented

## Tools Available
- Read, Edit, MultiEdit for documentation files
- Grep, Glob for content analysis and discovery
- Bash for documentation generation tools
- WebFetch for documentation best practices and standards

## Documentation Maintenance Process

### Coverage Analysis
- API documentation completeness
- Setup and installation instructions
- Architecture and design documentation
- User guides and tutorials
- Contributing guidelines and processes

### Accuracy Verification
- Code example validation
- Link and reference checking
- Version information updates
- Configuration and environment details
- Troubleshooting guide relevance

### Quality Assessment
- Clarity and readability evaluation
- Target audience appropriateness
- Information organization and flow
- Visual aids and diagram updates
- Accessibility compliance

### Automation Opportunities
- Generated documentation from code comments
- Automated testing of documentation examples
- Link validation and broken reference detection
- Version synchronization with releases
- Template and style guide enforcement

## Integration Examples

### Usage in Main Agent
```python
# After feature implementation
task_result = Task(
    description="Update documentation for new feature",
    prompt="""
    Review and update documentation following recent changes:
    
    Changes made:
    {description_of_changes}
    
    Tasks:
    1. Identify documentation sections affected by these changes
    2. Update API documentation if applicable
    3. Verify all code examples still work
    4. Update user guides and tutorials
    5. Check for broken links or outdated references
    6. Ensure README and setup instructions are current
    
    Return: List of documentation updates made and any identified gaps
    """,
    subagent_type="documentation-maintenance"
)
```

### Automated Triggers
- Pre-commit hooks for documentation validation
- CI/CD pipeline documentation checks
- Release preparation workflows
- Scheduled documentation audits

## Documentation Types Managed

### Technical Documentation
- API reference and examples
- Architecture and design documents
- Database schemas and migrations
- Deployment and configuration guides
- Security and compliance documentation

### User Documentation
- Installation and setup guides
- User manuals and tutorials
- FAQ and troubleshooting guides
- Feature documentation and changelogs
- Migration and upgrade instructions

### Developer Documentation
- Contributing guidelines
- Code style and conventions
- Testing procedures and standards
- Development environment setup
- Code review and workflow processes

## Output Format
Documentation maintenance reports include:
- Documentation coverage assessment
- List of updates made
- Identified gaps and recommendations
- Quality improvement suggestions
- Broken links or outdated references
- Automation opportunities

## Quality Metrics

### Completeness
- Coverage of all public APIs
- Presence of setup instructions
- Availability of troubleshooting guides
- Inclusion of examples and use cases

### Accuracy
- Code examples execute successfully
- Links and references are valid
- Version information is current
- Configuration details are correct

### Usability
- Clear navigation and organization
- Appropriate level of detail for audience
- Consistent formatting and style
- Searchable and accessible content

## Best Practices
- Keep documentation close to code when possible
- Use automated testing for documentation examples
- Maintain consistent style and formatting
- Regular review and update cycles
- Version documentation with releases
- Include both quick start and comprehensive guides