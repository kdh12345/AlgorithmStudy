import sys
n = int(sys.stdin.readline().rstrip())
dp = [0]*1000001

dp[1] = 0
dp[2] = 1
dp[3] = 2

for i in range(4,n+1):
    dp[i] = ( (dp[i-2]+dp[i-1])*(i-1) ) % 1000000000
print(dp[n])