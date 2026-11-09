# Changelog · submission walkthrough

The deck and both Excel workbooks are frozen. All case facts, scores, IDs and source values are preserved.

| Change | Submission reference | What a judge can test |
|---|---|---|
| 08:00 / 12:30 demo clock | Slide 9; Edge Tests / EDGE-OVERDUE | Advance time: overdue reviews pin above other work; Shruti shows a team-lead notice. Ages update. |
| Stable-key failed writeback | Slide 10 | Turn on Writeback fails, approve, retry: one key, one receipt. |
| Q-001 identity hold | Slide 10; Identity Hold / EDGE-ID | Reviewer and two identifiers required; no merge or outreach occurs. |
| Accepted cover | Slide 10 | Enter a cover RN name; ownership remains with Maria until acceptance. Name is TBD until entered. |
| Consent masking | Slides 5–6; Insight Recipes | Withdraw Pranav’s consent: clinical details hide while priority and coordination remain. |
| Jordan role | Slide 3 | Switch header role: one member, day-2 window, checklist; dose conflicts route to Maria. |
| Spanish reminder | Slide 10 | Draft, edit, approve; ready for Maria’s phone, never sent. |
| Scheduled filter | Slide 9 | Same label as the deck. |
| Session measurement | Slides 4, 12; Register / Instrumentation | Active prep and note timers, reviewed field and action counters; hidden/idle time excluded. |
| Team view | Slide 12 | Baseline → target numbers separated from this session; no pilot outcomes invented. |
| Welcome and mobile flow | Slides 8–10 | First-visit thesis; 12-step tour; banner → judgment → contact → next plan → evidence; sticky call action. |
| Persistent state, reset, keyboard | Product usability | Reload keeps local work; Reset clears it. J/K, Enter, C, / and ? work outside text fields. |
| Persistent safety escalation | Slide 10; BH-004C | Red-flag notes create an urgent task and require an explicit notification record; approval never hides it. |
| Why explanations | Slide 6; Insight Recipes | Queue actions, suggested tasks and brief lines show source IDs and the recipe. |
| Manual closure checks | Slide 11; Care Plan & Tasks | Open tasks, conflicts, assessment, receipt, urgent handoff and clinical evidence block closure until reviewed. |
| About and full source | Slides 8–10; all 12 datasets | Download the unchanged annex and full HTML; inspect simulations and evidence states. |

## Guided demo · at most 12 steps

1. Decide: four members due today; explain the recommended action.
2. Advance to 12:30: see overdue reviews, including Shruti’s noon review.
3. Mridul: compare the 40 mg discharge and 20 mg PCP lists; a prescriber confirms.
4. Vraj: facility first; missing setting, summary and working number.
5. Pranav: neutral shared-line callback; clinical details are consent gated.
6. Mridul: rough notes to a pending assessment.
7. Review before approval; failed writeback retries the same key.
8. Shlok: edit and approve a neutral Spanish reminder.
9. Jordan: day 2 of 7 and a checklist, with RN routing for medication questions.
10. Cover and closure: explicit acceptance and evidence checks.
11. Team: active-session measurements versus proposed baseline and targets.
12. About: inspect all 12 datasets, unchanged annex and simulation boundaries.

## A judge’s two minutes

- 0:00–0:15: read the thesis; choose Guided demo or explore.
- 0:15–0:35: select Mridul; compare both medication lists and open a source.
- 0:35–1:00: start the call; load clearly labelled fictional sample notes, draft and inspect the yellow source phrases.
- 1:00–1:20: approve; simulate writeback failure and retry the same key.
- 1:20–1:40: switch to Jordan or advance the clock; see the different workflow.
- 1:40–2:00: open Team view and About; distinguish your session measurements from the deck targets.

## Boundaries

All calls, messages, identity decisions, cover acceptance, escalation and receipts are local simulations. Extraction uses rules. Consent masking is a UI demonstration, not server-side authorization. Reviewer and cover RN names are TBD until supplied by the person testing. Physical Android/iOS devices are not available in this workspace; Chromium and WebKit provide browser and phone-layout validation.

## Reference-informed product redesign

Reviewed the reference prototype’s daily handoff, member and reviewer views. The implementation uses its useful interaction ideas with our existing case data and workflow.

- **Focused Today view:** the next member, one clear action, permitted contact window, and a panel of facts that still need confirmation. Shlok’s Tuesday call is visible as scheduled work. Priority remains the submitted scoring order.
- **Navigation:** persistent desktop workspace rail; four phone destinations (Today, Member, Call & note, More). More opens Team, Data & Trust, Saved Work, and downloads.
- **Member context:** quick member switching and a clear medication comparison for Mridul, with the original EHR-001A, EHR-001B and RX-001 source links. The existing prescriber-confirmation gate remains in force.
- **Guided assessment:** a ten-section index, review counts, next-section navigation and explicit review checkboxes. Section review never signs or submits the assessment; editing a field invalidates that section’s review.
- **Saved Work:** signed entries, field counts and receipt states retained per approved entry. Starting a new call does not change an earlier receipt.
- **Data & Trust:** the four original evidence labels, all 12 datasets, 75 source records and source-specific freshness rules.
- **Time model:** the register’s 10-, 14- and 18-minute preparation scenarios reproduce 122, 158 and 194 freed minutes, respectively. These are explicitly assumptions, separate from session measurements.
- **Phone clarity:** reduced member-header clutter, the top issue visible early, a persistent call action, and the full workflow in a high-contrast light theme.

The reference’s patient names, 28-dataset scope, clinical scenarios, pricing and alternative metrics were not imported. The submitted five members, twelve datasets, scores, facts and both Excel workbooks are unchanged.

## HiLabs theme · 9 November 2026

Matched the reference website’s Satoshi font, 42 px desktop / 28 px phone heading scale, blue/navy palette, aqua/purple gradients, pill buttons, rounded white cards, and HiLabs wordmark. The dashboard keeps its compact heading and anchored session popover. Phone layouts and clinical status contrast remain readable; case data and workflows are unchanged. Satoshi loads through Fontshare’s webfont API with system-font fallback.


## How to use · 9 November 2026

Added a plain-language guide at `#how-to-use`, accessible from the desktop sidebar, phone More menu, footer and first-visit welcome. Quick links jump to the people, diagram and practical walkthrough.

The responsive flowchart connects the twelve source datasets to the workbench, Maria’s five-member caseload, Jordan’s co-management of Pranav, call notes, reviewed drafts and simulated CM writeback. RN and LCSW are expanded, and the diagram makes consent, human approval and the feedback loop explicit. Buttons open each role’s queue and each member’s record; six practical steps link to the existing workflow.

Also corrected the queue’s role label when Jordan is selected and ensured the phone menu closes when its current destination is selected. The case facts, scores and Excel workbooks remain unchanged.
