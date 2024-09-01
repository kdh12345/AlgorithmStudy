import sys
input = sys.stdin.readline
def dfs(x,y):
    global board,visit,dx,dy,cnt
    visit[x][y] = 1
    for d in range(2):
        nx = x + dx[d]*board[x][y]
        ny = y + dy[d]*board[x][y]
        if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
            if nx == n-1 and ny == n-1:
                print('HaruHaru')
                exit(0)
            else:
                dfs(nx,ny)
    return False
n = int(input())
board = []
for _ in range(n):
    arr = list(map(int,input().split()))
    board.append(arr)
visit = [[0]*(n+1) for _ in range(n+1)]
cnt = 0
dx = [0,1]
dy = [1,0]
ans = dfs(0,0)

if ans == False:
    print('Hing')