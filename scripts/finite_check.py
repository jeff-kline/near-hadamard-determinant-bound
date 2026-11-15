"""Exact bounded certificate for MSX Classes (5) and (6).

No floating point is used in a decision. Full primitive orbits certify fields.
Res(1+X+...+X^(m-1), q+1-2s sum f_k X^k) is the nonprincipal
Fourier product, f_k=eta(w^(2k)-1). See FINITE-PROOF.md.
"""
import hashlib
import json
import math
from pathlib import Path
import resource
import sys
import time
from fractions import Fraction

import flint
from flint import fmpz_poly

ROOT = Path(__file__).resolve().parent


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def parameters():
    out = []
    for p in range(2, 1001):
        if not isprime(p):
            continue
        q, degree = p, 1
        while q < 1001:
            if q >= 29 and q % 4 == 1:
                out.append((q, p, degree))
            q *= p
            degree += 1
    return sorted(out)


class Field:
    def __init__(self, p, degree, modulus=None, primitive=None):
        assert isprime(p)
        self.p, self.degree, self.q = p, degree, p**degree
        self.digits = [self.decode(x) for x in range(self.q)]
        if degree == 1:
            self.modulus = [0, 1]
            candidates = [primitive] if primitive is not None else range(2, p)
            for w in candidates:
                orbit = self.orbit(w)
                if len(orbit) == self.q - 1:
                    break
            else:
                raise AssertionError('no primitive element')
        else:
            candidates = [modulus] if modulus is not None else (
                self.decode(c) + [1] for c in range(1, self.q) if c % p)
            w = p if primitive is None else primitive  # polynomial X
            for poly in candidates:
                assert len(poly) == degree + 1 and poly[-1] == 1
                self.modulus = poly
                orbit = self.orbit(w)
                if len(orbit) == self.q - 1:
                    break
            else:
                raise AssertionError('no primitive polynomial')
        # Every nonzero residue is a power of w: all are units, so this
        # quotient of F_p[X] is a field; this also proves w is primitive.
        assert set(orbit) == set(range(1, self.q))
        assert self.mul(orbit[-1], w) == 1
        self.w, self.powers = w, orbit
        self.logs = {x: k for k, x in enumerate(orbit)}
        self.H = orbit[::2]

    def decode(self, x):
        ans = []
        for _ in range(self.degree):
            ans.append(x % self.p)
            x //= self.p
        return ans

    def mul(self, x, y):
        p, d = self.p, self.degree
        if d == 1:
            return x*y % p
        a, b = self.digits[x], self.digits[y]
        c = [0]*(2*d - 1)
        for i in range(d):
            for j in range(d):
                c[i+j] += a[i]*b[j]
        for k in range(2*d-2, d-1, -1):
            t = c[k] % p
            for j in range(d):
                c[k-d+j] -= t*self.modulus[j]
        return sum((c[i] % p)*p**i for i in range(d))

    def sub(self, x, y):
        return sum(((a-b) % self.p)*self.p**i
                   for i, (a, b) in enumerate(zip(self.digits[x], self.digits[y])))

    def orbit(self, w):
        out, seen, x = [], set(), 1
        while x and x not in seen:
            seen.add(x)
            out.append(x)
            x = self.mul(x, w)
        return out if x == 1 else []

    def eta(self, x):
        return 0 if x == 0 else 1 - 2*(self.logs[x] % 2)


def run():
    assert sys.prefix != sys.base_prefix
    resource.setrlimit(resource.RLIMIT_CPU, (300, 305))
    start, cpu = time.perf_counter(), time.process_time()
    params = parameters()
    print(f'PRECHECK: {len(params)} fields, {2*len(params)} determinants, '
          f'max n={max(q+1 for q,_,_ in params)}, max resultant degree=497', flush=True)
    rows = []
    for q, p, degree in params:
        F = Field(p, degree)
        m = (q-1)//2
        f = [F.eta(F.sub(x, 1)) for x in F.H]
        assert f[0] == 0 and sum(f) == -1
        assert sum(x*x for x in f) == m-1
        assert all(f[k] == f[-k % m] for k in range(m))
        h = fmpz_poly([1]*m)
        W = 2*q*(q-1)**m
        values = []
        for s in (-1, 1):
            coeff = [-2*s*x for x in f]
            coeff[0] += q+1
            product = int(h.resultant(fmpz_poly(coeff)))
            assert product > 0
            K = (q-1)**2 if s == -1 else q*q+2*q+5
            D = K*product
            margin = 5*D-4*W
            assert margin > 0, (q, s, margin)
            ratio = Fraction(D, W)
            values.append(dict(class_number=5 if s == -1 else 6,
                nonprincipal_product=str(product), determinant=str(D),
                margin_5D_minus_4W=str(margin),
                ratio_numerator=str(ratio.numerator), ratio_denominator=str(ratio.denominator)))
        rows.append(dict(q=q, p=p, degree=degree, modulus=F.modulus,
                         primitive=F.w, f=f, W=str(W), values=values))
        print(f'q={q} certified', flush=True)
    minima = []
    for cls in (5, 6):
        candidates = [(Fraction(int(v['ratio_numerator']), int(v['ratio_denominator'])), r['q'])
                      for r in rows for v in r['values'] if v['class_number'] == cls]
        ratio, q = min(candidates)
        minima.append(dict(class_number=cls, q=q, n=q+1, ratio_exact=str(ratio),
                           ratio_display=float(ratio)))
    result = dict(status='EXACT FINITE CHECK PASSED', range='29 <= q < 1001',
        field_count=len(rows), determinant_count=2*len(rows), minima=minima, rows=rows,
        cpu_seconds=time.process_time()-cpu, wall_seconds=time.perf_counter()-start,
        python=sys.version, executable=sys.executable, flint_version=flint.__version__,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/'finite-certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}, indent=2))


if __name__ == '__main__':
    run()
