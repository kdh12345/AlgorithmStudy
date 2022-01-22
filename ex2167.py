import sys
n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)
k=int(sys.stdin.readline().rstrip())
for _ in range(k):
    i,j,x,y=map(int,sys.stdin.readline().split())
    i-=1
    j-=1
    x-=1
    y-=1
    total=0
    for r in range(i,x+1):
        for c in range(j,y+1):
            total+=arr[r][c]#(i,j)부터 (x,y)까지의 합
    print(total)