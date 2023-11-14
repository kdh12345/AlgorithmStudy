import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]
board = []
dq = deque()

def bfs(rx,ry,bx,by):
    dq = deque()
    dq.append([rx,ry,bx,by])
    visit = []
    visit.append([rx,ry,bx,by])
    cnt = 0
    while dq:
        for i in range(len(dq)):
            rx,ry,bx,by = dq.popleft()
            if cnt > 10:
                return 0
            if board[rx][ry] == 'O':
                return 1
            for d in range(4):
                nrx,nry = rx,ry
                while True:
                    nrx += dx[d]
                    nry += dy[d]
                    if board[nrx][nry] == '#':
                        nrx -= dx[d]
                        nry -= dy[d]
                        break
                    if board[nrx][nry] == 'O':
                        break
                nbx,nby = bx,by
                while True:
                    nbx += dx[d]
                    nby += dy[d]
                    if board[nbx][nby] == '#':
                        nbx -= dx[d]
                        nby -= dy[d]
                        break
                    if board[nbx][nby] == 'O':
                        break
                if board[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx-rx) + abs(nry- ry) > abs(nbx- bx) + abs(nby - by):
                        nrx -= dx[d]
                        nry -= dy[d]
                    else:
                        nbx -= dx[d]
                        nby -= dy[d]
                if [nrx,nry,nbx,nby] not in visit:
                    dq.append([nrx,nry,nbx,nby])
                    visit.append([nrx,nry,nbx,nby])
        cnt+=1
    return 0

for i in range(n):
    word = sys.stdin.readline().strip()
    board.append(word)


rx = 0
ry = 0
bx = 0
by = 0
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == 'R':
            rx = x
            ry = y
        elif board[x][y] == 'B':
            bx = x
            by = y

answer = bfs(rx,ry,bx,by)
print(answer)