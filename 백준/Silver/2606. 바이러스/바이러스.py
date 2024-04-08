import sys

n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())

dic = dict()
visit = [0 for _ in range(n+1)]
ans = 0

for _ in range(m):
    a,b= map(int,sys.stdin.readline().split())
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]

    if b in dic:
        dic[b].append(a)
    else:
        dic[b] = [a]

def dfs(u):
    visit[u] = 1
    if u in dic:
        for v in dic[u]:
            if visit[v] == 0:
                dfs(v)

dfs(1)

for i in range(2,n+1):
    if visit[i] == 1:
        ans+=1
print(ans)