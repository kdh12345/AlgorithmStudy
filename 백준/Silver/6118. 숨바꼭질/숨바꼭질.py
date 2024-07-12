n,m = map(int,input().split())
from collections import deque

visited = [-1 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited[1] = 0

q = deque()
q.append(1)

while q:
    now = q.popleft()
    for i in graph[now]:
        if visited[i] == -1:
            visited[i] = visited[now] + 1
            q.append(i)

dist = 0
target = 0
cnt = 0

for i in range(n+1):
    if dist < visited[i]:
        dist = visited[i]
        target = i
        cnt = 1
    elif visited[i] == dist:
        cnt+=1

print(target,dist,cnt)