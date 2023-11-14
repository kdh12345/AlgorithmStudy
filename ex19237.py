import sys
n,m,k = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

directions = list(map(int,sys.stdin.readline().split()))

smell = [[[0,0]] * n for _ in range(n)]

priorities = [[] for _ in range(m)]
for i in range(m):
     for j in range(4):
        priorities[i].append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def update_smell():

    for x in range(n):
        for y in range(n):
            if smell[x][y][1] > 0:
                smell[x][y][1] -= 1
            if arr[x][y] != 0:
                smell[x][y] = [arr[x][y], k]

def mov():
    new_arr = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                direction = directions[arr[x][y]-1]
                find = False
                for idx in range(4):
                    nx = x + dx[priorities[arr[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[priorities[arr[x][y] - 1][direction - 1][idx] - 1]
                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][1] == 0:
                            directions[arr[x][y] - 1] = priorities[arr[x][y] - 1][direction - 1][idx]

                            # 만약 이미 다른 상어 존재 번호가 낮은 상어 들어가도록
                            if new_arr[nx][ny] == 0:
                                new_arr[nx][ny] = arr[x][y]
                            else:
                                new_arr[nx][ny] = min(new_arr[nx][ny],arr[x][y])
                            find = True
                            break
                if find == True:
                    continue
                for idx in range(4):
                    nx = x + dx[priorities[arr[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[priorities[arr[x][y] - 1][direction - 1][idx] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == arr[x][y]: # 자신의 냄새 o
                            directions[arr[x][y] - 1] = priorities[arr[x][y] - 1][direction - 1][idx]
                            new_arr[nx][ny] = arr[x][y]
                            break
    return new_arr

time = 0
while True:
    update_smell()
    new_arr = mov()
    arr = new_arr
    time+=1

    chk = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                chk = False

    if chk:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
