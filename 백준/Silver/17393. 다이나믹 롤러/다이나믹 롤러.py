import sys
input = sys.stdin.readline
from bisect import bisect_right

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = []
for i, a in enumerate(a):
    tmp = bisect_right(b,a)-i-1
    ans.append(tmp)
print(*ans)