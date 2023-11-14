import sys
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def spread_virus():
    global board,q,c,ans
    cnt = 0
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 0 and c[nx][ny] == -1:
                    c[nx][ny] = c[x][y] + 1
                    cnt = max(cnt,c[nx][ny])
                    q.append((nx,ny))
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0 and c[x][y] == -1:
                cnt = 987654321
    ans = min(ans,cnt)
    return

def virus_put(idx,cnt):
    global board,q,c,ans
    if cnt == m:
        q = deque()
        c = [[-1]*n for _ in range(n+1)]
        for i in range(len(virus)):
            if sel[i] == 1:
                q.append((virus[i][0],virus[i][1]))
                c[virus[i][0]][virus[i][1]] = 0
        spread_virus()
        return
    for i in range(idx,len(virus)):
        if sel[i] == 1:
            continue
        sel[i] = 1
        virus_put(idx+1,cnt+1)
        sel[i] = 0

n,m = map(int,sys.stdin.readline().split())
sel = [ 0 for _ in range(11)]
board = []
for x in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)

virus = []
for x in range(n):
    for y in range(n):
        if board[x][y] == 2:
            virus.append((x,y))
            board[x][y] = 0
ans = 987654321
virus_put(0,0)
if ans == 987654321:
    print(-1)
else:
    print(ans)