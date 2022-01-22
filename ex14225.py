import sys
from itertools import combinations
n=int(sys.stdin.readline().rstrip())
numbers=list(map(int,sys.stdin.readline().split()))
total=sum(numbers)
store=[0]*2000001
for i in range(1,n+1):
    candi=list(combinations(numbers,i))
    for c in candi:
        arr = []
        for item in c:
            arr.append(item)
        temp=sum(arr)
        store[temp]=1
ans=0
for i in range(1,2000001):
    if store[i]==0:
        ans=i
        break
if ans==0:
    ans=total+1
print(ans)