# Admission record

**Current state:** ADMITTED

**Version:** 0.1.0

**Tag:** `v0.1.0` → `7fb488ddfd7a76cae6218b31f537e5199fe8519d`

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Current verdict: ADMITTED (2026-11-15)

**Version DOI:** [`10.5281/zenodo.24265533`](https://doi.org/10.5281/zenodo.24265533) · **Concept DOI:** `10.5281/zenodo.24265532` · **Record:** <https://zenodo.org/records/24265533>

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
| Immutable semantic tag | PASS | annotated `v0.1.0` (object `f81231e`) → `7fb488d`; tagger is the GitHub noreply identity. The tagged tree's paper was rebuilt from the Zenodo archive to the archived PDF byte for byte, and `make check` and the manifest pass there; the computational files are unchanged since `ed79d31` |
| Public permanent archive with provider byte identity | PASS | the pinned GitHub `zipball/v0.1.0` (downloaded twice, identical) and the Zenodo file are byte-identical: 812,435 bytes, SHA-256 `da00dc98a986fb670343750bfc76c07c4282603c429423167c9db23c70ee486a`; Zenodo MD5 `57323013fb510772e811d2aeb26445f6` |
| DOI resolves; living repository identifies the version | PASS | `doi.org/10.5281/zenodo.24265533` redirects to the Zenodo record; README, `CITATION.cff` and the living paper carry the version DOI |
| Archive metadata matches repository | PASS | title, creator Kline, Jeffery, version v0.1.0, publication date 2026-11-16 (UTC), license `gpl-3.0`, resource type software, open access, related identifier the `v0.1.0` tree |
| Machine-readable citation | PASS | `CITATION.cff` with version DOI, concept DOI and `date-released: 2026-11-16` (Zenodo's date) |

**R1 gate:** PASS.

**Admission verdict:** ADMITTED (2026-11-15). The accepted P1 residual and the residual risks in `audit/LEDGER.md` remain.

## External actions

| Action | Owner | Status |
|---|---|---|
| Local candidate commit | root agent, author authorization | done 2026-11-15 (authorized) |
| Private GitHub repository and push | author authorization | done 2026-11-15 (authorized): private `jeff-kline/near-hadamard-determinant-bound`, issues on, wiki off |
| Public visibility; secret scanning and push protection | author authorization | done 2026-11-15 (authorized): public; secret scanning and push protection enabled, as for the predecessor |
| Zenodo enablement before the Release | author, in the Zenodo portal | done 2026-11-15; Zenodo release webhook present and active |
| Annotated tag `v0.1.0`, GitHub Release | author authorization | done 2026-11-15 (23:32 UTC): Release "Version 0.1.0" |
| Public-site listing | author authorization (admission bundle) | done 2026-11-15: landing entry "The 0.8 bound for near-Hadamard determinants" at <https://jeff-kline.github.io/> (site commit `2ba2e68`); Pages build and live HTML checked for title, blurb, repository link and version DOI |
| Living-metadata update (this commit) | author authorization (admission bundle) | done 2026-11-15, pushed after the site listing was verified live |

## Archive verification

- Route: Zenodo GitHub integration; no manual deposit.
- Pinned before the GitHub Release: GitHub API `zipball/v0.1.0`, downloaded
  twice, identical, 812,435 bytes, SHA-256 `da00dc98a986fb670343750bfc76c07c4282603c429423167c9db23c70ee486a`.
- Zenodo file `jeff-kline/near-hadamard-determinant-bound-v0.1.0.zip`,
  downloaded through the record's file link: identical to the pinned zipball.
  Every file passes its `MANIFEST.sha256`.
- Separate determinism check: `git archive --format=zip
  --prefix=near-hadamard-determinant-bound-v0.1.0/ v0.1.0`, generated twice,
  identical, 811,259 bytes, SHA-256 `180c68748ebe35bc5cb53ffb714f6fbce28ef669601f0684db06dfec62874f6b`. This is a different file from
  the provider zipball and is not compared with it.
- Mechanical audit at the archived state, on the unchanged tagged tree:
  11 pass, 0 warnings, 0 fail.
