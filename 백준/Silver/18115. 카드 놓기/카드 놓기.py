import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int,input().split()))

dq = deque()
first = 1

now = 2

for i in range(n-2,-1,-1):
    cmd = arr[i]
    if cmd == 1:
        dq.appendleft(first)
        first = now
    elif cmd == 2:
        dq.appendleft(now)
    elif cmd == 3:
        dq.append(now)

    now += 1

print(first,end=' ')
for item in dq:
    print(item,end=' ')
