import sys
n=int(sys.stdin.readline().rstrip())
train=[0]+list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline().rstrip())
customer=[0]*50001
dp=[[0]*50001 for _ in range(4)]
for i in range(1,n+1):
    customer[i]=customer[i-1]+train[i]
ans=0
for i in range(1,4):
    for j in range(i*k,n+1):
        if i==1:
            dp[i][j]=max(dp[i][j-1],customer[j]-customer[j-k])
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j-k]+customer[j]-customer[j-k])
        ans=max(ans,dp[i][j])
print(ans)
