import sys
board = [[0]*100 for _ in range(101)]
n,m = map(int,sys.stdin.readline().split())
for _ in range(n):
    sx,sy,ex,ey = map(int,sys.stdin.readline().split())

    sx-=1
    sy-=1
    ex-=1
    ey-=1
    for i in range(sx,ex+1):
        for j in range(sy,ey+1):
            board[i][j] += 1

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > m:
            ans+=1

print(ans)