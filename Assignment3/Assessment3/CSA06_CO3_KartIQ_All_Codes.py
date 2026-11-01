"""CSA06 CO3 KartIQ case study: D&C algorithms for retail analytics."""
import random, time

# Module 1: stable merge sort by timestamp; original left item wins ties.
def merge_sort_orders(orders):
    if len(orders)<=1: return list(orders),0
    mid=len(orders)//2
    left,c1=merge_sort_orders(orders[:mid])
    right,c2=merge_sort_orders(orders[mid:])
    out=[];i=j=0;c=c1+c2
    while i<len(left) and j<len(right):
        c+=1
        if left[i][0] <= right[j][0]:
            out.append(left[i]);i+=1
        else:
            out.append(right[j]);j+=1
    return out+left[i:]+right[j:],c

# Module 2: randomized three-way quicksort; robust to duplicates.
def quick_sort_scores(values, seed=7):
    a=list(values); rng=random.Random(seed); comparisons=0; max_depth=0; partitions=[]
    def sort(lo,hi,depth):
        nonlocal comparisons,max_depth
        if lo>=hi:return
        max_depth=max(max_depth,depth)
        pivot=a[rng.randint(lo,hi)]
        lt=i=lo;gt=hi
        while i<=gt:
            comparisons+=1
            if a[i]<pivot:
                a[lt],a[i]=a[i],a[lt];lt+=1;i+=1
            else:
                comparisons+=1
                if a[i]>pivot:
                    a[i],a[gt]=a[gt],a[i];gt-=1
                else:i+=1
        partitions.append((lt-lo,gt-lt+1,hi-gt))
        sort(lo,lt-1,depth+1);sort(gt+1,hi,depth+1)
    sort(0,len(a)-1,1)
    return a,comparisons,partitions,max_depth

# Module 3: lower-bound binary search returns first timestamp occurrence.
def first_timestamp_index(sorted_orders,target):
    lo,hi=0,len(sorted_orders)
    comparisons=0
    while lo<hi:
        mid=(lo+hi)//2
        comparisons+=1
        if sorted_orders[mid][0] < target: lo=mid+1
        else: hi=mid
    if lo<len(sorted_orders):
        comparisons+=1
        if sorted_orders[lo][0]==target:return lo,comparisons
    return -1,comparisons

# Module 4: conventional multiplication.
def conventional(A,B):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): C[i][j]+=A[i][k]*B[k][j]
    return C,n**3

def add(A,B):
    n=len(A);return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def sub(A,B):
    n=len(A);return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]

def strassen(A,B,cutoff=32):
    n=len(A)
    if n<=cutoff:return conventional(A,B)
    h=n//2
    def split(M):
        return ([r[:h] for r in M[:h]],[r[h:] for r in M[:h]],
                [r[:h] for r in M[h:]],[r[h:] for r in M[h:]])
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

def strassen_any(A,B,cutoff=32):
    n=len(A)
    if not n or len(B)!=n or any(len(r)!=n for r in A+B):
        raise ValueError("A and B must be equal-size non-empty square matrices")
    size=1
    while size<n:size*=2
    def pad(M):
        return [r+[0]*(size-n) for r in M]+[[0]*size for _ in range(size-n)]
    C,count=strassen(pad(A),pad(B),cutoff)
    return [r[:n] for r in C[:n]],count

def run_experiments():
    print("CSA06 CO3 — KARTIQ CASE STUDY OUTPUTS")
    print("\\nMODULE 1 — STABLE MERGE SORT")
    orders=[(105,"O1"),(102,"O2"),(105,"O3"),(101,"O4"),(102,"O5"),(103,"O6")]
    sorted_orders,comp=merge_sort_orders(orders)
    print("Input:",orders)
    print("Sorted:",sorted_orders)
    print("Comparisons:",comp)
    print("Stable equal timestamp 102:",[o[1] for o in sorted_orders if o[0]==102])
    print("Stable equal timestamp 105:",[o[1] for o in sorted_orders if o[0]==105])
    n=10_000_000
    print("For 10,000,000 orders, log2(n)=",f"{n.bit_length()-1 + (1 if n&(n-1) else 0):,}")
    print("Approximate n*log2(n) comparison scale:",f"{n*(n.bit_length()-1):,} (upper scale estimate)")

    print("\\nMODULE 2 — RANDOMIZED THREE-WAY QUICK SORT")
    scores=[42,17,63,8,55,29]
    result,c,parts,depth=quick_sort_scores(scores)
    print("Input:",scores,"Sorted:",result)
    print("Comparisons:",c,"Partition sizes (less,equal,greater):",parts,"Max recursion depth:",depth)
    n=100_000
    print("Nearly sorted 100,000 sellers: randomized pivot gives expected O(n log n);")
    print("n*log2(n) comparison scale:",f"{n*(n.bit_length()-1):,} (not an exact measured count)")

    print("\\nMODULE 3 — FIRST-OCCURRENCE BINARY SEARCH")
    for target in (101,102,105,999):
        idx,c=first_timestamp_index(sorted_orders,target)
        print("Timestamp:",target,"first index:",idx,"order:",sorted_orders[idx] if idx!=-1 else "NOT FOUND","comparisons:",c)
    print("Maximum lower-bound iterations for 10,000,000 items: about ceil(log2(n+1)) =",
          (n.bit_length() if n==10_000_000 else 24))

    print("\\nMODULE 4 — STRASSEN MATRIX MULTIPLICATION")
    A=[[1,7],[3,5]];B=[[1,3],[7,5]]
    conventional_result,conv_count=conventional(A,B)
    strassen_result,strassen_count=strassen_any(A,B,cutoff=1)
    print("A:",A,"B:",B)
    print("Conventional result:",conventional_result,"scalar multiplications:",conv_count)
    print("Strassen result:",strassen_result,"scalar multiplications:",strassen_count)
    print("For n=1024 conventional multiplications:",1024**3)
    print("For n=1024 Strassen multiplications (7^10):",7**10)
    print("Ratio conventional / Strassen:",f"{(1024**3)/(7**10):.3f}")

    print("\\nVALIDATION")
    assert sorted_orders==[(101,"O4"),(102,"O2"),(102,"O5"),(103,"O6"),(105,"O1"),(105,"O3")]
    assert result==sorted(scores)
    assert first_timestamp_index(sorted_orders,102)[0]==1
    assert first_timestamp_index(sorted_orders,999)[0]==-1
    assert conventional_result==strassen_result==[[50,38],[38,34]]
    # Verify non-power-of-two padding path against conventional multiplication.
    X=[[1,2,3],[4,5,6],[7,8,9]]
    Y=[[9,8,7],[6,5,4],[3,2,1]]
    assert strassen_any(X,Y,cutoff=1)[0]==conventional(X,Y)[0]
    print("All validation tests: PASS")

if __name__=="__main__":run_experiments()
