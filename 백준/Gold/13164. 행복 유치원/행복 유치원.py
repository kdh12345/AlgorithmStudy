import sys

n,k= map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
res = []
for i in range(1,len(arr)):
    res.append(arr[i] - arr[i-1])

res.sort(reverse=True)
ans = sum(res[k-1:])# 가장 차이 k개 제외처리
print(ans)