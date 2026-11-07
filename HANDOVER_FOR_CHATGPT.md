# Handover: HiLabs APM Case 2026–27 · Case Management Workbench

**Read this first, ChatGPT.** You are taking over a near-final competition submission. Act as a senior product manager and APM-case judge. More than 500 candidates are solving the same case, so the work must be rigorous, consistent across every file, and evidence-backed.

**Rules for you**
- The facts in Section 5 are the single source of truth. Do not invent numbers, names, quotes, records or sources.
- The deck, the two Excel workbooks and the live prototype must say the same thing. Change one, check the others.
- Patient names are final: **Pranav, Mridul, Vraj, Shruti, Shlok**. BH co-manager / contrast persona: **Jordan, LCSW**. Never use "Kabir" or "Mmridul".
- Write in plain English. No internal jargon (T0/T1/T2, F1/F2/C1, "BH floor", "N flag").
- Every AI feature keeps a human in the loop. The product never picks a medication dose and never auto-closes a case.

---

## 1. The assignment (HiLabs Product Caselet, APM campus hiring 2026–27)

Design a web MVP **Case Management Workbench** for a US health plan that:
- (a) assembles a timely, trustworthy, holistic picture of each member;
- (b) tells the case manager whom to work on and what to do next;
- (c) cuts documentation and outreach friction.

Assume HiLabs already ingests and standardizes the data. The job is deciding which data matters and how it appears on screen.

**Persona in the brief:** Maria, RN case manager.
- 20 years ICU, 48 active cases, 6 discharge alerts since Friday.
- Opens 6–7 systems per member.
- Phone disconnected, medication lists disagree, a 40-field assessment to fill.
- By 3 pm she has had **2 real conversations**.

**Submit**
1. An 8–12 slide deck.
2. A spreadsheet annex with 5 synthetic patients:
   - records in at least 6 datasets each;
   - planted imperfections;
   - one "what should the case manager see and do at 8 am Monday" line per patient.

**Deck sections required by the brief**
- A Understand (persona, day in the life, ranked pains, where the day is lost, with assumptions)
- B Data strategy (dataset inventory + combinations)
- C Synthetic patients
- D Product design (≥ 3 screens, walk 2–3 patients through them, AI with human confirmation)
- E Prioritize & measure (MVP vs later, metrics with baseline → target, risks)
- Brownie points: pilot and go-to-market (buyer, pilot scope, pricing signal)

**Scoring**
- Problem depth 20%
- Data thinking 25%
- Synthetic data 20%
- Product design & prioritization 25%
- Metrics, risks & communication 10%

The judges' test for every item: *"What would Maria do differently because she saw this?"*

---

## 2. Author

Pranav Goldar · IIT Bombay · Roll no. 23B2101 · 23b2101@iitb.ac.in

---

## 3. Deliverables and where they live

GitHub repo: `pranavgoldar/HILabs`, branch `claude/peaceful-maxwell-l1boq7` (the only branch, so it is the default and production branch).

| Deliverable | Status | Location |
|---|---|---|
| Deck V3 (12 slides, PDF/PPTX) | Needs the final edits in Section 7 (being done in Claude Slides) | Author's machine |
| Synthetic Data Annex V2 | Final | `excel/HiLabs_Synthetic_Data_Annex_V2.xlsx` |
| Research & Decision Register V2 | Final | `excel/HiLabs_Research_and_Decision_Register_V2.xlsx` |
| Live prototype | Live | https://hilabs-five.vercel.app/ (Vercel auto-deploys on push) |
| Prototype source | — | `HiLabs_Workbench_Prototype_V3.html` (page content only) |
| Served page | Generated | `index.html` (built by `python3 scripts/build_index.py`; never edit by hand) |
| QR codes | Final | `assets/qr/` (PNG, SVG, slide card), all → hilabs-five.vercel.app |
| Screenshots for the deck | Final | `assets/screens/01…09-*.png` (2× resolution) |
| Old V1 prototype | Should be deleted (old names) | `archive/HiLabs_Workbench_Prototype_V1.html` |
| Vercel config | — | `vercel.json`; `README.md` has deploy steps |

---

## 4. Product summary (what the deck and prototype argue)

**Thesis:** "Give Maria back her clinical judgment: from 3 conversations a day to 6."

