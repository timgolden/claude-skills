# Contributing

## Adding a New Skill

### 1. Choose a category

Skills are grouped by domain. Current categories: `midi`. Add a new category folder if
none of the existing ones fit.

### 2. Create the skill directory

```
<category>/
└── <skill-name>/
    ├── SKILL.md
    └── references/       ← optional, for supplementary content
```

Use lowercase, hyphen-separated names (e.g., `roto-control`, `disting-nt`).

### 3. Write SKILL.md

`SKILL.md` must have YAML frontmatter with `name` and `description`:

```yaml
---
name: your-skill-name
description: >
  One or two sentences describing what this skill does and when Claude should use it.
  Be specific about triggers. End with: "When in doubt, trigger."
---
```

Rules for the main content:
- **≤ 500 lines and ≤ 5,000 tokens** — heavy lookup tables, checklists, and reference
  content belong in `references/*.md` instead
- Core rules, design principles, and schema quick-references belong in `SKILL.md`
- Reference files in `references/` are loaded by Claude when needed

### 4. Check your token count

```bash
python count-skill-tokens.py <category>/<skill-name>
```

A `⚠️` next to SKILL.md means you need to move content to `references/`.

### 5. Add to the README

Add your skill to the table in the relevant category section of `README.md`.

---

## Improving an Existing Skill

- Factual corrections (schema fields, device behavior) are always welcome
- Add confirmed information in the "Known Gaps" or relevant section with a note on how it was verified
- Add new example presets in an `examples/` subdirectory if applicable

---

## Skill Quality Bar

A good skill:
- Triggers reliably (the `description` frontmatter is the key trigger signal — be specific)
- Gives Claude correct, actionable guidance rather than vague suggestions
- Distinguishes confirmed facts from inferred/unverified behavior
- Keeps SKILL.md lean so it doesn't bloat every conversation context

---

## Resources

- [Claude Skills documentation](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Creating Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [posit-dev/skills](https://github.com/posit-dev/skills) — reference implementation from Posit
