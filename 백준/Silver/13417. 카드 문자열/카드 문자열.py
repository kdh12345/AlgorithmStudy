from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    words = list(map(str,input().split()))
    result = deque([words[0]])

    for item in words[1:]:
        if item > result[0]:
            result.append(item)
        else:
            result.appendleft(item)

    print(*result,sep='')

