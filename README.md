# Claude Skills

A personal collection of Claude Skills covering audio hardware, R/data workflows, and other domains.

Claude Skills extend Claude's capabilities with specialized knowledge. Once installed, Claude
automatically activates the relevant skill based on your task — no explicit invocation needed.
Learn more at the [Claude Skills documentation](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

---

## Available Skills

### MIDI

Skills for MIDI hardware and controllers.

| Skill | Description |
|-------|-------------|
| [roto-control](midi/roto-control) | Design, author, and review Melbourne Instruments ROTO-CONTROL MIDI preset JSON files — schema rules, label constraints, haptic detents, LED colors, page layout, and CC allocation |

---

## Installation

### Claude.ai (Projects)

1. Open [claude.ai](https://claude.ai) and create or open a **Project**
2. Go to **Project Instructions**
3. Paste the contents of the skill's `SKILL.md` into the instructions field
4. Optionally upload any files from the skill's `skeleton/` or `schema/` directories as Project files

The skill activates for all conversations in that project.

### Claude.ai (Single conversation)

Paste the contents of `SKILL.md` at the start of any conversation. Active for that conversation only.

### Claude Code

Install a skill directory directly:

```bash
cp -r midi/roto-control ~/.config/claude-code/skills/
```

---

## Repo Structure

Each skill lives in a category folder and follows this layout:

```
<category>/
└── <skill-name>/
    ├── SKILL.md          ← Claude loads this; core rules and trigger description
    ├── references/       ← Supplementary lookup content (color tables, field refs, checklists)
    │   └── *.md
    └── <supporting-files>/   ← Templates, schemas, examples (skill-specific)
```

`SKILL.md` is kept lean (≤ 500 lines / ≤ 5,000 tokens). Heavy reference content lives in
`references/` so Claude can load it on demand without bloating the base context.

---

## Token Audit

Use `count-skill-tokens.py` to check that a skill stays within recommended limits:

```bash
# Requires: pip install tiktoken python-frontmatter
python count-skill-tokens.py midi/roto-control
```

Limits (matching [posit-dev/skills](https://github.com/posit-dev/skills) conventions):
- SKILL.md: ≤ 500 lines, ≤ 5,000 tokens
- Description (frontmatter): ≤ 100 tokens

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT. See [LICENSE](LICENSE).
