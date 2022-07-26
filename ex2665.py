import sys
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(sx,sy):
    visit=[[-1]*(n+1) for _ in range(n+2)]
    dq = deque()
    visit[sx][sy] = 0
    dq.append((sx,sy))
    while dq:
        x,y = dq.popleft()
        if x==n-1 and y==n-1:
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == '1' and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y]
                    dq.appendleft((nx,ny))
                elif board[nx][ny] == '0' and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    board[nx][ny] = '1'
                    dq.append((nx,ny))
    return visit

n=int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
    arr = list(sys.stdin.readline().strip())
    board.append(arr)
ans = bfs(0,0)
print(ans[n-1][n-1])