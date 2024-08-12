import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    c,no,score = map(int,input().split())
    arr.append([c,no,score])

arr.sort(key=lambda x:-x[2])

medals = dict()
cnt = 0
for item in arr:
    c     = item[0]
    no    = item[1]
    score = item[2]
    if c not in medals:
        medals[c] = 1
    else:
        medals[c] += 1
    if c in medals and medals[c] > 2:
        continue
    cnt += 1
    if cnt > 3:
        break
    print(c,no)