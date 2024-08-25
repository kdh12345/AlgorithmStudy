import sys
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

t = int(input())

ans = [0,3] # (0,0), (1,0), (0,1)

for i in range(2,1001):
    now = 0
    for j in range(1,i):
        if gcd(i,j) == 1:
            now += 1
    ans.append(ans[-1]+now*2)

for _ in range(t):
    n = int(input())

    print(ans[n])