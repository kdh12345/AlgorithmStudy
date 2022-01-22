import sys
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m,k=map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
visit_num = 0

dice={'top' : 1, 'bottom' : 6,'up' : 2,'down' : 5,'left' : 4,'right' : 3}


def cnt_block(sx,sy):
    global visit, visit_num
    visit_num += 1

    target = board[sx][sy]
    visit[sx][sy] = visit_num
    q = deque()
    q.append([sx,sy])
    cnt = 0

    while q:
        x,y = q.popleft()
        cnt +=1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny] != visit_num and board[nx][ny] == target:
                    visit[nx][ny] = visit_num
                    q.append([nx,ny])
    return target, cnt

def mov_dice(x,y,d):
    global dice
    nx = x + dx[d]
    ny = y + dy[d]

    if nx<0 or nx>=n or ny<0 or ny>=m:
        d = (d+2)%4 #반대방향
        nx = x + dx[d]
        ny = y + dy[d]

    if d==0:
        temp = dice['top']
        dice['top'] = dice['down']
        dice['down'] = dice['bottom']
        dice['bottom'] = dice['up']
        dice['up'] = temp
    elif d == 1:
        temp = dice['top']
        dice['top'] = dice['left']
        dice['left'] = dice['bottom']
        dice['bottom'] = dice['right']
        dice['right'] = temp
    elif d == 2:
        temp = dice['top']
        dice['top'] = dice['up']
        dice['up'] = dice['bottom']
        dice['bottom'] = dice['down']
        dice['down'] = temp
    elif d == 3:
        temp = dice['top']
        dice['top'] = dice['right']
        dice['right'] = dice['bottom']
        dice['bottom'] = dice['left']
        dice['left'] = temp
    return nx,ny,d

def rotate_dice(x,y,d):
    a = dice['bottom']
    b = board[x][y]
    if a > b:
        d = (d+1)%4
    elif a < b:
        d = (d+3)%4
    return d




x=0
y=0
d = 1
score = 0
for _ in range(k): #k번 순회
    x,y,d = mov_dice(x,y,d)
    d = rotate_dice(x,y,d)
    target, cnt = cnt_block(x,y)
    score += target*cnt

print(score)

