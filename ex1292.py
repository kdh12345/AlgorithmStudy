import sys
a,b=map(int,sys.stdin.readline().split())
number=[]
for i in range(1,1001):
    for j in range(i):
        number.append(i)
ans=0
for i in range(a-1,b):
    ans+=number[i]
print(ans)