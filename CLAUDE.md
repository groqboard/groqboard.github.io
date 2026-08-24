# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A static landing page for **GroqBoard** — an AI voice keyboard for Android app. Deployed via GitHub Pages at `https://groqboard.com/`. No build system, no dependencies, no package manager.

## Files

- `index.html` — The entire landing page: all CSS (inline `<style>`), all JS (inline `<script>`), and all HTML in one file (~2800+ lines)
- `privacy.html` — Privacy policy page
- `robots.txt` / `sitemap.xml` — SEO files
- `screenshot*.{jpg,png}` — Product screenshots referenced in the page
- `*.mp4` — Demo videos embedded in the page

## Development

Open `index.html` directly in a browser — no server required. For live reload during editing, you can use any static file server:

```bash
# Python
python -m http.server 8000

# Node (if available)
npx serve .
```

## Architecture: Single-File Page

All styles, scripts, and markup live in `index.html`. The page sections in order:

1. **Hero** — headline, CTA button, app store badge
2. **Stats** — download/rating numbers
3. **Features** (`#features`) — feature cards grid
4. **Wear OS** (`#wearos`) — smartwatch support
5. **Screenshots** — product screenshot carousel
6. **How It Works** (`#how-it-works`) — 3-step explainer
7. **Privacy** (`#privacy`) — privacy-first messaging
8. **Reviews** (`#reviews`) — Google Play reviews
9. **FAQ** (`#faq`) — structured FAQ (also in JSON-LD for SEO)
10. **Power Tips** (`#power-tips`) — advanced usage tips
11. **Contact** (`#contact`) — support links
12. **CTA** — final conversion section

## Design Tokens

Defined as CSS custom properties in `:root`:

- Primary brand color: `--groq-orange: #f55036`
- Background: `--bg-dark: #0a0a0a`, cards: `--bg-card: #111111`
- Fonts: `Outfit` (body/headings), `Space Mono` (monospace accents) — loaded from Google Fonts

## SEO Notes

The page contains two `<script type="application/ld+json">` blocks:
- `SoftwareApplication` schema (for Google rich results)
- `FAQPage` schema (for "People Also Ask" — must stay in sync with the visible FAQ section)

Canonical URL: `https://groqboard.com/`
GA4 property: `G-EDZFTE6DDJ`
