#!/usr/bin/env python3
"""
Validate a skill directory by checking SKILL.md structure and frontmatter.

Usage:
    python -m scripts.quick_validate <path/to/skill-folder>
"""

import re
import sys
from pathlib import Path


def validate_skill(skill_path: str) -> tuple[bool, str]:
    """
    Validate a skill directory.

    Args:
        skill_path: Path to the skill directory

    Returns:
        Tuple of (is_valid, error_message)
    """
    skill_dir = Path(skill_path)

    # Check directory exists
    if not skill_dir.exists():
        return False, f"Directory does not exist: {skill_path}"

    if not skill_dir.is_dir():
        return False, f"Path is not a directory: {skill_path}"

    # Check SKILL.md exists
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False, "Missing required file: SKILL.md"

    # Read and parse SKILL.md
    try:
        content = skill_md.read_text()
    except Exception as e:
        return False, f"Failed to read SKILL.md: {e}"

    # Check frontmatter delimiters
    if not content.startswith("---"):
        return False, "SKILL.md must start with '---' frontmatter delimiter"

    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return False, "SKILL.md frontmatter missing closing '---' delimiter"

    frontmatter = content[3:end_match.start() + 3]

    # Validate name field
    name_match = re.search(r'^name:\s*["\']?([^"\'\n]+)["\']?\s*$', frontmatter, re.MULTILINE)
    if not name_match:
        return False, "Missing required frontmatter field: name"

    name = name_match.group(1).strip()

    # Validate name format (kebab-case, 1-64 chars)
    if not re.match(r'^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$', name):
        return False, f"Invalid name format: '{name}'. Must be kebab-case (lowercase letters, numbers, hyphens), no leading/trailing hyphens"

    if len(name) > 64:
        return False, f"Name too long: {len(name)} chars (max 64)"

    # Validate description field
    desc_match = re.search(r'^description:\s*', frontmatter, re.MULTILINE)
    if not desc_match:
        return False, "Missing required frontmatter field: description"

    # Extract full description for length check
    desc_content_match = re.search(r'^description:\s*([>|][-]?)?\s*(.*)$', frontmatter, re.MULTILINE)
    if desc_content_match:
        multiline = desc_content_match.group(1)
        first_line = desc_content_match.group(2).strip()

        if multiline:
            # Collect multiline content
            lines = [first_line] if first_line else []
            remaining = frontmatter[desc_content_match.end():]
            for line in remaining.split('\n'):
                if line.startswith('  ') or line.startswith('\t'):
                    lines.append(line.strip())
                elif line.strip() and not line.startswith(' '):
                    break
            description = ' '.join(lines)
        else:
            description = first_line

        if len(description) > 1024:
            return False, f"Description too long: {len(description)} chars (max 1024)"

        if '<' in description or '>' in description:
            return False, "Description contains angle brackets (< or >), which are not allowed"

    # Check for unexpected frontmatter keys
    allowed_keys = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}
    found_keys = set(re.findall(r'^([a-z-]+):', frontmatter, re.MULTILINE))
    unexpected = found_keys - allowed_keys
    if unexpected:
        return False, f"Unexpected frontmatter keys: {', '.join(sorted(unexpected))}"

    # Validate optional fields if present
    compat_match = re.search(r'^compatibility:\s*(.+)$', frontmatter, re.MULTILINE)
    if compat_match and len(compat_match.group(1)) > 500:
        return False, f"Compatibility field too long: {len(compat_match.group(1))} chars (max 500)"

    return True, "Skill validation passed"


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m scripts.quick_validate <path/to/skill-folder>")
        sys.exit(1)

    skill_path = sys.argv[1]
    is_valid, message = validate_skill(skill_path)

    print(message)
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
