import sys

n,l = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
for h in arr:
    if l>=h:
        l+=1
print(l)