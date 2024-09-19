import sys
input = sys.stdin.readline
a,b,c,num = map(int,input().split())

a1 = num // a
b1 = num // b
c1 = num // c
for i in range(0,a*a1+1,a):
    for j in range(0,b*b1+1,b):
        for k in range(0,c*c1+1,c):
            if i+j+k == num:
                print(1)
                exit(0)
print(0)