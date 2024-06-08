import sys

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

f =[[0]*n for _ in range(n)]

for k in range(n):
    for x in range(n):
        for y in range(n):
            if x==y:
                continue
            if arr[x][y] == 'Y' or (arr[x][k] == 'Y' and arr[k][y] == 'Y'):
                f[x][y] = 1


ans = 0
for r in f:
    ans = max(ans,sum(r))
print(ans)