import sys
n=int(sys.stdin.readline().rstrip())
parents=list(map(int,sys.stdin.readline().split()))
del_node=int(sys.stdin.readline().rstrip())
tree={}
for i in range(n):
    if i==del_node or parents[i]==del_node:
        continue
    if parents[i] in tree:
        tree[parents[i]].append(i)
    elif parents[i] not in tree:
        tree[parents[i]]=[i]
leaf=0
q=[]
if -1 in tree:
    q=[-1]
else:
    q=[]
while q:
    node=q.pop()
    if node not in tree:
        leaf+=1
    else:
        q+=tree[node]
print(leaf)