import sys, copy
from itertools import combinations
from collections import deque

def bfs():
    c = set()
    ans = 0
    qlen = len(q)
    while qlen:
        x = q.popleft()
        l = list(str(x))
        for i,j in candi:
            s = copy.deepcopy(l)
            tmp_i,tmp_j = s[i],s[j]
            s[i], s[j] = tmp_j, tmp_i
            if s[0] == '0':
                continue
            nx = int(''.join(s))
            if nx not in c:
                ans = max(ans,nx)
                c.add(nx)
                q.append(nx)
        qlen-=1
    return ans

n,k = map(int,sys.stdin.readline().split())
item = [i for i in range(len(str(n)))]
candi = list(combinations(item,2))
q = deque()
q.append(n)
ans = 0
for _ in range(k):
    ans = bfs()

if not ans:
        print(-1)
else:
    print(ans)

