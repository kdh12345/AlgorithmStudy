import sys
from collections import deque

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

n,m,k = map(int,sys.stdin.readline().split())
if n == 1:
    print(0)
    exit(0)
arr = [[5]*n for _ in range(n)]
tree = [[dict() for _ in range(n)] for _ in range(n)]
winter = []
for _ in range(n):
    winter.append(list(map(int,sys.stdin.readline().split())))

for _ in range(m):
    x,y,age = map(int,sys.stdin.readline().split())
    tree[x-1][y-1][age] = 1

while k > 0:

    # spring
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                tmp = dict()
                die = 0
                for age in sorted(tree[x][y].keys()):
                    if age * tree[x][y][age] <= arr[x][y]:
                        tmp[age+1] = tree[x][y][age]
                        arr[x][y] -= age * tree[x][y][age]
                    else: #summer
                        survive = arr[x][y] // age
                        if not survive:
                            die += (age // 2) * tree[x][y][age]
                            continue
                        arr[x][y] -= age * survive
                        tmp[age+1] = survive
                        die += (age//2) * (tree[x][y][age] - survive)
                tree[x][y] = tmp
                arr[x][y] += die
    # autumn
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                num = 0
                for age in tree[x][y].keys():
                    if age % 5 == 0:
                        num += tree[x][y][age]
                if num:
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<n and 0<=ny<n:
                            if 1 not in tree[nx][ny].keys():
                                tree[nx][ny] = num
                            else:
                                tree[nx][ny] += num
    #winter
    for x in range(n):
        for y in range(n):
            arr[x][y] += winter[x][y]
    k-=1

res = 0
for x in range(n):
    for y in range(n):
        res += sum(tree[x][y].values())

print(res)