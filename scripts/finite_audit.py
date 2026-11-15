"""Independent source-set/resultant and dense-matrix certificate audit."""
import sys,resource,time,json,math,hashlib
from pathlib import Path
from fractions import Fraction
assert sys.prefix != sys.base_prefix
resource.setrlimit(resource.RLIMIT_CPU,(178,180))
from flint import fmpz_poly,fmpz_mat
ROOT=Path(__file__).resolve().parent
start=time.process_time(); wall=time.monotonic()
cert=json.loads((ROOT/'finite-certificate.json').read_text())
# Independent coverage: factor each integer, rather than enumerate prime powers.
def prime_power(n):
    divisor=next((d for d in range(2,math.isqrt(n)+1) if n%d==0),n)
    rem=n; degree=0
    while rem%divisor==0: rem//=divisor; degree+=1
    return (divisor,degree) if rem==1 else None
expected=[(q,*prime_power(q)) for q in range(29,1001,4) if prime_power(q)]
assert [(r['q'],r['p'],r['degree']) for r in cert['rows']]==expected
assert len(expected)==89 and cert['field_count']==89 and cert['determinant_count']==178

class IndependentField:
    def __init__(self,r):
        self.p,self.d,self.q=r['p'],r['degree'],r['q']
        self.mod=r['modulus']; self.w=r['primitive']
        assert self.p**self.d==self.q
        assert len(self.mod)==self.d+1 and self.mod[-1]==1
        assert all(0<=a<self.p for a in self.mod)
        self.place=[self.p**i for i in range(self.d)]
        self.coeff=[[x//z%self.p for z in self.place] for x in range(self.q)]
        # Multiplication by X is independently tabulated; general multiplication
        # uses this linear map (Horner), not convolution plus reduction.
        self.shift=[]
        for row in self.coeff:
            nxt=[0]+row[:-1]; lead=row[-1]
            self.shift.append(sum((nxt[i]-lead*self.mod[i])%self.p*self.place[i] for i in range(self.d)))
        self.powers=[]; z=1
        for _ in range(self.q-1):
            self.powers.append(z); z=self.mul(z,self.w)
        assert z==1 and set(self.powers)==set(range(1,self.q))
        self.squares={self.mul(x,x) for x in range(1,self.q)}
        assert len(self.squares)==(self.q-1)//2
        self.H=self.powers[::2]
        assert set(self.H)==self.squares
    def add(self,x,y):
        return sum((a+b)%self.p*z for a,b,z in zip(self.coeff[x],self.coeff[y],self.place))
    def scale(self,x,k):
        return sum(a*k%self.p*z for a,z in zip(self.coeff[x],self.place))
    def mul(self,x,y):
        if self.d==1: return x*y%self.p
        val=0
        for k in reversed(self.coeff[y]):
            val=self.add(self.shift[val],self.scale(x,k))
        return val
    def source_sets(self,i):
        coset=self.squares if i==0 else set(range(1,self.q))-self.squares
        shifted={self.add(x,1) for x in coset}
        return shifted & self.squares,{self.mul(self.w,x) for x in shifted}&self.squares
    def sub1(self,x):
        return self.add(x,self.p-1)

results=[]; fields={}; exact_ratios={5:[],6:[]}
for r in cert['rows']:
    q=r['q']; F=IndependentField(r); m=(q-1)//2
    # Check stored f from squares, independent of the generator logarithms.
    f=[0 if F.sub1(x)==0 else (1 if F.sub1(x) in F.squares else -1) for x in F.H]
    assert f==r['f']
    W=2*q*(q-1)**m; assert W==int(r['W'])
    h=fmpz_poly([1]*m)
    assert [v['class_number'] for v in r['values']]==[5,6]
    for i,v in zip((1,0),r['values']):
        D,E=F.source_sets(i)
        assert len(D)==(q-1)//4-(i==0)
        assert len(E)==(q-1)//4
        coeff=[-4*int(x in D) for x in F.H]; coeff[0]+=q-1
        P=int(h.resultant(fmpz_poly(coeff)))
        K=4*m*m if i==1 else 4*(m*m+2*m+2)
        det=K*P
        assert P==int(v['nonprincipal_product']) and det==int(v['determinant'])
        margin=5*det-4*W
        assert margin==int(v['margin_5D_minus_4W']) and margin>0
        ratio=Fraction(det,W)
        assert ratio==Fraction(int(v['ratio_numerator']),int(v['ratio_denominator']))
        exact_ratios[v['class_number']].append((ratio,q))
    if q in (29,49,125,625,729,997): fields[q]=(F,r)
    results.append({'q':q,'source_set_resultants':'passed'})
for minimum in cert['minima']:
    ratio,q=min(exact_ratios[minimum['class_number']])
    assert q==minimum['q'] and str(ratio)==minimum['ratio_exact']
print('All 89 fields and 178 independent source-set resultants/margins passed; CPU',time.process_time()-start,flush=True)
report={'coverage_count':len(expected),'resultants_checked':178,'minima':cert['minima'],'dense':[],
        'certificate_sha256':hashlib.sha256((ROOT/'finite-certificate.json').read_bytes()).hexdigest()}
def checkpoint():
    report['cpu_seconds']=time.process_time()-start; report['wall_seconds']=time.monotonic()-wall
    (ROOT/'finite-audit-results.json').write_text(json.dumps(report,indent=2)+'\n')
checkpoint()
# Six independent dense source-matrix checks, both classes: 12 matrices,
# total matrix sizes 30,50,126,626,730,998; maximum 996004 integer entries.
for q in (29,49,125,625,729,997):
    F,r=fields[q]; m=(q-1)//2
    for i,v in zip((1,0),r['values']):
        D,E=F.source_sets(i)
        a=[2*int(x in D)-1 for x in F.H]; b=[2*int(x in E)-1 for x in F.H]
        # Direct source equations (2.3)/(2.4), retaining their border order.
        if i==1:
            rows=[[1]+[1]*m+[1]+[1]*m]
            rows += [[1]+[a[(t-r)%m] for t in range(m)]+[1]+[b[(t-r)%m] for t in range(m)] for r in range(m)]
            rows += [[1]+[1]*m+[-1]+[-1]*m]
            rows += [[1]+[b[(r-t)%m] for t in range(m)]+[-1]+[-a[(r-t)%m] for t in range(m)] for r in range(m)]
        else:
            rows=[[1]+[1]*m+[-1]+[-1]*m]
            rows += [[1]+[a[(t-r)%m] for t in range(m)]+[1]+[b[(t-r)%m] for t in range(m)] for r in range(m)]
            rows += [[1]+[1]*m+[1]+[1]*m]
            rows += [[-1]+[-b[(r-t)%m] for t in range(m)]+[1]+[a[(r-t)%m] for t in range(m)] for r in range(m)]
        d=abs(int(fmpz_mat(rows).det()))
        assert d==int(v['determinant'])
        report['dense'].append({'q':q,'class':v['class_number'],'passed':True})
        checkpoint()
        print('Dense source determinant passed',q,v['class_number'],'CPU',time.process_time()-start,flush=True)
print('COMPLETE',report['cpu_seconds'],flush=True)
