import sys
input = sys.stdin.readline

cem = list(input().rstrip())


stk = []

for c in cem:
    if c == '(':
        stk.append(c)
    elif c == ')':
        total = 0
        while True:
            if stk[-1] == '(':
                stk.pop()
                stk.append(total)
                break
            else:
                total += stk.pop()
    elif c == 'H':
        stk.append(1)
    elif c == 'C':
        stk.append(12)
    elif c == 'O':
        stk.append(16)
    else:
        stk.append(stk.pop()*int(c))

ans = sum(stk)

print(ans)