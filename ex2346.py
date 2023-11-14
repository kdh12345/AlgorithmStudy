from collections import deque


n = int(input())
baloons = deque(enumerate(map(int, input().split())))

answer = []
while baloons:
    index, paper = baloons.popleft()
    answer.append(index+1)

    if paper > 0:
        baloons.rotate(-(paper)+1)
    elif paper < 0:
        baloons.rotate(-paper)

for i in range(len(answer)):
    if i < len(answer) - 1:
        print(answer[i],end= ' ')
    elif i == len(answer) - 1:
        print(answer[i])

"""idx = 0
cnt = 1
start = baloons[0]
ans = []
ans.append([idx,cnt])
if len(baloons) > 1:
    baloons = baloons[1:]

    while baloons:
        if start > 0:
            idx += start
            if idx >= len(baloons):
                idx = len(baloons) - 1
            cnt += 1
            ans.append([idx+1,cnt])
            start = baloons[idx]
            baloons.pop(idx)

        elif start < 0:
            idx += start
            if idx < 0:
                idx = 0
            cnt += 1
            ans.append([idx+1,cnt])
            start = baloons[idx]
            baloons.pop(idx)


result = []
ans.sort()
for a in ans:
    result.append(a[1])

for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i],end= ' ')
    elif i == len(result) - 1:
        print(result[i])
"""