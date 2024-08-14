import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x,y):
    global visit,dx,dy,board
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<h and 0<=ny<w:
            if visit[nx][ny] == 0 and board[nx][ny] == '#':
                visit[nx][ny] = 1
                dfs(nx,ny)

t = int(input())
for _ in range(t):
    h,w = map(int,input().split())
    board = []
    for i in range(h):
        arr = list(sys.stdin.readline().strip())
        board.append(arr)
    visit = [[0]*(w+1) for _ in range(h+1)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and board[i][j] == '#':
                visit[i][j] = 1
                dfs(i,j)
                cnt+=1
    print(cnt)
