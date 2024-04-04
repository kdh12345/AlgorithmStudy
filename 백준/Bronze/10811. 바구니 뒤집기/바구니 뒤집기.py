import sys
n,m = map(int,sys.stdin.readline().split())

arr = []
for i in range(1,n+1):
    arr.append(i)

for _ in range(m):
    a,b= map(int,sys.stdin.readline().split())
    a-=1
    b-=1
    tmp = arr[a:b+1]
    tmp = list(reversed(tmp))
    for i in range(a,b+1):
        arr[i] = tmp[0]
        if len(tmp) > 0:
            tmp.pop(0)

for item in arr:
    print(item,end=' ')