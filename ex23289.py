import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

r,c,k = map(int,sys.stdin.readline().split())
temper = [[[0,0,0] for _ in range(c)] for _ in range(r)] #현재 온도, 현재 지점에 들어온 온도, 현재 지점에서 나간 온도
visit = [[0]*c for _ in range(r)]
visit_num = 0

targets = []
heaters = []
for x in range(r):
    temp = list(map(int,sys.stdin.readline().split()))
    for y in range(c):
        if temp[y] == 5:
            targets.append((x,y))
        elif temp[y] > 0:
            if temp[y] == 1:
                typ = 1
            elif temp[y] == 2:
                typ = 3
            elif temp[y] == 3:
                typ = 0
            else:
                typ = 2
            heaters.append((x,y,typ))

w = int(sys.stdin.readline().rstrip())
wall_board = [[[False]*4 for _ in range(c)] for _ in range(r)]
for _ in range(w):
    x,y,t = map(int,sys.stdin.readline().split())
    x -= 1
    y -= 1
    if t == 0:
        wall_board[x][y][0] = True
        wall_board[x-1][y][2] = True
    else:
        wall_board[x][y][1] = True
        wall_board[x][y+1][3] = True


def chk_targets():
    for x,y in targets:
        if temper[x][y][0] < k:
            return False
    return True

def set_temper():
    global temper

    for x in range(r):
        for y in range(c):
            if temper[x][y][0] == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if point_valid(nx,ny,(d+2)%4,False) and temper[x][y][0] > temper[nx][ny][0]:
                    temper[nx][ny][1] += (temper[x][y][0] - temper[nx][ny][0]) //4
                    temper[x][y][2] += (temper[x][y][0] - temper[nx][ny][0]) //4

    for x in range(r):
        for y in range(c):
            temper[x][y][0] += temper[x][y][1] - temper[x][y][2]
            temper[x][y][1] = temper[x][y][2] = 0

    for x in range(r):
        for y in range(c):
            if x == 0 or y == 0 or x == r-1 or y == c-1:
                if temper[x][y][0] > 0:
                    temper[x][y][0] -= 1

def spread_heat():
    global temper,visit,visit_num

    for sx,sy,typ in heaters:
        visit_num += 1
        sx += dx[typ]
        sy += dy[typ]

        q = deque()
        q.append([sx,sy])
        visit[sx][sy] = visit_num

        temper[sx][sy][0] += 5

        for amount in range(4,0,-1):
            if len(q) == 0:
                break

            q_len= len(q)
            for idx in range(q_len):
                x,y = q.popleft()
                nx = x + dx[typ] + dx[(typ-1)%4]
                ny = y + dy[typ] + dy[(typ-1)%4]
                if point_valid(nx,ny,(typ+2)%4) and not wall_board[x][y][(typ-1)%4]:
                    temper[nx][ny][0] += amount
                    visit[nx][ny] = visit_num
                    q.append([nx,ny])

                nx = x + dx[typ]
                ny = y + dy[typ]
                if point_valid(nx,ny,(typ+2)%4):
                    temper[nx][ny][0] += amount
                    visit[nx][ny] = visit_num
                    q.append([nx,ny])

                nx = x + dx[typ] + dx[(typ+1)%4]
                ny = y + dy[typ] + dy[(typ+1)%4]

                if point_valid(nx,ny,(typ+2)%4) and not wall_board[x][y][(typ+1)%4]:
                    temper[nx][ny][0] += amount
                    visit[nx][ny] = visit_num
                    q.appendleft([nx,ny])

def point_valid(x,y,type,flag=True):
    if x<0 and y<0 or x>=r or y>=c:
        return False
    elif wall_board[x][y][type] == True:
        return False
    elif flag==True and visit[x][y] == visit_num:
        return False
    return True


answer=0
while True:
    spread_heat()
    set_temper()
    answer+=1
    if chk_targets():
        print(answer)
        break
    if answer == 100:
        print(answer+1)
        break