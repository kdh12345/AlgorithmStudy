import sys
import heapq
n = int(sys.stdin.readline().rstrip())

h = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0] == 0:
        if len(h) == 0:
            print(-1)
        else:
            number = -heapq.heappop(h)
            print(number)
    elif arr[0] != 0:
        for i in range(1,len(arr)):
            heapq.heappush(h,-arr[i])