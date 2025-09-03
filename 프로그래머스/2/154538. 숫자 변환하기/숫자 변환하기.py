from collections import deque
def solution(x, y, n):
    answer = -1
    dq = deque()
    dq.append((x,0))
    visit = set()
    while dq:
        i,j = dq.popleft()
        if i > y or i in visit:
            continue
        visit.add(i)
        if i==y: # 변환 성공
            answer = j
            break
        for k in (i*3,i*2,i+n):
            if k<=y and k not in visit:
                dq.append((k,j+1))
    return answer 