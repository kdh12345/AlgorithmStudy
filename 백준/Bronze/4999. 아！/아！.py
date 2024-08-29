import sys
input = sys.stdin.readline

person = list(input().rstrip())
doctor = list(input().rstrip())

if len(person) < len(doctor):
    print('no')
else:
    print('go')