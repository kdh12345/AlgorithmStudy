import sys
import math

m = int(sys.stdin.readline())
stone = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
n = sum(stone)

total = math.comb(n,k)

sc = 0
for s in stone:
    sc += math.comb(s,k)

ans = sc/total
print(ans)