n = list(input())
b = 1
for item in n:
    if item == 'A':
        if b == 1: b = 2
        elif b == 2: b = 1
    if item == 'B':
        if b == 2: b=3
        elif b==3: b= 2
    if item == 'C':
        if b == 1: b = 3
        elif b==3 : b = 1
print(b)
