# Care Workbench · HiLabs APM case 2026–27

A clickable concept prototype of a case-management workbench for an RN case manager ("Maria").
It covers the three screens from the case deck:

| Screen | Job | What it shows |
|---|---|---|
| **Work queue** | Decide | Five members ranked by urgency, deadline, barriers and new events, with an explained score and up to three next actions |
| **Member 360** | Know | One member on one screen: the top issue, an AI brief linked to sources, evidence with confidence and freshness, and a timeline |
| **Call & note** | Do | Permitted contact routes (dead numbers blocked), a pre-filled assessment to confirm, and a note drafted from Maria's entries that she reviews and signs |

A **Guided demo** button walks a reviewer through Maria's Monday in nine steps.
All members, records and phone numbers are fictional. Nothing calls anyone or writes to a real system.

## Files

| Path | Purpose |
|---|---|
| `index.html` | The page Vercel serves. **Generated; do not edit by hand.** |
| `HiLabs_Workbench_Prototype_V3.html` | Source of the prototype (page content without the HTML document wrapper) |
| `scripts/build_index.py` | Wraps the source and inlines the annex records into `index.html` |
| `assets/annex-data.js` | Generated copy of all 75 records from the submission annex |
| `scripts/sync_annex.py` | Reads the annex without modifying either Excel workbook |
| `tests/test_workbench.py` | Browser checks for data, navigation, responsive layout and review gates |
| `vercel.json` | Static hosting settings for Vercel |
| `archive/` | Earlier V1 prototype, kept for reference |

## Edit and rebuild

```bash
python3 scripts/build_index.py
```

Run it after every change to `HiLabs_Workbench_Prototype_V3.html`, then commit both files.

The records mirror the submitted V2 workbook. If an explicitly approved workbook revision is supplied, regenerate the record asset with `python3 scripts/sync_annex.py` (requires `openpyxl`) before building. The script never writes to Excel.

## Responsive refresh · 7 November 2026

- Three consistent navigation tabs: Queue, Member, Call & note.
- The queue shows the next action first; scoring and supporting details expand on request.
- Evidence tables become cards on phones. Charts have a text event list at small widths.
- Call workflow separates contact/notes from assessment review. All 40 fields remain editable in expandable sections.
- Controls are at least 44 px high; mobile text inputs use 16 px type to avoid iPhone focus zoom. No external font downloads or application build dependencies.
- BH evidence links to the three BH records; the PCP appointment does not close the mental-health follow-up gap. Copied-forward safety remains unknown and stale.
- A dose conflict requires recorded prescriber confirmation. Editing notes clears the earlier AI draft and approval.
- “Save draft locally” persists an unsigned draft on that device. Reset removes saved drafts. The writeback receipt is explicitly simulated.

## Verify

```bash
python3 -m http.server 8765
# In another terminal (Playwright browsers must be installed):
python3 tests/test_workbench.py
BROWSER_ENGINE=webkit python3 tests/test_workbench.py
```

The suite covers 11 routes at 320, 390, 430, 768, 1024 and 1440 px; all 75 source dialogs; queue actions; clinical review gates; the five note journeys; draft restore; and failure simulations. Browser engines emulate phone layouts; this is not physical-device certification. The source Excel files and existing QR destination are unchanged.

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
