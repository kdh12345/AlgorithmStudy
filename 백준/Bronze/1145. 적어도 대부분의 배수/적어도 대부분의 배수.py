import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))
arr.sort()

ans = arr[0]
while True:
    cnt = 0
    for item in arr:
        if ans % item == 0:
            cnt += 1
    if cnt >= 3:
        break
    ans += 1
print(ans)