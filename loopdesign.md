# Loop Design Summary

## Goal
Build a durable multi-round Steiner-system research loop that:
- carries knowledge forward across runs (not just within one run),
- avoids repetitive Round-1 web searching,
- enforces stronger round-close quality gates,
- and supports proof-style reasoning with reproducible artifacts.

## Major Work Completed

### 1) Core loop + round control improvements
- Tuned defaults toward faster iteration and explicit round budgets.
- Added stricter close behavior for synthesis-quality checks (especially round 5).
- Added timeout-aware behavior so rounds can stop and summarize instead of drifting.

### 2) Verification and scoring foundations
- Added/extended `verify_steiner_system(instance, certificate)` flow and round metrics.
- Standardized round scoring fields (validity, exact-once coverage, uncovered, overcovered, expected vs actual blocks).
- Clarified that a local `100` score means a certificate solves that specific instance under current verifier, not the full open-ended task.

### 3) Logging redesign for knowledge transfer
- Kept per-round logs (`round_0001` ... `round_0005`) as redundant raw history.
- Added two cross-run aggregate logs:
  - `RESEARCH_LOG.md` for Round-1 research knowledge,
  - `PRACTICE_LOG.md` for Round-2..5 empirical attempts.
- Updated behavior so each new turn reads aggregate logs first, then latest round artifacts.
- Added log-size management: when aggregate logs exceed threshold (~50KB), summarize/compress instead of unbounded growth.
- Improved uniqueness/time-based run directories to avoid overwriting prior run logs.

### 4) Round-role separation
- Round 1: research-focused, less repeated links, more deep reasoning and hypothesis formation.
- Rounds 2-4: practical search/construction attempts with tracked metrics.
- Round 5: mandatory synthesis over rounds 1-4, with stronger “next-hypothesis” transfer for subsequent generations.

### 5) Research-first constraints for full problem framing
- Removed old `S(2,3,7)` warmup coupling where it polluted large-instance workflow.
- Refocused on admissible large-instance exploration under:
  - `n > q > r > 5`, `r < 10`, `n < 200`.
- Enforced better messaging for invalid instance choices (e.g., impossible or off-constraint parameters).

### 6) Paper ingestion and local knowledge memory
- Added `papers/` workflow and integrated local paper extraction notes.
- Processed `/root/openquestions/papers/oai_first_proof.pdf` into reusable local notes.
- Updated Round-1 prompts to prioritize local paper memory + reasoning transfer before external link expansion.
- Reduced link-heavy output in research summaries; increased proof-oriented narrative and method transfer.

### 7) Search strategy direction (implemented + planned hooks)
- Added stronger prefilters/admissibility-first framing.
- Shifted recommendations toward exact-cover backbone ideas (DLX/residual exact repair), absorber-aware planning, and hybrid pipelines.
- Highlighted a key blocker observed in runs: residual exact phase often not reached due to overcoverage dynamics.

## Current Observed State
- Multi-run logging and cross-run memory are in place.
- Paper-aware reasoning path is in place.
- Round synthesis requirements are stronger than earlier versions.
- Practical solver improvements are still needed to consistently move past plateaued scores on hard instances.

## Known Caveats
- OCR/text extraction from PDFs can introduce noise; notes are useful but may need manual cleanup.
- If overcoverage remains high, residual exact completion may never activate.
- A score improvement in one instance does not imply global progress for all admissible `(n,q,r)` under 200.

## Recommended Next Engineering Steps
1. Make conflict-free partial packing (keep overcovered at 0 by invariant).
2. Always trigger a residual exact-cover stage once leftovers are small enough.
3. Add exact local repair (mini-DLX) to replace weak swap-only plateau handling.
4. Add stronger symmetry breaking (even if full Kramer-Mesner compression is not used).
5. Continue growing `RESEARCH_LOG.md` and `PRACTICE_LOG.md` as primary memory, with periodic compression.

## Repo Handoff Note
This repository is now structured for cross-machine continuation: push logs + code together, then resume using the same Codex account and reload context from:
- `steiner_logs/RESEARCH_LOG.md`
- `steiner_logs/PRACTICE_LOG.md`
- `steiner_logs/PAPER_NOTES.md`
- latest run `round_0001` and `round_0005`
