import sys

total = 0
max_val = 0
for _ in range(10):
    down, up = map(int,sys.stdin.readline().split())
    total -= down
    total += up
    max_val = max(max_val,total)

print(max_val)