# Audit ledger

Release 0.1.0. All reviewers were AI agents run in separate contexts, each
read-only except for its own report. They are process-separated AI
auditors, not independent experts. Reports are in `audit/reports/`.

## Audits for this release (15 November 2026)

| Lane | Report | Verdict |
|---|---|---|
| Claims consistency across paper, README, CITATION, prior-art record and evidence | `reports/claims-consistency.md` | Discrepancies in wording and documentation only; all numbers consistent |
| Proof and certificate audit of the assembled manuscript, including equivalence with the earlier audited proofs and the new Section 5.3 | `reports/manuscript-proof.md` | VERIFIED; five documentation errata |
| Independent rebuild of the matrices from the MSX definitions, without FLINT | `reports/independent-rebuild.md` | AGREES at q = 29, 37, 41, 49 |

Earlier audits, made during the original work and not repeated here: a
proof audit of the Classes (5)–(6) derivation, an audit of the
correspondence with the MSX source, an audit of the finite certificate
with a separately written checker (`scripts/finite_audit.py`), and an
initial attack and proof audit of Class (4) with a separately written
checker (`scripts/class4_examiner_proof.py`). The manuscript-proof lane
compared the edited manuscript with those audited texts.

## Findings and dispositions

Each finding has one label: error, gap, missing hypothesis, sharpening, or
documentation.

| ID | Source | Finding | Label | Disposition |
|---|---|---|---|---|
| C1 | claims | README said the result answers Problem 7.1 "in full" | sharpening | Fixed: README states the sense (best constants and the limit); paper wording matched (see M2) |
| C2 | claims | ADMISSION.md, VERIFICATION.md, MANIFEST.sha256 and the audit ledger were linked but missing | documentation | Fixed: files written before freezing |
| C3 | claims | Makefile `infimum` comment said "several CPU hours" and passed an unsupported option | documentation | Fixed |
| C4 | claims | `make infimum` overwrote the pinned certificate without comparison | documentation | Fixed: the script writes next to itself; `compare_certificates.py infimum` compares with `evidence/` |
| C5 | claims | Li–Momihara–Xiang dated 2026 in some places, 2027 in others | documentation | Fixed: "2027; online August 2026" |
| C6 | claims | Process-history wording in PRIOR-ART; "process-separated AI reviews" unexplained | documentation | PRIOR-ART fixed; the review wording is kept, as in earlier releases, and explained here |
| C7 | claims | README introduction uses undefined terms (near-Hadamard, Gauss and Jacobi sums, ball arithmetic, FLINT) | documentation | Kept: standard terms for the audience; defined in the paper |
| C8 | claims | README: Class (4) "can take two" values; paper: "at most two" | sharpening | Fixed: "up to two". The rebuild found one value at q = 49 |
| C9 | claims | README: minima proved "above" the cutoffs; paper: from them | sharpening | Fixed |
| C10 | claims | README: MSX checks "n ≤ 1000"; MSX: n = 30 and 38 ≤ n ≤ 1000 | sharpening | Fixed |
| C11 | claims | CITATION.cff paired Problem 7.1 and Problem 15 as both fully answered | sharpening | Fixed |
| C12 | claims | PRIOR-ART page numbers for MSX not verified | documentation | Verified against the PDF: p. 4 (limit remark, Class (9)), p. 20 (Problem 7.1) |
| M1 | proof | Section 5.3 said "306 orders"; they are 306 determinants | documentation | Fixed |
| M2 | proof | "answers Problem 7.1" slightly strong | documentation | Fixed: answers Problem 15 (the 0.8 question of 7.1) and gives sharp constants in the sense of 7.1 |
| M3 | proof | Citation for (D5)–(D6) should include MSX Theorem 4.1 | documentation | Fixed |
| M4 | proof | "several hours" for exact computation had no recorded measurement | documentation | Fixed: measured about two minutes per exact determinant at q ≈ 10^4 |
| M5 | proof | `infimum_check.py` checked only ≥ for the non-minimizing Class (4) sign at q = 29 | documentation | Fixed: strict comparison everywhere except the minimizer, and exactly one minimizer per class asserted; rerun passed |
| R1 | rebuild | none | — | Rebuild code added as `scripts/independent_rebuild.py` (`make rebuild`) |
| H1 | root | Pinned certificates recorded a local interpreter path; audit reports named local directories | documentation | Removed the `executable` field from the pinned certificates (the comparison ignores it) and replaced local paths in the reports with repository-relative paths or placeholders; no other change to the reports |

## Residual risks

- **Novelty.** The full text of Li–Momihara–Xiang is unread
  (`PRIOR-ART.md`, N6).
- **Shared tools.** All certificates except the rebuild use FLINT and Arb
  through python-flint 0.8.0. The rebuild is independent of them but covers
  only q ≤ 49.
- **Upstream input.** The Class (4) bound $\lvert T_\psi\rvert\le2\sqrt q$
  rests on MSX Proposition 3.5, which was checked as quoted but not
  re-derived. The proof audit confirmed the bound numerically for every
  prime q < 5720 and every prime power q < 1000.
- **No human expert** has reviewed the proofs.
