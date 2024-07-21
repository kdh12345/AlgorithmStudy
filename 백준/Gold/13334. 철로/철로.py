import sys
import heapq

n = int(sys.stdin.readline().strip())

loc = []
for _ in range(n):
    h,o = map(int,sys.stdin.readline().strip().split())
    loc.append((min(h,o),max(h,o)))

d = int(sys.stdin.readline().strip())

loc.sort(key=lambda x:(x[1],x[0]))

h = []
max_cnt = 0

for l in loc:
    s,e = l
    heapq.heappush(h,s)
    line_start = e - d
    while len(h) >0 and h[0]<line_start:
        heapq.heappop(h)
    max_cnt = max(max_cnt,len(h))
print(max_cnt)