# Verification: M1 Gemini review

Reviewer: Gemini 2.5 Pro via Composio, cold (sent definitions + ratio table only, no sources). Raw output: `M1-gemini-review.md`.
Verifier: Claude, 2026-11-02. Each point graded ACCEPTED (change made), PARTLY ACCEPTED, or REJECTED (with reason).

| # | Gemini point | Verdict | Action / reason |
|---|---|---|---|
| 1 | Exclude leases from borrowings is non-standard | PARTLY ACCEPTED | Headline debt/equity stays on borrowings only, because the brief defines debt/equity as "only the borrowings" and that is what the balance sheet line says. Added lease-inclusive sensitivity (`debt_incl_leases_to_equity`, `roce_incl_leases`). Effect is small: Dabur FY26 D/E 0.09 to 0.11, ROCE 20.0% to 19.6%; Marico 0.08 to 0.13, ROCE 48.1% to 46.1%. Dabur FY25 lease balance is not a separate line in the FY25 filing (inside other financial liabilities), so FY25 sensitivity is n/a. |
| 2 | Capital employed uses total equity incl. NCI but ROE uses owners' equity | REJECTED | Intentional and standard: ROCE measures returns to all capital providers at group level (EBIT is pre-NCI), ROE measures returns to the parent's owners. Both definitions are stated and identical for both companies. |
| 3 | ROCE inflated by excluding leases | PARTLY ACCEPTED | True in direction, immaterial in size (see #1). |
| 4 | Closing-balance days distorted by Marico's late-year acquisitions | ACCEPTED as caveat | 4700BC (from 29 Jan 2026) and Cosmix (from 5 Feb 2026) bring full closing balances but only 2 months of revenue/COGS. Marico FY26 days are biased; direction depends on each acquiree's working capital. Will state in Part B. DuPont stays on closing balances, as required. |
| 5 | Debt/equity misleadingly low without leases | PARTLY ACCEPTED | See #1. Both companies are net cash regardless (Dabur 8,426 cr, Marico 2,221 cr), so the conclusion does not change. |
| 6 | Marico operating ROCE ex-treasury 93.5% "a fantasy" | REJECTED | Arithmetic checked: 2,126 / (4,849 - 2,576) = 93.5%; with leases 85.9%. It is high because Marico's operating asset base is small (PPE 832 cr) and suppliers and acquisition payables fund part of it. It is the misleading ratio for a different reason: the denominator includes 2,534 cr of goodwill and intangibles from acquisitions; that is noted. |
| 7 | Marico gross margin fall needs copra context | ACCEPTED | Material cost 49.7% to 55.5% of revenue (investor presentation). India value growth 28% on 8% volume. Will explain in Part B/C. |
| 8 | Marico CCC improvement may be an acquisition artefact | ACCEPTED as caveat | Same as #4. |
| 9 | Marico margin fell while revenue rose 26% | ACCEPTED (it is the story) | Price-led revenue on commodity pass-through dilutes margin %; operating EBIT still rose 8% (1,961 to 2,126). A mix-shift / input-cost question, not proven deterioration. |
| 10 | Marico FY25 CFO below PAT is a warning sign | ACCEPTED | FY25 working capital absorbed 293 cr (receivables -205, payables -218). FY26 reversed (+253). Will report both years in Part B. |
| 11 | Dabur operating ROCE jump 47.9% to 58.7% needs justification | ACCEPTED | Cause is the denominator, not the CCC: borrowings rose 730 to 1,063 cr while cash and investments rose 8,038 to 9,489 cr, so "capital employed less treasury" shrank 3,902 to 3,377 cr. Receivables also fell 888 to 715 cr (reported). This makes the ex-treasury ROCE sensitive; use it as an illustration of why headline ROCE misleads, not as a precise figure. |
| 12 | "Net debt" label wrong for negative values | ACCEPTED (cosmetic) | Relabelled `net_cash` (positive = net cash). The definition was already stated. |
| 13 | Show investing and financing uses of cash | ACCEPTED | Already in numbers.csv (capex, dividends, acquisitions, treasury purchases). Will tabulate in Part A element 3 and Part B. |
| 14 | Segment comparison missing | PARTLY ACCEPTED | Dabur segment note captured (Consumer Care / Food / Retail / Other). Marico reports India / International; rupee split not in the documents read. Will state where looked. Cross-company segment-by-segment comparison is out of scope (different segment definitions). |
| 15 | Qualitative analysis missing | REJECTED for M1 | M1 is the data layer. Business model and cost structure are M2. |
| 16 | Use average balances | REJECTED | Brief prescribes closing balances for DuPont; we use closing everywhere for consistency and state it. |

## Gemini's two cases (kept for Part C)
Kept verbatim in the raw file, section 5. Dabur case: stability, net cash, negative CCC, high cash conversion. Marico case: growth ~2x, ROE >40%, higher turnover and ROCE.

Status after verification: M1 data layer accepted with caveats above. M1 READY FOR REVIEW.
