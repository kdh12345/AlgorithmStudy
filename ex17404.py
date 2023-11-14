import sys
n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)


INF = 987654321
ans = INF
for x in range(3):
    dp = [[INF, INF, INF] for _ in range(n+1)]
    dp[0][x] = board[0][x]
    for y in range(1,len(board)):
        dp[y][0] = board[y][0] + min(dp[y-1][1],dp[y-1][2])
        dp[y][1] = board[y][1] + min(dp[y-1][0],dp[y-1][2])
        dp[y][2] = board[y][2] + min(dp[y-1][0],dp[y-1][1])
    for y in range(3):
        if x != y:
            ans = min(ans,dp[n-1][y])
print(ans)