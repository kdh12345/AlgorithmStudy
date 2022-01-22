import sys
from itertools import combinations_with_replacement
n=int(sys.stdin.readline().rstrip())
arr=[1,5,10,50]
candi=list(combinations_with_replacement(arr,n))
res=[]
for c in candi:
    total=0
    for item in c:
        total+=item
    res.append(total)
res=list(set(res))
ans=0
ans=len(res)
print(ans)