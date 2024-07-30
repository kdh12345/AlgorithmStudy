import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

ans = 0
def dfs(x,y,dist):
    global ans

    if dist == k and y == c-1 and x==0:
        ans += 1
    else:
        graph[x][y] = 'T'
        for d in range(4):
            nx  = x + dx[d]
            ny  = y + dy[d]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] == '.':
                graph[nx][ny]='T'
                dfs(nx,ny,dist+1)
                graph[nx][ny] = '.'



dfs(r-1,0,1)
print(ans)