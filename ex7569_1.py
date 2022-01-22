import sys
from collections import deque
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
def bfs():
    x=0
    y=0
    z=0
    while q:
        x,y,z=q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                if board[nx][ny][nz]==0 and visit[nx][ny][nz]==-1:
                    visit[nx][ny][nz]=visit[x][y][z]+1
                    board[nx][ny][nz]=1
                    q.append([nx,ny,nz])
    return visit[x][y][z]
m,n,h=map(int,sys.stdin.readline().split())
visit=[[[-1]*m for _ in range(n)] for _ in range(h)]
board=[[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k]==1 and visit[i][j][k]==-1:
                q.append([i,j,k])
                visit[i][j][k]=0

ans=bfs()
for i in board:
    for j in i:
        if 0 in j:
            print(-1)
            sys.exit()
print(ans)


