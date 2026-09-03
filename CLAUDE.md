# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

Static marketing / lead-generation site for ECOS Medicare Solutions (agent: Darin Weidauer, NPN 18580338) serving **Minnesota**, at https://minnesotamedicareenrollment.com. Sister sites: Georgia (`georgiamedicareenrollment`), Arizona (`medicare-enrollment-arizona`), the Medigap rate-research site (`my-medigap-rate`) and Darin's author page on MyECOS360. Each is its own site; they cross-link in the footer "Our network" strip and in the Organization `sameAs`.

## The generator is the source of truth

Unlike the Georgia and Arizona repos, the generator **is in this repo**: `source/generate.py` (engine, config, city and region tables), `source/content.py` (topic pages, FAQ page, about, privacy, terms), `source/scenes.py` (SVG hero art), `source/site.css`, `source/og.py`. The HTML at the root is output. **Edit the source and re-run `python3 source/generate.py`; never hand-edit a generated page.**

- Site-wide facts (phone, email, Web3Forms key, plan-year figures, network list, TPMO wording) live in the CONFIG block at the top of `generate.py`.
- Adding a city or region is one dict in `CITIES` / `REGIONS`; the generator writes the page, the footer links, the sitemap and both llms files.
- Adding a topic page is one dict in `TOPIC_PAGES`; give it `keyfacts` (answer-first summary), `faqs`, and `sources`.
- Links are root-absolute clean URLs (`/duluth`, not `duluth.html`). Vercel `cleanUrls` and GitHub Pages both resolve them.

## Compliance — do not weaken

CMS/TPMO rules apply.

- Every page carries the TPMO disclaimer and the "not connected with or endorsed by the United States government or the federal Medicare program" wording, plus the licensing/compensation disclosure, in the footer. Keep them.
- 1-800-MEDICARE, Medicare.gov and **Minnesota Aging Pathways (formerly the Senior LinkAge Line, 800-333-2433)** are named as the official, independent alternatives.
- The lead form carries the permission-to-contact checkbox and its wording; the hidden `consent_text` records exactly what was agreed. Do not remove either. The form asks no health questions.
- **Do not invent or "update" dollar figures.** The 2026 Medicare figures come from the CMS release of Nov 14, 2025 and live in `FIG` plus the costs page; the Minnesota figures (21 Cost-plan counties, the August 2026 Medigap window and its 15%→35% surcharge, MSP asset limits) are cited in each page's "Sources" block. Change them only with a source in hand, and keep `llms.txt` consistent (the generator does this).
- Minnesota-specific facts that other states' pages get wrong: Medigap here is **Basic / Extended Basic + riders**, not plan letters; **Cost plans** are still sold in 21 counties; **MSHO** is the dual-eligible program. Do not paste Georgia/Arizona plan-letter copy into this site.

## Conventions

- Aesthetic: "North Star almanac" — lake blue `--lake`, spruce, birch paper, harvest gold; Fraunces + Source Sans 3; WCAG 2.2 AA, 18px+ base, 56px tap targets. No photos; hero art is generated SVG.
- Each topic page: hero + lead form → "At a glance" key facts → body → FAQ (mirrored in FAQPage JSON-LD) → CTA → Sources → author byline with "Last reviewed".
- Structured data: every page emits the shared `@graph` (`#org` InsuranceAgency with `sameAs`, `#website`, `#darin` Person with `sameAs` to the canonical MyECOS360 profile), plus BreadcrumbList and page-type nodes. No `@id` reference may dangle — the validation snippet in the last build commit checks this.
- `analytics.js` is silent until a real GA4 ID is set. `thank-you` and `404` are noindex.

## Preview / checks

```bash
python3 source/generate.py && python3 -m http.server 8000   # open /index.html, /duluth.html
```
After a build: every JSON-LD block must parse, every `/slug` link must have a file, no `[[TOKEN]]` may remain, and `sitemap.xml` must list exactly the indexable pages.
