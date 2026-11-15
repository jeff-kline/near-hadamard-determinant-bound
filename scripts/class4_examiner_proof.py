"""Independent source/certificate checker; does not import project implementations."""
import copy, hashlib, json, math, resource, sys, time
from pathlib import Path
from fractions import Fraction
from flint import nmod_poly, fmpz_poly, fmpz_mat

assert sys.prefix != sys.base_prefix
resource.setrlimit(resource.RLIMIT_CPU,(180,185))
cpu=time.process_time();wall=time.perf_counter();root=Path(__file__).resolve().parent

def factor(n):
    ans={};r=2
    while r*r<=n:
        while n%r==0:ans[r]=ans.get(r,0)+1;n//=r
        r+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans

def power(x,n,mul,one):
    out=one
    while n:
        if n&1:out=mul(out,x)
        x=mul(x,x);n>>=1
    return out

class Arithmetic:
    def __init__(self,row):
        self.q=row['q'];self.p=row['p'];self.d=row['degree'];p=self.p;d=self.d
        assert factor(self.q)=={p:d}
        self.digits=[[(x//p**i)%p for i in range(d)] for x in range(self.q)]
        self.polys=[nmod_poly(x,p) for x in self.digits]
        self.mod=nmod_poly(row['modulus'],p)
        assert self.mod.degree()==d and int(self.mod[d])==1
        w=row['base_primitive']; orbit=[];x=1
        for _ in range(self.q-1):orbit.append(x);x=self.mul(x,w)
        assert x==1 and set(orbit)==set(range(1,self.q))
        self.squares={self.mul(x,x) for x in range(1,self.q)}
        assert len(self.squares)==(self.q-1)//2
        self.ns=row['quadratic_nonsquare'];assert self.ns not in self.squares and self.ns!=0
    def encode(self,co):return sum((int(c)%self.p)*self.p**i for i,c in enumerate(co))
    def mul(self,x,y):
        if self.d==1:return x*y%self.p
        z=(self.polys[x]*self.polys[y])%self.mod
        return self.encode([z[i] for i in range(self.d)])
    def add(self,x,y):return self.encode(a+b for a,b in zip(self.digits[x],self.digits[y]))
    def emul(self,x,y):
        a,b=x;c,d=y
        return (self.add(self.mul(a,c),self.mul(self.ns,self.mul(b,d))),self.add(self.mul(a,d),self.mul(b,c)))
    def epow(self,x,n):return power(x,n,self.emul,(1,0))
    def tr(self,x):
        y=self.epow(x,self.q)
        out=(self.add(x[0],y[0]),self.add(x[1],y[1]))
        assert out[1]==0
        return out[0]

def verify_values(row,computed):
    q=row['q'];W=2*q*(q-1)**((q-1)//2)
    assert int(row['W'])==W
    assert len(row['values'])==2 and {v['orientation'] for v in row['values']}=={-1,1}
    for value in row['values']:
        D=computed[value['orientation']]
        assert D>0 and int(value['determinant'])==D
        assert Fraction(value['ratio_exact'])==Fraction(D,W)
        assert int(value['margin_5D_minus_4W'])==5*D-4*W
        assert value['ratio_display']==float(Fraction(D,W))
        if q>=29:assert 5*D>4*W

def check(row,full=False):
    q=row['q'];v=(q+1)//2;E=Arithmetic(row);omega=tuple(row['omega']);N=q*q-1
    assert row['order_factors']==list(factor(N))
    assert E.epow(omega,N)==(1,0)
    assert all(E.epow(omega,N//r)!=(1,0) for r in factor(N))
    g=E.epow(omega,2*(q-1));H=[];x=(1,0)
    for _ in range(v):H.append(x);x=E.emul(x,g)
    assert x==(1,0) and len(set(H))==v
    alpha=E.epow(omega,v);alphaother=E.epow(alpha,N-1)
    A=[1 if E.tr(x) in E.squares else -1 for x in H]
    B=[1 if E.tr(E.emul(alpha,x)) in E.squares else -1 for x in H]
    Bother=[1 if E.tr(E.emul(alphaother,x)) in E.squares else -1 for x in H]
    assert row['D0']==[(a+1)//2 for a in A]
    assert row['L']==[(b+1)//2 for b in B]
    f=[b+int(i==0) for i,b in enumerate(B)]
    assert f==row['f'] and f[0]==0 and all(abs(x)==1 for x in f[1:])
    assert all(f[i]==f[-i%v] for i in range(v))
    assert Bother==[-1]+[-b for b in B[1:]]
    D={};h=fmpz_poly([-1]+[0]*(v-1)+[1])
    for sign,b in [(1,B),(-1,Bother)]:
        # Literal source autocorrelation, independent of the asserted spectral row.
        gram=[sum(A[k]*A[(k-r)%v]+b[k]*b[(k-r)%v] for k in range(v)) for r in range(v)]
        assert gram==[q+1]+[-2*sign*x for x in f[1:]]
        D[sign]=int(h.resultant(fmpz_poly(gram)))
        if full:
            M=[]
            for i in range(2*v):
                line=[]
                for j in range(2*v):
                    if i<v and j<v:z=A[(j-i)%v]
                    elif i<v:z=b[(j-v-i)%v]
                    elif j<v:z=b[(i-v-j)%v]
                    else:z=-A[(i-j)%v]
                    line.append(z)
                M.append(line)
            assert abs(int(fmpz_mat(M).det()))==D[sign]
    verify_values(row,D)
    return D

certificate=json.loads((root/'class4-certificate.json').read_text())
sanity=json.loads((root/'class4-sanity.json').read_text())
expected=[q for q in range(29,676) if q%4==1 and len(factor(q))==1]
assert [r['q'] for r in certificate['rows']]==expected
assert len(expected)==64 and certificate['field_count']==64 and certificate['determinant_count']==128
assert [r['q'] for r in sanity['rows']]==[5,9,13,17,25,29]
assert sanity['field_count']==6 and sanity['determinant_count']==12
selected={29,49,125,625,673};rows=[]
print('PRECHECK: 64 finite + 6 sanity fields; 140 products; 22 full determinants; max order 674',flush=True)
for row in certificate['rows']:
    D=check(row,row['q'] in selected)
    rows.append({'q':row['q'],'factorization':factor(row['q']),'source_sets':True,'source_Gram':True,'products':True,'full_block':row['q'] in selected})
    if row['q'] in selected:print('Full block determinants passed:',row['q'],'CPU',time.process_time()-cpu,flush=True)
for row in sanity['rows']:check(row,True)
negative=next(r for r in sanity['rows'] if r['q']==13)
assert Fraction(negative['values'][0]['ratio_exact'])==Fraction(841,1053)<Fraction(4,5)
corrupt=copy.deepcopy(certificate['rows'][0]);correct=check(corrupt)
corrupt['values'][0]['determinant']=str(int(corrupt['values'][0]['determinant'])+1)
try:verify_values(corrupt,correct)
except AssertionError:corruption_rejected=True
else:raise AssertionError('corrupted certificate accepted')
for data in (certificate,sanity):
    assert data['source_sha256']==hashlib.sha256((root/'class4_check.py').read_bytes()).hexdigest()
    assert data['field_dependency_sha256']==hashlib.sha256((root/'finite_check.py').read_bytes()).hexdigest()
    assert data['threshold']==676
    endpoint=Fraction(1,2*676**2)+Fraction(52,1875)
    assert Fraction(data['tail_error_endpoint'])==endpoint<Fraction(1,35)
    assert Fraction(data['gap_below_one_over_35'])==Fraction(1,35)-endpoint
    for sign in (1,-1):
        r,q=min((Fraction(v['ratio_exact']),row['q']) for row in data['rows'] for v in row['values'] if v['orientation']==sign)
        m=next(m for m in data['minima'] if m['orientation']==sign)
        assert m['q']==q and Fraction(m['ratio_exact'])==r and m['ratio_display']==float(r)
assert Fraction(163,60)>Fraction(784,289)
# Release copy: hash only files shipped in this repository (the audited
# original also hashed working notes and the MSX manuscript PDF).
files=['class4_check.py','finite_check.py','class4-certificate.json','class4-sanity.json']
result={'status':'INDEPENDENT CHECKS PASSED','coverage':rows,'finite_fields':64,'finite_orientations':128,'sanity_fields':6,'full_block_parameters':sorted(selected),'full_block_order_max':674,'q13_negative_control':True,'determinant_corruption_rejected':corruption_rejected,'shared_library':'python-flint for nmod_poly and exact fmpz resultants/determinants; no project implementation imports','cpu_seconds':time.process_time()-cpu,'wall_seconds':time.perf_counter()-wall,'file_sha256':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in files}}
(root/'class4-examiner-proof-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='coverage'},indent=2))
