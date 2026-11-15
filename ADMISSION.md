# Admission record

**Current state:** CANDIDATE (claims frozen; not tagged)

**Version:** 0.1.0

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Current verdict: NOT YET ADMITTED (no tag, archive or DOI)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** On 2026-11-15 the author asked for a review of
the draft paper and for this release to be prepared, with the result recorded
as proved and its novelty unconfirmed. The author approved including the
exact minima, the repository name `near-hadamard-determinant-bound`, and the
title. Each external action needs the author's explicit authorization.

## Principal claim

For every prime power $q\equiv1\pmod 4$ with $q\ge29$, every matrix of order
$n=q+1$ in Classes (4), (5) and (6) of Momihara–Suda–Xiang, Theorem 1.6,
built from any primitive element, satisfies $\lvert\det M\rvert>0.8W_n$
(paper Theorem 1.1).

Further results: the ratio tends to $\sqrt e/2$; the minima over $q\ge29$
are attained only at $q=29$, $37$ and $49$ in Classes (4), (5) and (6). No
new construction or record determinant is claimed.

## P1 — prior work and credit

| Check | Status | Evidence or residual |
|---|---|---|
| Closest mechanisms and parameter families compared | PASS | `audit/PRIOR-ART.md`: MSX (constructions, products, suggested limit, two-moment bound), Ipsen–Lee (trace–log expansion), the survey |
| Obtainable primary sources checked | PARTIAL | MSX accepted manuscript read in full; survey §5.2 and §5.6 read; Ipsen–Lee Theorem 2.6 read. **Li–Momihara–Xiang full text unread** (paywalled); only its preview was read |
| Contribution types distinguished | PASS | README "What is new" and "Not new"; paper §1.4 |
| Novelty bounded to searched corpus | PASS | "novelty unconfirmed" in the paper, README, CITATION.cff and `audit/PRIOR-ART.md` |
| Inaccessible or unperformed searches visible | PASS | Google Scholar, MathSciNet, zbMATH and the LMX full text logged NOT PERFORMED |
| Fast-follow scan within 7 days of tagging | PASS for 2026-11-15 | must be repeated if tagging happens after 2026-11-22 |

**P1 gate:** PARTIAL, residual accepted. On 2026-11-15 the author explicitly
accepted the named residual (Li–Momihara–Xiang full text unread), which is
stated with a pointer in the paper, README, CITATION.cff and
`audit/PRIOR-ART.md`.

## A1 — claim and artifact consistency

| Check | Status | Evidence or residual |
|---|---|---|
| Principal claim precise and no broader than proof | PASS | `audit/reports/manuscript-proof.md` (VERIFIED) |
| Scope visible near claim | PASS | Theorem 1.1 and the remarks after it; paper §6; README "Evidence and limits" |
| Proof, computation, literature separated | PASS | README evidence table; VERIFICATION.md |
| Credit | PASS | Ledger C5, C10, M3; README "Not new" |
| Public prose | PASS | `audit/reports/claims-consistency.md`; fixes C1–C12 |
| What is new | PASS | README section directly after the introduction, separate from "Earlier work"; known-before sentence, principal result marked, "Not new" list |
| Claims consistency | PASS | same results, numbers and novelty labels on README, abstract, introduction, CITATION.cff and `audit/PRIOR-ART.md`; theorem numbers checked against `main.aux` |
| Predecessor mirror | PASS | Modelled on `regularly-varying-mass-counts` v0.1.0: README layout, status line, CFF, CORRECTIONS, VERIFICATION, ADMISSION, checker, GPL-3.0-only |
| Metadata | PASS | title, author, version 0.1.0 and candidate status agree across README, PDF title page, `CITATION.cff` and this file |
| Adversarial check | PASS | three process-separated AI audits in `audit/LEDGER.md`, including an independent rebuild without FLINT; all findings resolved |

**A1 gate:** PASS. Any material claim edit reopens this gate.

## R1 — release and stewardship

| Check | Status | Evidence or residual |
|---|---|---|
| Reproduction | PASS | on 2026-11-15, a `git archive` extraction of commit `ed79d31` reproduced `paper/main.pdf` byte for byte (SHA-256 `48cd9e88…a599`); `make check` PASS; `make verify` and `make infimum` passed and matched the pinned certificates; `make rebuild` output equal to `evidence/independent-rebuild.log`; manifest check all OK. After that run the author asked for a plainer abstract and README introduction; the claims are unchanged (ledger U1). The revised paper was rebuilt twice with identical output, SHA-256 `070ade1a…17e2`, and `make check` passed. The computational files are unchanged since `ed79d31` |
| Artifact integrity | PASS (local) | deterministic PDF (fixed `SOURCE_DATE_EPOCH`); `MANIFEST.sha256` covers every tracked file |
| Hygiene | PASS | tree scanned for local paths and private data (ledger H1). README rendered with `gh api markdown` (GFM) on 2026-11-15: 56 inline and 1 display math elements, matching the source |
| Stewardship | PASS | `CORRECTIONS.md` |
| Tag, archive, DOI, metadata | NOT STARTED | require the author's authorization |

**Admission verdict:** NOT YET ADMITTED.

## External actions

| Action | Owner | Status |
|---|---|---|
| Local candidate commit | root agent, author authorization | done 2026-11-15 (authorized) |
| Private GitHub repository and push | author authorization | done 2026-11-15 (authorized): private `jeff-kline/near-hadamard-determinant-bound`, issues on, wiki off |
| Public visibility; secret scanning and push protection | author authorization | done 2026-11-15 (authorized): public; secret scanning and push protection enabled, as for the predecessor |
| Zenodo enablement before the Release | author, in the Zenodo portal | not done |
| Annotated tag `v0.1.0`, GitHub Release | author authorization | not authorized |
| Public-site listing; living-metadata update | author authorization (admission bundle) | not authorized |

Archive route (proposed, as for the predecessor): Zenodo GitHub integration,
with no manual deposit.
