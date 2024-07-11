import sys
sys.setrecursionlimit(3000000)
def dfs(x,y,cnt):
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<m and 0<=ny<n:
            if board[nx][ny] == 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dfs(nx,ny,cnt+1)
    return cnt
m,n=map(int,input().split())

board = []
for _ in range(m):
    arr = list(map(int,input().split()))
    board.append(arr)

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
visit = [[0]*(n+1) for _ in range(m+1)]
result = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            cnt2 = dfs(i,j,0)
            result.append(cnt2)

ans = len(result)
print(ans)