import sys
input = sys.stdin.readline

n,d = map(int,input().split())

ans = 0
for i in range(1,n+1):
    if str(i).count(str(d)):
        if i >= 10:
            ans += list(str(i)).count(str(d))
        else:
            ans += 1
print(ans)