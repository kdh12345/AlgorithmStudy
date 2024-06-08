import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    number = int(sys.stdin.readline().rstrip())
    arr.append(number)


arr.sort(reverse=True)

res = []
for i in range(len(arr)):
    diff = arr[i]-((i+1)-1)
    if diff <= 0:
        continue
    res.append(diff)

ans = sum(res)
print(ans)