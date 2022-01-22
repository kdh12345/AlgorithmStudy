import sys
from itertools import combinations
numbers=[]
for _ in range(9):
    num=int(sys.stdin.readline().rstrip())
    numbers.append(num)
candi=list(combinations(numbers,7))
res=[]
for c in candi:
    total=0
    for item in c:
        total+=item
    if total==100:
        res.append(c)
for item in res:
    for num in item:
        print(num)