import re
import sys
input = sys.stdin.readline

n = str(input().rstrip())
pattern = re.compile("(100+1+|01)+")
ans = bool(pattern.fullmatch(n))

if ans == True:
    print('SUBMARINE')
else:
    print('NOISE')