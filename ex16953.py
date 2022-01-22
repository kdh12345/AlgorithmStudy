import sys
from collections import deque
def atob(s,e):
    dq=deque()
    dq.append([s,0])
    cnt=0
    while dq:
        now,cnt=dq.popleft()
        if now==e:
            return cnt+1
        if 2*now<=e:
            dq.append([2*now,cnt+1])
        tmp=str(now)+'1'
        if int(tmp)<=e:
            dq.append([int(tmp),cnt+1])
    return -1
a,b=map(int,sys.stdin.readline().split())
ans=atob(a,b)
print(ans)