def solution(s):
    answer = 0

    stk = []
    s = list(s)
    for i in range(len(s)):
        if len(stk) > 0 and stk[-1] == s[i]:
            stk.pop(-1)
            continue
        stk.append(s[i])
    if len(stk) == 0:
        answer = 1
    else:
        answer = 0
    return answer