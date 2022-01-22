import sys
m,n,l=map(int,sys.stdin.readline().split())
loc=list(map(int,sys.stdin.readline().split()))
board=[]
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    board.append([a,b])
board.sort(key=lambda x:(x[0],x[1]))
