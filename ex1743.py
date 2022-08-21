import sys
from collections import deque

def bfs(sx,sy):
    global ans
    dq = deque()
    dq.append((sx,sy))
    visit[sx][sy] = 1
    cnt = 1
    while dq:
        x,y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == '#' and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    board[nx][ny] = 'x'
                    dq.append((nx,ny))
                    cnt+=1
    return cnt


ans = 0
dq = deque()
dx = (-1,0,1,0)
dy = (0,1,0,-1)
n,m,k = map(int,sys.stdin.readline().split())
board =[['.']*(m+1) for _ in range(n+1)]
visit = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,sys.stdin.readline().split())
    board[a-1][b-1] = '#'

for r in range(n):
    for c in range(m):
        if visit[r][c] == 0 and board[r][c] == '#':
            res = bfs(r,c)
            ans = max(res,ans)


print(ans)
