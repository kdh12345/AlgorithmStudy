import sys
n,m,b = map(int,sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

height = 0
ans    = 1000000000000000000000000000000
for h in range(257):
    bot = 0
    top = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] < h:
                bot += h-board[x][y]
            elif board[x][y] > h:
                top += board[x][y] - h
    inventory = top + b
    if inventory < bot:
        continue
    times = bot + top * 2
    if ans >= times:
        ans = times
        height = h

print(ans,height)
