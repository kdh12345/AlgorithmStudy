
n = int(input())
t = [0 for _ in range(n+1)]
p = [0 for _ in range(n+1)]

for i in range(1,n+1):
    t[i],p[i] = map(int,input().split())

dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i] = max(dp[i],dp[i-1]) # 이전까지의 최댓값
    fin_day = i-1+t[i] # 당일 포함
    if fin_day <= n: # 최종일 안에 일이 끝나는 경우
        dp[fin_day] = max(dp[fin_day],dp[i-1]+p[i])

ans = max(dp)
print(ans)