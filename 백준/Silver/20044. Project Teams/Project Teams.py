import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

s = 0
e = len(arr) - 1

ans = int(1e9)
while s < e:
    total = 0
    if s < len(arr) and e >= 0:
        total = arr[s] + arr[e]
    ans = min(ans,total)
    s+=1
    e-=1

print(ans)