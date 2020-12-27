import sys
n=int(sys.stdin.readline().rstrip())
dp=[[0]*10 for _ in range(1001)]
for i in range(10):
    dp[1][i]=1
for i in range(2,n+1):
    for now in range(10):
        for prev in range(now,10):
            dp[i][now]+=dp[i-1][prev]%10007

ans=0
for i in range(10):
    ans=(ans+dp[n][i])%10007
print(ans)