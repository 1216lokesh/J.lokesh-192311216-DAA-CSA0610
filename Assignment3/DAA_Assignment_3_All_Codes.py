"""DAA Assignment 3 CO3: runnable implementations and experiments."""
import random, time, math

def find_min_max(a):
    if not a: raise ValueError("Input cannot be empty")
    c=0
    if len(a)%2==0:
        c+=1
        mn,mx=(a[0],a[1]) if a[0]<a[1] else (a[1],a[0]); i=2
    else: mn=mx=a[0]; i=1
    while i<len(a)-1:
        c+=1
        lo,hi=(a[i],a[i+1]) if a[i]<a[i+1] else (a[i+1],a[i])
        c+=1
        if lo<mn: mn=lo
        c+=1
        if hi>mx: mx=hi
        i+=2
    return mn,mx,c

def binary_search(a,x):
    lo,hi,c=0,len(a)-1,0
    while lo<=hi:
        m=(lo+hi)//2; c+=1
        if a[m]==x: return m,c
        c+=1
        if x<a[m]: hi=m-1
        else: lo=m+1
    return -1,c

def merge_sort(a):
    c=0
    def rec(x):
        nonlocal c
        if len(x)<2:return x
        m=len(x)//2; l=rec(x[:m]); r=rec(x[m:]); out=[]; i=j=0
        while i<len(l) and j<len(r):
            c+=1
            if l[i]<=r[j]:out.append(l[i]);i+=1
            else:out.append(r[j]);j+=1
        return out+l[i:]+r[j:]
    return rec(list(a)),c

def quick_sort(a):
    a=list(a); c=0; parts=[]; depthmax=0
    def rec(lo,hi,d):
        nonlocal c,depthmax
        if lo>=hi:return
        depthmax=max(depthmax,d); pivot=a[hi]; i=lo
        for j in range(lo,hi):
            c+=1
            if a[j]<=pivot:a[i],a[j]=a[j],a[i];i+=1
        a[i],a[hi]=a[hi],a[i];parts.append((i-lo,hi-i))
        rec(lo,i-1,d+1);rec(i+1,hi,d+1)
    rec(0,len(a)-1,1)
    return a,c,parts,depthmax

def standard_multiply(x,y):
    sx,sy=int(x),int(y); sign=-1 if (sx<0)^(sy<0) else 1
    x,y=abs(sx),abs(sy)
    def f(a,b):
        if a<10 or b<10:return a*b,1
        m=max(len(str(a)),len(str(b)))//2; base=10**m
        ah,al=divmod(a,base);bh,bl=divmod(b,base)
        p1,c1=f(ah,bh);p2,c2=f(ah,bl);p3,c3=f(al,bh);p4,c4=f(al,bl)
        return p1*base*base+(p2+p3)*base+p4,c1+c2+c3+c4
    z,c=f(x,y);return sign*z,c

def karatsuba(x,y):
    sx,sy=int(x),int(y); sign=-1 if (sx<0)^(sy<0) else 1
    def f(a,b):
        if a<10 or b<10:return a*b,1
        m=max(len(str(a)),len(str(b)))//2; base=10**m
        ah,al=divmod(a,base);bh,bl=divmod(b,base)
        z0,c0=f(al,bl);z2,c2=f(ah,bh);z1,c1=f(al+ah,bl+bh)
        return z2*base*base+(z1-z2-z0)*base+z0,c0+c1+c2
    z,c=f(abs(sx),abs(sy));return sign*z,c

def add(A,B):return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def sub(A,B):return [[A[i][j]-B[i][j] for j in range(len(A))] for i in range(len(A))]
def conventional(A,B):
    n=len(A);C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):C[i][j]+=A[i][k]*B[k][j]
    return C,n**3
def strassen(A,B,cutoff=2):
    n=len(A)
    if n<=cutoff:return conventional(A,B)
    h=n//2
    split=lambda M:( [r[:h] for r in M[:h]],[r[h:] for r in M[:h]],[r[:h] for r in M[h:]],[r[h:] for r in M[h:]] )
    a,b,c,d=split(A);e,f,g,h2=split(B)
    m1,c1=strassen(add(a,d),add(e,h2),cutoff)
    m2,c2=strassen(add(c,d),e,cutoff)
    m3,c3=strassen(a,sub(f,h2),cutoff)
    m4,c4=strassen(d,sub(g,e),cutoff)
    m5,c5=strassen(add(a,b),h2,cutoff)
    m6,c6=strassen(sub(c,a),add(e,f),cutoff)
    m7,c7=strassen(sub(b,d),add(g,h2),cutoff)
    c11=add(sub(add(m1,m4),m5),m7);c12=add(m3,m5)
    c21=add(m2,m4);c22=add(add(sub(m1,m2),m3),m6)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        C[i][:h]=(c11 if i<h else c21)[i%h]
        C[i][h:]=(c12 if i<h else c22)[i%h]
    return C,c1+c2+c3+c4+c5+c6+c7
