import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int,sys.stdin.readline().split()))
arr = sorted(lst)

p = []
for i in range(n):
    p.append(arr.index(lst[i]))
    arr[arr.index(lst[i])] = - 1

for i in range(n):
    print(str(p[i]) , end = ' ')
