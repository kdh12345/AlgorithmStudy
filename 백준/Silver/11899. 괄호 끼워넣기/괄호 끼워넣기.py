str = list(input())

stk = []
cnt = 0
for item in str:
    if item == '(':
        stk.append('(')
    else:
        if len(stk) > 0:
            stk.pop()
            cnt += 2

ans = len(str) - cnt
print(ans)