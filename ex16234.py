import sys
from collections import deque
n,l,r=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    graph.append(arr)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def go(a,b,index):
    q=deque()
    united=[]
    q.append((a,b))
    united.append((a,b))
    res=graph[a][b]
    union[a][b]=index
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if l<=abs(graph[nx][ny]-graph[x][y])<=r and union[nx][ny]==-1:
                    united.append((nx, ny))
                    q.append((nx, ny))
                    union[nx][ny] = index
                    res += graph[nx][ny]
                    cnt+=1
    for x,y in united:
        graph[x][y]=res//cnt
    return cnt

ans=0
while True:
    union=[[-1]*n for _ in range(n+1)]
    idx=0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                go(i,j,idx)
                idx+=1
    if idx==n*n:
        break
    ans+=1
print(ans)