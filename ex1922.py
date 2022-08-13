import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent=[0]*(n+1)
result = 0

for i in range(1,n+1):
    parent[i] = i

graph = []
for _ in range(m):
    a,b,cost = map(int,sys.stdin.readline().split())
    graph.append((cost,a,b))

graph.sort()

for g in graph:
    cost,a,b = g
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)