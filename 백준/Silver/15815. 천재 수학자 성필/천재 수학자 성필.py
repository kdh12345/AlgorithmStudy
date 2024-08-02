import sys
word = list(sys.stdin.readline().rstrip())

stk = []
ans = 0
for item in word:
    if item == '*':
        first = stk[-1]
        stk.pop()
        second = stk[-1]
        stk.pop()
        total = first * second
        stk.append(total)
    elif item == '+':
        first = stk[-1]
        stk.pop()
        second = stk[-1]
        stk.pop()
        total = first + second
        stk.append(total)
    elif item == '-':
        first = stk[-1]
        stk.pop()
        second = stk[-1]
        stk.pop()
        total = second - first
        stk.append(total)
    elif item == '/':
        first = stk[-1]
        stk.pop()
        second = stk[-1]
        stk.pop()
        total = second // first
        stk.append(total)
    else:
        stk.append(int(item))


for j in stk:
    print(j)