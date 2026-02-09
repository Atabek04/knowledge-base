A **virtual environment** (venv) is an isolated Python workspace that contains its own interpreter copy and package installation directory.

## The Problem Without Virtual Environments

All packages install globally to system Python by default.

This creates version conflicts when different projects need different package versions.
Project A might need `requests==2.25.0` while Project B needs `requests==2.31.0`.
Only one version can exist in the global installation.

## How Virtual Environments Solve This

Each venv creates separate directories for:

**Python interpreter**: Isolated copy of Python binary.

**Site-packages**: Independent package installation directory.

**pip**: Project-specific package manager instance.

## Working Without Virtual Environments

You can technically develop without venvs.

But version conflicts appear immediately when working on multiple projects.
It's considered unprofessional practice in Python development.

## Common Commands

```bash
# Create virtual environment
python -m venv myenv

# Activate (Linux/Mac)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Deactivate
deactivate
```

---

**Links**: [[Python MOC]] | [[requirements.txt specifies Python package dependencies]]
