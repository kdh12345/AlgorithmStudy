from collections import deque
def solution(order):
    answer = 0

    con = deque()
    idx = 0
    max_val = len(order)
    for i in range(1,max_val+1):
        con.append(i)
        while (con) and (con[-1] == order[idx]):
            idx += 1
            answer += 1
            if len(con) > 0:
                con.pop()
    
    return answer