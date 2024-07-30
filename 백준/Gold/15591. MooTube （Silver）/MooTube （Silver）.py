from collections import deque
def bfs(usado,start):
    q = deque()
    q.append(start)
    visit = [0]*(n+1)
    res = 0
    while q:
        cur = q.popleft()
        for nxt, k in node[cur]:
            if visit[nxt] == 0 and nxt!=start:
                if k >= usado:
                    res += 1
                    q.append(nxt)
                    visit[nxt] = 1
    return res


n,q = map(int,input().split())

node = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c= map(int,input().split())
    node[a].append((b,c))
    node[b].append((a,c))

for _ in range(q):
    k,v = map(int,input().split())

    ans = bfs(k,v)
    print(ans)