import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)]
ans = 0

def dfs(x,y):
    global ans
    visit[y][x] = 1

    cycle.append((x,y))

    if board[y][x] == 'U' and y > 0: #up
        y -= 1
    elif board[y][x] == 'D' and y < n-1: #down
        y += 1
    elif board[y][x] == 'L' and x > 0: #left
        x -= 1
    elif board[y][x] == 'R' and x < m-1: #right
        x += 1

    if visit[y][x] == 1:
        if (x,y) in cycle:
            ans += 1
    else:
        dfs(x,y)

for i in range(m):
    for j in range(n):
        if visit[j][i] == 0:
            cycle = []
            dfs(i,j)
print(ans)