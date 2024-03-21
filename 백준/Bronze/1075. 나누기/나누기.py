import sys

n = (int(sys.stdin.readline().rstrip())//100) * 100
f = int(sys.stdin.readline().rstrip())

for i in range(100):
    if n%f == 0:
        tmp = str(n)
        ans = tmp[-2:]
        print(ans)
        exit(0)
    n = n+1
