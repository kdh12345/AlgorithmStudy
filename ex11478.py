import sys

word = sys.stdin.readline().rstrip()

sets = set()

for i in range(len(word)):
    for j in range(len(word)):
        sets.add(word[i:j+1])

ans = len(sets) - 1
print(ans)