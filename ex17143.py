import sys

def fish(k):
    for i in range(r):
        if board[i][k]:
            x = board[i][k][2]
            board[i][k] = 0
            return x
    return 0


def get_nxt_loc(i,j,s,dirs):
    if dirs == 0 or dirs == 1:
        cycle = r*2 - 2
        if dirs == 0:
            s += 2*(r-1) - i
        else:
            s += i
        s %= cycle
        if s>=r:
            return (cycle-s,j,0)
        return (s,j,1)
    else:
        cycle = c*2-2
        if dirs == 3:
            s += 2*(c-1)-j
        else:
            s += j
        s %= cycle
        if s >= c:
            return (i,cycle-s,3)
        return (i,s,2)


def move():
    global board
    new_board = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j]:
                ni, nj, nd = get_nxt_loc(i,j,board[i][j][0],board[i][j][1])
                if new_board[ni][nj]:
                    new_board[ni][nj] = max(
                        new_board[ni][nj],
                        (board[i][j][0], nd, board[i][j][2]),
                        key=lambda x: x[2],
                    )
                else:
                    new_board[ni][nj] = (board[i][j][0], nd, board[i][j][2])
    board = new_board

r,c,m = map(int,sys.stdin.readline().split())
board = [[0 for _ in range(c)] for _ in range(r)]

for i in range(m):
    w,h,s,d,z = map(int,sys.stdin.readline().split())
    w -=1
    h -=1
    d -=1
    board[w][h] = (s,d,z)
ans = 0
for i in range(c):
    ans += fish(i)
    move()

print(ans)