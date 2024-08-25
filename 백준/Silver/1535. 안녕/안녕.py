import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
J = list(map(int,input().split()))

L = [0]+L
J = [0]+J

dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if L[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])

ans = dp[n][99]
print(ans)