import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
dq = deque()
for i in range(1,n+1):
    dq.append(i)

while len(dq) >= k:
    now = dq.popleft()
    dq.append(now)
    for i in range(k-1):
        dq.popleft()

ans = dq[0]
print(ans)