# CLAUDE.md

This repo is a collection of Claude Skills. Each skill lives in a category subfolder
and follows the structure described in CONTRIBUTING.md.

## When Working in This Repo

- Do not modify `SKILL.md` or reference files without understanding the skill's domain context
- After editing any skill, run `python count-skill-tokens.py <category>/<skill-name>` to
  verify it stays within token limits
- Keep `SKILL.md` lean — move supplementary content to `references/*.md`
- Update the root `README.md` skills table when adding a new skill

## Token Limits

| File | Lines | Tokens |
|------|-------|--------|
| SKILL.md | ≤ 500 | ≤ 5,000 |
| Frontmatter description | — | ≤ 100 |
| references/*.md | no limit | no limit |
