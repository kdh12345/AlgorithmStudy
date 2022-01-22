import sys
n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())
def init():
    for i in range(1,n+1):
        parent[i]=i
def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ux=find(x)
    uy=find(y)
    if ux!=uy:
        parent[uy]=ux


parent=[0]*200
init()
for i in range(1,n+1):
    city=list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(city)+1):
        if city[j-1]==1:
            union(i,j)
plan=list(map(int,sys.stdin.readline().split()))
result=set([find(p) for p in plan])
if len(result)==1:
    print('YES')
else:
    print('NO')