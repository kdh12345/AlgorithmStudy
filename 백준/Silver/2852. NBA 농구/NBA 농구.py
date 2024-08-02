n = int(input())

prv = [0,0]
team1 = [0,0]
team2 = [0,0]

for _ in range(n):
    win, time = input().split()
    if win == '1':
        team1[0] += 1
    else:
        team2[0] += 1
    minute, second = map(int,time.split(':'))
    time = minute*60+ second
    if team1[0] == team2[0]: # 동점
        if prv[1] == 1:
            team1[1] += time - prv[0]
        else:
            team2[1] += time - prv[0]
        prv[1] = 0
    elif team1[0] > team2[0]: # 팀 1 이겼다면?
        if prv[1] == 0: # 이전까지는 비기고 있었다면?
            prv[0] = time
            prv[1] = 1
    else: # 팀 2 이겼다면?
        if prv[1] == 0: # 이전까지는 비기고 있었다면?
            prv[0] = time
            prv[1] = 2

if prv[1] == 1:
    team1[1] += 48*60 - prv[0]
if prv[1] == 2:
    team2[1] += 48*60 - prv[0]

print('%02d:%02d' %(team1[1]//60, team1[1]%60))
print('%02d:%02d' %(team2[1]//60, team2[1]%60))