A **requirements.txt** file is a plain text document listing all Python packages a project depends on.

## Purpose

**Documentation**: Records exact dependencies needed to run the project.

**Reproducibility**: Enables identical environment setup across machines.

**Collaboration**: Others can recreate your environment with one command.

## File Format

```
pandas==2.0.1          # Exact version
numpy>=1.24.0          # Minimum version
requests               # Latest version
flask==2.3.0
```

Each line specifies a package with optional version constraints.

## Common Workflows

**Generate from current environment:**
```bash
pip freeze > requirements.txt
```

This captures all installed packages and their exact versions.

**Install from requirements file:**
```bash
pip install -r requirements.txt
```

This installs all listed packages in one command.

## Version Specifiers

**`==2.0.1`**: Exact version (most common for production).

**`>=1.24.0`**: Minimum version or higher.

**`~=2.0`**: Compatible release (2.0.x, not 2.1+).

## Relationship with Virtual Environments

requirements.txt documents **what** dependencies exist.

Virtual environments provide **where** those dependencies install.

Together they enable reproducible Python environments.

---

**Links**: [[Python MOC]] | [[Python virtual environments isolate project dependencies]]
