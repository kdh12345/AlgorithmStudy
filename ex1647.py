import sys
n,m=map(int,sys.stdin.readline().split())
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,x,y):
    x=find_parent(parent,x)
    y=find_parent(parent,y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
res=0
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
graph=[]
for _ in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    graph.append([z,x,y])
graph.sort()
last=0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
for g in graph:
    cost,a,b=g
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        res+=cost
        last=cost
print(res-last)
