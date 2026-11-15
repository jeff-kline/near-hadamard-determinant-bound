# Corrections, withdrawals, and supersession

This repository keeps a visible record of material corrections to released
claims and artifacts.

## Policy

- Minor typographical or navigational fixes may be made on the living default
  branch without changing an archived release.
- A change to a theorem statement, hypothesis, proof dependency, citation that
  affects priority or scope, or verification artifact creates a new version.
  The earlier tag and permanent archive remain unchanged and identifiable.
- A material error that invalidates a principal claim will be marked
  prominently in the README and in this file. The affected release will not be
  deleted or silently replaced.
- A withdrawn result remains findable with the reason, date, affected
  versions, and any replacement or correction linked here.
- Public tags and archived files are immutable. Corrections are made in a new
  commit and, when material, a new tagged release.
- If earlier work is found that anticipates a result here, the novelty
  statements will be narrowed and the source credited in a new version. In
  particular, the full text of Li, Momihara and Xiang (2027; online August
  2026) was not openly
  accessible at release; see [audit/PRIOR-ART.md](audit/PRIOR-ART.md).

Suspected errors may be reported through the repository's issue tracker:
<https://github.com/jeff-kline/near-hadamard-determinant-bound/issues>.

## Version history

### 0.1.0 — released 2026-11-15

- Tag `v0.1.0` at commit `7fb488d`; version DOI
  [`10.5281/zenodo.24265533`](https://doi.org/10.5281/zenodo.24265533), concept DOI `10.5281/zenodo.24265532`. Zenodo
  records the publication date as 2026-11-16 (UTC).
- The tagged snapshot retains its prepublication “release candidate” wording
  and carries no DOI, because the DOI was minted by Zenodo after the GitHub
  Release. The living repository and paper now carry the active DOI; the
  archived files were not changed.
- After the tag, the living README, `CITATION.cff` and `audit/PRIOR-ART.md`
  say that the Li–Momihara–Xiang full text "was not openly accessible at the
  time of writing" instead of "has not been read". Both describe the same
  fact: the paper is paywalled and no open copy was found.
- Release preparation, before the tag: the dispositions of all audit findings
  are in `audit/LEDGER.md`.
