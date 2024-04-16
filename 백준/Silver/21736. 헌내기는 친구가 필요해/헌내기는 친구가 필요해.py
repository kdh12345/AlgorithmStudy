import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

board = []
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    board.append(word)

sx = 0
sy = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 'I':
            sx = i
            sy = j

dq = deque()
dq.append((sx,sy))
visit = [[0]*(m+1) for _ in range(n+1)]
visit[sx][sy] = 1
dx = [-1,0,1,0]
dy = [0,-1,0,1]

ans = 0
while dq:
    x,y = dq.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == 'O' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dq.append((nx,ny))
            elif board[nx][ny] == 'P' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                ans += 1
                dq.append((nx, ny))



if ans == 0:
    print('TT')
else:
    print(ans)
