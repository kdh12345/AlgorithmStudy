import sys
input = sys.stdin.readline

h,w,x,y = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(h+w)]

for i in range(x,h):
    for j in range(y,w):
        arr[i][j] = arr[i][j] - arr[i-x][j-y]

for item in arr[:h]:
    print(*item[:w])