import sys
input = sys.stdin.readline

n,m = map(int,input().split())
if n == 0:
    print(0)
    exit(0)
arr = list(map(int,input().split()))

ans = 1
total = 0
for item in arr:
    if total + item > m:
        total = item
        ans+=1
    else:
        total+=item

print(ans)