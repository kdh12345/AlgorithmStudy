import sys
n,m = map(int,sys.stdin.readline().split())
def dfs(x,y,color):
    visit[x][y] = 1
    cnt = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<m and 0<=ny<n:
            if visit[nx][ny] == 0 and graph[nx][ny] == color:
                visit[nx][ny] = 1
                cnt += dfs(nx,ny,color)
    return cnt

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visit = [[0]*101 for _ in range(102)]
graph = []
for i in range(m):
    arr = list(sys.stdin.readline().strip())
    graph.append(arr)

res = {'W':0,'B':0}
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if visit[i][j] == 0:
            res[graph[i][j]] += dfs(i,j,graph[i][j]) ** 2
ans1 = res['W']
ans2 = res['B']
print(ans1, ans2)