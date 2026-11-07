# Test results · focused workspace redesign

**1270 of 1270 enabled controls respond; 0 console errors.**

The control audit clicks every enabled button, link, checkbox and radio in 20 enumerated desktop states across 15 routes: Today, Team, About, Data & Trust, Saved Work, five Member views, and notes/review for each of five Call views. Details are expanded. Downloads are verified as downloads and selected controls as selected. 15 controls with unmet prerequisites were counted separately. The figure describes enumerated states, not every possible input combination.

| Check | Result |
|---|---|
| New workspace workflows | Chromium and WebKit pass: phone More menu; all 12 datasets; source dialogs; medication comparison; section review and receipt history; three time-model scenarios |
| Responsive layout | 15 routes × 5 widths (320, 390, 768, 1366, 1920 px), in both engines: 150 checks, no horizontal overflow |
| Existing workflows | Chromium and WebKit pass: welcome, overdue clock, Jordan, consent masking, Spanish review, accepted cover, closure, identity hold, retry, escalation and Team view |
| Existing regression | 66 route/width checks and all 75 source dialogs pass in Chromium; zero script errors |
| Assessment samples | 24 / 24 / 15 / 24 / 21 of 40 fields drafted for Pranav / Mridul / Vraj / Shruti / Shlok, unchanged |
| Human review | Section review persists without approving. Editing a field invalidates that section’s review. Final RN sign-off is still required |
| Accessibility | 22 route/width WCAG A/AA scans: zero detected violations; high-contrast light theme and visible focus states retained |
| Session timing | Prep and documentation boundaries, 60-second idle cap and hidden-tab pause pass deterministic checks |
| Tour | All 12 phone highlights remain visible without overlay overlap |
| Saved work | A signed entry retains its field counts and receipt; starting a new call cannot replace an earlier receipt |
| Clinical and privacy boundaries | Prescriber gate, blocked phone, unknown values, consent masking and persistent escalation remain intact |
| Data integrity | Both supplied Excel SHA-256 hashes match; no patient, source record, clinical value, score or submitted target changed |
| Dependencies | Single vanilla HTML/CSS/JS source; no new external JS library or UI framework |

## Reproduce

```bash
python3 scripts/build_index.py
python3 -m http.server 8765
# In another terminal, with Playwright browsers installed:
python3 tests/test_workbench.py
python3 tests/test_submission_features.py
ENGINE=webkit python3 tests/test_submission_features.py
python3 tests/test_session_timers.py
python3 tests/test_product_redesign.py
ENGINE=webkit python3 tests/test_product_redesign.py
python3 tests/test_controls.py
```

The source and downloadable HTML are generated from the same file. The submitted deck and both Excel workbooks are frozen. The change log contains the submission mapping and judge walkthrough.

## Scope of the prototype

Browser and phone-layout checks use Chromium and WebKit. Physical-device certification is outside this workspace. Calls, messages, identity joins, cover acceptance and writeback remain explicit simulations. Consent masking demonstrates UI behavior; real authorization requires server enforcement. Session measurements are labelled as session data, and the time-model scenarios remain assumptions from the register. Cover RN and reviewer names remain TBD until entered by the tester.
