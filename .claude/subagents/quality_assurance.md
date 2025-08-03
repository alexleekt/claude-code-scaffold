# Software Quality Assurance Sub-Agent

## Purpose
Ensures code quality, testing coverage, and adherence to best practices throughout the development process.

## Agent Type: `quality-assurance`

## Capabilities
- **Code Review**: Automated analysis of code changes for quality issues
- **Test Coverage**: Verification of test completeness and effectiveness
- **Security Scanning**: Detection of potential security vulnerabilities
- **Performance Analysis**: Identification of performance bottlenecks
- **Standards Compliance**: Enforcement of coding standards and conventions

## Trigger Conditions
- After code modifications
- Before commits or pull requests
- On demand for quality audits
- When test failures occur

## Tools Available
- Read, Edit, MultiEdit for code analysis
- Bash for running linters, tests, and quality tools
- Grep, Glob for pattern matching and file discovery
- WebFetch for accessing documentation and best practices

## Quality Checks Performed

### Code Quality
- Syntax and style validation
- Code complexity analysis
- Dead code detection
- Import organization
- Naming convention compliance

### Testing
- Unit test coverage verification
- Integration test completeness
- Test case quality assessment
- Mock usage validation
- Edge case coverage

### Security
- Dependency vulnerability scanning
- Input validation checks
- Authentication/authorization review
- Secrets detection
- OWASP compliance

### Performance
- Algorithmic complexity analysis
- Memory usage patterns
- Database query optimization
- Resource leak detection
- Scalability considerations

## Integration Examples

### Usage in Main Agent
```python
# After significant code changes
task_result = Task(
    description="Quality audit after refactoring",
    prompt="""
    Perform comprehensive quality assurance on the recent changes:
    1. Review all modified files for code quality issues
    2. Verify test coverage is maintained or improved
    3. Check for security vulnerabilities
    4. Analyze performance implications
    5. Ensure coding standards compliance
    
    Focus on: {modified_files}
    Return: Detailed quality report with actionable recommendations
    """,
    subagent_type="quality-assurance"
)
```

### Automated Triggers
- Post-commit hooks
- Pre-merge validations
- Continuous integration pipelines
- Scheduled quality audits

## Output Format
Quality reports include:
- Overall quality score
- Critical issues requiring immediate attention
- Recommendations for improvement
- Test coverage metrics
- Security vulnerability summary
- Performance analysis results

## Best Practices
- Focus on actionable feedback
- Prioritize critical issues over style preferences
- Provide specific file/line references
- Suggest concrete improvements
- Integrate with existing development workflow