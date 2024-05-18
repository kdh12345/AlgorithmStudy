import sys

n,m = map(int,sys.stdin.readline().split())
j = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(j):
    apple = int(sys.stdin.readline().rstrip())
    arr.append(apple)



ans = 0
now = 1
for i in range(len(arr)):
    if now<= arr[i] and now+(m-1) >= arr[i]:
        pass
    elif now > arr[i]: #left
        ans += abs(arr[i]-now)
        now = arr[i]
    else: #right
        ans += arr[i]-(m-1)-now
        now = arr[i]-(m-1)

print(ans)