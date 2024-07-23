def find(x,cnt):
    global ans
    if x < 500:
        return
    if cnt == n:
        ans += 1
        return
    x -= k
    for i in range(n):
        if visit[i] == 0:
            visit[i]= 1
            find(x+kits[i],cnt+1)
            visit[i] = 0

import sys
n,k = map(int,sys.stdin.readline().split())
kits = list(map(int,sys.stdin.readline().split()))

ans = 0
visit = [0]*n
find(500,0)
print(ans)