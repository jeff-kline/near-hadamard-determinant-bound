# Verification record — version 0.1.0

Recorded 2026-11-15.

## What is verified here

This record covers artifact consistency and reproducibility. It shows that
the document builds deterministically, that its labels, citations and log are
clean, that the certificates used in the proof regenerate and match the
pinned copies, and that every tracked file matches the manifest. It does not
verify proofs. The proof audits and their dispositions are in
[audit/LEDGER.md](audit/LEDGER.md) and `audit/reports/`.

Three computations are part of the proof of Theorem 1.1:

- the exact $0.8$ certificate for Classes (5)–(6), $29\le q<1001$
  (`scripts/finite_check.py`, 89 fields, 178 determinants);
- the exact $0.8$ certificate for Class (4), both signs, $29\le q<676$
  (`scripts/class4_check.py --finite`, 64 fields, 128 determinants);
- the ball-arithmetic certificate for the minima below the cutoffs
  $5720$, $5039$ and $10525$ (`scripts/infimum_check.py`, 666 fields).

`scripts/finite_audit.py` and `scripts/class4_examiner_proof.py` are
separately written checkers of the first two. `scripts/independent_rebuild.py`
builds the matrices directly, without FLINT, at four small orders.

## Environment

| Tool | Version |
|---|---|
| pdfTeX | 3.141592653-2.6-1.40.22 (TeX Live 2021, MacPorts 2021.58693_2) |
| Python (isolated virtual environment) | 3.12.14 |
| python-flint (FLINT and Arb) | 0.8.0 (`requirements.txt`) |
| Poppler `pdfinfo` / `pdftotext` | 26.07.0 |
| OS | macOS (Darwin 25.6.0) |

The Makefile sets `SOURCE_DATE_EPOCH=1794700800` (2026-11-15 00:00 UTC) and
`FORCE_SOURCE_DATE=1`, which fixes the PDF creation date and identifiers.

## Commands and outputs

`PYTHON` must be the absolute path of an isolated virtual-environment
interpreter. The Makefile refuses a base interpreter.

```sh
make paper                        # four pdfLaTeX passes; fails on any warning
make check   PYTHON=/abs/path/to/venv/bin/python
make verify  PYTHON=/abs/path/to/venv/bin/python
make infimum PYTHON=/abs/path/to/venv/bin/python
make rebuild PYTHON=/abs/path/to/venv/bin/python
shasum -a 256 -c MANIFEST.sha256
```

Results on 2026-11-15, one processor core:

- `make paper`: two consecutive builds gave the same `paper/main.pdf`,
  SHA-256 `070ade1a57eda5f40eba890ddd678f37f361dc9fdfa8fa4c4910adfe5ee317e2`,
  9 pages, no warnings.
- `make check`: `"status": "PASS"`, 9 pages, 30 labels, 27 references,
  4 bibliography entries, all 4 cited, no errors.
- `make verify` (about 2 CPU-minutes): `EXACT FINITE CHECK PASSED` for
  both certificates, `SOURCE SANITY CHECKS PASSED`, the Classes (5)–(6)
  checker completed its 178 resultant checks, `INDEPENDENT CHECKS PASSED`
  for Class (4), and `CERTIFICATES MATCH`: the regenerated certificates
  equal the pinned copies in `evidence/` except for timing and interpreter
  fields.
- `make infimum` (54 CPU-seconds): `INFIMUM CHECK PASSED`, 306 consistency
  checks against the exact determinants, one minimizer per class, and the
  result matches `evidence/infimum-certificate.json`.
- `make rebuild` (4 CPU-seconds): 120 ratio lines, every Gram check passes,
  and the three exact minima appear; the recorded output is
  `evidence/independent-rebuild.log`.

## Scope

- Every certificate except the rebuild uses FLINT and Arb, so a defect in
  that library would be shared.
- The ball arithmetic proves inequalities; the minima themselves are exact
  rationals taken from the exact certificates.
- None of these commands checks a proof.
