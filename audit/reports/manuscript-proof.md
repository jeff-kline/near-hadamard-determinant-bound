STAGE: PROOF-AUDIT
VERDICT: VERIFIED

CLAIM: paper/main.tex (SHA-256 7af465d3d940be2e546131ff696b40df8fada7eb73647efb3e5fbd38f7a174f0), Theorem 1.1. Take a prime power q ≡ 1 (mod 4) with q ≥ 29, and any matrix of Class (4), (5) or (6) of MSX Theorem 1.6 built from any primitive element. Then:
- R_i(q) = |det M| / (2q(q-1)^((q-1)/2)) > 4/5.
- R_i(q) → sqrt(e)/2, uniformly in the primitive element.
- The minima over q ≥ 29 and all primitive elements are
  - min R_4 = R_4(29) = 16067122183125/19668469112621 ≈ 0.81690,
  - min R_5 = R_5(37) = 690199704608000/846441320833557 ≈ 0.81541,
  - min R_6 = R_6(49) = 13602934789834170625/16620815899787526144 ≈ 0.81843.
- Every other q gives a strictly larger value in the same class, for both signs in Class (4).

The verdict covers the whole statement. It depends on the published MSX results listed under DEPENDENCIES and on FLINT/Arb being correct.

EVIDENCE:

1. Lemma 2.1 (main.tex:149-169) is correct. For |t| ≤ ρ < 1:
   - |log(1-t) + t + t²/2| ≤ Σ_{k≥3} |t|^k / k ≤ |t|³ / (3(1-ρ)).
   - Summing over j with Σ|t_j|³ ≤ ρV gives the bound in the lemma.
   - ρ = 2√q/(q+1) gives 1-ρ = (√q-1)²/(q+1), so ρ/(3(1-ρ)) = 2√q/(3(√q-1)²).
   - V < 1 holds in both uses: V = (q²-4q-1)/(q+1)² for Classes (5)-(6) and V = (q-1)/(q+1) for Class (4).

2. Proposition 3.1 (main.tex:194-233) is correct. Each step was checked by hand:
   - Conjugation: Ū_j = V_j via x = 1/y, using η(-1) = 1.
   - Nontriviality: χ^j, η and χ^jη are all nontrivial for 1 ≤ j < m, so |U_j| = √q.
   - Square indicator: on F_q*, (1+η)/2 gives 2Y_j = U_j + V_j. The x = 0 terms vanish under the zero extension.
   - Trivial character: J(1,η) = -1, and J(η,η) = -1 via u = x/(1-x), which maps F_q\{1} onto F_q\{-1}. Hence Y_0 = -1.
   - Orthogonality on H: Σ_j Y_j = m·g(1) = 0 and Σ_j Y_j² = m(m-1). This uses g(x⁻¹) = g(x), which holds because η(x) = 1 on H.
   - Arithmetic: 4m(m-1) - 4 = q² - 4q - 1.

3. Proposition 4.1 (main.tex:298-339) is correct.
   - Group facts: G has odd order v; x^q = x⁻¹ on G; α^(q-1) = ω^((q²-1)/2) = -1; Tr(αx) = α(x - x⁻¹), which vanishes only at x = 1.
   - L is inverse-closed and 1 ∉ L.
   - Eigenvalues for nontrivial ψ: T_ψ = 4ψ(L) + 2 and the eigenvalue is q+1-T_ψ.
   - Trivial character: T_1 = 4|L| - (q-1) and the eigenvalue is 2q - 4|L|. This agrees with MSX Prop 2.5, X = 2G + (2v-2)[0] - 4L, with 2v-2 = q-1.
   - Characters of G: gcd(v, 2(q-1)) = 1, so the restrictions of θ^h give all characters of G.
   - Bound: the constants in MSX Prop 3.5 cancel exactly in T_ψ, giving |T_ψ| ≤ (√q/q)(2q) = 2√q.
   - Moments: Σ T_ψ = 0 and Σ T_ψ² = 4v(v-1) = q² - 1.
   - |det M| = det C, because MM^T = diag(C, C) and C is positive definite.

4. Prefactors and E_56, E_4 (main.tex:235-258, 341-356) are correct.
   - Product structure: R_s = K_s/(2q(q-1)) · ((q+1)/(q-1))^((q-3)/2) · Π(1-t_j), because W = 2q(q-1)^m. Likewise C_4 = (q+1)/(2q) · ((q+1)/(q-1))^((q-1)/2), because v = m+1.
   - Class (5): log((q-1)/(2q)) ≥ -log 2 - 1/(q-1).
   - Class (6): K/(q(q-1)) > 1, so the same bound holds.
   - (q-3)/2 · log((q+1)/(q-1)) ≥ (q-3)/q.
   - log C_4 ≥ -log 2 + 1/q - 1/(2q²) + (q-1)/q = 1 - log 2 - 1/(2q²).
   - Combining with -S ≥ -2/(q+1), V < 1 and Lemma 2.1 gives E_56 and E_4 exactly as stated, for every admissible q ≥ 5.
   - Monotonicity: d/du [2u/(3(u-1)²)] = -2(u+1)/(3(u-1)³), so each term of E decreases in q.

