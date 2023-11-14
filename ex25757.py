import sys
n,play = sys.stdin.readline().split()
n = int(n)

players = []
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    players.append(temp)

players = list(set(players))

if play == 'Y':
    print(len(players))
elif play == 'F':
    ans = len(players) // 2
    print(ans)
else:
    ans = len(players) // 3
    print(ans)