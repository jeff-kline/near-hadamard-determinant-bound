"""Exact infimum of |det M_{q+1}| / W_{q+1} over q >= 29, for Classes (4)-(6).

For each class c the paper proves R_c(q) >= (sqrt(e)/2) exp(-E_c(q)), with
E_c decreasing in q. Let m_c be the smallest ratio in the exact certificates.
This script finds, in exact rational arithmetic, a cutoff Q_c with
(sqrt(e)/2)(1 - E_c(Q_c)) > m_c, so R_c(q) > m_c for every q >= Q_c. For each
admissible q with 29 <= q < Q_c it then proves R_c(q) >= m_c, with equality
only at the known minimizer, using rigorous ball arithmetic (Arb, via
python-flint): the determinant is a product over the nontrivial characters
(Classes 5-6) or all characters (Class 4) of q+1-2s*ghat_j, where ghat is the
discrete Fourier transform of the +-1 sequence, computed by acb.dft with
guaranteed error bounds. This costs O(q log q) per field instead of an exact
resultant. Orders below 1001 (Classes 5-6) and 676 (Class 4) are also
compared with the exact certificates as a consistency check.

Usage: .venv/bin/python scripts/infimum_check.py
"""
import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import flint
from flint import arb, acb

from finite_check import Field, isprime
from class4_check import Quadratic

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / 'infimum-certificate.json'   # pinned copy: evidence/
PREC = 128

# The smallest ratios in the exact certificates (evidence/*-certificate.json).
START = {
    '4': (29, Fraction(16067122183125, 19668469112621)),
    '5': (37, Fraction(690199704608000, 846441320833557)),
    '6': (49, Fraction(13602934789834170625, 16620815899787526144)),
}


