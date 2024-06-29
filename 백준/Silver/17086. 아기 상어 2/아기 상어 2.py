from collections import deque

d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
def bfs(ax,ay):
    global a,b,ans
    dq = deque()
    dq.append((ax,ay))
    visit = [[0]*(b+1) for _ in range(a+1)]
    isShark = False
    while dq:
        x,y = dq.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<a and 0<=ny<b and visit[nx][ny] == 0:
                if board[nx][ny] == 0:
                    dq.append((nx,ny))
                    visit[nx][ny] = visit[x][y] + 1
                else:
                    ans = visit[x][y] + 1
                    isShark = True
        if isShark == True:
            break
    return ans


a,b = map(int,input().split())

board = []
for _ in range(a):
    arr = list(map(int,input().split()))
    board.append(arr)

ans = 0
for i in range(a):
    for j in range(b):
        if board[i][j] == 0:
            ans = max(ans,bfs(i,j))

print(ans)