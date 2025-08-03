# Implementation Standards Sub-Agent

## Purpose
Ensures consistent implementation of best practices using modern tooling with zero local dependencies, leveraging Astral UV for Python and Finch for containerization.

## Agent Type: `implementation-standards`

## Capabilities
- **Dependency-Free Development**: All tools run in containers or via uv, no local installation required
- **Modern Python Tooling**: Leveraging uv for fast, reliable Python package management
- **Container-First Architecture**: Using Finch for efficient, secure containerization
- **Development Environment Standardization**: Consistent environments across all developers and CI/CD
- **Performance Optimization**: Fast builds, installs, and execution through modern tooling

## Core Tooling Standards

### Python Development with UV
**UV (Astral)** - Ultra-fast Python package manager and project manager

#### Project Structure
```
project/
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Locked dependency versions
├── .python-version         # Python version specification
├── src/                    # Source code
├── tests/                  # Test files
└── scripts/                # Development scripts
```

#### UV Commands and Patterns
```bash
# Project initialization
uv init --lib myproject
uv init --app myproject

# Dependency management
uv add requests            # Add production dependency
uv add --dev pytest       # Add development dependency
uv add --optional[dev] black ruff  # Add optional dependency group

# Virtual environment management
uv venv                    # Create virtual environment
uv pip install -e .       # Install project in development mode

# Running commands
uv run python script.py   # Run Python with project dependencies
uv run pytest            # Run tests
uv run ruff check        # Run linting

# Lock file management
uv lock                   # Update lock file
uv sync                   # Sync environment with lock file
```

### Container Development with Finch
**Finch** - Fast, minimal container runtime with reduced resource usage

#### Container Standards
```dockerfile
# Multi-stage builds with UV
FROM python:3.12-slim as builder
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

FROM python:3.12-slim as runtime
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY src/ /app/src/
WORKDIR /app
```

#### Finch Commands and Patterns
```bash
# Container management
finch build -t myapp .     # Build container image
finch run -it myapp       # Run container interactively
finch compose up          # Run multi-container applications

# Development workflows
finch run -v $(pwd):/app myapp uv run pytest  # Run tests in container
finch run -v $(pwd):/app myapp uv run ruff check  # Run linting in container

# Multi-architecture builds
finch buildx build --platform linux/amd64,linux/arm64 -t myapp .
```

## Implementation Patterns

### Project Setup Standards
```bash
# New Python project initialization
uv init --lib myproject
cd myproject

# Add common development dependencies
uv add --dev pytest pytest-cov black ruff mypy pre-commit

# Add common production dependencies based on project type
uv add fastapi uvicorn  # For web APIs
uv add click           # For CLI applications
uv add pandas numpy    # For data processing
```

### Development Environment
```yaml
# compose.yml for development
services:
  app:
    build: .
    volumes:
      - .:/app
    environment:
      - PYTHONPATH=/app/src
    command: uv run uvicorn src.main:app --reload --host 0.0.0.0

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### CI/CD Integration
```yaml
# .github/workflows/test.yml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install uv
        uses: astral-sh/setup-uv@v1
        
      - name: Set up Python
        run: uv python install
        
      - name: Install dependencies
        run: uv sync
        
      - name: Run tests
        run: uv run pytest
        
      - name: Run linting
        run: uv run ruff check
        
      - name: Run type checking
        run: uv run mypy src/
```

## Quality Standards

### Code Quality Tools (via UV)
```toml
# pyproject.toml configuration
[tool.ruff]
target-version = "py312"
line-length = 88
select = ["E", "W", "F", "I", "B", "C901"]

[tool.ruff.isort]
known-first-party = ["myproject"]

