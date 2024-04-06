import sys
n = int(sys.stdin.readline().rstrip())

arr = []
for i in range(n):
    num = list(map(int,sys.stdin.readline().split()))
    arr.append(num)


for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            arr[i][0] += arr[i-1][0]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])

ans = max(arr[n-1])
print(ans)
