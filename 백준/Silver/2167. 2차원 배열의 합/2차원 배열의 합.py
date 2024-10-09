import sys
input = sys.stdin.readline

n,m = map(int,input().split())

numbers = []
for i in range(n):
    arr = list(map(int,input().split()))
    numbers.append(arr)
k = int(input())
do = [list(map(int,input().split())) for _ in range(k)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]+numbers[i-1][j-1]

for _,l in enumerate(do):
    i,j,x,y = l
    ans = dp[x][y] -(dp[x][j-1]+dp[i-1][y])+dp[i-1][j-1]
    print(ans)