def strassen_any(A,B):
    n=len(A)
    if not n or len(B)!=n or any(len(r)!=n for r in A+B):raise ValueError("Square equal matrices required")
    s=1
    while s<n:s*=2
    def pad(M):return [r+[0]*(s-n) for r in M]+[[0]*s for _ in range(s-n)]
    C,c=strassen(pad(A),pad(B))
    return [r[:n] for r in C[:n]],c

def closest_brute(P):
    n=len(P)
    if n<2:return None,float("inf"),0
    best=(0,1);d2=(P[0][0]-P[1][0])**2+(P[0][1]-P[1][1])**2;c=1
    for i in range(n-1):
        for j in range(i+1,n):
            if (i,j)==(0,1):continue
            z=(P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2;c+=1
            if z<d2:d2=z;best=(i,j)
    return best,math.sqrt(d2),c

def closest_dc(P):
    if len(P)<2:return None,float("inf"),0
    X=sorted([(x,y,i) for i,(x,y) in enumerate(P)])
    Y=sorted(X,key=lambda p:p[1]); count=0
    def d2(a,b):
        nonlocal count
        count+=1;return (a[0]-b[0])**2+(a[1]-b[1])**2
    def rec(x,y):
        n=len(x)
        if n<=3:
            best=float("inf");pair=None
            for i in range(n):
                for j in range(i+1,n):
                    z=d2(x[i],x[j])
                    if z<best:best=z;pair=(x[i][2],x[j][2])
            return pair,best
        mid=n//2;lx=x[:mid];rx=x[mid:];ids={p[2] for p in lx}
        ly=[p for p in y if p[2] in ids];ry=[p for p in y if p[2] not in ids]
        splitx=rx[0][0];pl,dl=rec(lx,ly);pr,dr=rec(rx,ry)
        pair,best=(pl,dl) if dl<=dr else (pr,dr)
        strip=[p for p in y if (p[0]-splitx)**2<best]
        for i in range(len(strip)):
            for j in range(i+1,min(i+8,len(strip))):
                if (strip[j][1]-strip[i][1])**2>=best:break
                z=d2(strip[i],strip[j])
                if z<best:best=z;pair=(strip[i][2],strip[j][2])
        return pair,best
    pair,z=rec(X,Y);return pair,math.sqrt(z),count

def quickselect(a,k):
    a=list(a);c=0;lo=0;hi=len(a)-1
    if not 0<=k<len(a):raise IndexError
    while True:
        if lo==hi:return a[lo],c
        p=a[hi];i=lo
        for j in range(lo,hi):
            c+=1
            if a[j]<p:a[i],a[j]=a[j],a[i];i+=1
        a[i],a[hi]=a[hi],a[i]
        if i==k:return a[i],c
        if k<i:hi=i-1
        else:lo=i+1

def median_of_medians(a,k):
    c=0
    if not 0<=k<len(a):raise IndexError
    def sel(x,k):
        nonlocal c
        if len(x)<=5:
            c+=max(0,len(x)-1);return sorted(x)[k]
        meds=[]
        for i in range(0,len(x),5):
            g=sorted(x[i:i+5]);c+=len(g)-1;meds.append(g[len(g)//2])
        p=sel(meds,len(meds)//2);lo=[];eq=[];hi=[]
        for v in x:
            c+=1
            (lo if v<p else hi if v>p else eq).append(v)
        if k<len(lo):return sel(lo,k)
        if k<len(lo)+len(eq):return p
        return sel(hi,k-len(lo)-len(eq))
    return sel(list(a),k),c

def subset_sum_mitm(a,target):
    mid=len(a)//2;left=a[:mid];right=a[mid:];lookup={}
    for mask in range(1<<len(left)):
        s=sum(left[i] for i in range(len(left)) if mask>>i&1)
        lookup.setdefault(s,[i for i in range(len(left)) if mask>>i&1])
    for mask in range(1<<len(right)):
        s=sum(right[i] for i in range(len(right)) if mask>>i&1);need=target-s
        if need in lookup:return lookup[need]+[mid+i for i in range(len(right)) if mask>>i&1]
    return None

def run_all():
    print("DAA ASSIGNMENT 3 — CO3 OUTPUTS")
    print("\nQ1A MAX/MIN")
    for a in ([7],[4,9],[3,8,1,7,2,9],list(range(1,17))):
        print("n=",len(a),"min/max/comparisons=",find_min_max(a))
    print("\nQ1B BINARY SEARCH")
    for x in (0,50,98,51):print("target",x,"=>",binary_search(list(range(0,100,2)),x))
    print("\nQ2 MERGE SORT / QUICK SORT")
    for label,a in (("balanced-style",[1,2,6,4,5,7,3]),("unbalanced ascending",list(range(1,21)))):
        m,mc=merge_sort(a);q,qc,parts,dep=quick_sort(a)
        print(label,"merge comparisons",mc,"quick comparisons",qc,"partition sizes",parts[:6],"max depth",dep,"correct",m==q==sorted(a))
    print("\nQ3 KARATSUBA")
    for x,y in ((1234,5678),(12345678,87654321),(123456789012,987654321098)):
        s,sc=standard_multiply(x,y);k,kc=karatsuba(x,y)
        print("digits",len(str(x)),"correct",s==k==x*y,"standard base products",sc,"Karatsuba base products",kc)
    print("\nQ3 TIMING")
    rng=random.Random(7)
    for digits in (8,16,32,64,128):
        x=rng.randrange(10**(digits-1),10**digits);y=rng.randrange(10**(digits-1),10**digits);reps=15
        t=time.perf_counter()
        for _ in range(reps):standard_multiply(x,y)
        ts=(time.perf_counter()-t)/reps;t=time.perf_counter()
        for _ in range(reps):karatsuba(x,y)
        tk=(time.perf_counter()-t)/reps
        print("digits",digits,"standard",f"{ts:.7e}","Karatsuba",f"{tk:.7e}")
    print("\nQ4 STRASSEN")
    rng=random.Random(11)
    for n in (2,4,8,16):
        A=[[rng.randint(-5,5) for _ in range(n)] for _ in range(n)];B=[[rng.randint(-5,5) for _ in range(n)] for _ in range(n)]
        t=time.perf_counter();C,c1=conventional(A,B);tc=time.perf_counter()-t
        t=time.perf_counter();S,c2=strassen_any(A,B);ts=time.perf_counter()-t
        print("n",n,"correct",C==S,"conventional multiplications",c1,"Strassen multiplications",c2,"times",f"{tc:.6e}",f"{ts:.6e}")
    print("\nQ5 CLOSEST PAIR")
    rng=random.Random(21)
    for n in (100,500,1000,2000):
        P=[(rng.random()*10000,rng.random()*10000) for _ in range(n)]
        t=time.perf_counter();_,db,cb=closest_brute(P);tb=time.perf_counter()-t
        t=time.perf_counter();_,dd,cd=closest_dc(P);td=time.perf_counter()-t
        print("n",n,"same distance",abs(db-dd)<1e-9,"brute calculations",cb,"D&C calculations",cd,"times",f"{tb:.5f}",f"{td:.5f}")
    print("\nQ6A SELECTION")
    a=[29,10,14,37,13,5,42,8,21,17,3,31,25];k=5
    q,qc=quickselect(a,k);m,mc=median_of_medians(a,k)
    print("kth",k,"QuickSelect",q,"comparisons",qc,"Median of Medians",m,"comparisons",mc)
    print("\nQ6B MEET IN THE MIDDLE")
    a=[3,34,4,12,5,2];target=9;ans=subset_sum_mitm(a,target)
    print("values",a,"target",target,"selected indices",ans,"selected values",[a[i] for i in ans] if ans is not None else None)
    print("\nVALIDATION")
    assert find_min_max([5])[:2]==(5,5)
    assert binary_search([],1)[0]==-1
    assert merge_sort([])[0]==[] and quick_sort([])[0]==[]
    assert karatsuba(12345,67890)[0]==12345*67890
    A=[[1,2,3],[4,5,6],[7,8,9]];B=[[9,8,7],[6,5,4],[3,2,1]]
    assert strassen_any(A,B)[0]==conventional(A,B)[0]
    assert closest_brute([(0,0)])[0] is None
    assert abs(closest_brute([(0,0),(1,1)])[1]-closest_dc([(0,0),(1,1)])[1])<1e-9
    assert median_of_medians(a,2)[0]==sorted(a)[2]
    assert ans is not None and sum(a[i] for i in ans)==target
    print("All validation tests: PASS")

if __name__=="__main__":run_all()
