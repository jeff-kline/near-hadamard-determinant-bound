"""Independent rebuild of MSX Classes (4)-(6) from the source definitions.

Written separately from the other scripts: own finite-field arithmetic, no
FLINT, matrices assembled as in MSX (2.2)-(2.4), Theorems 3.4 and 4.1, and
exact determinants by fraction-free Bareiss elimination. Checks the Gram
structure and prints |det M| / W_n for every primitive element.

Usage: python independent_rebuild.py {4|56} q p e   (q = p^e)
"""
import sys, time, itertools, random
from fractions import Fraction
from math import gcd

def factor(n):
    f=set(); d=2
    while d*d<=n:
        while n%d==0: f.add(d); n//=d
        d+=1
    if n>1: f.add(n)
    return f

class Field:
    """F_{p^k} = F_p[x]/(f), elements are tuples of length k (low degree first). f monic, chosen so x is primitive."""
    def __init__(s,p,k):
        s.p,s.k,s.size=p,k,p**k
        s.one=(1,)+(0,)*(k-1); s.zero=(0,)*k
        N=s.size-1; s.N=N; pf=factor(N)
        rng=random.Random(12345)
        cands = ([ (-r)%p for r in range(1,p)] if k==1 else None)
        while True:
            if k==1:
                if not cands: raise SystemExit
                c=cands.pop(0); s.f=(c,)   # x + c  => x = -c
            else:
                s.f=tuple(rng.randrange(p) for _ in range(k))  # x^k = -sum f_i x^i
            x=(0,1)+(0,)*(k-2) if k>1 else ((-s.f[0])%p,)
            s.x=x
            if all(s.pow(x,N//r)!=s.one for r in pf) and s.pow(x,N)==s.one:
                break
    def add(s,a,b): return tuple((u+v)%s.p for u,v in zip(a,b))
    def mul(s,a,b):
        k,p=s.k,s.p
        if k==1: return ((a[0]*b[0])%p,)
        prod=[0]*(2*k-1)
        for i,u in enumerate(a):
            if u:
                for j,v in enumerate(b): prod[i+j]+=u*v
        for d in range(2*k-2,k-1,-1):
            c=prod[d]%p
            if c:
                for i in range(k): prod[d-k+i]-=c*s.f[i]
            prod[d]=0
        return tuple(c%p for c in prod[:k])
    def pow(s,a,e):
        r=s.one
        while e:
            if e&1: r=s.mul(r,a)
            a=s.mul(a,a); e>>=1
        return r
    def inv(s,a): return s.pow(a,s.N-1)
    def neg(s,a): return tuple((-u)%s.p for u in a)
    def sub(s,a,b): return s.add(a,s.neg(b))
    def emb(s,n): return ((n%s.p,)+(0,)*(s.k-1))

def bareiss(M):
    n=len(M); A=[r[:] for r in M]; sign=1; prev=1
    for i in range(n-1):
        if A[i][i]==0:
            for r in range(i+1,n):
                if A[r][i]!=0:
                    A[i],A[r]=A[r],A[i]; sign=-sign; break
            else: return 0
        for r in range(i+1,n):
            for c in range(i+1,n):
                A[r][c]=(A[r][c]*A[i][i]-A[r][i]*A[i][c])//prev
        prev=A[i][i]
    return sign*A[n-1][n-1]

def type1(v,S):
    S=set(S); return [[1 if ((b-a)%v) in S else -1 for b in range(v)] for a in range(v)]
def T(M): return [list(r) for r in zip(*M)]
def neg(M): return [[-u for u in r] for r in M]

def assemble_NH(A,B,v):
    At,Bt=type1(v,A),type1(v,B)
    top=[At[i]+Bt[i] for i in range(v)]
    bt=T(Bt); att=neg(T(At))
    bot=[bt[i]+att[i] for i in range(v)]
    return top+bot
def assemble_NH1(A,B,v):   # (2.3)
    At,Bt=type1(v,A),type1(v,B); BtT=T(Bt); AtT=T(At)
    one=[1]*v
    M=[[1]+one+[1]+one]
    for i in range(v): M.append([1]+At[i]+[1]+Bt[i])
    M.append([1]+one+[-1]+[-1]*v)
    for i in range(v): M.append([1]+BtT[i]+[-1]+[-u for u in AtT[i]])
    return M
def assemble_NH2(A,B,v):   # (2.4)
    At,Bt=type1(v,A),type1(v,B); BtT=T(Bt); AtT=T(At)
    one=[1]*v
    M=[[1]+one+[-1]+[-1]*v]
    for i in range(v): M.append([1]+At[i]+[1]+Bt[i])
    M.append([1]+one+[1]+one)
    for i in range(v): M.append([-1]+[-u for u in BtT[i]]+[1]+AtT[i])
    return M

def gram(M):
    n=len(M); return [[sum(a*b for a,b in zip(M[i],M[j])) for j in range(n)] for i in range(n)]

def check_gram(M,half,kind):
    n=len(M)
    assert all(abs(u)==1 for r in M for u in r)
    G=gram(M)
    ok=True; bad=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                if G[i][j]!=n: ok=False; bad.append(('diag',i,G[i][j]))
            elif (i<half)!=(j<half):
                if G[i][j]!=0: ok=False; bad.append(('cross',i,j,G[i][j]))
            else:
                if abs(G[i][j]) not in (0,2) and True: ok=False; bad.append(('off',i,j,G[i][j]))
    # count entries: within-block offdiag must be +-2 for NH (all), for NH* border entries (row0 vs others) are 0 or 2 per source Gram
    nz = sum(1 for i in range(n) for j in range(n) if i!=j and G[i][j]==0)
    return ok, nz, bad[:3]

def Wn(n): return (2*n-2)*(n-2)**((n-2)//2)

def ratio(M):
    n=len(M); d=abs(bareiss(M)); R=Fraction(d,Wn(n)); return d,R

def sets_diffcheck(v,A,B,k_target=None):
    # returns dict of coefficients of A A^-1 + B B^-1 over G=Z_v
    c=[0]*v
    for S in (A,B):
        for x in S:
            for y in S: c[(x-y)%v]+=1
    return c

out=[]
def log(*a):
    s=' '.join(str(x) for x in a); print(s); sys.stdout.flush()

def class4(q,p,e):
    F=Field(p,2*e)  # F_{q^2}
    N=F.N; w0=F.x
    v=(q+1)//2
    # F_q subfield elements
    # squares in F_q: t^((q-1)/2)==1
    g0=F.pow(w0,2*(q-1))
    Gel=[F.one];
    for a in range(1,v): Gel.append(F.mul(Gel[-1],g0))
    assert F.mul(Gel[-1],g0)==F.one and len(set(Gel))==v
    def tr(z): return F.add(z,F.pow(z,q))
    def sq(t): return F.pow(t,(q-1)//2)==F.one
    results={}
    seen={}
    js=[j for j in range(1,N) if gcd(j,N)==1]
    for j in js:
        tau=F.pow(w0,j*((q+1)//2))
        D0=[a for a,x in enumerate(Gel) if sq(tr(x))]   # i=0 independent of omega
        D1=[a for a,x in enumerate(Gel) if sq(tr(F.mul(x,tau)))]
        key=(tuple(D0),tuple(D1))
        if key not in seen: seen[key]=[]
        seen[key].append(j)
    return F,v,seen,js

def run4(q,p,e):
    t=time.process_time()
    F,v,seen,js=class4(q,p,e)
    rows=[]
    for (D0,D1),jl in seen.items():
        # almost supp. diff set check: coefficient pattern with leave set L=D1
        c=sets_diffcheck(v,D0,D1)
        L=set(D1); k=len(D0)+len(D1)
        lam=None
        vals_L={c[x] for x in range(1,v) if x in L}; vals_o={c[x] for x in range(1,v) if x not in L}
        M=assemble_NH(D0,D1,v)
        ok,nz,bad=check_gram(M,v,'NH')
        # NH: all in-block offdiag must be +-2 (or 2 and -2); check none zero
        d,R=ratio(M)
        rows.append((jl,len(D0),len(D1),sorted(vals_L),sorted(vals_o),c[0],ok,nz,d,R))
    log(f"Class4 q={q} order n={q+1} v={v}: {len(js)} primitive omega=w0^j; {len(seen)} distinct (D0,D1)")
    for jl,k0,k1,vl,vo,c0,ok,nz,d,R in rows:
        log(f"  j in {jl[:3]}..(count {len(jl)}, j=1:{1 in jl}, j=-1:{(F.N-1) in jl}) |D0|={k0} |D1|={k1} coef(L)={vl} coef(nonL)={vo} c0={c0} gram_ok={ok} zero_offdiag={nz} |det|={d} R={R} = {float(R):.6f}")
    log(f"  cpu {time.process_time()-t:.1f}s")
    return rows

def run56(q,p,e):
    t=time.process_time()
    F=Field(p,e); N=F.N; v=(q-1)//2
    w0=F.x
    g0=F.mul(w0,w0)
    Gel=[F.one]
    for a in range(1,v): Gel.append(F.mul(Gel[-1],g0))
    idx={x:a for a,x in enumerate(Gel)}
    def issq(t): return t!=F.zero and F.pow(t,(q-1)//2)==F.one
    def isns(t): return t!=F.zero and F.pow(t,(q-1)//2)!=F.one
    one=F.one
    js=[j for j in range(1,N) if gcd(j,N)==1]
    seen={}
    for j in js:
        w=F.pow(w0,j)
        D={}
        for i,test in ((0,issq),(1,isns)):
            # D_{i,0} = (C_i+1)∩C0 : x in C0 with x-1 in C_i
            D[(i,0)]=sorted(a for a,x in enumerate(Gel) if test(F.sub(x,one)))
            winv=F.inv(w)
            D[(i,1)]=sorted(a for a,x in enumerate(Gel) if test(F.sub(F.mul(x,winv),one)))
        key=tuple(tuple(D[k]) for k in sorted(D))
        seen.setdefault(key,[]).append(j)
    rows=[]
    log(f"Classes5/6 q={q} order n={q+1} v={v}: {len(js)} primitive omega; {len(seen)} distinct set-quadruples")
    for key,jl in seen.items():
        D={k:list(key[n]) for n,k in enumerate(sorted([(0,0),(0,1),(1,0),(1,1)]))}
        sizes={k:len(s) for k,s in D.items()}
        for cls,(A,B),asm,half in ((5,(D[(1,0)],D[(1,1)]),assemble_NH1,v+1),(6,(D[(0,0)],D[(0,1)]),assemble_NH2,v+1)):
            c=sets_diffcheck(v,A,B)
            L=set(A)
            vl={c[x] for x in range(1,v) if x in L}; vo={c[x] for x in range(1,v) if x not in L}
            M=asm(A,B,v)
            ok,nz,bad=check_gram(M,half,cls)
            d,R=ratio(M)
            rows.append((cls,jl,len(A),len(B),sorted(vl),sorted(vo),c[0],ok,nz,d,R))
            log(f"  Class {cls}: j-count {len(jl)} (j=1:{1 in jl}, j=-1:{(N-1) in jl}, first {jl[:3]}) |A|={len(A)} |B|={len(B)} coef(L)={sorted(vl)} coef(nonL)={sorted(vo)} c0={c[0]} gram_ok={ok} zero_offdiag={nz} |det|={d} R={R} = {float(R):.6f}")
    log(f"  cpu {time.process_time()-t:.1f}s")
    return rows

if __name__=="__main__":
    which=sys.argv[1]; q,p,e=map(int,sys.argv[2:5])
    if which=='4': run4(q,p,e)
    else: run56(q,p,e)
