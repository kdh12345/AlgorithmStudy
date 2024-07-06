import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()

    for i in range(n):
        if parents[i] == -1:
            ans[i] = 0
            q.append(i)

    while q:
        cur = q.popleft()

        for child in graph[cur]:
            if ans[child] == -1:
                ans[child] = ans[cur] + 1
                q.append(child)

n = int(input())

graph = [[] for _ in range(n)]

tmp = [[] for _ in range(n)]

graph_siz = [0]*n

parents = [-1]*n

ans = [-1]*n

for _ in range(n):
    s,e = map(int,input().split())
    s-=1
    e-=1
    graph[s].append(e)
    tmp[s].append(e)
    graph_siz[s] += 1
    graph[e].append(s)
    tmp[e].append(s)
    graph_siz[e] += 1


while True:
    flag = True
    for i in range(n):
        if graph_siz[i] == 1:
            parent = tmp[i].pop()
            parents[i] = parent
            tmp[parent].remove(i)
            graph_siz[i] = 0
            graph_siz[parent] -= 1
            flag = False
    if flag == True:
        break


bfs()

print(*ans)
