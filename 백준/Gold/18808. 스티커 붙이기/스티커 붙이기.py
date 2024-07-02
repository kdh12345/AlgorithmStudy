import sys
from collections import deque

def rotate(origin):
    new_r = len(origin[0])
    new_c = len(origin)
    new_sticker = [[0 for _ in range(new_c)] for _ in range(new_r)]

    q = deque()
    for i in range(len(origin)):
        for j in range(len(origin[0])):
            q.append(origin[i][j])

    for j in range(new_c-1,-1,-1):
        for i in range(new_r):
            new_sticker[i][j] = q.popleft()
    return new_sticker

def can_put(r_s,c_s,now_sticker):
    global board
    stick_r_idx = 0
    for r in range(r_s,r_s+len(now_sticker)):
        stick_c_idx = 0
        for c in range(c_s,c_s+len(now_sticker[0])):
            if r <0 or r>=n or c<0 or c>=m:
                return False
            if now_sticker[stick_r_idx][stick_c_idx] == 1 and board[r][c] == 1:
                return False
            stick_c_idx += 1
        stick_r_idx += 1
    return True

def find_pos(now_sticker):
    global board
    for r_s in range(n):
        for c_s in range(m):
            res = can_put(r_s,c_s,now_sticker)
            if res == True:
                return True,r_s,c_s
    return False,-1,-1



n,m,k = map(int,sys.stdin.readline().rstrip().split())

board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(1,k+1):
    r,c = map(int,sys.stdin.readline().rstrip().split())

    sticker = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(r)]

    for d in range(4):
        can_stick = find_pos(sticker)

        if can_stick[0]:
            stick_r_idx = 0
            for i in range(can_stick[1], can_stick[1]+len(sticker)):
                stick_c_idx = 0
                for j in range(can_stick[2],can_stick[2]+len(sticker[0])):
                    if sticker[stick_r_idx][stick_c_idx] == 1:
                        board[i][j] = 1
                    stick_c_idx += 1
                stick_r_idx+=1
            break
        else:
            sticker = rotate(sticker)

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            ans += 1
print(ans)