import sys
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(cheese):
    while q:
        x,y=q.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if visit[nx][ny]==False:
                    visit[nx][ny]=True
                    if board[nx][ny]==1:
                        board[nx][ny]=-1
                        cheese-=1
                    else:
                        q.append([nx,ny])
    return cheese


def delete():
    for i in range(r):
        for j in range(c):
            if board[i][j]==-1:
                board[i][j]=0
r,c=map(int,sys.stdin.readline().split())
board=[]
cheese=0
for _ in range(r):
    arr=list(map(int,sys.stdin.readline().split(' ')))
    board.append(arr)
for i in range(r):
    for j in range(c):
        if board[i][j] == 1:
            cheese += 1
cnt=0
tmp=cheese
q=deque()
while cheese!=0:
    visit=[[False]*c for _ in range(r+1)]
    q.append([0,0])
    visit[0][0]=True
    cheese=bfs(cheese)
    if cheese!=0:
        tmp=cheese
    cnt+=1
    delete()
print(cnt)
print(tmp)