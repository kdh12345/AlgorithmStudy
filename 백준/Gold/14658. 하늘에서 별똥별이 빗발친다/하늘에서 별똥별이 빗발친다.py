import sys
input = sys.stdin.readline

n,m,l,k = map(int,input().split())
pos = [tuple(map(int,input().split())) for _ in range(k)]
ans = 0

for x,y in pos:
    for nx,ny in pos:
        stars = 0
        for px,py in pos:
            if x<=px<=x+l and ny<=py<=ny+l:
                stars+=1
        ans = max(ans,stars)
ans = k - ans
print(ans)