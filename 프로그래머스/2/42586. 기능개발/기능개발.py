from collections import Counter
def solution(progresses, speeds):
    answer = []
    stk = []
    for i in range(len(progresses)):
        diff = 0
        if (100-progresses[i]) % speeds[i] == 0:
            diff = (100-progresses[i])//speeds[i]
        else:
            diff = (100-progresses[i])//speeds[i] + 1
        if len(stk) > 0 and stk[-1] > diff:
            diff = stk[-1]
        stk.append(diff)
    cnts = Counter(stk)
    res = []
    for i,c in cnts.items():
        res.append(c)
    for item in res:
        answer.append(item)
    return answer