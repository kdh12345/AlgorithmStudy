import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    global group_number

    visit[x][y] = 1
    q = deque()
    q.append((x,y))

    area = 1
    group = []
    group.append((x,y))
    while q:
        px,py = q.popleft()
        wall = arr[px][py]
        for i in range(4):
            if wall >= binary[i]:
                wall -= binary[i]
            else:
                nx = px+dx[i]
                ny = py+dy[i]
                if 0<=nx<m and 0<=ny<n and visit[nx][ny] == 0:
                    area += 1
                    q.append((nx,ny))
                    visit[nx][ny] = 1
                    group.append((nx,ny))
    for i,j in group:
        room_info[i][j].append(group_number)
        room_info[i][j].append(area)
    group_number += 1
    return area

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

binary = [8,4,2,1] # south,east, north, west

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
visit = [[0 for _ in range(n)] for _ in range(m)]
# land num, size
room_info = [[[] for _ in range(n)] for _ in range(m)]

group_number = 0
max_area = 0
for x in range(m):
    for y in range(n):
        if visit[x][y] == 0:
            max_area = max(max_area,bfs(x,y))
            cnt += 1

maybe_max_val = 0
for x in range(m):
    for y in range(n):
        for d in range(4):
            if arr[x][y] >= binary[d]:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<m and 0<=ny<n:
                    if room_info[x][y][0] != room_info[nx][ny][0]:
                        maybe_max_val = max(maybe_max_val, room_info[x][y][1]+room_info[nx][ny][1])

print(cnt)
print(max_area)
print(maybe_max_val)