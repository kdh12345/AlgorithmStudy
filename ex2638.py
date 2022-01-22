import sys
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs():
    while q:
        x,y=q.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==-1:
                    if board[nx][ny]>=1:
                        board[nx][ny]+=1
                    else:
                        visit[nx][ny]=0
                        q.append([nx,ny])

def melt():
    cheese=0
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 3:
                board[i][j] = 0
                cheese = 1
            elif board[i][j] == 2:
                board[i][j] = 1
    return cheese

n,m=map(int,sys.stdin.readline().split())
board=[]
for _ in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    board.append(arr)



cnt=0
q=deque()
cheese=0
while True:
    visit=[[-1]*m for _ in range(n+1)]
    q.append([0,0])
    visit[0][0]=True
    bfs()
    cheese=melt()
    if cheese==1:
        cnt+=1
    else:
        break

print(cnt)