import sys

n,m = map(int,sys.stdin.readline().split())
dy = [1,1,1]
dx = [-1,0,1]
 # d 0 1 2
graph = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    graph.append(arr)


def search(y,x,now_d, min_fuel, now_fuel):
    if y == n-1:
        return min(min_fuel,now_fuel)
    for k in range(3):
        if now_d != k:
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<n and 0<=nx<m:

                min_fuel = search(ny, nx, k, min_fuel, now_fuel+graph[ny][nx])
    return min_fuel

min_fuel = int(sys.maxsize)
for i in range(m):
    min_fuel = min(search(0,i,-1,min_fuel,graph[0][i]), min_fuel)

print(min_fuel)

"""dq = deque()
sy = 0
sx = 0
isStart = False
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 1:
            sy = i
            sx = j
            isStart = True
            break
    if isStart == True:
        break
print(sy,sx)
dq.append([sy,sx])

visited = [[0]*m for _ in range(n)]
ans = 0

while dq:
    y,x = dq.popleft()
    for d in range(3):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<n and 0<=nx<m:
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dq.append([ny,nx])
                ans += graph[ny][nx]

print(ans)"""
