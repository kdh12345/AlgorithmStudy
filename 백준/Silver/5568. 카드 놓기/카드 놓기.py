import sys
from itertools import permutations
arr = []
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    arr.append(num)

permu = list(permutations(arr,k))
res = []
for p in permu:
    word = ''
    for item in p:
        word+=str(item)
    res.append(word)

ans = len(list(set(res)))
print(ans)