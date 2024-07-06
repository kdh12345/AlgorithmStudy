import sys

n = int(sys.stdin.readline())
m = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)
ans = - 1

for i in range(n-2):
    if m[i] < m[i+1]+m[i+2]:
        ans = m[i] + m[i+1] + m[i+2]
        break

print(ans)