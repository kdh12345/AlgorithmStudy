import heapq
n = int(input())

arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort()
h = []
ans = 1
heapq.heappush(h,arr[0][1])
for i in range(1,len(arr)):
    if arr[i][0] >= h[0]:
        heapq.heappop(h)
    else:
        ans+=1
    heapq.heappush(h,arr[i][1])

print(ans)