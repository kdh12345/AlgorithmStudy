import sys

player = int(input())

pl = []
for i in range(1,player+1):
    pl.append(i)

cnt = 0
s = 0
rmvNum = 0

for i in range(1,player):
    cnt = (i**3)%len(pl)

    rmvNum = (cnt-1+s)%len(pl) # pop 할꺼 -1
    if rmvNum < 0:
        rmvNum+=len(pl)
    pl.pop(rmvNum)
    s = rmvNum

ans = pl[0]
print(ans)