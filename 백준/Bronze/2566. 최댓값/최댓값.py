import sys

board = []
for _ in range(9):
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)

ans =0
ax = 0
ay = 0
for x in range(len(board)):
    for y in range(len(board[0])):
        if ans < board[x][y]:
            ans = board[x][y]
            ax = x
            ay = y

ax+=1
ay+=1
print(ans)
print(ax,ay)