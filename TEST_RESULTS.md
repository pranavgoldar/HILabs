# Test results · submission walkthrough

**976 of 976 enabled controls respond; 0 console errors.**

Scope: automated Chromium clicks on every rendered enabled button, link, checkbox and radio in 18 enumerated states across all 13 routes: Queue, Team, About, five Member views, and the notes/review states of five Call views. All details were expanded. Downloads were verified as downloads, and selected controls as selected. Fifteen disabled controls were counted separately because their prerequisites were unmet. New role, clock, identity, handover, reminder, consent, retry, closure and escalation transitions also have dedicated functional checks. This count describes the tested states, not every possible combination of user-entered text.

Two navigation issues found by the audit were corrected: Skip to main content preserves the current route and moves focus; Evidence & records opens the section with visible feedback. All 23 affected control checks passed after those corrections; the other 953 checks remained valid.

| Check | Result |
|---|---|
| New functional suite | Chromium and WebKit pass: welcome, overdue clock, Jordan, consent, Spanish review, cover acceptance, closure blockers, identity hold, retry, escalation and Team view |
| Responsive views | 13 routes × 3 widths (390, 1366, 1920 px) in each engine: 78 checks, no horizontal overflow |
| Existing workflow regression | 66 additional route/width checks in Chromium at 320, 390, 430, 768, 1024 and 1440 px; all 75 source dialogs open; no script errors |
| Drafted fields from existing samples | Pranav 24; Mridul 24; Vraj 15; Shruti 24; Shlok 21 of 40, unchanged |
| Accessibility | 18 desktop/phone route scans and 6 additional states (welcome, Jordan, consent, handover, Spanish pending, escalation); zero detected WCAG A/AA violations after fixing consent-mask list markup |
| Timers | Deterministic clock verifies prep stops at call start; note timing starts on first keystroke; idle is capped at 60 seconds; hidden-tab time is excluded |
| Guided tour | All 12 highlighted targets visible without overlay overlap at 390 px |
| Writeback | Failure + reload + Retry preserves the same key and one approved-call count |
| Closure | Missing evidence disables closure; completion evidence, clinical attestation, approved assessment and receipt enable a final manual RN action |
| Keyboard | J/K queue movement, Enter member view, C call route; / search and ? sheet are available outside text entry |
| Delivery | Downloaded HTML is the same full source used to build index.html; no framework or external JS dependency |
| Frozen files | Both Excel SHA-256 hashes match the supplied versions; no deck or workbook edited |

## Reproduce locally

```bash
python3 scripts/build_index.py
python3 -m http.server 8765
# In another terminal, with Playwright and its browsers installed:
python3 tests/test_workbench.py
python3 tests/test_submission_features.py
ENGINE=webkit python3 tests/test_submission_features.py
python3 tests/test_session_timers.py
python3 tests/test_controls.py
```

## Limits and missing facts

- This workspace cannot test physical Android/iPhone devices. Chromium and WebKit check browser behavior and phone layouts; this is not physical-device certification.
- Real calls, messages, identity joins, RN authentication and CM writeback remain simulated as required. Client-side consent masking demonstrates behavior; production would require server-side access controls.
- A cover RN name and data-quality reviewer identity were not supplied. The UI marks them TBD and requires the tester to enter them; no static names were invented.
- Session measurements are labelled “Your session · not pilot data.” Contact rates and safety outcomes cannot be inferred from sample calls; Team view says so explicitly.

The full slide/annex mapping, twelve-step guided-demo text and two-minute judge walkthrough are in [CHANGELOG.md](CHANGELOG.md).
