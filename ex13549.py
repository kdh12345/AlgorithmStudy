import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
def bfs(now):
    q=deque()
    q.append(now)
    visit=[-1]*200001
    visit[now]=0
    while q:
        x=q.popleft()
        if x==k:
            return visit[x]
        if 2 * x <= 200000 and visit[2 * x] == -1:
            visit[2 * x] = visit[x]
            nx = 2 * x
            q.append(nx)
        if 0<=x-1 and visit[x-1]==-1:
            visit[x-1]=visit[x]+1
            nx=x-1
            q.append(nx)
        if x+1<=200000 and visit[x+1]==-1:
            visit[x+1]=visit[x]+1
            nx=x+1
            q.append(nx)

ans=bfs(n)
print(ans)