import sys
input = sys.stdin.readline

a = int(input())
cmd = input().rstrip()
b = int(input())

if cmd == '+':
    print(a+b)
elif cmd == '*':
    print(a*b)