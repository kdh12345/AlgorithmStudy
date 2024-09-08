import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

total = sum(arr[:m])
ans = sum(arr[:m])
for i in range(n-m):
    total -= arr[i]
    total += arr[i+m]
    ans = max(ans,total)
print(ans)