**Three jobs:**
- **KNOW:** prep 14 → 5 min
- **DECIDE:** triage 40 → 10 min
- **DO:** notes 30 → 12 min

Screen order follows her day: **Decide → Know → Do**.

**Opportunity line:** "Maria doesn't lack data. She lacks data she can trust, ranked, and ready to act on."

**Four MVP features**
1. **Ranked work queue (DECIDE).**
   - Each row shows the trigger with source and age (e.g. "ADT ALERT · Admitted, diagnosis blank · 13 h ago").
   - Risk flags and a "Next ▸" action; at most 3 actions per member (accept / edit / dismiss with a reason).
   - The score explains itself.
2. **Member 360 (KNOW).** One screen with everything about one member:
   - The top issue first.
   - Conflicts shown side by side; Maria clicks **Confirm clinical reality**.
   - Provenance (source + age + record ID) on every value; unknown is never shown as "no".
   - A contact & barriers strip; a 3-line AI brief with every line linked to a record.
3. **Outreach helper (DO).**
   - Dead numbers blocked, with alternative routes beside them.
   - Neutral script for shared phones; best time and language.
4. **Notes → 40-field assessment (DO).**
   - Maria types rough call notes; **Auto-draft assessment** fills the form.
   - AI values stay **yellow (pending)**, each showing the phrase it came from, until she clicks **Approve & Submit**.
   - One approval writes the assessment, care plan, tasks, note and audit back to the plan's existing CM system.

**AI contract**
- AI drafts and summarizes; Maria confirms.
- **Never automated:** medication or dose decisions, case closure, priority overrides, contacting a member on its own.

**Why rules, not ML, for ranking:** there are no outcome labels yet, and nurses must be able to argue with the score. The pilot creates the labels.

---

## 5. Fact base (single source of truth)

### Snapshot
Monday 2 Nov 2026, 08:00 America/New_York. All data fictional; phones 216-555-01xx.

### Counts
- 5 members, 12 datasets, **75 source records**.
- **19 imperfections + 1 negative control**; 5 edge tests.
- Hospital alert rows since Fri 30 Oct: 5 raw → 4 events (one duplicate merged).
- 4 plan lines: MA PPO, MA D-SNP, Medicaid, Commercial.
- Datasets with records per member: Pranav 12 · Mridul 11 · Vraj 10 · Shruti 11 · Shlok 10.

### The 12 datasets (all MVP)

| Maria's question | Datasets |
|---|---|
| Who is this member? | Member & Eligibility · Care Plan & Tasks (past CM notes) · Medical Claims |
| What just happened? | Hospital ADT · Discharge & Clinical (EHR) · Lab Results · Behavioral Health (consent-gated) |
| Can they get care? | Pharmacy (PBM) · Prior Auth & Services (UM) · Care Access (PCP & appointments) · Social Needs (HRA) |
| How do I reach them? | Contact History & preferences |

**Later (deliberately out of the MVP):** HEDIS gaps, risk scores, HF home weights, referral loop, call-center logs, transport vendor, deprivation index.

**Freshness rules:** ADT stale after 48 h · pharmacy after 7 days · claims 45 days = normal lag · social screens after 6 months.

