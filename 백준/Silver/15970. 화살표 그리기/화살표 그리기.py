import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]
for _ in range(n):
    p,c = map(int,input().split())
    arr[c-1].append(p)

ans = 0
for item in arr:
    item.sort()
    if len(item) <= 1:
        continue
    ans += abs(item[0] - item[1]) + abs(item[-1]-item[-2]) # point 2
    for j in range(1,len(item)-1): # point 3 이상
        ans += min(abs(item[j]-item[j-1]), abs(item[j] - item[j+1]))

print(ans)
