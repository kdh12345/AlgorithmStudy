from collections import deque
def solution(maps):
    answer = -1
    dq = deque()
    dq.append((0,0))
    visit = [[-1]*len(maps[0]) for _ in range(len(maps))]
    visit[0][0] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    n = len(maps)
    m = len(maps[0])
    while dq:
        x,y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1 and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    dq.append((nx,ny))
                    if nx == n-1 and ny == m-1:
                        answer = visit[nx][ny]
                        return answer
    return answer