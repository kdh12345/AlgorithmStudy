import sys

n,m = map(int,sys.stdin.readline().split())

a = set(list(map(int,sys.stdin.readline().split())))
b = set(list(map(int,sys.stdin.readline().split())))

res1 = a-b
res2 = b-a
ans = len(res1)+len(res2)
print(ans)