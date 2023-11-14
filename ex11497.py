import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    trees = list(map(int,sys.stdin.readline().split()))
    trees.sort()
    ans = 0
    for i in range(2,n):
        ans = max(ans,abs(trees[i] - trees[i-2]))
    print(ans)