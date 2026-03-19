---
name: mvp-launcher
description: End-to-end MVP builder that takes an idea and delivers a fully deployed product. Orchestrates discovery, branding, UI/UX design, React/Next.js code generation with shadcn/ui, Vercel deployment, and launch kit creation in a single guided workflow. Use this skill whenever the user wants to build an app, create a product, launch an MVP, start a new project from scratch, prototype an idea, build a SaaS, create a dashboard, make a landing page, or says anything like "I have an idea for..." or "build me a..." or "I want to create...". Even if they just mention an app concept casually, this skill turns it into a shipped product.
---

# MVP Launcher

Turn an idea into a live, deployed product. This skill runs a 6-phase pipeline — each phase builds on the previous one, and you end up with a real app running on Vercel with branding, responsive UI, and a launch kit.

The magic is in the orchestration: instead of asking the user to make dozens of micro-decisions, each phase makes smart defaults based on context from earlier phases. The user steers at the phase level, not the pixel level.

## The Pipeline

```
💡 Discovery → 🎨 Brand → 🖼️ Design → ⚡ Build → 🚀 Deploy → 📦 Launch Kit
```

Run phases sequentially. After each phase, present a brief summary and ask for a thumbs-up before moving on. If the user says "just go" or "do everything", skip the check-ins and run the full pipeline.

## Phase 1: Discovery (5 min)

The goal is to understand what we're building in enough detail to make good decisions in later phases — but not so much detail that we're doing waterfall planning. This is an MVP, so scope should be ruthlessly small.

### Interview

Ask these questions conversationally (not as a numbered list). Adapt based on what the user already told you:

1. **What's the core problem?** — One sentence. If the user gives you a paragraph, distill it.
2. **Who's the user?** — Persona in 2-3 words (e.g., "small restaurant owners", "freelance designers")
3. **What's the one thing it must do?** — The single most important feature. Not three things. One.
4. **What's the vibe?** — Professional? Playful? Minimal? Dark mode? Ask casually: "what should it feel like?"

### Output

Create a `discovery.md` file in the project root:

```markdown
# [Product Name] — Discovery

## Problem
[One sentence]

## Target User
[2-3 words]

## Core Feature
[One thing the MVP does]

## Vibe
[2-3 adjectives]

## Scope Boundaries
- IN: [what we're building]
- OUT: [what we're explicitly not building yet]
```

Keep the discovery doc under 30 lines. If you're writing more, you're overthinking it.

## Phase 2: Brand (2 min)

Generate a complete brand identity based on the discovery. The user shouldn't need to pick colors from a wheel — make confident choices and present them.

### What to Generate

1. **Product Name** — if the user hasn't named it yet, suggest 3 options (short, memorable, domain-available-feeling). Let them pick or go with your top choice.

2. **Color Palette** — 5 colors total:
   - Primary (brand color — used for CTAs, headers)
   - Secondary (complement — used for accents)
   - Background (light or dark based on vibe)
   - Surface (cards, containers)
   - Text (high contrast against background)

   Reference the ui-ux-pro-max skill's palette database if available. Match colors to the vibe from discovery.

3. **Typography** — Pick a font pairing:
   - Headings: something with personality matching the vibe
   - Body: highly readable, clean
   - Use Google Fonts only (free, easy to load)

   Reference ui-ux-pro-max font pairing database if available.

4. **Logo Concept** — Generate a simple SVG logo. Keep it to:
   - An icon (geometric shape or simple symbol) + wordmark
   - Use the primary color
   - Must work at 32x32 (favicon) and 200px wide

### Output

