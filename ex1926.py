import sys
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    area = 1
    while dq:
        x,y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    area+=1
                    dq.append((nx,ny))
    return area
n,m = map(int,sys.stdin.readline().split())
board = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)

visit = [[0]*m for _ in range(n+1)]
ans = 0
cnt  = 0
area = 0

for x in range(n):
    for y in range(m):
        if board[x][y] == 1 and visit[x][y] == 0:
            visit[x][y] = 1
            area = bfs(x,y)
            ans = max(ans,area)
            cnt+=1
print(cnt)
print(ans)