5. Threshold arithmetic (main.tex:384-398), recomputed with exact Fraction arithmetic:
   - E_4(676) = 47527379/1713660000 < 1/35.
   - 31.5² = 992.25 < 1001, and 2(63/2)/(3(61/2)²) = 84/3721.
   - The E_56 upper sum is 53309553221/1866085221000 < 1/35.
   - 163/60 > 784/289, so √e > 28/17.
   - With e^(-x) ≥ 1-x, R > 17√e/35 > 4/5.

6. Section 4.1, primitive-element choice (main.tex:360-374), is correct.
   - Write ω' = ω^r with r odd. Then G is unchanged and α' = α·(ω^(q+1))^((r-1)/2).
   - ω^(q+1) generates F_q*, so the extra factor has η = (-1)^((r-1)/2).
   - So L is replaced by L or by G\(L∪{1}), which is f ↦ ±f, and |det M| = det C depends only on L.
   - ω⁻¹ gives (r-1)/2 = (q²-3)/2, which is odd because q² ≡ 1 (mod 8). So both signs occur.
   - class4_check.py also asserts at every q that α⁻¹ gives the complementary leave set.
   - The moments are invariant under f ↦ -f, so the analytic bound covers both signs.

7. MSX citations, checked against sources/original-accepted-manuscript.txt:
   - Theorem 1.6 (l.140-166): the Class (4) product runs over h = 0..(q-1)/2, so it includes the trivial character. The Class (5)/(6) products run over j = 1..(q-3)/2 with q+1 ± (J(ηχ^j,η) + J(χ^j,η)) and prefactors (q-1)² and q²+2q+5. Ratios 0.844, 0.846 and 0.823 at n = 30, and ≥ 0.8 for 38 ≤ n ≤ 1000, are reported at l.202-209, together with the √e/2 remark.
   - Prop 2.1 / Lemma 2.2 (l.218-245): a two-moment determinant bound, as the paper says.
   - Prop 2.5 (l.342-372): matrix (2.2) and the Gram element X = 2G + (2v-2)[0] - 4L. This matches eq. (gram4).
   - Props 2.6 and 2.8 (l.382-475): substituting Prop 4.2 reproduces (D5) and (D6) exactly.
     - Class (5): 2^(m+1)m² Π (m + 1 + X_j/2) = (q-1)² Π (q+1+X_j).
     - Class (6): 4(m² + 2m + 2) = q² + 2q + 5.
   - Theorem 3.4 (l.678-686): D_i uses ω^((q+1)i/2), so α = ω^v; the leave set is L = D_1.
   - Prop 3.5 (l.705-814): the statement matches main.tex:322-326.
   - Prop 4.2 (l.886-916): χ^j(D_{i,0}) = -1/2 + (-1)^i (U+V)/4. This agrees with the paper's own Y_j derivation.
   - MSX's convention χ(0) = 1 for the trivial character (l.583) is as main.tex:190 says, and does not affect the products.
   - Problem 7.1 (l.1264-1266) is quoted correctly.
   - EKLO Problem 15 in sources/prior-survey-v2.html matches the paper's wording. I did not confirm the §5.6 section number.

8. Resultants (Section 5.2):
   - Res(h, F) = Π F(z_a) for monic h is standard.
   - The roots of 1 + … + X^(m-1) are exactly the nontrivial characters of H evaluated at w².
   - The roots of X^v - 1 are all characters of G evaluated at γ.
   - F_s(ζ^j) = q+1 - 2sY_j = q+1 - sX_j, and F_{4,ε} = q+1 - εT_ψ.
   - Code checks in finite_check.py and class4_check.py:
     - Fields are certified by a full orbit of the primitive element.
     - ω is certified by order tests; Tr(a+bu) = 2a since u^q = -u; the F_{q²} multiplication is correct.
     - The sets follow Theorem 3.4 literally; the margin 5D - 4W is an integer.
   - Certificate data:
     - The source_sha256 values in both evidence certificates match the current scripts.
     - All 306 margins are positive.
     - There are 64 / 89 / 89 field orders. My own enumeration also gives 64 and 89.
     - At q = 29 the two Class (4) signs are 16601167080000/19668469112621 ≈ 0.84405 and 16067122183125/19668469112621 ≈ 0.81690.
   - Second program (read from evidence, not rerun): the dense matrices in finite_audit.py follow MSX (2.3)/(2.4) and the Theorem 4.1 sets entry by entry. finite-audit-results.json records 12 dense determinants as passed (q = 29, 49, 125, 625, 729, 997). The class4 examiner records full-block checks at 29, 49, 125, 625, 673.

