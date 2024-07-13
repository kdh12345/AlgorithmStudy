from copy import deepcopy

t = int(input())
h = list(map(int,input().split()))

s = deepcopy(h)
ans = 0

for i in range(1,t):
    s[i] += s[i-1]

for i in range(1,t-1):
    ans = max(ans,2*s[-1]-h[0]-h[i]-s[i])

for i in range(1,t-1):
    ans = max(ans, s[-1]-h[-1]-h[i]+s[i-1])

for i in range(1,t-1):
    ans = max(ans,s[i]-h[0]+s[-1]-s[i-1]-h[-1])

print(ans)