Create `brand.md` in the project root with all decisions, plus:
- `public/logo.svg` — the logo
- `public/favicon.svg` — 32x32 version
- Save color tokens as CSS custom properties (they'll be used in Phase 4)

```markdown
# Brand Guide — [Product Name]

## Colors
| Token | Hex | Usage |
|-------|-----|-------|
| --primary | #... | CTAs, links, active states |
| --secondary | #... | Accents, highlights |
| --background | #... | Page background |
| --surface | #... | Cards, modals |
| --text | #... | Body text |

## Typography
- **Headings:** [Font] — [why it fits]
- **Body:** [Font] — [why it's readable]
- **Google Fonts import:** `[URL]`

## Logo
See `public/logo.svg`
```

## Phase 3: Design (5 min)

Plan the UI architecture. The goal isn't pixel-perfect mockups — it's a clear component tree and page structure that makes Phase 4 fast and consistent.

### Page Map

Define every page/route the MVP needs. For most MVPs this is 2-4 pages:

```
/               → Landing/Home (hero, features, CTA)
/app            → Main app view (the core feature)
/app/[detail]   → Detail view (if needed)
```

Resist the urge to add pages. Every page added doubles the build time.

### Component Architecture

For each page, define the component tree. Follow React composition patterns:

```
HomePage
├── Navbar (logo, nav links, CTA button)
├── HeroSection (headline, subtext, CTA, hero image/illustration)
├── FeaturesGrid (3-4 feature cards)
├── Footer (links, copyright)
```

Reference the composition-patterns skill for compound component patterns where relevant (e.g., data tables, forms with validation, multi-step wizards).

### Design Decisions

For each component, note:
- Which shadcn/ui component to use (Button, Card, Dialog, etc.)
- Layout approach (flex, grid, with breakpoints)
- Key interactions (hover states, transitions, loading states)

### Output

Create `design.md` in the project root:

```markdown
# Design — [Product Name]

## Pages
[Route map with descriptions]

## Component Tree
[ASCII tree for each page]

## shadcn/ui Components Needed
[List with installation commands]

## Responsive Strategy
- Mobile: [approach]
- Desktop: [approach]
```

## Phase 4: Build (15-30 min)

This is the big phase. Generate a complete, working Next.js application.

### Tech Stack (Fixed)

These choices are non-negotiable — they're optimized for speed, quality, and deployability:

- **Framework:** Next.js 14+ (App Router)
- **UI:** shadcn/ui + Tailwind CSS
- **Language:** TypeScript
- **Icons:** Lucide React
- **Fonts:** Google Fonts (from Phase 2)
- **State:** React hooks (useState, useReducer) — no external state libs for MVP
- **Data:** Local state or mock data — no database for v1 unless explicitly needed

### Project Setup

```bash
npx create-next-app@latest [project-name] --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
```

Then install shadcn/ui and needed components:

```bash
npx shadcn@latest init
npx shadcn@latest add [components from Phase 3]
```

### Code Quality Standards

Follow react-best-practices skill guidelines:
- Server Components by default, Client Components only when needed (interactivity, hooks)
- No prop drilling — use composition and context where appropriate
- Responsive from the start — mobile-first breakpoints
- Accessible — proper ARIA labels, keyboard navigation, color contrast
- Performance — lazy load below-fold content, optimize images with next/image

### Brand Integration

Apply the brand from Phase 2:
- Set CSS custom properties in `globals.css` using the color tokens
- Configure Tailwind `theme.extend` with brand colors
- Load Google Fonts in `layout.tsx`
- Place logo in Navbar

### File Structure

```
src/
├── app/
│   ├── layout.tsx          (root layout with fonts, metadata)
│   ├── page.tsx            (landing page)
│   ├── globals.css         (brand tokens + tailwind)
│   └── [app-routes]/
├── components/
│   ├── ui/                 (shadcn components)
│   ├── layout/             (Navbar, Footer, Sidebar)
│   └── features/           (domain-specific components)
├── lib/
│   └── utils.ts            (shadcn utils + helpers)
└── public/
    ├── logo.svg
    └── favicon.svg
```

### Build Verification

After generating all code, run:

```bash
npm run build
```

If the build fails, fix the errors before moving on. A failing build means deployment will fail. Do not skip this step.

## Phase 5: Deploy (2 min)

Ship it to the internet.

### Deployment Steps

1. Initialize git repo and commit all code
2. Deploy to Vercel using the deploy-to-vercel skill or CLI:

```bash
cd [project-name]
git init && git add -A && git commit -m "Initial MVP launch"
npx vercel --yes
```

3. If the user has a custom domain, configure it
4. Verify the deployment is live by checking the URL

### Output

Save the live URL. You'll need it for the Launch Kit.

## Phase 6: Launch Kit (3 min)

Generate everything the user needs to share and promote their new product.

### Generate These Files

1. **README.md** — Professional project README:
   ```markdown
   # [Product Name]
   [One-line description]

   🌐 **Live:** [deployed-url]

   ## Features
   - [Feature 1]
   - [Feature 2]

   ## Tech Stack
   [Stack list]

   ## Getting Started
   [Local dev instructions]

   ## License
   MIT
   ```

2. **OG Image** — Create an HTML file that renders a 1200x630 Open Graph image:
   - Product name in heading font
   - One-line tagline
   - Brand colors as background
   - Logo in corner
   - Save as `public/og.png` (or generate via an OG image route)

3. **Meta Tags** — Update `layout.tsx` with:
   - Title, description
   - Open Graph tags (title, description, image, url)
   - Twitter card tags
   - Favicon

4. **Launch Checklist** — Create `LAUNCH.md`:
   ```markdown
   # Launch Checklist — [Product Name]

   ## Done
   - [x] App built and deployed
   - [x] Branding applied
   - [x] OG image generated
   - [x] Meta tags configured
   - [x] README written

   ## Next Steps
   - [ ] Share on social media
   - [ ] Submit to Product Hunt
   - [ ] Set up analytics (Vercel Analytics or Plausible)
   - [ ] Add custom domain
   - [ ] Set up error monitoring (Sentry)
   - [ ] Plan v2 features based on user feedback
   ```

## Completion Summary

When all 6 phases are done, present a summary:

```
🎉 [Product Name] is LIVE!

🌐 URL: [deployed-url]
🎨 Brand: [primary color] + [font pairing]
📱 Pages: [count] pages, [count] components
⚡ Stack: Next.js + shadcn/ui + Tailwind
📦 Launch Kit: README, OG image, meta tags

Total time: ~30-45 minutes from idea to production

Next steps are in LAUNCH.md
```

## Adaptation Notes

Not every MVP is the same. Here's how to adapt:

- **"I just want a landing page"** — Skip Phase 4's app routes. Build only the landing page with hero, features, CTA, and footer. Still do branding and deployment.
- **"I need a dashboard"** — Lean heavily on shadcn/ui's Table, Chart, and Card components. Use mock data. Structure as a sidebar layout.
- **"I need authentication"** — Add NextAuth.js or Clerk. This adds complexity — warn the user it'll take longer.
- **"I need a database"** — Suggest Supabase for speed. Add as a Phase 3.5 with schema design.
- **"I already have a design"** — Skip Phases 2-3. Go straight to build with their design specs.

## Skill Dependencies

This skill works best alongside these other skills (reference them when relevant):
- **ui-ux-pro-max** — for style/color/typography databases
- **react-best-practices** — for React/Next.js performance patterns
- **composition-patterns** — for component architecture
- **deploy-to-vercel** — for deployment specifics
- **project-manager** — for project charter template (Phase 1)
