# Minnesota Medicare Enrollment

Static lead-generation site for **ECOS Medicare Solutions** (Darin Weidauer, NPN 18580338) serving Minnesota — https://minnesotamedicareenrollment.com

## What's here

- `*.html` at the repo root — the site (40 indexable pages + thank-you + 404). Served at clean URLs (`/duluth`, `/medicare-cost-plans`).
- `site.css`, `site.js`, `analytics.js`, `favicon.svg`, `og-image.png`, `darin.jpg` — shared assets.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt` — crawl and AI-discovery files.
- `vercel.json` (clean URLs, security headers), `CNAME` + `.nojekyll` (GitHub Pages fallback).
- `source/` — **the generator.** `generate.py` builds every page from `content.py` (topic pages), the city/region tables, and `site.css`; `scenes.py` draws the hero illustrations; `og.py` renders the share image.

## Editing

```bash
python3 source/generate.py     # rebuild every page + sitemap + llms files
python3 source/og.py           # rebuild og-image.png (needs Pillow)
python3 -m http.server 8000    # preview: open /index.html, /duluth.html etc.
```

Edit `source/content.py` or the tables in `source/generate.py`, re-run, commit. Do not hand-edit the generated HTML — the next build overwrites it.

## Before launch (Darin's checklist)

1. **Phone number.** `PHONE`/`TEL` in `source/generate.py` are the agency's main line; swap in a Minnesota tracking number and rebuild.
2. **GA4.** Set `MEASUREMENT_ID` in `analytics.js` (it stays silent until you do).
3. **Web3Forms.** The form uses the shared agency key, so leads already arrive; create a Minnesota-specific key if you want them routed separately.
4. **TPMO disclaimer.** The footer uses the count-free CMS wording. If you want the "we represent N organizations offering M products" version, add the Minnesota numbers to `TPMO` in `generate.py`.
5. **Cost-plan county list** and the **August 2026 Medigap rule** are cited to the Minnesota Department of Commerce and industry sources; re-check both each fall when the new Cost plan guide is published.
6. Vercel: import the repo, add the domain. (GitHub Pages also works — extensionless URLs resolve there too.)
