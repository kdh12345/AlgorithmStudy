import sys
import heapq
def dijkstra(start):
    dist=[INF]*(n+1)
    heapq.heappush(q,[0,start])
    dist[start]=0
    while q:
        d,now=heapq.heappop(q)
        for nd,next_now in route[now]:
            nd+=d
            if nd<dist[next_now]:
                dist[next_now]=nd
                heapq.heappush(q,[nd,next_now])
    return dist
INF=int(1e9)
n,m,x=map(int,sys.stdin.readline().split())
route=[[]*n for _ in range(n+1)]

q=[]
for _ in range(m):
    s,e,t=map(int,sys.stdin.readline().split())
    route[s-1].append([t,e-1])
answer=[0]*n
for i in range(n):
    d=dijkstra(i)
    answer[i]+=d[x-1] # 끝점까지 가는 최단 시간 경로
    d=dijkstra(x-1)
    answer[i]+=d[i] # 다시 시작점으로 돌아오는 최단 시간 경로
ans=max(answer)
print(ans)