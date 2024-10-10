import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]

chk = []
def bfs(sx,sy,chkidx):
    q = deque()
    q.append((sx,sy))
    visit[sx][sy] = 1
    chk = [(sx,sy)]
    while q:
        x,y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx>=n or ny<0 or ny>=m:
                continue
            if visit[nx][ny] == 1:
                continue
            if board[x][y] < board[nx][ny]: #봉오리x
                return 0
            if board[x][y] == board[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx,ny))
                chk.append((nx,ny))
        chkidx+=chk
    return 1



ans = 0
for i in range(n):
    for j in range(m):
        if (i,j) not in chk:
            visit=[[0]*m for _ in range(n)]
            ans+=bfs(i,j,chk)
print(ans)