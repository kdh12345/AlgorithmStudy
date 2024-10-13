from collections import deque
def solution(people, limit):
    answer = 0
    dq = deque(sorted(people))
    while dq:
        p = dq.pop()
        if len(dq) > 0 and p + dq[0] <= limit:
            dq.popleft()
        answer+=1
    return answer