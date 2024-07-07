from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
max_val = 0
for i in range(n):
    combi = list(combinations(arr[i],3))
    tmp = 0
    for item in combi:
        tmp = max(tmp,sum(item)%10)
    if max_val <= tmp:
        max_val = tmp
        ans = i+1
print(ans)