import sys

arr = []
for _ in range(28):
    number = int(sys.stdin.readline().rstrip())
    arr.append(number)

arr.sort()
last = arr[-1]
arr = set(arr)


res = []
for i in range(1,31):
    if i not in arr:
        res.append(i)

res.sort()
f = res[0]
s = res[1]
print(f)
print(s)