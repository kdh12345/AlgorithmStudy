import sys
input = sys.stdin.readline

N,m,M,T,R = map(int,input().split())

ans = 0
cur = m
if m+T > M:
    print(-1)
else:
    while True:
        if N == 0:
            break
        if cur + T <= M:
            cur += T
            N -= 1
        elif cur - R < m:
            cur = m
        elif cur - R >= m:
            cur -= R
        ans += 1
    print(ans)