"""Utility functions for skill-creator scripts."""

import re
from pathlib import Path


def parse_skill_md(skill_path: str) -> tuple[str, str, str]:
    """
    Parse a SKILL.md file and extract frontmatter fields.

    Args:
        skill_path: Path to the skill directory containing SKILL.md

    Returns:
        Tuple of (name, description, full_content)

    Raises:
        ValueError: If frontmatter is malformed
        FileNotFoundError: If SKILL.md doesn't exist
    """
    skill_md_path = Path(skill_path) / "SKILL.md"
    if not skill_md_path.exists():
        raise FileNotFoundError(f"SKILL.md not found at {skill_md_path}")

    content = skill_md_path.read_text()

    # Find frontmatter
    if not content.startswith("---"):
        raise ValueError("SKILL.md must start with '---' frontmatter delimiter")

    # Find closing delimiter
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        raise ValueError("SKILL.md frontmatter missing closing '---' delimiter")

    frontmatter = content[3:end_match.start() + 3]

    # Extract name
    name_match = re.search(r'^name:\s*["\']?([^"\'\n]+)["\']?\s*$', frontmatter, re.MULTILINE)
    if not name_match:
        raise ValueError("SKILL.md frontmatter missing 'name' field")
    name = name_match.group(1).strip()

    # Extract description (supports multiline YAML)
    desc_match = re.search(r'^description:\s*([>|][-]?)?\s*(.*)$', frontmatter, re.MULTILINE)
    if not desc_match:
        raise ValueError("SKILL.md frontmatter missing 'description' field")

    multiline_indicator = desc_match.group(1)
    first_line = desc_match.group(2).strip()

    if multiline_indicator:
        # Multiline description - collect indented lines
        lines = [first_line] if first_line else []
        remaining = frontmatter[desc_match.end():]
        for line in remaining.split('\n'):
            if line.startswith('  ') or line.startswith('\t'):
                lines.append(line.strip())
            elif line.strip() and not line.startswith(' '):
                break
            elif not line.strip():
                continue
        description = ' '.join(lines)
    else:
        description = first_line

    return name, description, content