9. Section 5.3 and scripts/infimum_check.py (new material):
   - (a) DFT factors.
     - Classes (5)-(6): the sequence is g_k = η(w^(2k)-1), with H = orbit[::2] in order w^(2k). The code skips j = 0 (trivial), uses factor q+1-2s·ĝ_j, K = (q-1)² for s = -1 (Class 5) and q²+2q+5 for s = +1 (Class 6), and the log W = log 2q + ((q-1)/2)·log(q-1) normalization. This matches (D5) and (D6).
     - Class (4): the code includes all v characters, uses K = 1, and evaluates both signs ±.
     - Arb's DFT uses e^(-2πijk/n), so ĝ_j = Y_{-j}. Because the sequence is symmetric and real, ĝ_j is real and even, so the indexing does not matter.
     - `(q-1)/2` multiplies an arb object, so no float enters.
   - (b) Rational tail argument.
     - s = isqrt(e_lo·10^60)/10^30, with s² ≤ e_lo < e, where e_lo = Σ_{k≤20} 1/k!.
     - tail_upper uses u = isqrt(q·10^24)/10^12 ≤ √q in the decreasing term, which gives an upper bound.
     - E(q) ≤ E(Q) ≤ E_upper(Q) for q ≥ Q, and e^(-x) ≥ 1-x. Strictness comes from the rational > comparison.
     - Recomputing with 200-bit Arb and the exact √e confirms that Q = 5720, 5039 and 10525 are the smallest passing integers. The margin is +5.9e-7, +7.3e-7, +1.8e-7 at Q and negative at Q-1.
   - (c) Rigor of the ball comparison.
     - Arb ball semantics are used throughout: the `arb >` comparison is true only for the whole ball, and the code asserts factor > 0 before taking logs.
     - Orders with exact certificates use the exact rational. Their balls are asserted to contain the exact log value (306 consistency checks passed), and the decision is r > μ, or r ≥ μ only at q = q_min.
   - (d) Coverage.
     - admissible(29, 10525) lists every prime power q ≡ 1 (mod 4) in the range. I enumerated independently and got 392, 352 and 666 orders, matching the paper.
     - The prime powers covered are 49, 81, 121, 125, 169, 289, 361, 529, 625, 729, 841, 961, 1369, 1681, 1849, 2197, 2209, 2401, 2809, 3125, 3481, 3721, 4489, 4913, 5041, 5329, 6241, 6561, 6889, 7921, 9409 and 10201.
     - The regenerated certificate's rows equal this list exactly, with exactly the required keys per q.
   - (e) Class (4) equality only at q = 29: for every q ≠ 29 below 5720, both signs are checked strictly. The non-minimizing sign at q = 29 is checked only as ≥ (see ERRATA), but its exact value 0.84405 is plainly larger.
   - Independent recomputation, with my own float64/numpy code and my own GF(p^d) arithmetic in scratch. It covers:
     - Classes (5)-(6): every admissible q < 10525.
     - Class (4): every prime q < 5720 and every prime power q < 1000.

     It reproduces every certificate ratio_display to within 5e-7 and gives the same minimizers. The runners-up are:
     - Class (4): 0.81715 at q = 41.
     - Class (5): 0.82142 at q = 101.
     - Class (6): 0.82044 at q = 53.

     So there are no near-ties. The same run confirmed max|T|/(2√q) ≤ 1, ΣT = 0 or 2s, and ΣT² as stated, for every field it computed. This is numerical corroboration of Props 3.1/4.1 and of the consequence of MSX Prop 3.5 that the paper uses.

10. Rerun of infimum_check.py (nice -n 19, 59.0 CPU-s): status INFIMUM CHECK PASSED, with 306 exact consistency checks. Compared field by field with the original evidence/infimum-certificate.json (backed up beforehand), the regenerated file differs only in cpu_seconds (59.1 → 59.0) and wall_seconds (59.2 → 59.0). source_sha256 is unchanged at f165d9d1…acc40b. I then restored the original bytes, so the file is back to SHA-256 4446d791…e1a8ab870eafc99 (sha256 4446d7916b2e6e55603776bd12946e53b88b720c5c7b19947d8f045865edf1a1).

11. Rerun of class4_check.py --finite (1.1 CPU-s): it passed with the same 64 fields and 128 determinants. It writes scripts/class4-certificate.json (not evidence/); the output differed from the prior file only in cpu_seconds, wall_seconds and the executable path string. I restored the original bytes (SHA-256 17e97f60…cefdb). scripts/class4-certificate.json and evidence/class4-certificate.json (and likewise the finite-certificate pair) differ only in timing and executable fields.

