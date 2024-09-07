import sys
input = sys.stdin.readline
from collections import deque
def bfs(x1,y1):
    global n, visit

    dx = [-2,-2,0,0,2,2]
    dy = [-1,1,-2,2,-1,1]
    dq = deque()
    dq.append((x1,y1))
    visit[x1][y1] = 0
    while dq:
        x,y = dq.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    dq.append((nx,ny))



n = int(input())
r1,c1,r2,c2 = map(int,input().split())
visit = [[-1]*(n+1) for _ in  range(n+1)]

bfs(r1,c1)
ans = visit[r2][c2]
print(ans)