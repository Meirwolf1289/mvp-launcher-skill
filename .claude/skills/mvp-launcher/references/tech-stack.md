# Tech Stack Reference

## Core Stack (Non-negotiable)

| Layer | Technology | Why |
|-------|-----------|-----|
| Framework | Next.js 14+ (App Router) | Best DX, great deployment story, RSC support |
| UI Library | shadcn/ui | Copy-paste components, fully customizable, accessible |
| Styling | Tailwind CSS | Utility-first, works perfectly with shadcn/ui |
| Language | TypeScript | Catches bugs early, great IDE support |
| Icons | Lucide React | Consistent, tree-shakeable, large library |
| Fonts | Google Fonts | Free, fast CDN, huge selection |
| Deploy | Vercel | Zero-config for Next.js, instant previews |

## Optional Add-ons (Only when needed)

### Authentication
| Option | When to Use |
|--------|-------------|
| NextAuth.js | OSS, flexible, multiple providers |
| Clerk | Fastest setup, great UI, managed service |
| Supabase Auth | If already using Supabase for DB |

### Database
| Option | When to Use |
|--------|-------------|
| Supabase | Postgres + realtime + auth in one |
| Vercel Postgres | Simple SQL, tight Vercel integration |
| None (mock data) | Default for MVP — add DB in v2 |

### State Management
| Option | When to Use |
|--------|-------------|
| React hooks | Default — useState, useReducer, useContext |
| Zustand | When state gets complex across many components |
| TanStack Query | When fetching remote data with caching needs |

### Analytics
| Option | When to Use |
|--------|-------------|
| Vercel Analytics | Zero-config, privacy-friendly |
| Plausible | OSS alternative, EU-friendly |
| PostHog | Product analytics + session replay |

## shadcn/ui Component Quick Reference

### Layout & Navigation
- `Navbar` (custom) — build with shadcn Button, NavigationMenu
- `Sidebar` — use Sheet on mobile, fixed on desktop
- `Footer` (custom) — simple flex layout

### Data Display
- `Card` — content containers, feature grids
- `Table` — data tables with sorting
- `Badge` — status indicators, tags
- `Avatar` — user profiles

### Forms & Input
- `Input` — text fields
- `Textarea` — multiline input
- `Select` — dropdowns
- `Switch` — toggles
- `Form` — with react-hook-form + zod validation

### Feedback
- `Dialog` — modals, confirmations
- `Toast` — notifications (via sonner)
- `Alert` — inline messages
- `Skeleton` — loading placeholders

### Actions
- `Button` — primary actions (use brand primary color)
- `DropdownMenu` — more actions
- `Command` — command palette / search

### Installation Pattern
```bash
# Install specific components
npx shadcn@latest add button card input dialog toast

# Install multiple at once
npx shadcn@latest add button card input dialog toast table form select
```
