import sys
n = int(sys.stdin.readline().rstrip())
vote_list = []
cnt = 0
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    vote_list.append(num)

if n == 1:
    print(0)
else:
    dasom = vote_list[0]
    not_dasom = sorted(vote_list[1:], reverse=True)
    for idx,num in enumerate(not_dasom):
        if dasom == num:
            print(1)
            break
        while not_dasom[0] >= dasom:
            cnt += 1
            dasom += 1
            not_dasom[0] -= 1
            not_dasom = sorted(not_dasom, reverse=True)
        print(cnt)
        break