import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            arr[i][j] = 0

for _ in range(m):
    a,b = map(int,input().split())
    arr[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

for i in range(1,n+1):
    cnt = -1
    for j in range(1,n+1):
        if arr[i][j] == 0 and arr[j][i] == 0: #관게가 없는 케이스
            cnt += 1
    print(cnt)