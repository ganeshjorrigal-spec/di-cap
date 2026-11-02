# AGENTS.md (project: di-cap)

This file only ADDS project rules. Ganesh's global preferences stay in force. If anything here conflicts with them, follow the global ones and flag the conflict in today's log.

## What this is
Ganesh's individual capstone for the Foundation of Finance course: Dabur India (tracked company) against Marico (peer). Question: which is the stronger, more resilient business, and what would change his mind. Full scope: `CHARTER.md`. Brief: `docs/sources/course/Capstone_Brief.md`.

## Who does what
- **Claude (HQ and builder)** researches, computes, drafts. Writes every file except where noted.
- **Gemini 2.5 Pro (via Composio)** is the independent reviewer. It gets each finished piece cold and attacks it. Its output is saved verbatim as `docs/review/<milestone>-gemini-review.md`, then Claude writes `<milestone>-verification.md` grading each point ACCEPTED / REJECTED (with reason).
- **Ganesh** ticks milestones DONE. Claude only marks READY FOR REVIEW.
- Gemini via the API has no live web access. Never take a number from Gemini. Numbers come only from annual reports, stock-exchange filings or screener.in, logged in `data/numbers.csv`.

## Start of every session, read in this order, nothing else unless asked
1. `CHARTER.md`  2. `STATE.md`  3. `MILESTONES.md` (current milestone only)  4. `DECISIONS.md`  5. the last two files in `docs/log/`  6. `SCRATCHPAD.md`
Run `git pull` first.

## How work runs
1. One milestone at a time. Run its acceptance checks, record evidence in today's log.
2. Mark it `READY FOR REVIEW`, never `DONE`.
3. Overwrite `STATE.md`, append to `docs/log/YYYY-MM-DD.md`, clear checked items in `SCRATCHPAD.md`, commit and push.

## Memory rules
- Save before you forget: past about half the context, or before any compaction, append to today's log and refresh `STATE.md`.
- Logs and decisions are append-only.
- Ganesh's live instructions go into `SCRATCHPAD.md` as checkboxes immediately.

## Rules for every number (from the brief)
- Every figure: statement, year, source location, definition, type (Reported / Calculated / Assumed). One row in `data/numbers.csv`.
- Consolidated statements, same years and same definitions for both companies.
- DuPont on closing balances: ROE = (NP / Revenue) x (Revenue / closing total assets) x (closing total assets / closing equity). Must tie to NP / closing equity.
- CCC = receivable days + inventory days - payable days. Components must add.
- "Not disclosed, looked in X" is a full answer. Never invent a number.

## Writing rules for anything submitted
- No em dashes. Commas, colons, semicolons or restructured sentences instead.
- Never mention class, sessions, session names, the faculty or "as learnt in class". Cite websites, annual reports and published books only.
- Plain language, no jargon. Written in Ganesh's voice, first person where the brief asks for a view.
- Light backgrounds only for any HTML or slides.
- Excel: one font, no shading or italics; table headers black fill, white font.

## Safety
- No secrets in any file. Commit small, clear messages. No force pushes.
