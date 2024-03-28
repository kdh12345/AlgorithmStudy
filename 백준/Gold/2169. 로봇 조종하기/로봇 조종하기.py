import sys
from collections import deque

dx = [0,0,1]
dy = [-1,1,0]
n,m = map(int,sys.stdin.readline().split())
board = []

for i in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)

for i in range(1,m):
     board[0][i] += board[0][i-1]

for i in range(1,n):
    lr = board[i][:]
    rl = board[i][:]

    # l -> r
    for j in range(m):
        if j == 0:
            lr[j] += board[i-1][j]
        else:
            lr[j] += max(board[i-1][j],lr[j-1])

    # r -> l
    for j in range(m-1,-1,-1):
        if j == m-1:
            rl[j] += board[i-1][j]
        else:
            rl[j] += max(board[i-1][j], rl[j+1])

    for j in range(m):
        board[i][j] = max(lr[j],rl[j])

ans = board[n-1][m-1]
print(ans)