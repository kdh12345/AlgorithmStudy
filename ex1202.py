import sys
import heapq
n,k=map(int,sys.stdin.readline().split())
jew=[]
for _ in range(n):
    w,p=map(int,sys.stdin.readline().split())
    heapq.heappush(jew,[w,p])
weights=[]
for _ in range(k):
    weight=int(sys.stdin.readline().rstrip())
    weights.append(weight)
weights.sort()
ans=0
temp=[]
for w in weights:
    while len(jew)>0 and w>=jew[0][0]:
        heapq.heappush(temp,-heapq.heappop(jew)[1])
    if len(temp)>0:
        ans-=heapq.heappop(temp)
    elif len(jew)==0:
        break

print(ans)
