import sys
input = sys.stdin.readline
from math import lcm

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

leng = lcm(len(s), len(t))

s *= leng // len(s)
t *= leng // len(t)

if s == t:
    print(1)
else:
    print(0)
