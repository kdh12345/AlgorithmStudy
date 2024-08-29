import sys
input = sys.stdin.readline

number = int(input())

n = 1
while True:
    if number == 1:
        break
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = 3*number + 1
    n+=1

print(n)