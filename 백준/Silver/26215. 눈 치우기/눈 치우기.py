import sys
import heapq

n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
if n==1:
    if arr[0]>1440:
        print(-1)
        exit(0)
    else:
        print(arr[0])
        exit(0)

ans = 0
h = []
for item in arr:
    if item > 1440:
        print(-1)
        exit(0)
    else:
        heapq.heappush(h,-item)
while len(h) > 1:
    max_val = -heapq.heappop(h)
    sec_val = -heapq.heappop(h) if h else 0

    heapq.heappush(h,-(max_val-sec_val))
    ans += sec_val

ans += -heapq.heappop(h) if h else 0
if ans > 1440:
    print(-1)
else:
    print(ans)