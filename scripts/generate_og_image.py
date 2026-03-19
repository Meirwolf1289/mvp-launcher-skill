#!/usr/bin/env python3
"""Generate an OG image as an HTML file for screenshot or Next.js OG route.

Usage:
    python generate_og_image.py --name "Product Name" --tagline "One-line description" \
        --primary "#6366F1" --background "#FFFFFF" --text "#1E1B4B" \
        --font "Inter" --output public/og.html

The generated HTML is exactly 1200x630px and can be:
1. Screenshotted to produce og.png
2. Used as reference for a Next.js OG image route
"""

import argparse
from pathlib import Path


def generate_og_html(name: str, tagline: str, primary: str, background: str,
                     text_color: str, font: str) -> str:
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family={font.replace(' ', '+')}:wght@700&display=swap" rel="stylesheet">
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    width: 1200px;
    height: 630px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: {background};
    font-family: '{font}', system-ui, sans-serif;
    position: relative;
    overflow: hidden;
}}
/* Decorative gradient orb */
.orb {{
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: {primary};
    opacity: 0.08;
    filter: blur(100px);
    top: -200px;
    right: -100px;
}}
.orb-2 {{
    position: absolute;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    background: {primary};
    opacity: 0.06;
    filter: blur(80px);
    bottom: -150px;
    left: -50px;
}}
.content {{
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 0 80px;
}}
.badge {{
    display: inline-block;
    background: {primary};
    color: white;
    padding: 8px 24px;
    border-radius: 100px;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 32px;
}}
h1 {{
    font-size: 72px;
    font-weight: 700;
    color: {text_color};
    line-height: 1.1;
    margin-bottom: 24px;
}}
p {{
    font-size: 28px;
    color: {text_color};
    opacity: 0.7;
    line-height: 1.4;
    max-width: 800px;
    margin: 0 auto;
}}
.bottom-bar {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: {primary};
}}
</style>
</head>
<body>
<div class="orb"></div>
<div class="orb-2"></div>
<div class="content">
    <div class="badge">Launch</div>
    <h1>{name}</h1>
    <p>{tagline}</p>
</div>
<div class="bottom-bar"></div>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate OG image HTML")
    parser.add_argument("--name", required=True, help="Product name")
    parser.add_argument("--tagline", required=True, help="One-line tagline")
    parser.add_argument("--primary", default="#6366F1", help="Primary brand color")
    parser.add_argument("--background", default="#FFFFFF", help="Background color")
    parser.add_argument("--text", default="#1E1B4B", help="Text color")
    parser.add_argument("--font", default="Inter", help="Google Font name")
    parser.add_argument("--output", default="og.html", help="Output file path")
    args = parser.parse_args()

    html = generate_og_html(
        name=args.name,
        tagline=args.tagline,
        primary=args.primary,
        background=args.background,
        text_color=args.text,
        font=args.font,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)
    print(f"✅ OG image HTML generated: {output_path}")
    print(f"   Size: 1200x630px")
    print(f"   Open in browser and screenshot, or use as Next.js OG route reference")


if __name__ == "__main__":
    main()
