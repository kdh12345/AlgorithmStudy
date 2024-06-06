import sys
from collections import deque
def bfs(a,b):
    sheep,wolf = 0,0
    dq.append((a,b))
    visit[a][b] = 1
    while dq:
        x,y = dq.popleft()
        if board[x][y] == 'k':
            sheep+=1
        if board[x][y] == 'v':
            wolf += 1
        for d in range(4):
            nx = x +dx[d]
            ny = y+dy[d]
            if 0<=nx<r and 0<=ny<c and visit[nx][ny] == 0 and board[nx][ny] != '#':
                visit[nx][ny] = 1
                dq.append((nx,ny))
    if sheep>wolf:
        wolf = 0
    else:
        sheep = 0
    return sheep,wolf
r,c = map(int,sys.stdin.readline().split())
visit = [[0]*c for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dq = deque()
ans_sheep = 0
ans_wolf = 0
board = []
for _ in range(r):
    arr = list(sys.stdin.readline().rstrip())
    board.append(arr)

for i in range(r):
    for j in range(c):
        if board[i][j] in ('v','k') and visit[i][j] == 0:
            res1, res2 = bfs(i,j)
            ans_sheep+=res1
            ans_wolf+=res2

print(ans_sheep,ans_wolf)
