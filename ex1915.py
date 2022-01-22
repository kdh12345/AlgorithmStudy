import sys
n,m=map(int,sys.stdin.readline().split())
board=[]
for _ in range(n):
    arr=list(map(int,sys.stdin.readline().rstrip()))
    board.append(arr)

for i in range(1,n):
    for j in range(1,m):
        if board[i][j]==1:
            board[i][j]+=min(board[i][j-1],board[i-1][j],board[i-1][j-1])
ans=0
for r in board:
    ans=max(ans,max(r))
print(ans**2)


