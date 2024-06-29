def egg_game(start):

    global ans
    if start == n:
        total = 0
        for i in range(n):
            if egg[i][0] <= 0:
                total += 1

        ans = max(ans,total)
        return

    if egg[start][0]<=0:
        egg_game(start+1)
        return

    chk = True
    for i in range(n):
        if start == i:
            continue
        if egg[i][0] > 0:
            chk = False
            break

    if chk == True:
        ans = max(ans,n-1)
        return

    for i in range(n):
        if start == i or egg[i][0]<=0:
            continue
        egg[start][0] -= egg[i][1]
        egg[i][0] -= egg[start][1]
        egg_game(start+1)
        egg[start][0] += egg[i][1]
        egg[i][0] += egg[start][1]




n  = int(input())
egg = [list(map(int,input().split())) for _ in range(n) ] #내구도와 무게
ans = 0
egg_game(0)

print(ans)