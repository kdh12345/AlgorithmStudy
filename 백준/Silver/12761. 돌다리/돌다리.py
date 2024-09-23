import sys
from collections import deque
input = sys.stdin.readline

a,b,n,m = map(int,input().split())

visit = [0 for _ in range(100001)]

def dist(cur,idx):
    global a,b
    arr = [cur+1,cur-1,cur*a,-cur*a,cur*b,-cur*b,cur+a,cur-a,cur+b,cur-b]
    return arr[idx]

def bfs(s):
    global m
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        now = q.popleft()
        for i in range(10):
            nxt = dist(now,i)
            if 0<=nxt<=100000 and not visit[nxt]:
                visit[nxt] = visit[now] + 1
                q.append(nxt)
                if nxt == m:
                    return

bfs(n)
ans = max(visit) - 1
print(ans)