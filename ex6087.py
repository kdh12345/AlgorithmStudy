import sys
from collections import deque
w,h = map(int,sys.stdin.readline().split())
INF = int(1e9)

dx = [0,-1,0,1]
dy = [-1,0,1,0]
def bfs(sx,sy,ex,ey):
    visit = [[[INF] * 4 for _ in range(w)] for _ in range(h)]
    q = deque()
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]
        if 0<=nx<h and 0<=ny<w:
            if board[nx][ny] != '*':
               q.append([nx,ny,d])
               visit[nx][ny][d] = 0
    while q:
        x,y, direction = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<h and 0<=ny<w:
                if board[nx][ny] != '*':
                    cnt = visit[x][y][direction]
                    if direction == 0 or direction == 2:
                        if d == 1 or d == 3:
                            cnt +=1
                    else:
                        if d == 0 or d == 2:
                            cnt+=1
                    if visit[nx][ny][d] == -1:
                        visit[nx][ny][d] = cnt
                        q.append([nx,ny,d])
                    else:
                        if visit[nx][ny][d] > cnt:
                            visit[nx][ny][d] = cnt
                            q.append([nx,ny,d])
    return min(visit[ex][ey])

point = []
board = []
for i in range(h):
    board.append(list(sys.stdin.readline().strip()))
    for j in range(w):
        if board[i][j] == "C":
            point.append([i,j])

ans = bfs(point[0][0],point[0][1],point[1][0],point[1][1])
print(ans)