import sys
from collections import Counter
n,m = map(int,sys.stdin.readline().split())
arr = []
word_set = set()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        arr.append(word)
        word_set.add(word)

cnt = Counter(arr)
result = []
for w in word_set:
    result.append([cnt[w], len(w), w])

result.sort(key=lambda x:(-x[0],-x[1],x[2]))
for r in result:
    print(r[2])