import sys
while True:
    num = int(sys.stdin.readline().rstrip())
    if num==0:
        break
    number=list(str(num))
    if number==number[::-1]:
        print('yes')
    else:
        print('no')

