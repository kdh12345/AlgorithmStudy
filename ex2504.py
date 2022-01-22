import sys
paren = list(sys.stdin.readline().rstrip())

stack = []
score = 1
answer = 0
for idx in range(len(paren)):

    if paren[idx] == "(":
        stack.append("(")
        score *= 2
    elif paren[idx] == "[":
        stack.append("[")
        score *= 3

    elif paren[idx] == ")":
        if len(stack) == 0 or stack[-1] == "[":
            answer = 0
            break
        if paren[idx-1] == "(":
            answer += score
        stack.pop(-1)
        score //=2
    else:
        if len(stack) == 0 or stack[-1] == "(":
            answer = 0
            break
        if paren[idx-1] == "[":
            answer += score

        stack.pop(-1)
        score //=3

if len(stack) != 0:
    print(0)
else:
    print(answer)
