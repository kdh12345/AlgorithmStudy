import sys
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def destroy(now,left):
    x,y=r-now,0 #밑이 1이기 때문에 반대로
    if left==1:#left
        for k in range(c):
            if board[x][k]=='x':
                board[x][k]='.'
                y=k
                break
    else:#right
        for k in range(c-1,-1,-1):
            if board[x][k]=='x':
                board[x][k]='.'
                y=k
                break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny]=='x':
                dq.append([nx,ny])

def bfs(x,y):
    q=deque()
    visit=[[0]*c for _ in range(r+1)]
    fall_list=[] #떨어질 수 있는 좌표
    q.append([x,y])
    visit[x][y]=1
    while q:
        x,y=q.popleft()
        if x==r-1:
            return
        if board[x+1][y]=='.':
            fall_list.append([x,y])
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if board[nx][ny]=='x' and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append([nx,ny])
    fall(fall_list,visit)
def fall(fall_list,visit):
    next_idx,flag=1,False
    while True: #미네랄 ㅇㄷ까지?
        for x,y in fall_list:
            if x+next_idx==r-1:
                flag=True
                break
            if board[x+1+next_idx][y]=='x' and visit[x+1+next_idx][y]==0:
                flag=True
                break
        if flag==True:
            break
        next_idx+=1
    for i in range(r-2,-1,-1): #fall 작업
        for j in range(c):
            if board[i][j]=='x' and visit[i][j]==1:
                board[i][j]='.'
                board[i+next_idx][j]='x'
r,c=map(int,sys.stdin.readline().split())
board=[]
for _ in range(r):
    arr=list(sys.stdin.readline().strip())
    board.append(arr)
n=int(sys.stdin.readline().rstrip())
height=list(map(int,sys.stdin.readline().split()))
dq=deque()
left=1
while n:
    idx=height.pop(0)
    destroy(idx,left)
    while dq:
        x,y=dq.popleft()
        bfs(x,y)
    n-=1
    left*=-1
for i in range(r):
    for j in range(c):
        print(board[i][j],end='')
    print()