[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--cov=src --cov-report=term-missing"

[tool.coverage.run]
source = ["src"]
omit = ["tests/*"]
```

### Pre-commit Configuration
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: ruff-check
        name: ruff-check
        entry: uv run ruff check
        language: system
        types: [python]
        
      - id: ruff-format
        name: ruff-format
        entry: uv run ruff format
        language: system
        types: [python]
        
      - id: mypy
        name: mypy
        entry: uv run mypy
        language: system
        types: [python]
        
      - id: pytest
        name: pytest
        entry: uv run pytest
        language: system
        types: [python]
```

## Container Best Practices

### Multi-Stage Builds
```dockerfile
# Optimized Dockerfile with UV
FROM python:3.12-slim as base
WORKDIR /app
RUN pip install uv

FROM base as builder
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-cache

FROM base as development
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache
COPY . .
CMD ["uv", "run", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]

FROM python:3.12-slim as production
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY src/ ./src/
USER 1000
CMD ["python", "-m", "src.main"]
```

### Container Optimization
```bash
# .dockerignore
.git
.pytest_cache
.mypy_cache
.ruff_cache
__pycache__
*.pyc
.env
.venv
tests/
docs/
```

## Integration Examples

### Usage in Main Agent
```python
# When setting up new projects
task_result = Task(
    description="Setup project with implementation standards",
    prompt="""
    Set up a new Python project following implementation standards:
    
    Project Type: {project_type}
    Requirements: {requirements}
    
    Tasks:
    1. Initialize project with uv following standard structure
    2. Configure pyproject.toml with appropriate dependencies
    3. Set up Dockerfile with multi-stage builds using uv
    4. Create compose.yml for development environment
    5. Configure code quality tools (ruff, mypy, pytest)
    6. Set up pre-commit hooks for quality enforcement
    7. Create CI/CD workflow using uv and finch
    8. Ensure zero local dependencies except uv and finch
    
    Return: Complete project setup with all configuration files
    """,
    subagent_type="implementation-standards"
)
```

### Development Workflow Standards
```python
# For enforcing development practices
Task(
    description="Audit project for implementation standards compliance",
    prompt="Review existing project for compliance with UV, Finch, and container best practices. Suggest improvements and provide migration path.",
    subagent_type="implementation-standards"
)
```

## Architecture Patterns

### Microservices with UV and Finch
```yaml
# Multi-service development
services:
  api:
    build:
      context: ./api
      target: development
    volumes:
      - ./api:/app
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/api
    depends_on:
      - db

  worker:
    build:
      context: ./worker
      target: development
    volumes:
      - ./worker:/app
    environment:
      - REDIS_URL=redis://redis:6379
    depends_on:
      - redis

  frontend:
    build:
      context: ./frontend
    volumes:
      - ./frontend:/app
    ports:
      - "3000:3000"

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: api
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass

  redis:
    image: redis:7-alpine
```

### Monorepo Structure
```
project/
├── services/
│   ├── api/
│   │   ├── pyproject.toml
│   │   ├── uv.lock
│   │   ├── Dockerfile
│   │   └── src/
│   ├── worker/
│   │   ├── pyproject.toml
│   │   ├── uv.lock
│   │   ├── Dockerfile
│   │   └── src/
│   └── shared/
│       ├── pyproject.toml
│       └── src/
├── compose.yml
├── compose.override.yml
└── scripts/
    ├── setup.sh
    ├── test.sh
    └── deploy.sh
```

## Performance Optimization

### UV Performance Features
- **Parallel installs**: UV installs packages in parallel for faster setup
- **Global cache**: Shared package cache across projects
- **Lock file optimization**: Faster dependency resolution
- **Minimal virtual environments**: Reduced overhead

### Finch Performance Features
- **Shared base images**: Efficient image layering and caching
- **Multi-architecture**: Native performance on ARM and x86
- **Resource efficiency**: Lower memory and CPU usage than Docker
- **Fast container startup**: Optimized runtime performance

## Security Standards

### Container Security
```dockerfile
# Security best practices
FROM python:3.12-slim
RUN groupadd -r appuser && useradd -r -g appuser appuser
WORKDIR /app
RUN pip install uv
COPY --chown=appuser:appuser pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY --chown=appuser:appuser src/ ./src/
USER appuser
EXPOSE 8000
CMD ["uv", "run", "python", "-m", "src.main"]
```

### Dependency Security
```bash
# Security scanning with uv
uv run pip-audit          # Scan for vulnerabilities
uv sync --upgrade         # Update to latest secure versions
uv export --format requirements.txt | safety check  # Safety scanning
```

## Best Practices Summary

### Development Workflow
1. **Use uv for all Python operations** - No pip, pipenv, or poetry
2. **Container-first development** - All services run in containers
3. **Zero local dependencies** - Only uv and finch required locally
4. **Reproducible environments** - Lock files and container images
5. **Fast feedback loops** - Quick tests, builds, and deployments

### Project Standards
1. **Standard project structure** - Consistent across all projects
2. **Quality tool integration** - Ruff, mypy, pytest via uv
3. **Pre-commit hooks** - Automated quality enforcement
4. **CI/CD standardization** - GitHub Actions with uv and finch
5. **Documentation requirements** - README, API docs, deployment guides

### Performance Focus
1. **Optimize for speed** - Fast builds, tests, and deployments
2. **Efficient resource usage** - Minimal containers and dependencies
3. **Parallel execution** - Concurrent operations where possible
4. **Caching strategies** - UV cache, Docker layers, CI cache
5. **Monitoring integration** - Performance and error tracking