**Evidence states:**
- ✓ Confirmed (2+ independent sources; duplicate messages don't count)
- ◐ Single source
- ⚠ Conflict
- ? Unknown

### Queue and scores
Points = urgency /40 + deadline /30 + barriers /20 + new event /10 (inputs 0–4 / 0–3 / 0–2 / 0–1, × 10).

| # | Member | Plan | Score | Due | Trigger |
|---|---|---|---|---|---|
| 1 | Pranav, 36 (SYN-004) | Medicaid | 40/30/20/10 = **100** | Mon 09:00 | ADT · BH discharge Sat 31 Oct 11:00 (46 h ago) |
| 2 | Mridul, 72 (SYN-001) | MA PPO | 40/30/20/10 = **100** | Mon 10:00 | ADT · HF discharge Fri 30 Oct 14:00 (67 h ago) |
| 3 | Vraj, 44 (SYN-003) | Medicaid | 30/30/20/10 = **90** | Mon 11:00 | ADT · admitted Sun 1 Nov 19:00, diagnosis blank (13 h ago) |
| 4 | Shruti, 81 (SYN-005) | MA D-SNP | 30/30/20/10 = **90** | Mon 12:00 | ADT · fall discharge Thu 29 Oct 11:00 (4 days ago) |
| 5 | Shlok, 58 (SYN-002) | Commercial PPO | 20/20/10/0 = **50** | Tue 3 Nov 18:00 | Pharmacy · refill reversed 18 Oct (15 days ago) |

- **Tie rule:** overdue first → behavioral-health safety rule → score → earlier due time. So Pranav goes before Mridul.
- **Deadline buckets:** ≤ 1 day = 3 · ≤ 3 days = 2 · ≤ 5 days = 1 · later = 0.
- Score weights are a proposal for medical-director sign-off.

### Patient facts (record IDs in brackets)
- **Pranav**
  - Discharged 31 Oct from Willow Crisis Unit [ADT-004].
  - 15 Oct safety screen copied forward; current safety unknown [EHR-004, BH-004C].
  - PCP visit Tue 3 Nov 10:30 at Willow Community Clinic [ACC-004]. No mental-health visit before the 7-day FUH window closes Sat 7 Nov [BH-004B].
  - Lost housing, in a shelter (30 Oct) vs "stable rented room" (15 Apr) [SOC-004B vs SOC-004A].
  - Only phone is the shared shelter reception desk (216-555-0104); neutral callbacks only; 09:00–11:00 [OUT-004].
  - Sertraline 50 mg filled 12 Oct [RX-004]. Housing navigation accepted, placement unconfirmed [SVC-004].
  - Consent for care coordination [BH-004A]; no SUD records in scope. Co-managed by Jordan, LCSW.
- **Mridul**
  - Discharge summary furosemide **40 mg** daily [EHR-001B, 30 Oct] vs PCP list **20 mg** [EHR-001A, 1 Oct]; no reason given.
  - Only fill 20 mg on 1 Oct, ended 30 Oct [RX-001].
  - Discharge message arrived twice and was merged [ADT-001A/B]; admitted 28 Oct [ADT-001C].
  - K 4.2 mmol/L, creatinine 1.1 mg/dL (30 Oct) [LAB-001A/B]; weight unknown.
  - PCP Dr. Rowan Ash, Thu 5 Nov 10:00; transport not requested [ACC-001, SVC-001].
  - Last claim 15 Sep [CLM-001]. Lives alone; a neighbor checks in [SOC-001]. Phone verified at the bedside [OUT-001].
- **Vraj**
  - Admitted Elm Hospital Sun 1 Nov 19:00, no reason, no discharge [ADT-003D]; facility team 216-555-0133.
  - ED visits 29 Sep, 12 Oct, 30 Oct (the 30 Oct alert arrived 37 h late) [ADT-003A/B/C]. Claims show only 15 Aug [CLM-003].
  - ED summary describes 12 Oct, not 30 Oct [EHR-003].
  - Phone 216-555-0103 disconnected on 21 and 26 Oct; the old auto-dialer retried it [OUT-003A/B].
  - Scheduling feed down since 31 Oct [ACC-003]. PCP Dr. Ellis Fern (216-555-0123).
  - May social screen stale [SOC-003]. Albuterol filled 10 Oct [RX-003].
- **Shruti**
  - Home health and walker authorized 30 Oct; first visit and delivery unconfirmed [SVC-005A/B].
  - Daughter Riya authorized for care coordination (216-555-0106, 09:00–11:00) [OUT-005A]; can't manage transfers alone [OUT-005B].
  - February "lives independently" vs 30 Oct "daughter helping" [SOC-005A vs 005B].
  - Amlodipine refilled 3 days early [RX-005]. Hemoglobin 11.8 g/dL, lab feed stale [LAB-005].
  - PCP Dr. Sage Elm, Wed 4 Nov 11:00 [ACC-005].
- **Shlok**
  - Metformin ER 500 mg × 2 supply ended 17 Oct [RX-002]; the 18 Oct refill was paid then reversed [RX-002P/R]; ~15 uncovered days (estimate).
  - A1c 8.1% (12 May) → 9.6% (15 Oct) [LAB-002A/B]. Copay delays refills; Spanish, 17:30–19:00 [OUT-002].
  - The 1 Sep dose increase was documented by the prescriber, so it is **not** a conflict [EHR-002I].
  - PCP Dr. Quinn Lake, Thu 12 Nov 16:00 [ACC-002]. Affordability review drafted [SVC-002].

### 8 AM Monday lines (exact)
- **Pranav:** "Neutral callback request through the shelter desk, 09:00–11:00. When he calls back, check privately that he is safe. Book a mental-health visit before Sat 7 Nov (the 3 Nov PCP visit does not count). Confirm the housing navigator."
- **Mridul:** "He came home Friday on double his water pill and has no fill of the new dose. Call by 10, check the pills in hand, his weight and his symptoms, and get the prescriber to confirm the dose."
- **Vraj:** "Stop dialing the dead number. Call Elm Hospital to confirm where he is and why, and get the summary. Then use a route his PCP, Dr. Ellis Fern, approves."
- **Shruti:** "Approved isn't delivered. Call her daughter Riya in her 09:00–11:00 window, confirm the first home-health visit and the walker, and ask how she is coping. Due by 12:00."
- **Shlok:** "Not urgent today. Schedule a Spanish call for Tuesday 17:30–19:00 with an interpreter, ask about cost and what metformin he has at home, and move him to a generic or 90-day supply."

### Imperfections (19 + 1 control) → what catches each
- **Mridul**
  - IMP-01 duplicate ADT → event merge
  - IMP-02 conflicting med lists → side-by-side resolve
  - IMP-03 45-day claim lag → alerts first; claims blind spot
- **Shlok**
  - IMP-04 supply gap + cost → "no fill seen", cost conversation
  - IMP-14 paid-then-reversed → nets to zero
  - **IMP-16 negative control:** documented dose change is NOT flagged
- **Vraj**
  - IMP-05 stale May screen → re-ask
  - IMP-06 dead phone still listed → blocked + alternatives
  - IMP-07 late alert + wrong-visit summary → reason unknown
  - IMP-08 claims miss recent ED visits → ADT count + time-lag chart
  - IMP-12 scheduling feed down → "unknown", never "none"
  - IMP-13 admission with blank diagnosis → missing-context checklist
- **Pranav**
  - IMP-09 shared shelter phone → neutral script
  - IMP-10 copied-forward safety screen → safety unknown, private same-day check
  - IMP-18 stale April housing screen → side-by-side resolve
  - IMP-20 PCP visit ≠ mental-health visit → FUH gap stays open
- **Shruti**
  - IMP-11 approved ≠ delivered → delivery task
  - IMP-15 early refill overlap → no adherence claim
  - IMP-17 stale lab feed → dated value + Stale label
  - IMP-19 stale "lives independently" → side-by-side resolve

### Insight recipes (deck slide 6)
1. Mridul: discharge 40 mg + PCP 20 mg + only 20 mg filled → dose confusion → call by 10:00, prescriber confirms.
2. Pranav: BH discharge + no mental-health visit + housing loss + shared phone → day-7 gap + privacy risk.
3. Vraj: repeat ED + admission-only alert + dead phone → unreachable frequent ED user.
4. Shruti: authorized services + no delivery + caregiver strain → approved ≠ delivered.
5. Shlok: reversed fill + supply gap + rising A1c + cost → stopped refills because of cost.
6. All members: connect history + phone type → best time and channel.

If a source is missing, the recipe shows "unknown", never a negative finding.

### Time model (480-minute day; deck slide 4)

| Activity | Today | Target | How today is derived | Fix |
|---|---|---|---|---|
| Triage / who's next | 40 | 10 | Alerts, queue, sheet (A) | Ranked queue |
| Prep / data hunting | 126 (9 × 14) | 60 (12 × 5) | 14 min (A); 6–7 screens (B) | One screen |
| Failed calls + logging | 56 (14 × 4) | 36 (9 × 4) | (A) | Dead numbers blocked |
| Conversations | 75 (3 × 25) | 150 (6 × 25) | 25 min (A); 2 by 3 pm (B) | Calls not shortened |
| Documentation | 120 (3 × 30 + 6 × 5) | 78 (6 × 12 + 6 × 1) | (A) | Capture once; AI drafts |
| Care coordination | 45 | 90 | (A) | More follow-up |
| Team / admin | 18 | 18 | (A) | — |
| Buffer | 0 | 38 | — | Urgent call-backs |
| **Total** | **480** | **480** | | |

(A) = author's assumption · (B) = from the brief.

- Judgment time 120 → 240 min (25% → 50%). Connect rate 3 ÷ 17 ≈ 18% → 6 ÷ 15 = 40%.
- Freed 158 min (33% of the day). Stress test, prep at 10 / 14 / 18 min → 122 / 158 / 194 freed.
- Pains ranked: prep 126 · notes 120 · failed calls 56 · triage 40 · late data ~5.
- Root causes: no trust signals → nothing ranked → typed twice.

### Metrics (deck slide 12)
- ★ Conversations per RN-day: 3 → 6
- Prep per member: 14 → 5 min
- Documentation per contact: 30 → 12 min
- Connect rate: ~18% → 40%
- Contact ≤ 2 business days: ~55% → 85% (assumption)
- Judgment share: 25% → 50%

**Pass if, vs control RNs:** ≥ 5 conversations per RN-day, prep ≤ 6 min, no rise in safety misses, ≥ 75% weekly active RNs.

**Guardrails**
- Average call ≥ 20 min.
- Note-audit pass rate ≥ baseline.
- < 1% unsupported AI lines.
- Dismissals > 40% → retune.
- After-hours notes trend down; RN satisfaction holds.
- Lagging: HEDIS MRP, FUH, 30-day readmissions.

### Pilot & go-to-market
- **Buyer:** VP Care Management at an existing HiLabs MA customer.
- **Sponsor:** CMO / Stars lead. **Approve:** IT and privacy.
- **Scope:** transitions of care · 12 RNs · 12 weeks.
  - Weeks 1–2 baseline.
  - Weeks 3–6: 6 champion RNs vs 6 caseload-matched RNs.
  - Weeks 7–12: all 12.
- **Price:** paid pilot $25k, then $300 per RN-month.

### Economics (Register › Economics, live formulas)
- Capacity value: 50 RNs × 20% × $115k loaded = **$1.15M/yr** (capacity, not cash).
- $115k = BLS median RN wage $93,600 (May 2024) × ~1.23.
- Subscription: 50 × $300 × 12 = **$180k/yr** → ~6.4×.
- Recurring cost ~$90 per RN-month → **~70% gross margin** before R&D.
- One readmission ≈ **$15.2k** (HCUP SB #278, 2018) ≈ **4 RN seats for a year**.

### Prioritization (slide 11)

| Feature | Min/day | Call |
|---|---|---|
| Ranked queue | 30 | MVP |
| Member 360 + conflicts + brief | 66 | MVP |
| Assessment pre-fill + note draft | 42 | MVP |
| Outreach helper | 20 | MVP |
| Writeback to CM | — | MVP |
| ML ranking | — | Later |
| HF weights / referral loop | — | Later |
| Auto-close / member chatbot / app | — | Never |

MVP minutes sum to 158, the same as the time model.

### Roadmap (gates, not dates)
- **Phase 0 · Discover (4 weeks):** shadow 5 RNs, map the real 40 fields, confirm feeds and writeback, check HiLabs CureX overlap. Gate: medical-director sign-off + BAA/HIPAA review + FDA clinical decision support intended-use review.
- **Phase 1 · MVP pilot (12 weeks).** Gate: ≥ 5 conversations/day, no safety rise.
- **Phase 2 · Scale to all CM programs.** Gate: ≥ 75% weekly active RNs.
- **Phase 3 · Learn:** ML ranking trained on pilot outcomes; HEDIS gap closure.

### Competition
- ZeOmega Jiva and HealthEdge Clinical Edge: CM systems of record; we sit on top and write back.
- **ZeOmega Jiva PrudenceAI (Oct 2026)** and **Innovaccer Care Management Copilot** already ship AI drafting with clinician review. Drafting alone is not unique.
- Our angle: (1) conflicts resolved by the clinician, never auto-merged; (2) source + age on every value, unknown ≠ no; (3) AI output pending until approved, with its source phrase.
- **HiLabs' own products:** MCheck (incl. Outreach Intelligence) and MCheck VBC incl. **CureX** (prioritizes care opportunities with AI summaries). Position the workbench as the RN-facing work layer on the same trusted data, and validate CureX overlap in Phase 0.

### Sources (checked 7 Nov 2026)

**Verified**
- Coleman et al. 2005: 14.1% post-discharge medication discrepancies.
- Jencks et al. 2009 NEJM: 19.6% of Medicare patients readmitted within 30 days (2003–04).
- AHRQ HCUP NRD 2020: Medicare readmission rate 17.0 per 100 (2020).
- AHRQ HCUP SB #278: 3.8M readmissions, ~$15.2k average (2018, all payers).
- KFF: MA quality bonuses ≥ $12.7B (2025), ≥ $13.4B (2026).
- GMI: care-management solutions ~$13.8B (2023), ~13.7% CAGR.
- BLS: RN median $93,600 (May 2024).
- CMS TCM (2-business-day contact) · 42 CFR 482.24(d) (ADT notifications) · 42 CFR Part 2 (SUD records) · NCQA HEDIS FUH / TRC / MRP · FDA CDS guidance (Jan 2026).

**Partly verified**
- Hendrich et al. 2008: ~35% of *hospital* nurse time documenting (35.3% seen only in a secondary summary). Must be labeled "directional only".

**Do not use**
- "$16.3k, 3.85M (SB #304)": not in that brief.
- "$43.3B by 2032 (GMI)": that figure is SNS Insider's.

Full list with URLs: Register › Sources and Register › Deck Claim Check.

---

## 6. Design system (deck and prototype)

**Colors**
- Navy `#121957`, deep navy `#0B0F3F`, indigo `#381E8C` (cover gradient)
- Blue `#0053EF`, violet `#603CE4`, red `#981A1A`
- Pale blue `#EDF2FE`, amber panel `#FDF2C6`, green panel `#DBFBE6`

**Tags:** KNOW = blue · DECIDE = violet · DO = navy.

**Type:** Plus Jakarta Sans (body/display), JetBrains Mono (record IDs). High contrast; dark text on light backgrounds.

---

## 7. Deck V3 → final: changes still to apply

These are being applied in Claude Slides. Verify them on the returned deck.

- **Everywhere**
  - "Kabir" → "Pranav"; co-manager Jordan.
  - Every number must match Section 5.
  - Section letters: A 2–4 · B 5–6 · C 7 · D 8–10 · E 11–12.
- **Slide 1:** Kabir → Pranav in the queue mock (or use `02-queue-rows.png`).
- **Slide 2**
  - "17.0% in 2020 (AHRQ HCUP NRD)".
  - Documentation: "hospital nurses, directional".
  - Cost row: "$15.2k, 3.8M a year (HCUP SB #278, 2018)".
  - Add "No payer RNs interviewed yet; Phase 0 shadows 5 RNs."
- **Slide 3:** "Pranav is Jordan's kind of case; Jordan co-manages him with Maria."
- **Slide 5**
  - "12 datasets, all in the Synthetic Data Annex V2" (remove "11 + plan CM notes").
  - Labs used for Mridul · Shlok · Pranav · Shruti.
- **Slide 6:** "12 raw feeds"; Pranav card mentions "PCP visit booked but no mental-health visit".
- **Slide 7**
  - Header "5 members · 12 datasets · 75 records · 19 imperfections + 1 negative control · 4 plan lines".
  - Dataset counts per patient. IMP IDs on each imperfection. The exact 8 AM lines.
- **Slide 8:** add PrudenceAI/Innovaccer and HiLabs CureX rows to the landscape; "drafts 15–24 of 40 fields per call".
- **Slide 9**
  - Shlok score row "20 · 20 · 10 · 0 = 50".
  - Screenshots `02-queue-rows.png` and `04-conflict-resolution.png`.
- **Slide 10**
  - Screenshots `05-missing-context-vraj.png`, `09-assessment-pending.png` (and `06-time-lag-vraj.png` inset).
  - AI contract Assessment row updated.
- **Slide 11:** Phase 0 gate adds BAA/HIPAA + FDA CDS review; two new open questions (FDA CDS; CureX overlap).
- **Slide 12**
  - Market "$13.8B in 2023, ~13.7% a year (GMI)" (remove $43.3B).
  - Readmissions "$15.2k, ≈ 4 RN seats".
  - Add "Paid pilot $25k" and "~70% gross margin".

---

## 8. The two workbooks

### Synthetic Data Annex V2 (23 sheets)
- **Front sheets:** Start Here (hyperlinked index, counts, legend, freshness rules) · Patient Cards (the brief's Dataset | Sample record | Planted imperfection format + 8 AM line) · 8 AM Monday (live score formulas).
- **12 dataset sheets:** record_id, member_id and member_name first; evidence and freshness columns; grey "lineage" columns at the right with ET date-times + ISO.
- **Other sheets:** Imperfections (what's wrong, why it happens, what a naive system would do, what the workbench does, where to see it) · Insight Recipes · Scoring · Pharmacy Ledger Netting · Identity Hold (Q-001, not a 6th patient) · Edge Tests · Capture-Once Field Map (the 40 fields in 10 sections) · Data Dictionary.

### Research & Decision Register V2 (21 sheets)
- Start Here · Sources · **Deck Claim Check** · Consultation Audit
- Data Inventory · Time Model · Metric Dictionary · Guardrails · Pilot & GTM · Economics · Vendor Cost · Pilot Delivery Cost
- Prioritization · Roadmap & Open Questions · Risks · Competitive Landscape
- **Decision Log (12 decisions)** · Instrumentation · Assumptions · Requirements Map · Prototype Evidence

Both were generated by Python (openpyxl) and recalculated in LibreOffice so formulas show values. All internal links work.

---

## 9. The live prototype

Single-file HTML/CSS/JS (no framework), fictional data, runs in the browser.

**Screens (hash routes)**
- `#queue`: Work queue (DECIDE).
- `#member-<name>`: Member 360 (KNOW). Names: pranav · mridul · vraj · shruti · shlok.
- `#outreach-<name>`: Call & note (DO).

**Main features**
- Trigger badges with live ages.
- Score breakdown pane; accept / edit / dismiss-with-reason.
- Conflict resolution (Mridul dose, Pranav housing, Shruti living situation).
- Shlok's "checked: not a conflict" card.
- Vraj's missing-context checklist; time-lag chart (Mridul, Vraj).
- Contact & barriers strip with alternative routes.
- Notes → Auto-draft → 40 fields pending in yellow → Approve & Submit → saved to 7 places with a simulated CM receipt.
- Footer toggles: **Pharmacy feed down** (fills show unknown) and **Pause AI assist** (manual path).
- **Guided demo:** 9 steps.

**Honesty notes**
- The AI extraction is rule-based in the browser (no model call). Production would use a model behind the same approval gate.
- No real calls, messages or writeback.

**Tested**
- 695 of 695 controls produce a visible effect; 0 script errors.
- Text contrast ≥ 4.5:1; no sideways scroll at 390 px.
- Measured drafts per call: Pranav 24 · Mridul 24 · Vraj 15 · Shruti 24 · Shlok 21 of 40 fields.

**Edit workflow**
1. Edit `HiLabs_Workbench_Prototype_V3.html`.
2. Run `python3 scripts/build_index.py`.
3. Commit both files and push; Vercel redeploys.

---

## 10. Open items (what is left)

1. **Data Dictionary:** 100 of 244 rows in the annex still have a generic meaning ("… as reported by the source system"). Write a real meaning and example for each.
2. **Delete `archive/HiLabs_Workbench_Prototype_V1.html`.** It is publicly served at `/archive/…` with old names (Mmridul, Asha, Nia, Rohan).
3. **Check the live site** in a private window: "Mridul" with one m, the trigger badges, Jordan as co-manager.
4. **Review the deck returned by Claude Slides** against Section 5 and Section 7, slide by slide.
5. **User research:** none done. If the author interviews even one nurse or case manager, add a dated, real quote. Never invent one.
6. **Assumptions judges may probe:** 14-minute prep, 25-minute calls, ~55% two-day contact baseline, 20% capacity credit, $300 seat price, 1.23 loaded multiplier. All are labeled as assumptions in the Register.
7. **Interview prep:** have a one-sentence answer for each of these.
   - Why 14 minutes?
   - What if the pharmacy feed is down?
   - Why rules, not ML?
   - How do you stop alert fatigue?
   - How is this different from CureX or PrudenceAI?
   - What would you cut with half the team?
