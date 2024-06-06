import sys
def sol():
    dp[0][0][1] = 1
    for i in range(2,n):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    for x in range(1,n):
        for y in range(1,n):
            if board[x][y] == 0 and board[x][y-1] == 0 and board[x-1][y] == 0: #diagonal
                dp[1][x][y] = dp[0][x-1][y-1] + dp[1][x-1][y-1] + dp[2][x-1][y-1]

            if board[x][y] == 0: #row col
                dp[0][x][y] = dp[0][x][y-1] + dp[1][x][y-1]
                dp[2][x][y] = dp[2][x-1][y] + dp[1][x-1][y]
    result = sum(dp[i][n-1][n-1] for i in range(3))
    return result


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
ans = sol()
print(ans)