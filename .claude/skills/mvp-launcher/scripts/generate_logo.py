#!/usr/bin/env python3
"""Generate a simple SVG logo with icon + wordmark.

Usage:
    python generate_logo.py --name "AppName" --primary "#6366F1" --style geometric \
        --output public/logo.svg --favicon public/favicon.svg

Styles: geometric, rounded, abstract, letter, minimal
"""

import argparse
from pathlib import Path


ICONS = {
    "geometric": lambda c: f'''<rect x="4" y="4" width="24" height="24" rx="4" fill="{c}" opacity="0.9"/>
    <rect x="10" y="10" width="12" height="12" rx="2" fill="white" opacity="0.9"/>''',

    "rounded": lambda c: f'''<circle cx="16" cy="16" r="14" fill="{c}"/>
    <circle cx="16" cy="16" r="7" fill="white" opacity="0.9"/>''',

    "abstract": lambda c: f'''<path d="M16 2 L30 28 L2 28 Z" fill="{c}" opacity="0.8"/>
    <path d="M16 10 L24 26 L8 26 Z" fill="white" opacity="0.8"/>''',

    "minimal": lambda c: f'''<rect x="2" y="8" width="28" height="4" rx="2" fill="{c}"/>
    <rect x="2" y="16" width="20" height="4" rx="2" fill="{c}" opacity="0.6"/>
    <rect x="2" y="24" width="12" height="4" rx="2" fill="{c}" opacity="0.3"/>''',
}


def generate_logo(name: str, primary: str, style: str) -> str:
    icon_fn = ICONS.get(style, ICONS["geometric"])
    icon_svg = icon_fn(primary)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 32" height="32">
  <g transform="translate(0, 0)">
    {icon_svg}
  </g>
  <text x="40" y="24" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{primary}">{name}</text>
</svg>'''


def generate_favicon(primary: str, style: str) -> str:
    icon_fn = ICONS.get(style, ICONS["geometric"])
    icon_svg = icon_fn(primary)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  {icon_svg}
</svg>'''


def letter_logo(name: str, primary: str) -> str:
    letter = name[0].upper()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 32" height="32">
  <rect x="2" y="2" width="28" height="28" rx="6" fill="{primary}"/>
  <text x="16" y="24" font-family="system-ui, sans-serif" font-size="20" font-weight="700" fill="white" text-anchor="middle">{letter}</text>
  <text x="40" y="24" font-family="system-ui, sans-serif" font-size="20" font-weight="700" fill="{primary}">{name}</text>
</svg>'''


def letter_favicon(name: str, primary: str) -> str:
    letter = name[0].upper()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect x="2" y="2" width="28" height="28" rx="6" fill="{primary}"/>
  <text x="16" y="24" font-family="system-ui, sans-serif" font-size="20" font-weight="700" fill="white" text-anchor="middle">{letter}</text>
</svg>'''


def main():
    parser = argparse.ArgumentParser(description="Generate SVG logo")
    parser.add_argument("--name", required=True, help="Product name")
    parser.add_argument("--primary", default="#6366F1", help="Primary brand color")
    parser.add_argument("--style", default="geometric",
                       choices=["geometric", "rounded", "abstract", "letter", "minimal"],
                       help="Icon style")
    parser.add_argument("--output", default="logo.svg", help="Logo output path")
    parser.add_argument("--favicon", default="favicon.svg", help="Favicon output path")
    args = parser.parse_args()

    # Generate logo
    if args.style == "letter":
        logo_svg = letter_logo(args.name, args.primary)
        fav_svg = letter_favicon(args.name, args.primary)
    else:
        logo_svg = generate_logo(args.name, args.primary, args.style)
        fav_svg = generate_favicon(args.primary, args.style)

    logo_path = Path(args.output)
    logo_path.parent.mkdir(parents=True, exist_ok=True)
    logo_path.write_text(logo_svg)
    print(f"✅ Logo generated: {logo_path}")

    fav_path = Path(args.favicon)
    fav_path.parent.mkdir(parents=True, exist_ok=True)
    fav_path.write_text(fav_svg)
    print(f"✅ Favicon generated: {fav_path}")


if __name__ == "__main__":
    main()
