from collections import deque

T = int(input())
gears = [0]+[deque(map(int,list(input()))) for _ in range(T)]
k = int(input())
turn = [list(map(int,input().split())) for _ in range(k)]

for t,d in turn:
    turnE = []
    # left
    for i in range(t-1,0,-1):
        if gears[i][2] != gears[i+1][6]:
            turnE.append(i)
        else:
            break

    # right
    for i in range(t+1,T+1):
        if gears[i][6] != gears[i-1][2]:
            turnE.append(i)
        else:
            break

    # rotate
    gears[t].rotate(d)

    for e in turnE:
        gears[e].rotate(-d if (e-t)%2 else d)
ans = sum(gears[i][0] for i in range(1,T+1))
print(ans)