import sys
from bisect import bisect_left,bisect_right
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    s1=list(map(int,sys.stdin.readline().split()))
    m=int(sys.stdin.readline().rstrip())
    s2=list(map(int,sys.stdin.readline().split()))
    s1.sort()
    for item in s2:
        left=bisect_left(s1,item)
        right=bisect_right(s1,item)
        count=right-left
        if count==0:
            print(0)
        else:
            print(1)