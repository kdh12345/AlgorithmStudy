import sys
import heapq

def dijikstra(start):
    h = []
    heapq.heappush(h,[0,start])
    dp = [100000000 for i in range(n + 1)]
    dp[start] = 0
    while h:
        we, nu = heapq.heappop(h)
        for ne, nw in s[nu]:
            wei = we + nw
            if dp[ne] > wei:
                dp[ne] = wei
                heapq.heappush(h,[wei,ne])
    return dp

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n,m,c = map(int,sys.stdin.readline().split())
    start, g, h = map(int,sys.stdin.readline().split())
    s = [[] for i in range(n+1)]
    de = []
    for i in range(m):
        a,b,d = map(int,sys.stdin.readline().split())
        s[a].append([b,d])
        s[b].append([a,d])
    for k in range(c):
        de.append(int(sys.stdin.readline().strip()))

    res_start = dijikstra(start)
    res_g     = dijikstra(g)
    res_h     = dijikstra(h)
    ans = []
    for item in de:
        if res_start[g] + res_g[h] + res_h[item] == res_start[item] or res_start[h] + res_h[g] + res_g[item] == res_start[item]:
            ans.append(item)
    ans.sort()
    for a in ans:
        print(a,end=' ')