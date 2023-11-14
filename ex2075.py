import sys
import heapq
n = int(sys.stdin.readline().rstrip())

h = []
for i in range(n):
    numbers = list(map(int,sys.stdin.readline().split()))

    for num in numbers:
        if len(h) < n:
            heapq.heappush(h,num)
        else:
            if h[0] < num:
                heapq.heappop(h)
                heapq.heappush(h,num)