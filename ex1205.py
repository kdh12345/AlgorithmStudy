import sys

n,score, p = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
ans = n+1
if n == 0:
    print(1)
else:
    if n == p and arr[-1] >= score:
        print(-1)
    else:
        for i in range(n):
            if arr[i] <= score:
                ans = i+1
                break

        print(ans)