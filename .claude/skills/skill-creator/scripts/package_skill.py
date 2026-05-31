#!/usr/bin/env python3
"""
Package a skill directory into a distributable .skill file.

Usage:
    python -m scripts.package_skill <path/to/skill-folder> [output-directory]
"""

import os
import sys
import zipfile
from pathlib import Path

from .quick_validate import validate_skill


# Directories to exclude from packaging
EXCLUDED_DIRS = {
    '__pycache__',
    'node_modules',
    '.git',
    '.venv',
    'venv',
    'env',
}

# Files to exclude from packaging
EXCLUDED_FILES = {
    '.DS_Store',
    'Thumbs.db',
    '.gitignore',
}

# Extensions to exclude
EXCLUDED_EXTENSIONS = {
    '.pyc',
    '.pyo',
}


def should_exclude(path: Path, skill_root: Path) -> bool:
    """Check if a path should be excluded from packaging."""
    # Check directory exclusions
    for part in path.parts:
        if part in EXCLUDED_DIRS:
            return True

    # Check file exclusions
    if path.name in EXCLUDED_FILES:
        return True

    # Check extension exclusions
    if path.suffix in EXCLUDED_EXTENSIONS:
        return True

    # Exclude evals folder at skill root only
    rel_path = path.relative_to(skill_root)
    if rel_path.parts and rel_path.parts[0] == 'evals':
        return True

    return False


def package_skill(skill_path: str, output_dir: str | None = None) -> str | None:
    """
    Package a skill directory into a .skill file.

    Args:
        skill_path: Path to the skill directory
        output_dir: Optional output directory (defaults to current directory)

    Returns:
        Path to the created .skill file, or None on failure
    """
    skill_dir = Path(skill_path).resolve()

    # Validate first
    is_valid, message = validate_skill(str(skill_dir))
    if not is_valid:
        print(f"Validation failed: {message}")
        return None

    # Determine output path
    skill_name = skill_dir.name
    output_path = Path(output_dir) if output_dir else Path.cwd()
    output_path = output_path / f"{skill_name}.skill"

    # Create the zip file
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(skill_dir):
                root_path = Path(root)

                # Filter out excluded directories (modifying dirs in-place)
                dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

                for file in files:
                    file_path = root_path / file

                    if should_exclude(file_path, skill_dir):
                        continue

                    # Add file with relative path
                    rel_path = file_path.relative_to(skill_dir)
                    zf.write(file_path, rel_path)

        print(f"Created: {output_path}")
        return str(output_path)

    except Exception as e:
        print(f"Failed to create package: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m scripts.package_skill <path/to/skill-folder> [output-directory]")
        sys.exit(1)

    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    result = package_skill(skill_path, output_dir)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
