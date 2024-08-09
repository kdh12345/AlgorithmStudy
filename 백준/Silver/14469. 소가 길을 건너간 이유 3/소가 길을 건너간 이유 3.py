import sys
input = sys.stdin.readline

t = int(input())
arr = []
for _ in range(t):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort()

total = arr[0][0]+arr[0][1]

for i in range(1,len(arr)):
    if total > arr[i][0]:
        total += arr[i][1]
    else:
        total = arr[i][0]+arr[i][1]
print(total)
