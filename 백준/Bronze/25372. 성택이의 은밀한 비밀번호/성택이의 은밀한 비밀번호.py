import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    pw = input()
    if len(pw) >= 6 and len(pw) <= 9:
        print('yes')
    else:
        print('no')