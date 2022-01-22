import sys
INF=int(1e9)
v,e=map(int,sys.stdin.readline().split())
graph=[[INF]*(v+1) for _ in range(v+1)]
for i in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a][b]=c

for i in range(1,v+1):
    for j in range(1,v+1):
        if a==b:
            graph[a][b]=0

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
ans=INF
for a in range(1,v+1):
    ans=min(ans,graph[a][a]) #최소 사이클
if ans==INF:
    print(-1)
else:
    print(ans)