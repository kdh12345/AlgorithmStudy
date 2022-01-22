import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
board=[]
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    board.append(arr)
q=deque([[n-1,0],[n-1,1],[n-2,0],[n-2,1]])
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(m):
    visit=[[0]*n for _ in range(n)]
    d,s=map(int,sys.stdin.readline().split())
    d-=1
    q_len=len(q)
    #1
    while q_len>0:
        x,y=q.popleft()
        nx=x+dx[d]*s
        ny=y+dy[d]*s
        if nx>=n:
            nx%=n
        elif nx<0:
            nx=(n-1)-(((-1)*nx-1)%n)
        if ny>=n:
            ny%=n
        elif ny<0:
            ny=(n-1)-(((-1)*ny-1)%n)
        q.append([nx,ny])
        q_len-=1
    #2
    for item in q:
        x,y=item
        if visit[x][y]==0:
            board[x][y]+=1
            visit[x][y]=1
    #3
    q=deque([])
    #4
    for x in range(n):
        for y in range(n):
            if visit[x][y]==1:
                cnt=0
                for k in range(1,8,2):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if board[nx][ny]>0:
                            cnt+=1
                board[x][y]+=cnt
    #5
    for x in range(n):
        for y in range(n):
            if board[x][y]>=2:
                if visit[x][y]==0:
                    q.append([x,y])
                    board[x][y]-=2

ans=sum(sum(res) for res in board)
print(ans)