# Prior-art record

**Verdict: novelty unconfirmed.** No earlier proof of the 0.8 bound or of the
exact infima for Classes (4)–(6) was found in the sources checked. The full
text of the closest follow-up, Li–Momihara–Xiang (2026), was not openly
accessible at the time of writing (paywalled; no open copy found), so
overlap with it is not excluded. This record bounds the search; it is not a
worldwide novelty claim, and no priority is claimed.

## Anchor sources

| Source | What was read | What it gives | What it does not give |
|---|---|---|---|
| Momihara, Suda, Xiang, *Linear Algebra Appl.* 654 (2022), doi:10.1016/j.laa.2022.08.028 (MSX) | Full accepted manuscript | Classes (4)–(6) of Theorem 1.6; the determinants as products of Gauss and Jacobi sums; ratios 0.844, 0.846, 0.823 at $n=30$; checks through $n\le1000$; the suggested limit $\sqrt e/2$ for these classes (p. 4) and its proof for Class (9); a two-moment lower bound (Prop. 2.1) whose normalized limit is zero; Problem 7.1 | A proof of the 0.8 bound, the limit for Classes (4)–(6), or the infima |
| Egan, Kotsireas, London, Ó Catháin, *Recent progress in the construction of Hadamard matrices*, arXiv:2610.27175v2 (3 Nov 2026) | §5.2 and §5.6 | Problem 15 restates the 0.8 part of MSX Problem 7.1 as open; §5.2 cites Li–Momihara–Xiang | — |
| Li, Momihara, Xiang, *New constructions of square (±1)-matrices with large determinants*, *Linear Algebra Appl.* 752 (2027) 66–106, doi:10.1016/j.laa.2026.08.013 (LMX) | Publisher preview only: abstract, introduction, section openings, first sentence of the concluding remarks | Type I near-Hadamard constructions, whose ratio tends to 1; its Theorem 1.7 concerns MSX Classes (7)–(8) | **Unread:** the body and the rest of the concluding remarks. The visible text does not mention Classes (4)–(6), Problem 7.1 or the 0.8 bound, but this is not evidence of absence |
| Ipsen, Lee, *Determinant approximations*, arXiv:1105.0437 (2011), Theorem 2.6 | Full text, Theorem 2.6 and proof | A trace-log expansion of $\log\det$ with an explicit error bound; with the class moments inserted it gives the limit $\sqrt e/2$ | The class moments, the $2\sqrt q$ spectral bound, explicit thresholds, or the finite range |

The strongest contemporaneous evidence is that the survey, revised on
3 November 2026, still poses the question while citing LMX. That is evidence
about the survey authors' knowledge, not proof that LMX does not contain a
solution.

## Claim ledger

| ID | Claim | Outcome | Consequence for the paper |
|---|---|---|---|
| N1 | The 0.8 bound is an explicit open problem for exactly these three classes | Confirmed: MSX Problem 7.1 (p. 20); survey Problem 15 | Stated as the question answered |
| N2 | The limit $\sqrt e/2$ is discovered here | Overclaim: MSX suggest it for these classes and prove it for Class (9) | Credited to MSX as a suggestion; the proof for Classes (4)–(6) is stated as a proof of their suggestion |
| N3 | The constructions, determinant formulas or numerical evidence are new | Overclaim: all in MSX | Credited to MSX |
| N4 | The moment method is new | Overclaim: MSX use two moments; Ipsen–Lee give the trace-log expansion | Method credited; only its application with explicit constants is claimed |
| N5 | The survey treats the bound as open while citing LMX | Confirmed | Recorded above |
| N6 | LMX proves the bound or limit for these classes | Unverifiable: full text unread | Novelty unconfirmed |
| N7 | An older general theorem already states the MSX result | Not found | No claim of a new general theorem |
| N8 | This is the first proof | Gap: N6 open | No first-proof claim |
| N9 | The exact infima over $q\ge29$ are new | No source computes them; MSX report only that the ratio exceeds 0.8 for $n\le1000$ | Stated as new within the sources checked |

## Searches

Earlier searches, 15 November 2026, made during the original work:
OpenAlex and Semantic Scholar forward citations of MSX; Crossref metadata;
OpenAlex phrase search; arXiv metadata queries for "near-Hadamard",
"Momihara" with determinant/Hadamard, and "large determinants"; Zenodo
queries; GitHub code and repository queries; targeted web searches combining
the authors with "bound", "limit", "asymptotic", "0.8", "0.824", "sqrt(e)",
"Problem 7.1", "solved" and "resolved". Results: no source proving the bound.
Two follow-up attempts to obtain the LMX full text failed (publisher access,
author pages).

Fast-follow scan, 15 November 2026 (raw responses in `audit/searches/`):

| Query | Result |
|---|---|
| `gh search repos "near-Hadamard"` | 1 hit, unrelated (imaging) |
| `gh search repos "Ehlich Wojtas"` | 1 hit: mattppal/ehlich-wojtas, a Lean formalization of the upper bound itself; no constructions |
| `gh search repos "D-optimal determinant"` | 0 hits |
| `gh search code "Momihara"` | 20 hits; screened: bibliographies, record tables, Hadamard construction data; none on Classes (4)–(6) or Problem 7.1 |
| `gh search code "Ehlich-Wojtas"` | 9 hits; screened: OEIS data, max-determinant record tasks (elder-plinius/V3R1T4S), a two-circulant search script; none on these classes |
| arXiv API: `"near-Hadamard"` or Momihara+determinant or Ehlich+determinant, newest first | 4 entries, 2004–2013; none relevant |
| Zenodo API: `"near-Hadamard"` or Momihara+determinant or `"Ehlich-Wojtas"` | 0 records |
| OpenAlex: works citing MSX | 1: LMX |
| OpenAlex: works citing LMX | 0 (known indexing gap: the survey cites LMX) |
| Semantic Scholar: works citing MSX | 2: LMX and the survey |

**Not performed:** Google Scholar (inaccessible to automated clients); full
text of LMX (paywalled; no open copy found); Cohn, *Almost D-optimal designs*
(2000), full text; MathSciNet and zbMATH.

Repeat this scan within 7 days before tagging.
