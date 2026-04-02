#!/usr/bin/env python3
"""Count lines and estimate tokens for a Claude skill directory.

Usage:
    python count-skill-tokens.py <skill-directory>
    python count-skill-tokens.py eurorack/roto-control

Requires: pip install tiktoken PyYAML

Finds SKILL.md and references/**/*.md, counts lines and tokens,
and outputs a Markdown summary table. Flags files that exceed limits.
"""

import sys
import re
from pathlib import Path

try:
    import tiktoken
except ImportError:
    print("Missing dependency: pip install tiktoken", file=sys.stderr)
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("Missing dependency: pip install PyYAML", file=sys.stderr)
    sys.exit(1)


METADATA_TOKEN_LIMIT = 100
SKILL_TOKEN_LIMIT = 5_000
SKILL_LINE_LIMIT = 500


def count_tokens(text: str, encoding: tiktoken.Encoding) -> int:
    return len(encoding.encode(text))


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from a markdown file."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    front = text[3:end].strip()
    body = text[end + 4:].lstrip()
    try:
        attrs = yaml.safe_load(front) or {}
    except yaml.YAMLError:
        attrs = {}
    return attrs, body


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <skill-directory>", file=sys.stderr)
        sys.exit(1)

    skill_dir = Path(sys.argv[1]).resolve()
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        print(f"Error: {skill_md} not found", file=sys.stderr)
        sys.exit(1)

    enc = tiktoken.get_encoding("cl100k_base")

    raw = skill_md.read_text()
    attrs, _ = parse_frontmatter(raw)
    skill_name = attrs.get("name", skill_dir.name)
    skill_description = str(attrs.get("description", "")) if attrs.get("description") else ""

    # Collect files: SKILL.md first, then references sorted alphabetically
    files: list[Path] = [skill_md]
    refs_dir = skill_dir / "references"
    if refs_dir.is_dir():
        files.extend(sorted(refs_dir.rglob("*.md")))

    rows: list[tuple[str, int, int]] = []
    total_lines = 0
    total_tokens = 0

    for f in files:
        text = f.read_text()
        n_lines = text.count("\n")
        if text and not text.endswith("\n"):
            n_lines += 1
        n_tokens = count_tokens(text, enc)
        rel_path = str(f.relative_to(skill_dir))
        rows.append((rel_path, n_lines, n_tokens))
        total_lines += n_lines
        total_tokens += n_tokens

    desc_tokens = count_tokens(skill_description, enc) if skill_description else 0

    print(f"### {skill_name} ({total_lines:,} lines, ~{total_tokens:,} tokens total)\n")

    if skill_description:
        desc_warn = " ⚠️  (exceeds 100-token limit)" if desc_tokens > METADATA_TOKEN_LIMIT else ""
        print(f"Skill description: ~{desc_tokens:,} tokens{desc_warn}")
        print(f"> {skill_description}\n")

    print("| File | Lines | ~Tokens | |")
    print("|------|------:|--------:|-|")
    for rel_path, n_lines, n_tokens in rows:
        warn = ""
        if rel_path == "SKILL.md":
            issues = []
            if n_tokens > SKILL_TOKEN_LIMIT:
                issues.append(f"exceeds {SKILL_TOKEN_LIMIT:,}-token limit")
            if n_lines > SKILL_LINE_LIMIT:
                issues.append(f"exceeds {SKILL_LINE_LIMIT}-line limit")
            if issues:
                warn = f"⚠️  {', '.join(issues)}"
        print(f"| {rel_path} | {n_lines:,} | {n_tokens:,} | {warn}")


if __name__ == "__main__":
    main()
