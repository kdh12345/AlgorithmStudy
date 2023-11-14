import sys
while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    max_beun = max(a,b,c)
    if a == max_beun:
        if a >= b+c:
            print('Invalid')
            continue
    elif b == max_beun:
        if b >= a+c:
            print('Invalid')
            continue
    elif c == max_beun:
        if c >= a+b:
            print('Invalid')
            continue

    if a == b == c:
        print('Equilateral')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')