import sys
import heapq
n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    arr.append([a,b])
arr.sort(key=lambda x:(x[0],x[1]))
end=arr[0][1]
q=[]
heapq.heappush(q,end)
for i in range(1,n):
    if arr[i][0]<q[0]:
        heapq.heappush(q,arr[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q,arr[i][1])
