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
