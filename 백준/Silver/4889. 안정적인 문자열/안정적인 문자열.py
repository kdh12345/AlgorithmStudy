import sys
input = sys.stdin.readline


cnt = 1
result = []
while True:
    word = list(sys.stdin.readline().strip())
    ans = 0
    if word[0] == '-':
        break

    # correct parthensis
    stk = []
    for i in range(len(word)):
        if word[i] == '{':
            stk.append('{')
        elif word[i] == '}':
            if len(stk) > 0 and stk[-1] == '{':
                stk.pop()
            else:
                stk.append('}')
    if len(stk) == 0:
        ans = 0
    else:
        for i in range(0,len(stk)-1,2):
            if stk[i] == stk[i+1]:
                ans += 1
            else:
                ans += 2

    result.append(ans)

for i in range(len(result)):
    print(i+1, end='. ')
    print(result[i])
