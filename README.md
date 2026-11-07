# Care Workbench · HiLabs APM case 2026–27

A clickable concept prototype of a case-management workbench for an RN case manager ("Maria").
It covers the three screens from the case deck:

| Screen | Job | What it shows |
|---|---|---|
| **Work queue** | Decide | Five members ranked by urgency, deadline, barriers and new events, with an explained score and up to three next actions |
| **Member 360** | Know | One member on one screen: the top issue, an AI brief linked to sources, evidence with confidence and freshness, and a timeline |
| **Call & note** | Do | Permitted contact routes (dead numbers blocked), a pre-filled assessment to confirm, and a note drafted from Maria's entries that she reviews and signs |

A **Guided demo** button walks a reviewer through Maria's Monday in seven steps.
All members, records and phone numbers are fictional. Nothing calls anyone or writes to a real system.

## Files

| Path | Purpose |
|---|---|
| `index.html` | The page Vercel serves. **Generated; do not edit by hand.** |
| `HiLabs_Workbench_Prototype_V3.html` | Source of the prototype (page content without the HTML document wrapper) |
| `scripts/build_index.py` | Wraps the source into `index.html` |
| `vercel.json` | Static hosting settings for Vercel |
| `archive/` | Earlier V1 prototype, kept for reference |

## Edit and rebuild

```bash
python3 scripts/build_index.py
```

Run it after every change to `HiLabs_Workbench_Prototype_V3.html`, then commit both files.

## Run locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploy on Vercel

1. Sign in at vercel.com with GitHub and choose **Add New → Project**.
2. Import the `pranavgoldar/HILabs` repository.
3. Framework preset: **Other**. Leave the build command and output directory empty (the site is static files at the repo root).
4. Choose **Deploy**. Vercel gives a public `*.vercel.app` address.

Every push to the production branch redeploys automatically.
