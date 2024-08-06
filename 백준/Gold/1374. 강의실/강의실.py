import heapq
import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[1])

h = []
h.append(arr[0][2])
ans = 1
for i in arr[1:]:
    while h:
        if h[0] > i[1]:
            heapq.heappush(h, i[2])
            break
        else:
            heapq.heappop(h)
    ans = max(ans,len(h))
print(ans)