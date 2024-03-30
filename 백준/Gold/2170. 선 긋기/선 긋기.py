import sys

n = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(n):
    a,b= map(int,sys.stdin.readline().split())
    arr.append([a,b])

arr.sort()
ps = arr[0][0]
pe = arr[0][1]

ans = 0
for i in range(1,n):
    s,e= arr[i][0], arr[i][1]

    if s <= pe:
        pe = max(pe,e)
    else:
        ans += pe - ps
        ps,pe = s,e

ans += pe - ps
print(ans)
