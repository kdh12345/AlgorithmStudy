import sys
from collections import deque
n=int(sys.stdin.readline().rstrip())
jump=list(map(int,sys.stdin.readline().split()))
dp=[-1]*n
start=0
dq=deque([start])
dp[start]=0
while dq:
    x=dq.popleft()
    now=jump[x]
    for i in range(now,0,-1):
        if x+i<n and dp[x+i]==-1:
            dp[x+i]=dp[x]+1
            dq.append(x+i)
print(dp[-1])
