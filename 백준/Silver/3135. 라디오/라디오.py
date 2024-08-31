import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n = int(input())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

diff1 = abs(b-a)
pos = 987654321
for item in arr:
    if abs(pos-b) > abs(b-item):
        pos = item

ans = 1
if pos > b:
    ans += pos - b
else:
    ans += b - pos

if abs(a-b) < ans:
    print(abs(a-b))
else:
    print(ans)