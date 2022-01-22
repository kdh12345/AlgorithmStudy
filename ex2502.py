import sys
d,k=map(int,sys.stdin.readline().split())
a,b=1,1
for _ in range(4,d+1):
    a,b=b,a+b

ac=1
bc=0
while True:
    temp=k-a*ac
    if temp<0:
        break
    if temp%b==0:
        bc=temp//b
        break
    ac+=1

print(ac)
print(bc)