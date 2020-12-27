maps=[]
dx=[0,1]
dy=[1,0]
for i in range(10):
    arr=list(map(int,input().split()))
    maps.append(arr)
x=1
y=1
maps[x][y]=9
while maps[x][y]!=2:
    maps[x][y]=9
    nx=x+1
    ny=y+1
    if maps[x][ny]!=1:
        y+=1
    elif maps[nx][y]!=1:
        x+=1
    else:
        break
maps[x][y]=9

for i in range(10):
    for j in range(10):
        print(maps[i][j],end=' ')
    print()


