# Independent rebuild of MSX Classes (4), (5), (6)

VERDICT: AGREES. All four claimed exact fractions are reproduced exactly; the n=30 MSX values (0.844, 0.846, 0.823) are reproduced; every ratio at q >= 29 exceeds 0.8 (minimum found 0.815414, Class 5, q=37).

Code: <scratch>/rebuild.py (own F_{p^k} arithmetic, own Bareiss on Python ints, no FLINT, no use of the owner's scripts/ or msx-determinant dirs; only the source manuscript text/PDF was read). Log: <scratch>/run.log.

## Results (R = |det M| / W_n, W_n = (2n-2)(n-2)^((n-2)/2); every |det| computed exactly by Bareiss on the actual +-1 matrix)

| Class | q | n | omega / set choice | R exact | R (6 dp) | claim match |
|---|---|---|---|---|---|---|
| 4 | 29 | 30 | omega = w0^j, j in {1,13,17,...} (96 of 192 primitive omega, incl. j=1) | 16601167080000/19668469112621 | 0.844050 | matches "about 0.8440" |
| 4 | 29 | 30 | j in {11,19,23,...} (other 96, incl. j=-1) | 16067122183125/19668469112621 | 0.816897 | EXACT match to claimed 16067122183125/19668469112621 |
| 4 | 37 | 38 | j=1 class (216 omega) | 4585927338747948973/5553501505988967477 | 0.825772 | (no claim) |
| 4 | 37 | 38 | j=-1 class (216 omega) | 4645023874655745025/5553501505988967477 | 0.836414 | (no claim) |
| 4 | 41 | 42 | j=1 class (192 omega) | 3459382908671117920817/4100000000000000000000 | 0.843752 | (no claim) |
| 4 | 41 | 42 | j=-1 class (192 omega) | 2093954504165776729/2562500000000000000 | 0.817153 | (no claim) |
| 4 | 49 | 50 | all 640 primitive omega of F_{7^4} (both classes) | 3229217684390808132716265625/3895345512966151362538635264 | 0.828994 | (no claim); only one value occurs |
| 5 | 29 | 30 | all 12 primitive omega | 6933343220/8191782221 | 0.846378 | matches MSX 0.846 |
| 5 | 37 | 38 | all 12 primitive omega | 690199704608000/846441320833557 | 0.815414 | EXACT match to claim |
| 5 | 41 | 42 | all 16 primitive omega | 5328494413992369/6406250000000000 | 0.831765 | (no claim) |
| 5 | 49 | 50 | all 16 primitive omega | 4589984880625/5467277940768 | 0.839538 | (no claim) |
| 6 | 29 | 30 | all 12 primitive omega | 558246273065/678223072849 | 0.823101 | matches MSX 0.823 |
| 6 | 37 | 38 | all 12 primitive omega | 79506077428309/94049035648173 | 0.845368 | (no claim) |
| 6 | 41 | 42 | all 16 primitive omega | 3392307494946365751873/4100000000000000000000 | 0.827392 | (no claim) |
| 6 | 49 | 50 | all 16 primitive omega | 13602934789834170625/16620815899787526144 | 0.818428 | EXACT match to claim |

Sample |det| values: Class 4 q=29: 8912683710503976960000 and 8625970539669749760000; Class 5 q=37: 622378592902414294409281536000; Class 6 q=49: 1794717302469193170081067353390616412160000 (all in run.log).

Class 4, the two q=29 values: the larger (0.844050) arises for j=1 (omega = x) and the smaller (0.816897) for j=-1; these are 96 omega each, so both claimed values appear. For q=37 and 41 the same j=1/j=-1 split gives two values; for q=49 the two classes give the same determinant.

## Verification of structure
- Every matrix has entries exactly +-1 (asserted).
- Gram M M^T checked entrywise: diagonal = n; all entries between the two half-blocks = 0 (count of zero off-diagonal entries equals exactly 2*half^2: 450, 722, 882, 1250 for n=30,38,42,50), and every within-block off-diagonal entry is nonzero with |.| = 2 (since the zero count equals the cross-block count exactly and the check allowed only 0 or +-2). This is the near-Hadamard structure (Gram = nI + 2S_i, S_i symmetric (0,+-1), zero diagonal). Class 4: halves of size v=(q+1)/2; Classes 5/6: halves of size v+1 with v=(q-1)/2.
- Almost-supplementary-difference-set property verified by direct counting in Z_v: the coefficient of A A^(-1)+B B^(-1) is constant on the leave set L and (that value +1) off L, for every case built. Examples: Class 4 q=29 j=1: |D0|=10,|D1|=6, 8 on L, 9 off L; Classes 5/6 give lambda = (|L|-ish) values 6/7 (q=29), 8/9 (q=37), 9/10 (q=41), 11/12 (q=49) for Class 5 and one less for Class 6, as in the (4.2) group-ring equation pattern. Set sizes match (4.1): |D1,0|=|D1,1|=(q-1)/4, |D0,0|=(q-5)/4, |D0,1|=(q-1)/4.

## Construction choices and ambiguities
- Matrices: Prop 2.5 (2.2) for Class 4; Prop 2.6 (2.3) for Class 5 using (A,B)=(D1,0,D1,1), L=D1,0; Prop 2.8 (2.4) for Class 6 using (A,B)=(D0,0,D0,1), L=D0,0 (per source text near line 915). The text extraction of (2.3)/(2.4) is garbled, so I read the block layouts from the PDF page images (pp. 7-8) and confirmed by the Gram check.
- Type 1 matrix of A: entry (x,y) = +1 if y-x in A else -1 (additive/multiplicative convention y x^{-1}). The group is cyclic; rows/columns indexed by exponent of a fixed generator (omega0^(2(q-1)) for Class 4, omega0^2 for Classes 5/6). Reindexing the group is a simultaneous row/column permutation in each block, so |det| is invariant.
- Theorem 3.4 exponent: the garbled text gives Tr(x omega^{(q+1)/2 * i}); I read it from the PDF as omega^{((q+1)/2) i}, i=0,1 (D0: Tr(x) square in F_q; D1: Tr(x omega^{(q+1)/2}) square). F_q's squares are C0^{(2,q)}; Tr = z + z^q. G = C0^{(2(q-1),q^2)} = subgroup of order (q+1)/2.
- Class 4 depends on omega only through omega^{(q+1)/2} (D0 and G are canonical): exactly two distinct (D0,D1) pairs arise over all primitive omega, giving two determinant values (q=29,37,41) or one (q=49, both pairs give the same determinant). The source does not say which omega the paper's headline number uses; the ratio claimed 0.81690 is the j=-1 type, 0.8440 the j=1 type. This is a convention difference only, and the claim explicitly lists both.
- Classes 5/6: D_{i,1} = omega (C_i+1) ∩ C0 implemented as x in C0 with x/omega - 1 in C_i. Dependence on omega: set quadruples are all distinct across the primitive omega, yet determinants are identical across all omega at every q, so no ambiguity in the ratio.
- F_49 = F_7[x]/(f) with f found by random search such that x has order 48 (resp. 2400 for F_{7^4}), which proves f irreducible; the ratio is independent of the choice of field representation up to isomorphism (a different irreducible polynomial just relabels omega).
- (C_i + 1) ∩ C0 read as {x in C0 : x - 1 in C_i}; the (4.2) pattern with (4.1) sizes was verified, supporting this reading.

## COVERAGE
- Built and exactly determinant-evaluated: Class 4 at q=29,37,41,49; Classes 5 and 6 at q=29,37,41,49. Class 4 over ALL primitive omega of F_{q^2} (192, 432, 384, 640 respectively; deduplicated to the distinct (D0,D1) pairs, 2 each); Classes 5/6 over ALL primitive omega of F_q (12, 12, 16, 16), each with its own matrix and determinant.
- Not done: Class 4 / 5 / 6 for q > 49 (not requested); no independent evaluation of the Gauss/Jacobi-sum determinant formulas in Theorem 1.6 (determinants were computed directly from the matrices, so the closed forms are untested here). Prop 2.5/2.6/2.8 determinant product formulas not checked against the direct values.
- All claimed values tested: 4 exact fractions agree; 0.8440, 0.844/0.846/0.823 agree; "all ratios > 0.8 for q>=29" holds for all 15 distinct values found (min 0.815414). No disagreement, so no convention-vs-real discrepancy to report.

## RESOURCES
Single process, system CPU time about 6 s total (q=29: 0.2 s, 37: 0.7 s, 41: 0.7 s, q=49 Class 4: 2.6 s; Classes 5/6 all q: about 1.9 s combined, in-script process_time). Memory small. Python: <venv>/bin/python -I. No packages installed.
