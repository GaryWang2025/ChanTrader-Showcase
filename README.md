# ChanTrader Showcase v0.1

Public, bilingual, static product showcase for ChanTrader. It is intentionally isolated from the private research system: there are no APIs, tracking scripts, credentials, market feeds, accounts, broker integrations, or order functions.

## Build and preview

```sh
python3 build.py
python3 -m http.server 4173 --directory dist
```

Open `http://localhost:4173`. The `dist/` directory is the deployment artifact and can be uploaded unchanged to GitHub Pages, Cloudflare Pages, Netlify, Vercel, or a conventional Nginx directory.

## Content integrity

- “Verified” claims describe already accepted research capabilities only.
- The SPCX graphic is deliberately illustrative and static; it is labelled as such in both languages.
- “In development” and “Planned” are visibly separate from verified capabilities.
- No private-system hostnames, local paths, internal ports, account details, or personal data are present.

## Deployment and rollback

Build locally with `python3 build.py`, publish only the contents of `dist/`, and retain the previous `dist/` artifact or release in the hosting provider. To roll back, redeploy that prior static artifact. No database or provider-specific runtime is used.

## Migration and cost

The site has no build-time package dependency and no vendor runtime. Move `dist/` to any static HTTPS host. Cloudflare Pages, GitHub Pages, Netlify, and Vercel all offer suitable free static tiers; no paid domain or service is required.
