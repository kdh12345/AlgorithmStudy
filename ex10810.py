import sys
n,m=map(int,sys.stdin.readline().split())
numbers=[0]*n
for _ in range(m):
    i,j,k=map(int,sys.stdin.readline().split())
    for idx in range(i,j+1):
        numbers[idx-1]=k
for item in numbers:
    print(item,end=' ')