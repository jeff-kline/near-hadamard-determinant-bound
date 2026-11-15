# Sharp determinant bounds for three near-Hadamard families

Jeffery Kline

**Version 0.1.0 — release candidate, not yet published.** No public tag or
DOI exists yet. Admission under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html)
is a release decision, not peer review or a correctness certificate. The
release checklist is [ADMISSION.md](ADMISSION.md).

The paper is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex). **Novelty is unconfirmed:** the full text
of a closely related paper by Li, Momihara and Xiang, published online in 2026, has not been read
(see [Earlier work](#earlier-work)).

## Introduction

No $n\times n$ matrix with entries $\pm1$, where $n\equiv2\pmod 4$, has
determinant larger in absolute value than the Ehlich–Wojtas bound

```math
W_n=(2n-2)(n-2)^{(n-2)/2}.
```

For each prime power $q\equiv1\pmod 4$, Momihara, Suda and Xiang (2022)
constructed three such matrices of order $n=q+1$, their Classes (4), (5)
and (6). They wrote the determinants as products over Gauss and Jacobi sums
without evaluating them, and asked whether each family reaches at least
$0.8W_n$ for every $n\ge30$. A 2026 survey lists this as open (Problem 15).

This paper proves that every matrix of order $n\ge30$ in the three families
exceeds $0.8W_n$, and that in each family the ratio to $W_n$ tends to
$\sqrt e/2\approx0.824$, the limit Momihara, Suda and Xiang suggested. It
also finds the smallest ratio in each family exactly: about $0.8169$,
$0.8154$ and $0.8184$, attained only at $n=30$, $38$ and $50$.

The proof needs only two exact facts about the factors of each product,
their sum and their sum of squares, both given by character orthogonality,
together with the size of a Gauss sum. This settles every $q\ge676$ for
Class (4) and every $q\ge1001$ for Classes (5) and (6). Exact integer
computations settle the remaining 306 determinants. The same estimate
exceeds the three smallest ratios for every $q\ge10525$, and a rigorous
interval computation covers the orders below.

## What is new

Momihara, Suda and Xiang built the three families, wrote their
determinants as character-sum products, computed the ratios at $n=30$,
checked that they are at least $0.8$ for $38\le n\le1000$, and suggested the limit
$\sqrt e/2$, which they proved for a different family, their Class (9).
Their Problem 7.1 asks for sharp lower bounds and, in particular, for the
$0.8$ bound. New here:

1. **Principal result: the $0.8$ bound.** For every prime power
   $q\equiv1\pmod 4$ with $q\ge29$, every matrix $M$ of order $n=q+1$ in
   Classes (4), (5) and (6), built from any primitive element, satisfies
   $\lvert\det M\rvert\gt 0.8W_n$ (paper Theorem 1.1). This answers survey
   Problem 15.
2. **The limit.** In each class the ratio $\lvert\det M\rvert/W_n$ tends to
   $\sqrt e/2$, uniformly in the primitive element. This proves the limit
   Momihara, Suda and Xiang suggested for these classes.
3. **The exact minima.** Over all $q\ge29$ the smallest ratios are about
   $0.81690$ (Class 4, $q=29$), $0.81541$ (Class 5, $q=37$) and $0.81843$
   (Class 6, $q=49$), with exact rational values in the paper; every other
   order gives a strictly larger ratio. These are the best constants
   $c_i$ with $\lvert\det M\rvert\ge c_iW_n$ for all $n\ge30$; with the
   limit, they give the sharp lower bounds Problem 7.1 asks for, in that
   sense.
4. **Both orientations of Class (4).** The Class (4) matrix can take up to two
   determinant values at each $q$, depending on the primitive element. The
   minimum at $q=29$ comes from the one Momihara, Suda and Xiang did not
   report; the other gives their value, about $0.844$.

Not new:

- The constructions and the determinant products are those of Momihara,
  Suda and Xiang (Theorem 1.6 and its propositions).
- Bounding a determinant through the first two moments of its spectrum is
  standard: Momihara, Suda and Xiang use a two-moment bound, and Ipsen and
  Lee (Theorem 2.6) give a general trace–log expansion with error bounds.
  What is new is the pair of exact moment identities for these families,
  the explicit thresholds and the finite computations.
- The limiting value $\sqrt e/2$ was suggested by Momihara, Suda and Xiang.

These statements rest on a bounded comparison recorded in
[audit/PRIOR-ART.md](audit/PRIOR-ART.md). We have not found the results above
in the sources checked, but one closely related paper is unread; this is
not a novelty claim.

## Earlier work

- **Momihara, Suda and Xiang (2022)**, *Square (1, −1)-matrices with large
  determinants and near-Hadamard matrices*, Linear Algebra Appl. 654,
  [doi:10.1016/j.laa.2022.08.028](https://doi.org/10.1016/j.laa.2022.08.028):
  the nine families, the determinant products, the numerical ratios, the
  suggested limit, and Problem 7.1.
- **Egan, Kotsireas, London and Ó Catháin (2026)**,
  [*Recent progress in the construction of Hadamard matrices*](https://arxiv.org/abs/2610.27175v2),
  version 2 of 3 November 2026: Problem 15 in §5.6 restates the $0.8$
  question as open.
- **Li, Momihara and Xiang (2027; online August 2026)**, *New constructions of square
  (±1)-matrices with large determinants*, Linear Algebra Appl. 752,
  [doi:10.1016/j.laa.2026.08.013](https://doi.org/10.1016/j.laa.2026.08.013).
  Only the public preview was read. Its abstract, introduction and section
  openings concern type I near-Hadamard matrices, whose ratio tends to $1$,
  and do not mention Classes (4)–(6) or Problem 7.1. Its full text could
  contain overlapping results. The survey cites this paper and still lists
  the question as open.
- **Ipsen and Lee (2011)**, [*Determinant approximations*](https://arxiv.org/abs/1105.0437),
  Theorem 2.6: the trace–log expansion of a determinant with an error
  bound.

## Evidence and limits

| Claim | Status |
|---|---|
| Moment identities and the bound $\lvert T\rvert\le2\sqrt q$ (Propositions 3.1 and 4.1) | proved on paper, from the products of Momihara, Suda and Xiang |
| $0.8$ bound for $q\ge676$ (Class 4) and $q\ge1001$ (Classes 5–6), and the limit | proved on paper |
| $0.8$ bound for $29\le q$ below those thresholds | certified computation: 306 exact integer determinants, `scripts/finite_check.py`, `scripts/class4_check.py` |
| Exact minima | proved on paper for $q\ge5720$, $5039$ and $10525$ respectively; certified ball-arithmetic computation below, `scripts/infimum_check.py` |

- The finite certificates were rechecked by separately written programs
  (`scripts/finite_audit.py`, `scripts/class4_examiner_proof.py`). These and
  the minima certificate use the FLINT and Arb libraries, so the arithmetic
  library is shared.
- A rebuild written independently, without FLINT, constructs the matrices
  from the definitions of Momihara, Suda and Xiang at $q=29$, $37$, $41$
  and $49$, for every primitive element, and reproduces the three minima
  exactly (`scripts/independent_rebuild.py`).
- The bound $\lvert T\rvert\le2\sqrt q$ in Class (4) uses the Gauss-sum
  formula of Momihara, Suda and Xiang (their Proposition 3.5), which was
  checked as quoted but not re-derived.
- The proofs were checked by process-separated AI reviews. No independent
  human expert has examined them. Agreement among AI checks is evidence
  about a process, not independent validation.
- The theorem bounds three existing families; it constructs no new matrices
  and improves no record determinant.

## Reproduce

Requirements: pdfLaTeX and an isolated Python environment with the packages
in `requirements.txt` (python-flint 0.8.0). Set `PYTHON` to the
environment's absolute interpreter path.

```sh
make paper                                             # four pdfLaTeX passes; fixed SOURCE_DATE_EPOCH
make check PYTHON=/absolute/path/to/venv/bin/python     # labels, citations, TeX log, PDF text
make verify PYTHON=/absolute/path/to/venv/bin/python    # exact certificates for the 0.8 bound
make infimum PYTHON=/absolute/path/to/venv/bin/python   # interval certificate for the minima
make rebuild PYTHON=/absolute/path/to/venv/bin/python   # independent rebuild, q = 29, 37, 41, 49
shasum -a 256 -c MANIFEST.sha256
```

`make verify` regenerates the exact certificates, reruns the two separately
written checkers, and compares the results with the pinned copies in
`evidence/`. `make infimum` takes about a minute on one core and compares
its result with `evidence/infimum-certificate.json` in the same way. Neither
checks the proofs. [VERIFICATION.md](VERIFICATION.md) records the commands,
outputs and environment.

## Repository contents

- `paper/`: LaTeX source `main.tex` and the reading copy `main.pdf`.
- `scripts/finite_check.py`, `scripts/class4_check.py`: exact certificates
  for the $0.8$ bound below the analytic thresholds.
- `scripts/finite_audit.py`, `scripts/class4_examiner_proof.py`: separately
  written checkers of those certificates.
- `scripts/infimum_check.py`: the ball-arithmetic certificate for the minima.
- `scripts/independent_rebuild.py`: the independent rebuild of the matrices.
- `scripts/compare_certificates.py`, `scripts/check_paper.py`: comparison
  with the pinned certificates, and the document consistency checker.
- `evidence/`: the pinned certificates and checker outputs.
- `audit/`: the prior-art record, the review reports and the audit ledger.

## Citation

Jeffery Kline, *Sharp determinant bounds for three near-Hadamard families*,
version 0.1.0 (2026). Machine-readable metadata is in
[CITATION.cff](CITATION.cff).

## License and corrections

The paper, source, prose and code are licensed under
[GPL-3.0-only](LICENSE). See [CORRECTIONS.md](CORRECTIONS.md) for the
correction, withdrawal and supersession policy. AI systems assisted
development, writing, computation and checking under the author's
direction; the author is responsible for the work.
