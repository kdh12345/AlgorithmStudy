import sys
n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())
vip=[0]*41
for i in range(1,m+1):
    num=int(sys.stdin.readline().rstrip())
    vip[i]=num
dp=[0]*41
dp[0]=1
dp[1]=1
# 1~n 까지 계산해보니 피보나치
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
# 문제예시를 계산 dp[3]*dp[2]*dp[2]=12
ans=1
for i in range(1,m+1):
    ans*=dp[vip[i]-vip[i-1]-1]
ans*=dp[n-vip[m]] # 마지막은 인덱스가 vip번호 왼쪽이므로
print(ans)
