# Page Patterns

Common page structures for different MVP types. Copy the component tree that matches your product.

## Landing Page (Every MVP needs this)

```
LandingPage
├── Navbar
│   ├── Logo
│   ├── NavLinks (Features, Pricing, About)
│   └── CTAButton ("Get Started" / "Try Free")
├── HeroSection
│   ├── Badge ("New" / "Beta" / tagline)
│   ├── Headline (max 8 words)
│   ├── Subheadline (max 20 words)
│   ├── CTAGroup
│   │   ├── PrimaryButton ("Start Free")
│   │   └── SecondaryButton ("See Demo")
│   └── HeroVisual (screenshot / illustration / animation)
├── LogoCloud (optional — "Trusted by..." social proof)
├── FeaturesSection
│   ├── SectionHeader ("Features" heading + subtext)
│   └── FeatureGrid (3 or 6 cards)
│       └── FeatureCard (icon + title + description)
├── HowItWorks (optional — 3 steps)
│   └── StepCard (number + title + description)
├── TestimonialsSection (optional)
│   └── TestimonialCard (quote + name + role + avatar)
├── PricingSection (optional)
│   └── PricingCard (tier + price + features + CTA)
├── CTASection (final call-to-action banner)
│   ├── Headline
│   └── CTAButton
└── Footer
    ├── Logo + tagline
    ├── LinkColumns (Product, Company, Legal)
    └── Copyright
```

### Hero Variants

**Centered Hero** (most common for SaaS):
```
[           Badge           ]
[     Big Bold Headline     ]
[   Supporting subheadline  ]
[  [Primary CTA] [Secondary CTA]  ]
[       Screenshot/Visual          ]
```

**Split Hero** (product + visual side by side):
```
[  Headline        |  Screenshot  ]
[  Subheadline     |  or Visual   ]
[  [CTA] [CTA]    |              ]
```

## Dashboard App

```
DashboardLayout
├── Sidebar
│   ├── Logo
│   ├── NavItems
│   │   ├── NavItem (icon + label, active state)
│   │   └── ...
│   ├── Spacer
│   └── UserMenu (avatar + name + dropdown)
├── TopBar (mobile: hamburger menu + breadcrumb)
└── MainContent
    ├── PageHeader (title + description + action buttons)
    ├── StatsGrid (4 metric cards)
    │   └── StatCard (label + value + trend indicator)
    ├── ContentArea
    │   ├── DataTable or CardGrid
    │   └── Pagination
    └── EmptyState (when no data)
```

## CRUD App (Task Manager, Inventory, etc.)

```
CRUDLayout
├── Navbar (with search)
├── MainContent
│   ├── ActionBar
│   │   ├── SearchInput
│   │   ├── FilterDropdowns
│   │   └── CreateButton (opens dialog)
│   ├── ItemList
│   │   └── ItemRow (data + edit + delete actions)
│   ├── EmptyState
│   └── Pagination
├── CreateDialog (form with validation)
├── EditDialog (pre-filled form)
└── DeleteConfirmation (alert dialog)
```

## Marketplace / Directory

```
MarketplacePage
├── Navbar (with search bar prominent)
├── SearchHero
│   ├── Headline
│   ├── SearchInput (large, centered)
│   └── PopularTags
├── FilterSidebar
│   ├── CategoryFilter
│   ├── PriceFilter
│   └── RatingFilter
├── ResultsGrid
│   └── ListingCard (image + title + price + rating)
├── Pagination
└── Footer
```

## Multi-Step Form / Wizard

```
WizardLayout
├── ProgressBar (step 1 of N)
├── StepContent
│   ├── StepTitle
│   ├── StepDescription
│   └── FormFields (varies per step)
├── NavigationButtons
│   ├── BackButton
│   └── NextButton / SubmitButton
└── StepIndicator (dots or numbered list)
```

## Responsive Patterns

### Mobile Adaptations
- **Navbar** → Hamburger menu with Sheet (slide-out)
- **Sidebar** → Bottom tab bar or hamburger
- **Grid columns** → Stack vertically (1 column)
- **Tables** → Card list on mobile
- **Dialogs** → Full-screen on mobile (Drawer component)

### Breakpoints
```
sm:  640px  (mobile landscape)
md:  768px  (tablet)
lg:  1024px (desktop)
xl:  1280px (wide desktop)
```
