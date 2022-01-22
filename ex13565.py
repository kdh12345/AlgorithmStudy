import sys
sys.setrecursionlimit(3000000)

def dfs(x,y):
    maps[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if maps[nx][ny] == 0:
                dfs(nx,ny)

n,m = map(int,sys.stdin.readline().split())
maps = [list(map(int, list(input()))) for _ in range(n)] # str -> int


dx=[-1,0,1,0]
dy=[0,1,0,-1]
visit=[[0]*m for _ in range(n)]

for y in range(m):
    if maps[0][y] == 0:
        visit[0][y] = 1
        dfs(0,y)


if -1 in maps[-1]:
    print('YES')
else:
    print('NO')
