"""arr = []
for i in range(19):
    arr.append([])
    for j in range(19):
        arr[i].append(0)
for i in range(19):
    arr[i]=list(map(int,input().split()))
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    for j in range(19):
        if arr[a-1][j]==0:
            arr[a-1][j]=1
        else:
            arr[a-1][j]=0
    for j in range(19):
        if arr[j][b-1]==0:
            arr[j][b-1]=1
        else:
            arr[j][b-1]=0

for i in range(19):
    for j in range(19):
        print(arr[i][j],end=' ')
    print()"""
maps=[[0]*100 for _ in range(101)]
h,w=map(int,input().split(' '))
n=int(input())
for i in range(n):
    l,d,x,y=map(int,input().split())
    x-=1
    y-=1
    if d==0:
        for j in range(y,y+l):
            maps[x][j]=1
    elif d==1:
        for j in range(x,x+l):
            maps[j][y]=1

for i in range(h):
    for j in range(w):
        print(maps[i][j],end=' ')
    print()


