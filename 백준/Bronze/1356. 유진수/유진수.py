import sys
input = sys.stdin.readline

arr = list(input().rstrip())
if len(arr) == 1:
    print('NO')
    exit(0)

isYou = False
for i in range(len(arr)):
    num1 = arr[:i+1]
    num2 = arr[i+1:]

    number1 = 1
    for item in num1:
        number1 *= int(item)
    number2 = 1
    for item in num2:
        number2 *= int(item)
    if number1 == number2:
        print('YES')
        isYou = True
        break

if isYou == False:
    print('NO')
