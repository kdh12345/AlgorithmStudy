import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque()

dq.appendleft(n)

for i in range(n-1,0,-1):
    dq.appendleft(i)

    for j in range(i):
        cur = dq.pop()
        dq.appendleft(cur)

print(*dq)