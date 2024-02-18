import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
go = dict()
def dice_game(arr):
    visit = [-1]*101
    dq = deque([1])
    visit[1] = 0
    while dq:
        cur = dq.popleft()
        if cur == 100:
            return visit[100]
        for d in range(1,7): # dice
            next = cur + d
            if next < 0 or next>100:
                break
            if next in go:
                next = go[next]
            if visit[next] >= 0:
                continue
            visit[next] = visit[cur] + 1 # go
            dq.append(next)
# ladder
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    go[x] = y

# snake
for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    go[u] = v

ans = dice_game(go)
print(ans)