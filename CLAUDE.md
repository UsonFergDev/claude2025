# CLAUDE.md - AI Assistant Guide

This document provides comprehensive guidance for AI assistants (like Claude) working on this repository. It covers codebase structure, development workflows, and key conventions to follow.

## Table of Contents

- [Repository Overview](#repository-overview)
- [Codebase Structure](#codebase-structure)
- [Development Workflows](#development-workflows)
- [Git Conventions](#git-conventions)
- [Code Style & Best Practices](#code-style--best-practices)
- [Testing Strategy](#testing-strategy)
- [AI Assistant Guidelines](#ai-assistant-guidelines)
- [Common Tasks](#common-tasks)

---

## Repository Overview

**Repository**: claude2025
**Owner**: UsonFergDev
**Purpose**: [To be documented as the project evolves]

### Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd claude2025

# Install dependencies (if applicable)
# npm install / pip install -r requirements.txt / etc.

# Run tests (if applicable)
# npm test / pytest / etc.

# Start development server (if applicable)
# npm run dev / python manage.py runserver / etc.
```

---

## Codebase Structure

> **Note**: This section should be updated as the codebase grows.

### Recommended Directory Structure

```
claude2025/
├── src/                    # Source code
│   ├── components/         # Reusable components
│   ├── services/           # Business logic and services
│   ├── utils/              # Utility functions
│   ├── models/             # Data models
│   └── config/             # Configuration files
├── tests/                  # Test files
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── e2e/                # End-to-end tests
├── docs/                   # Documentation
├── scripts/                # Build and deployment scripts
├── .github/                # GitHub workflows and templates
├── CLAUDE.md               # This file
├── README.md               # Project documentation
└── package.json            # Dependencies and scripts (if Node.js)
```

### Key Files and Directories

- **CLAUDE.md**: AI assistant guidance (this file)
- **README.md**: Human-readable project documentation
- **Configuration Files**: (To be documented)

---

## Development Workflows

### Setting Up Development Environment

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd claude2025
   ```

2. **Install dependencies**
   ```bash
   # Add appropriate installation commands
   ```

3. **Configure environment variables**
   ```bash
   # Copy example env file if it exists
   # cp .env.example .env
   ```

4. **Run initial setup**
   ```bash
   # Add setup commands
   ```

### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b claude/<descriptive-branch-name>-<session-id>
   ```

2. **Make your changes**
   - Follow the code style guidelines
   - Write tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   # Run tests
   # Run linters
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "descriptive commit message"
   git push -u origin <branch-name>
   ```

---

## Git Conventions

### Branch Naming

- **Feature branches**: `claude/<description>-<session-id>`
- **Bug fixes**: `fix/<description>`
- **Hotfixes**: `hotfix/<description>`
- **Experimental**: `experiment/<description>`

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semi-colons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(auth): add user authentication system
fix(api): resolve null pointer exception in user endpoint
docs(readme): update installation instructions
refactor(utils): simplify date formatting logic
```

### Git Operations Best Practices

#### Pushing Changes
- Always use: `git push -u origin <branch-name>`
- Branch names must start with `claude/` and end with the session ID
- If push fails due to network errors, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)

#### Fetching/Pulling
- Prefer fetching specific branches: `git fetch origin <branch-name>`
- For pulls use: `git pull origin <branch-name>`
- Apply the same retry logic as pushing for network failures

### Pull Request Guidelines

1. **PR Title**: Should be descriptive and follow commit message conventions
2. **PR Description**: Should include:
   - Summary of changes (1-3 bullet points)
   - Motivation and context
   - Testing performed
   - Screenshots (if UI changes)

3. **Before Creating PR**:
   - Ensure all tests pass
   - Update documentation
   - Rebase on latest main if needed
   - Review your own changes

---

## Code Style & Best Practices

### General Principles

1. **KISS (Keep It Simple, Stupid)**
   - Write simple, readable code
   - Avoid over-engineering
   - Don't add features that aren't requested

2. **DRY (Don't Repeat Yourself)**
   - Extract repeated logic into reusable functions
   - But avoid premature abstraction

3. **YAGNI (You Aren't Gonna Need It)**
   - Don't implement features for hypothetical future requirements
   - Build what's needed now

### Security Best Practices

- Never commit secrets, API keys, or credentials
- Validate all user inputs at system boundaries
- Protect against common vulnerabilities:
  - SQL Injection
  - XSS (Cross-Site Scripting)
  - CSRF (Cross-Site Request Forgery)
  - Command Injection
  - Path Traversal

### Error Handling

- Only add error handling for realistic scenarios
- Trust internal code and framework guarantees
- Validate at system boundaries (user input, external APIs)
- Provide meaningful error messages

### Code Documentation

- Add comments only where logic isn't self-evident
- Use clear, descriptive variable and function names
- Document complex algorithms and business logic
- Keep documentation close to the code it describes

---

## Testing Strategy

### Testing Pyramid

```
    /\
   /  \    E2E Tests (Few)
  /____\
 /      \   Integration Tests (Some)
/________\  Unit Tests (Many)
```

### Test Guidelines

1. **Unit Tests**
   - Test individual functions and components in isolation
   - Mock external dependencies
   - Aim for high coverage of business logic

2. **Integration Tests**
   - Test interactions between components
   - Verify API contracts
   - Test database operations

3. **E2E Tests**
   - Test critical user journeys
   - Verify the entire system works together
   - Keep these minimal due to maintenance cost

### Running Tests

```bash
# Run all tests
# npm test / pytest / etc.

# Run specific test file
# npm test <file> / pytest <file> / etc.

# Run with coverage
# npm run test:coverage / pytest --cov / etc.
```

---

## AI Assistant Guidelines

### When Working on This Repository

1. **Always Read Before Modifying**
   - Never propose changes to code you haven't read
   - Understand existing patterns before suggesting modifications

2. **Use the TodoWrite Tool**
   - Create a todo list for multi-step tasks (3+ steps)
   - Update task status in real-time
   - Mark tasks complete immediately after finishing

3. **Prefer Existing Tools**
   - Use Read/Edit/Write tools instead of bash commands for file operations
   - Use specialized tools when available

4. **Stay Focused**
   - Only make changes that are directly requested or clearly necessary
   - Don't add unsolicited features, refactoring, or "improvements"
   - A bug fix doesn't need surrounding code cleaned up

5. **Avoid Over-Engineering**
   - Don't add error handling for scenarios that can't happen
   - Don't create helpers/utilities for one-time operations
   - Don't design for hypothetical future requirements
   - Three similar lines of code is better than a premature abstraction

6. **Security First**
   - Be careful not to introduce security vulnerabilities
   - If you notice insecure code you wrote, fix it immediately
   - Don't commit files that likely contain secrets (.env, credentials.json, etc.)

7. **No Backwards Compatibility Hacks**
   - Don't rename unused variables with `_prefix`
   - Don't re-export types that aren't needed
   - Don't add `// removed` comments for deleted code
   - If something is unused, delete it completely

### Git Workflow for AI Assistants

1. **Check Current Branch**
   ```bash
   git status
   git branch -a
   ```

2. **Create/Switch to Feature Branch**
   ```bash
   git checkout -b claude/<description>-<session-id>
   ```

3. **Make Changes**
   - Use Read/Edit/Write tools
   - Follow code style guidelines

4. **Commit Changes** (only when explicitly requested)
   ```bash
   git status
   git diff
   git log --oneline -5
   git add <files>
   git commit -m "$(cat <<'EOF'
   <type>(<scope>): <description>
   EOF
   )"
   ```

5. **Push Changes**
   ```bash
   git push -u origin <branch-name>
   ```

### Creating Pull Requests

When explicitly requested to create a PR:

1. **Review all changes**
   ```bash
   git status
   git diff origin/main...HEAD
   git log origin/main...HEAD
   ```

2. **Create PR**
   ```bash
   gh pr create --title "title" --body "$(cat <<'EOF'
   ## Summary
   - Bullet points of changes

   ## Test plan
   - Testing steps
   EOF
   )"
   ```

---

## Common Tasks

### Adding a New Feature

1. Understand the requirement
2. Create a todo list with steps
3. Read relevant existing code
4. Implement the feature
5. Write tests
6. Update documentation
7. Commit and push (if requested)

### Fixing a Bug

1. Reproduce the bug
2. Locate the problematic code
3. Understand the root cause
4. Implement the fix
5. Add a test to prevent regression
6. Commit and push (if requested)

### Refactoring Code

1. Ensure tests exist for the code being refactored
2. Make incremental changes
3. Run tests after each change
4. Keep refactoring separate from feature changes
5. Commit and push (if requested)

### Updating Dependencies

1. Check for breaking changes in changelogs
2. Update one dependency at a time (for major versions)
3. Run tests after each update
4. Fix any breaking changes
5. Commit and push (if requested)

---

## Project-Specific Information

> **Note**: This section should be updated with project-specific details as the codebase evolves.

### Architecture Decisions

- [To be documented]

### Third-Party Dependencies

- [To be documented]

### API Endpoints

- [To be documented]

### Database Schema

- [To be documented]

### Environment Variables

- [To be documented]

### Deployment Process

- [To be documented]

---

## Resources

### Documentation
- [Project README](./README.md)
- [API Documentation](./docs/api.md) (if applicable)
- [Architecture Decisions](./docs/architecture.md) (if applicable)

### External Resources
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)

---

## Maintenance

This document should be updated whenever:
- Project structure changes significantly
- New conventions are established
- Development workflows are modified
- New tools or frameworks are adopted
- Security practices are updated

**Last Updated**: 2025-11-24
**Maintained By**: AI Assistants working on this repository

---

## Questions or Issues?

If this document is unclear or missing important information:
1. Ask the human developer for clarification
2. Update this document with the new information
3. Commit the changes for future reference
