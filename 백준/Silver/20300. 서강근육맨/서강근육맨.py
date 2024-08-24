import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

if len(arr) % 2 == 1:
    s = 0
    e = len(arr) -2
    ans = 0
    total = 0
    while s < e:
        total = arr[s]+arr[e]
        if ans < total:
            ans = total
        s += 1
        e -= 1
    if arr[-1] > ans:
        ans = arr[-1]
    print(ans)
else:
    s = 0
    e = len(arr) - 1
    ans = 0
    total = 0
    while s < e:
        total = arr[s] + arr[e]
        if ans < total:
            ans = total
        s += 1
        e -= 1
    print(ans)