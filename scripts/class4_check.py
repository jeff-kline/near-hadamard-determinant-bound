"""Class (4) exact source construction, sanity checks, and finite certificate."""
import argparse
import hashlib
import json
import resource
import sys
import time
from fractions import Fraction
from pathlib import Path
import flint
from flint import fmpz_poly, fmpz_mat
from finite_check import Field, parameters

ROOT=Path(__file__).resolve().parent


def prime_divisors(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:
                n//=d
        d+=1
    if n>1:
        out.append(n)
    return out


class Quadratic:
    """F_q[u]/(u^2-d), with d a certified primitive (hence nonsquare) element."""
    def __init__(self,F,omega=None):
        self.F=F
        self.d=F.w
        self.q=F.q
        self.N=F.q**2-1
        self.factors=prime_divisors(self.N)
        assert F.eta(self.d)==-1
        candidates=[tuple(omega)] if omega is not None else (
            (a,b) for b in range(1,self.q) for a in range(self.q))
        for z in candidates:
            if all(self.pow(z,self.N//r)!=(1,0) for r in self.factors):
                assert self.pow(z,self.N)==(1,0)
                self.omega=z
                break
        else:
            raise AssertionError('no primitive element')

    def add_base(self,a,b):
        return self.F.sub(a,self.F.sub(0,b))

    def mul(self,z,t):
        a,b=z; c,d=t; F=self.F
        return (self.add_base(F.mul(a,c),F.mul(self.d,F.mul(b,d))),
                self.add_base(F.mul(a,d),F.mul(b,c)))

    def pow(self,z,k):
        ans=(1,0)
        while k:
            if k&1:
                ans=self.mul(ans,z)
            z=self.mul(z,z)
            k//=2
        return ans

    def trace(self,z):
        return self.add_base(z[0],z[0])

    def data(self):
        v=(self.q+1)//2
        g=self.pow(self.omega,2*(self.q-1))
        alpha=self.pow(self.omega,v)
        H=[]; x=(1,0)
        for _ in range(v):
            H.append(x); x=self.mul(x,g)
        assert x==(1,0) and len(set(H))==v
        assert self.pow(alpha,self.q)==(self.F.sub(0,alpha[0]),self.F.sub(0,alpha[1]))
        D0=[int(self.F.eta(self.trace(x))==1) for x in H]
        L=[int(self.F.eta(self.trace(self.mul(alpha,x)))==1) for x in H]
        f=[2*t-1+int(k==0) for k,t in enumerate(L)]
        assert f[0]==0 and all(abs(x)==1 for x in f[1:])
        assert all(f[k]==f[-k%v] for k in range(v))
        # Verify the other primitive choice actually realizes the complementary leave set.
        alpha_inv=self.pow(alpha,self.N-1)
        Lother=[int(self.F.eta(self.trace(self.mul(alpha_inv,x)))==1) for x in H]
        assert Lother==[0]+[1-t for t in L[1:]]
        return D0,L,f


def source_matrix(D0,L):
    v=len(L)
    a=[2*x-1 for x in D0]; b=[2*x-1 for x in L]
    return ([[a[(j-i)%v] for j in range(v)]+[b[(j-i)%v] for j in range(v)] for i in range(v)]
          +[[b[(i-j)%v] for j in range(v)]+[-a[(i-j)%v] for j in range(v)] for i in range(v)])


def check(q,p,degree,dense=False):
    F=Field(p,degree); E=Quadratic(F)
    D0,L,f=E.data(); v=len(f)
    h=fmpz_poly([-1]+[0]*(v-1)+[1])
    W=2*q*(q-1)**(v-1)
    values=[]
    for sign in (1,-1):
        coeff=[-2*sign*x for x in f]; coeff[0]+=q+1
        determinant=int(h.resultant(fmpz_poly(coeff)))
        assert determinant>0
        ratio=Fraction(determinant,W)
        margin=5*determinant-4*W
        if q>=29:
            assert margin>0,(q,sign,ratio)
        if dense:
            leave=L if sign==1 else [0]+[1-x for x in L[1:]]
            M=source_matrix(D0,leave)
            assert len(M)==q+1
            direct=abs(int(fmpz_mat(M).det()))
            assert direct==determinant,(q,sign,direct,determinant)
            # Gram first-row identity, including the principal mode.
            a=M[0][:v]; b=M[0][v:]
            gram=[sum(a[k]*a[(k-r)%v]+b[k]*b[(k-r)%v] for k in range(v)) for r in range(v)]
            assert gram==coeff
        values.append(dict(orientation=sign,determinant=str(determinant),
                           margin_5D_minus_4W=str(margin),ratio_exact=str(ratio),
                           ratio_display=float(ratio),dense_checked=dense))
    return dict(q=q,p=p,degree=degree,modulus=F.modulus,base_primitive=F.w,
                quadratic_nonsquare=E.d,omega=list(E.omega),order_factors=E.factors,
                D0=D0,L=L,f=f,W=str(W),values=values)


def run(finite=False):
    assert sys.prefix!=sys.base_prefix
    resource.setrlimit(resource.RLIMIT_CPU,(180,185))
    cpu=time.process_time(); wall=time.perf_counter()
    params=[x for x in parameters() if x[0]<676] if finite else [(5,5,1),(9,3,2),(13,13,1),(17,17,1),(25,5,2),(29,29,1)]
    print(f'PRECHECK fields={len(params)}, products={2*len(params)}, max matrix order={max(q+1 for q,_,_ in params)}; no enumeration of all F_(q^2) elements',flush=True)
    rows=[]
    for q,p,d in params:
        row=check(q,p,d,dense=not finite)
        rows.append(row)
        print(q,[(v['orientation'],v['ratio_display']) for v in row['values']],flush=True)
    endpoint=Fraction(1,2*676**2)+Fraction(52,1875)
    assert endpoint<Fraction(1,35)
    minima=[]
    for sign in (1,-1):
        rat,q=min((Fraction(v['ratio_exact']),r['q']) for r in rows for v in r['values'] if v['orientation']==sign)
        minima.append(dict(orientation=sign,q=q,ratio_exact=str(rat),ratio_display=float(rat)))
    result=dict(status='EXACT FINITE CHECK PASSED' if finite else 'SOURCE SANITY CHECKS PASSED',
        range='29 <= q < 676' if finite else '5,9,13,17,25,29',field_count=len(rows),
        determinant_count=2*len(rows),minima=minima,rows=rows,
        threshold=676,tail_error_endpoint=str(endpoint),
        gap_below_one_over_35=str(Fraction(1,35)-endpoint),
        cpu_seconds=time.process_time()-cpu,wall_seconds=time.perf_counter()-wall,
        python=sys.version,executable=sys.executable,flint_version=flint.__version__,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        field_dependency_sha256=hashlib.sha256((ROOT/'finite_check.py').read_bytes()).hexdigest())
    name='class4-certificate.json' if finite else 'class4-sanity.json'
    (ROOT/name).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--finite',action='store_true')
    run(parser.parse_args().finite)
