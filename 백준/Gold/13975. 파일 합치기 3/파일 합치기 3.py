import sys
import heapq

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int,sys.stdin.readline().split()))
    heapq.heapify(arr)
    ans = 0
    while len(arr) > 1:
        a = heapq.heappop(arr) #30
        b = heapq.heappop(arr) #30
        ans = ans+a+b
        heapq.heappush(arr,a+b)
    print(ans)
