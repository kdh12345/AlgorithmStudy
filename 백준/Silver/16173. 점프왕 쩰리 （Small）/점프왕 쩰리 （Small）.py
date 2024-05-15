import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)

dx = [1,0]
dy = [0,1]

dq = deque()
dq.append([0,0,board[0][0]])
visit = [[0]*(n+1) for _ in range(n+2)]
visit[0][0] = 1

while dq:
    x,y,go = dq.popleft()
    if x==n-1 and y==n-1:
        print('HaruHaru')
        exit(0)
    for d in range(2):
        nx = x + dx[d]*go
        ny = y + dy[d]*go
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dq.append([nx,ny,board[nx][ny]])

print('Hing')