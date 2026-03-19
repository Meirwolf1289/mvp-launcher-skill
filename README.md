# 🚀 MVP Launcher — Skill for Claude Code

**From idea to deployed product in 30 minutes.**

A Claude Code skill that orchestrates the complete MVP pipeline:

```
💡 Discovery → 🎨 Brand → 🖼️ Design → ⚡ Build → 🚀 Deploy → 📦 Launch Kit
```

## What It Does

Tell Claude your app idea. It handles the rest:

1. **Discovery** — Interviews you to define scope, target user, and core feature
2. **Brand** — Generates name, color palette, typography, SVG logo & favicon
3. **Design** — Plans page structure, component tree, shadcn/ui components
4. **Build** — Generates a complete Next.js + TypeScript + Tailwind + shadcn/ui app
5. **Deploy** — Ships to Vercel with a live URL
6. **Launch Kit** — Creates README, OG image, meta tags, and launch checklist

## Installation

### Claude Code (Plugin — recommended)
```bash
claude marketplace add https://github.com/Meirwolf1289/mvp-launcher-skill.git
claude plugin install mvp-launcher
```

### Claude Code (Manual)
```bash
git clone https://github.com/Meirwolf1289/mvp-launcher-skill.git /tmp/mvp-launcher
cp -r /tmp/mvp-launcher/.claude/skills/mvp-launcher ~/.claude/skills/
```

### Cowork / Claude.ai
Add the marketplace and install:
```bash
claude marketplace add https://github.com/Meirwolf1289/mvp-launcher-skill.git
claude plugin install mvp-launcher
```
Or copy the `SKILL.md` contents into your project knowledge.

## Usage

Just tell Claude what you want to build:

```
"I want to build a task management app for small teams"
"Build me a SaaS dashboard for tracking sales metrics"
"I have an idea for a restaurant reservation system"
"Create a portfolio website for a photographer"
```

The skill triggers automatically and guides you through each phase.

## Tech Stack (Fixed)

| Layer | Technology |
|-------|-----------|
| Framework | Next.js 14+ (App Router) |
| UI | shadcn/ui + Tailwind CSS |
| Language | TypeScript |
| Icons | Lucide React |
| Deploy | Vercel |

## Included Tools

| Script | Purpose |
|--------|---------|
| `setup_project.sh` | Scaffolds Next.js + shadcn/ui project |
| `generate_logo.py` | Creates SVG logo + favicon (5 styles) |
| `generate_og_image.py` | Creates 1200x630 OG image HTML |

## References

| File | Content |
|------|---------|
| `brand-palettes.md` | 10 pre-built color palettes + 10 font pairings |
| `page-patterns.md` | Component trees for landing pages, dashboards, CRUD apps, marketplaces |
| `tech-stack.md` | Stack decisions, shadcn/ui component reference, optional add-ons |

## Works Best With

- [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — 67 styles, 96 palettes, 57 font pairings
- [react-best-practices](https://github.com/vercel-labs/agent-skills) — React/Next.js performance rules
- [deploy-to-vercel](https://github.com/vercel-labs/agent-skills) — Vercel deployment automation
- [project-manager](https://github.com/Meirwolf1289/project-manager-skill) — Sprint planning & PM workflows

## Example Output

After running the full pipeline you get:
- ✅ Live app on Vercel with custom branding
- ✅ SVG logo + favicon
- ✅ OG image for social sharing
- ✅ Complete meta tags (SEO + social)
- ✅ Professional README
- ✅ Launch checklist with next steps

## License

MIT