def sqrt_e_lower():
    """A rational s with s < sqrt(e): e > sum_{k<=20} 1/k! >= s^2."""
    e_lo = sum(Fraction(1, math.factorial(k)) for k in range(21))
    scale = 10**30
    s = Fraction(math.isqrt(e_lo.numerator * scale**2 // e_lo.denominator), scale)
    assert s * s <= e_lo
    return s


def tail_upper(q):
    """Upper bound for 2 sqrt(q)/(3 (sqrt(q)-1)^2), decreasing in sqrt(q)."""
    scale = 10**12
    u = Fraction(math.isqrt(q * scale**2), scale)
    assert u * u <= q and u > 1
    return 2 * u / (3 * (u - 1)**2)


def E_upper(cls, q):
    if cls == '4':
        return Fraction(1, 2 * q * q) + tail_upper(q)
    return Fraction(1, q - 1) + Fraction(3, q) + Fraction(2, q + 1) + tail_upper(q)


def cutoff(cls, m, s):
    q = 29
    while not (s / 2 * (1 - E_upper(cls, q)) > m):
        q += 1
    return q


def admissible(lo, hi):
    out = []
    for q in range(lo, hi):
        if q % 4 != 1:
            continue
        p = next(d for d in range(2, q + 1) if q % d == 0)
        d, x = 0, q
        while x % p == 0:
            x //= p
            d += 1
        if x == 1 and isprime(p):
            out.append((q, p, d))
    return out


def log_ratio(seq, q, s, skip_zero, K):
    """Ball for log(K * prod_j (q+1 - 2 s ghat_j) / W), W = 2q(q-1)^((q-1)/2)."""
    ghat = acb.dft([acb(x) for x in seq])
    total = arb(K).log() - arb(2 * q).log() - arb(q - 1).log() * (q - 1) / 2
    for j, z in enumerate(ghat):
        if skip_zero and j == 0:
            continue
        assert z.imag.contains(0)           # symmetric sequence: real factors
        factor = (q + 1) - 2 * s * z.real
        assert factor > 0
        total += factor.log()
    return total


def ratios(q, p, d, classes):
    F = Field(p, d)
    out = {}
    if '5' in classes or '6' in classes:
        m = (q - 1) // 2
        g = [F.eta(F.sub(x, 1)) for x in F.H]
        assert g[0] == 0 and all(g[k] == g[-k % m] for k in range(m))
        for s, c, K in ((-1, '5', (q - 1)**2), (1, '6', q * q + 2 * q + 5)):
            if c in classes:
                out[c] = log_ratio(g, q, s, True, K)
    if '4' in classes:
        _, _, f = Quadratic(F).data()
        assert f[0] == 0 and all(f[k] == f[-k % len(f)] for k in range(len(f)))
        out['4+'] = log_ratio(f, q, 1, False, 1)
        out['4-'] = log_ratio(f, q, -1, False, 1)
    return out


def exact_table():
    """Exact ratios from the pinned certificates, keyed by (class, q)."""
    tab = {}
    cert = json.loads((ROOT / 'evidence' / 'finite-certificate.json').read_text())
    for r in cert['rows']:
        for v in r['values']:
            tab[(str(v['class_number']), r['q'])] = Fraction(
                int(v['ratio_numerator']), int(v['ratio_denominator']))
    cert4 = json.loads((ROOT / 'evidence' / 'class4-certificate.json').read_text())
    for r in cert4['rows']:
        for v in r['values']:
            key = '4+' if v['orientation'] == 1 else '4-'
            tab[(key, r['q'])] = Fraction(v['ratio_exact'])
    return tab


def main():
    assert sys.prefix != sys.base_prefix, 'run inside the project venv'
    flint.ctx.prec = PREC
    t0, c0 = time.perf_counter(), time.process_time()
    s = sqrt_e_lower()
    cut = {c: cutoff(c, START[c][1], s) for c in START}
    print(f'cutoffs {cut}', flush=True)
    exact = exact_table()
    rows, consistency = [], 0
    minimizers = {c: [] for c in START}
    for q, p, d in admissible(29, max(cut.values())):
        need = [c for c in START if q < cut[c]]
        balls = ratios(q, p, d, need)
        row = dict(q=q, values={})
        for key, ball in balls.items():
            c = key[0]
            qmin, m = START[c]
            logm = arb(m.numerator).log() - arb(m.denominator).log()
            if (key, q) in exact:
                r = exact[(key, q)]
                assert ball.contains(arb(r.numerator).log() - arb(r.denominator).log()), (key, q)
                consistency += 1
                ok = r > m or (q == qmin and r == m)
                if r == m:
                    minimizers[c].append((key, q))
            else:
                ok = bool(ball > logm)          # rigorous: whole ball above log m
            assert ok, (key, q, ball, m)
            row['values'][key] = dict(log_ratio_lower=float(ball.lower()),
                                      ratio_display=round(math.exp(float(ball.mid())), 6))
        rows.append(row)
    for c in START:
        assert len(minimizers[c]) == 1 and minimizers[c][0][1] == START[c][0], minimizers[c]
    result = dict(status='INFIMUM CHECK PASSED', precision_bits=PREC,
                  sqrt_e_lower=f'{s.numerator}/{s.denominator}',
                  exact_consistency_checks=consistency, classes={})
    for c in sorted(START):
        qmin, m = START[c]
        result['classes'][c] = dict(
            infimum_exact=f'{m.numerator}/{m.denominator}', infimum_display=float(m),
            attained_at_q=qmin, cutoff_Q=cut[c],
            orders_checked=len([r for r in rows if any(k[0] == c for k in r['values'])]),
            E_upper_at_Q=str(E_upper(c, cut[c])),
            tail_bound_at_Q=float(s / 2 * (1 - E_upper(c, cut[c]))))
    result.update(rows=rows, cpu_seconds=round(time.process_time() - c0, 1),
                  wall_seconds=round(time.perf_counter() - t0, 1),
                  python=sys.version, flint_version=flint.__version__,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    OUT.write_text(json.dumps(result, indent=1) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=1))


if __name__ == '__main__':
    main()