12. Equivalence with the earlier audited texts (DERIVATION.md, FINITE-PROOF.md, CLASS4-PROOF.md):
   - No step was lost or changed in meaning.
   - The manuscript drops the reconstructed M_s matrices and works directly from MSX's published products. FINITE-PROOF.md had already made this move, and the dense checks against the MSX matrices back it.
   - The constants, inequalities, thresholds, both-sign treatment and resultant setup are identical.
   - Class (4) follows CLASS4-PROOF.md line for line.

COVERAGE: All of main.tex was read: Sections 1-5, the Remarks and the bibliography. I checked every load-bearing step of Lemma 2.1, Props 3.1 and 4.1, (P56)/(E56), (P4)/(E4), Section 4.1, the thresholds and Sections 5.2-5.3. Scripts read in full: infimum_check.py, finite_check.py, class4_check.py and finite_audit.py. Of class4_examiner_proof.py I read only the parts that matter (grep plus the evidence JSON). I did not rerun finite_audit.py or class4_examiner_proof.py, as instructed, so their dense-matrix results are taken from evidence/*.json. I read MSX Prop 3.5's proof but did not independently re-derive its Gauss-sum evaluation (Theorems 2.12/2.13 of MSX).

DEPENDENCIES:
- MSX (LAA 654, 2022), peer-reviewed:
  - Theorem 1.6, Theorem 3.4 and Theorem 4.1 (constructions and types).
  - Props 2.5, 2.6 and 2.8 (determinant formulas).
  - Prop 4.2 (consistent with the paper's own derivation).
  - Prop 3.5: the only external input for |T_ψ| ≤ 2√q in Class (4). It is corroborated numerically for every prime q < 5720 and every prime power q < 1000.
- Standard Gauss/Jacobi sum facts: |G| = √q over F_q, |G| = q over F_{q²}, and the Gauss-Jacobi identity.
- FLINT (exact resultants and determinants) and Arb's acb_dft through python-flint 0.8.0 (rigorous ball enclosures). Both programs share this library.

ERRATA:
- documentation — paper/main.tex:491-492. "For the 306 orders with exact determinants" should say determinants or cases, not orders. 306 = 128 (64 Class (4) orders × 2 signs) + 89 + 89, which spans only 89 distinct orders.
- documentation — paper/main.tex:94-98. "It also answers Problem 7.1" is slightly stronger than what is shown. The paper settles the 0.8 question and gives the sharp constants c_i for n ≥ 30, plus the asymptotic constant. Problem 7.1's "sharp lower bounds" is open-ended: it is not restricted to n ≥ 30 or to constant multiples of Δ_n, and q = 13 already gives 841/1053 < 4/5. Suggested wording: "answers the 0.8 question of Problem 7.1 and gives its sharp constants for n ≥ 30". The mathematics as stated in the sentence that follows is correct.
- documentation — paper/main.tex:183. The citation for (D5)/(D6) should also name MSX Theorem 4.1, which defines the sets and their NH*1/NH*2 types; the MSX table cites "Thm. 4.1, Prop. 4.2".
- documentation — paper/main.tex:496-497. "computing the same determinants as exact integers would take several hours" is not backed by any recorded measurement in the repository. I did not verify it.
- documentation — scripts/infimum_check.py:150-153. At q = q_min the code accepts both Class (4) signs with r ≥ μ, so it does not itself assert that the non-minimizing sign at q = 29 is strictly larger. That sign's exact value is 0.84405 > μ_4 (evidence/class4-certificate.json), and the theorem's strictness claim concerns other q, so nothing in the theorem is affected.

No error, gap or missing hypothesis was found.

EXPOSURE:
- Read in full: paper/main.tex; the scripts listed under COVERAGE; MSX accepted-manuscript text (l.120-916 and 1250-1300); DERIVATION.md, FINITE-PROOF.md, CLASS4-PROOF.md, CLASS4-AUDIT-ERRATA.md and audit-proof.md in msx-determinant-2026-11-15/.
- Read only the Problem 15 passage of the survey HTML.
- Did not read audit/reports/claims-consistency.md or independent-rebuild.md.
- scripts/independent_rebuild.py appeared in scripts/ during this audit (written by another process, not me). I did not read it.

RESOURCES:
- Single process at a time, about 112 CPU-seconds in total:
  - infimum_check.py: 59.0 s.
  - My independent float check (~/.venvs/claude, numpy, ulimit -t 120): 51 s.
  - class4_check.py --finite: 1.1 s.
  - Exact-rational and Arb scalar checks: under 1 s.
- Scratch files are in <scratch>: the original-certificate backups, run logs, and indep/indep_ratios.py with its output indep.json.
- Repository writes: this report, plus two regenerated files (evidence/infimum-certificate.json and scripts/class4-certificate.json), both restored byte-for-byte to their original hashes.
