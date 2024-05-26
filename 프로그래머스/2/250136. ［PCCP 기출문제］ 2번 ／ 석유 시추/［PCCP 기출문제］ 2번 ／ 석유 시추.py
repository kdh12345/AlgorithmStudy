from collections import deque
def bfs(a,b,visit,land,r,c,res):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    cnt = 0
    visit[a][b] = 1
    q = deque()
    q.append((a,b))
    min_y = b
    max_y = b
    while q:
        x,y = q.popleft()
        min_y = min(min_y,y)
        max_y = max(max_y,y)
        cnt += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<r and 0<=ny<c:
                if visit[nx][ny] == 0 and land[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
    for i in range(min_y,max_y+1):
        res[i] += cnt
    return res
def solution(land):
    answer = 0
    r = len(land)
    c = len(land[0])
    
    
    res = [0 for i in range(c+1)]
    visit=[[0 for i in range(c)] for j in range(r+1)]
    result = []
    for i in range(r):
        for j in range(c):
            if visit[i][j] == 0 and land[i][j] == 1:
                result= bfs(i,j,visit,land,r,c,res)
    answer = max(result)
    return answer