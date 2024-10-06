import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
def div(x):
    max_x = arr[0]
    min_x = arr[0]
    cnt = 1
    for i in range(1,n):
        max_x = max(max_x,arr[i])
        min_x = min(min_x,arr[i])
        diff = max_x - min_x
        if diff > x: # 구간 증가
            cnt += 1
            max_x = arr[i]
            min_x = arr[i]
    return cnt
s = 0
e = max(arr)
ans = 0
while s <= e:
    mid = (s+e) // 2
    if div(mid) <= m: # target <= m 이면 감소
        e = mid - 1
        ans = mid
    else: # 증가
        s = mid + 1
print(ans)