import sys
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(sx,sy):

    answer = 0
    dq = deque()
    dq.append([sx,sy,board[sx][sy]])
    chk.append(board[sx][sy])
    while dq:
        x,y,s = dq.popleft()
        answer = max(answer,len(s))

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<r and 0<=ny<c:
                if board[nx][ny] not in s:
                    ns = s + board[nx][ny]
                    if ns not in chk[nx][ny]:
                        chk[nx][ny].add(ns)
                        dq.append([nx,ny,ns])
    return answer
r,c = map(int,sys.stdin.readline().split())
board = []
for _ in range(r):
    arr = list(sys.stdin.readline().strip())
    board.append(arr)
chk = [[set() for _ in range(c)] for _ in range(r)]
ans = 0

ans = bfs(0,0)
print(ans)
