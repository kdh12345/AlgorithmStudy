import sys
n = int(sys.stdin.readline().rstrip())
cmd = int(sys.stdin.readline().rstrip())

rooms = [0]*(n+1)
for _ in range(cmd):
    x,y = map(int,input().split())
    for i in range(x,y):
        rooms[i] = 1

ans = rooms.count(0)
ans -= 1
print(ans)