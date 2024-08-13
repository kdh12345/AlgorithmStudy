import sys
input = sys.stdin.readline

n,k = map(int,input().split())

chk = k*(k+1)//2

if n < chk:
    print(-1)
elif (n-chk) % k ==0:
    print(k-1)
else:
    print(k)