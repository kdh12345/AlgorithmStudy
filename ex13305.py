import sys
n=int(sys.stdin.readline().rstrip())
roads=list(map(int,sys.stdin.readline().split()))
costs=list(map(int,sys.stdin.readline().split()))
now=costs[0]
dist=0
ans=costs[0]*roads[0]
for i in range(1,n-1):
    if costs[i]<now:
        ans+=now*dist
        now=costs[i]
        dist=roads[i]
    else:
        dist+=roads[i]
    if i==n-2:
        ans+=now*dist
print(ans)