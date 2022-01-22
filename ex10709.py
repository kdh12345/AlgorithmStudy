import sys
from collections import deque
h,w=map(int,sys.stdin.readline().split())
def bfs(sx,sy):
    dq = deque()
    dq.append([sx,sy])
    while dq:
        x,y = dq.popleft()
        nx = x + dx[0]
        ny = y + dy[0]
        if 0<=nx<h and 0<=ny<w:
            if places[nx][ny] == '.' and goorm[nx][ny] == -1:
                goorm[nx][ny] = goorm[x][y] + 1
                dq.append([nx,ny])
places = []
for _ in range(h):
    tmp = list(sys.stdin.readline().strip())
    places.append(tmp)
dx=[0]
dy=[1]
goorm = [[-1]*w for _ in range(h+1)]
for x in range(h):
    for y in range(w):
        if places[x][y] == 'c':
            goorm[x][y] = 0
            bfs(x,y)

for i in range(h):
    for j in range(w):
        print(goorm[i][j],end = ' ')
    print()

