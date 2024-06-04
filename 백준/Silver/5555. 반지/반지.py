
t = input()
n = int(input())

ans = 0
for i in range(n):
    ring = input()
    if t in ring*2:
        ans += 1

print(ans)