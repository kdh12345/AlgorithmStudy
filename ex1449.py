import sys
n,l=map(int,sys.stdin.readline().split())
loc_arr=list(map(int,sys.stdin.readline().split()))
loc_arr.sort()
s=loc_arr[0]
e=s+l-0.5
ans=0
for loc in loc_arr:
    if e>=loc: #추가 필요 x
        continue
    ans+=1
    e=loc+l-0.5
ans+=1
print(ans)
