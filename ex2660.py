import sys
n=int(sys.stdin.readline().rstrip())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
while True:
    a,b=map(int,sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    graph[a][b]=1
    graph[b][a]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

min_val=INF
for i in range(1,n+1):
    min_val=min(min_val,max(graph[i][1:]))


candi=[]
for i in range(1,n+1):
    if min_val==max(graph[i][1:]):
        candi.append(i)

candi.sort()
print(min_val,len(candi))
print(' '.join(map(str,candi)))