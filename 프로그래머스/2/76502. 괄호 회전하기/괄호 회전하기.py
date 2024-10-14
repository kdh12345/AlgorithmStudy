from collections import deque
def solution(s):
    answer = 0
    cnt = 0
    dq = deque(s)
    while cnt < len(s):
        dq = deque(s)
        for i in range(cnt):
            now = dq.popleft()
            dq.append(now)
        # check
        stk = []
        open_cnt = 0
        close_cnt = 0
        for i in range(len(dq)):
            if dq[i] == '[' or dq[i] == '(' or dq[i] == '{':
                stk.append(dq[i])
                open_cnt +=1
            elif dq[i] == ']':
                if len(stk) > 0 and stk[-1] == '[':
                    stk.pop()
                close_cnt += 1
            elif dq[i] == '}':
                if len(stk) > 0 and stk[-1] == '{':
                    stk.pop()
                close_cnt += 1
            elif dq[i] == ')':
                if len(stk) > 0 and stk[-1] == '(':
                    stk.pop()
                close_cnt += 1
        if len(stk) == 0 and close_cnt == open_cnt:
            answer+=1
        cnt += 1
    return answer