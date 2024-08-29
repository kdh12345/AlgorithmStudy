import sys
input = sys.stdin.readline

from collections import deque
def bfs(sx,sy,h):
    global ans,visit

    q = deque()
    q.append((sx,sy))
    chk = True

    visit[sx][sy] = 1
    cnt = 1
    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                chk = False
                continue
            if board[nx][ny] <= h and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    if chk == True:
        ans += cnt

visit = []
ans = 0

n,m = map(int,input().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for number in range(1,9):
    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] <= number and visit[i][j] == 0:
                bfs(i,j,number)
print(ans)