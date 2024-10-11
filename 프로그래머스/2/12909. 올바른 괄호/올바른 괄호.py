def solution(s):
    answer = True
    open_cnt = 0
    close_cnt = 0
    stk = []
    for item in s:
        if item == '(':
            stk.append('(')
            open_cnt += 1
        elif item == ')':
            if len(stk) > 0 and stk[-1] == '(':
                stk.pop(-1)
            close_cnt+=1
    if len(stk) == 0 and open_cnt == close_cnt:
        answer = True
    else:
        answer = False

    return answer