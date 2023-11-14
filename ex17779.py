import sys
n = int(sys.stdin.readline().rstrip())
maps = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

def sol(x,y,d1,d2):
    tmp = [[0]*(n+1) for _ in range(n+1)]

    #2
    tmp[x][y] = 5
    for i in range(1,d1+1):
        tmp[x+i][y-i] = 5
    for i in range(1,d2+1):
        tmp[x+i][y+i] = 5
    for i in range(1,d2+1):
        tmp[x+i+d1][y-d1+i] = 5
    for i in range(1,d1+1):
        tmp[x+i+d2][y-i+d2] = 5

    people = [0]*5
    #1선거구
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if tmp[r][c] == 5:
                break
            else:
                people[0]+=maps[r][c]
    #2번선거구
    for r in range(1,x+d2+1):
        for c in range(n,y,-1):
            if tmp[r][c] == 5:
                break
            else:
                people[1]+=maps[r][c]
    #3번선거구
    for r in range(x+d1,n+1):
        for c in range(1,y-d1+d2):
            if tmp[r][c] == 5:
                break
            else:
                people[2]+=maps[r][c]
    #4번선거구
    for r in range(x+d2+1,n+1):
        for c in range(n,y-d1+d2-1,-1):
            if tmp[r][c] == 5:
                break
            else:
                people[3]+=maps[r][c]
    #5번선거구
    people[4] = total - sum(people)
    return max(people) - min(people)





total = 0
for i in range(1,n+1):
    total += sum(maps[i])

answer = 987654321
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                # 1
                if x+d1+d2 > n:
                    continue
                if y-d1 < 1:
                    continue
                if y+d2 > n:
                    continue
                answer = min(answer,sol(x,y,d1,d2))
print(answer)