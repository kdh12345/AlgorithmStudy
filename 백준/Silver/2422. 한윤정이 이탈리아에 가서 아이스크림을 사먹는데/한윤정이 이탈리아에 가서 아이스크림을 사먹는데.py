import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
ice = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    ice[a-1][b-1] = 1
    ice[b-1][a-1] = 1


ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if ice[i][j] == 0 and ice[i][k] == 0 and ice[j][k] == 0:
                ans += 1
print(ans)