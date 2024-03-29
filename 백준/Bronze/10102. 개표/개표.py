import sys
v= int(sys.stdin.readline().rstrip())
number = sys.stdin.readline().rstrip()

a = number.count('A')
b = number.count('B')
if a>b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')