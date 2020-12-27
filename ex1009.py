import sys
t=int(sys.stdin.readline().rstrip())
ans=[]
for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    res=a
    b=b%4+4 #모든 수는 4주기마다 동일한 숫자나옴
    for i in range(2,b+1):
        res=(res*a)%10
    if res==0:
        res=10
    print(res)