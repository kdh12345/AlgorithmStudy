import heapq
def solution(operations):
    answer = []
    h1 = [] 
    for o in operations:
        tmp = o.split(' ')
        cmd = tmp[0]
        num = int(tmp[1])
        if cmd == 'I':
            heapq.heappush(h1,num)
        elif cmd == 'D' and num == 1:
            if len(h1) > 0:
                h1.sort()
                h1.pop()
        elif cmd == 'D' and num == -1:
            if len(h1) > 0:
                heapq.heappop(h1)
    h1.sort()
    if len(h1) == 0:
        answer = [0,0]
    else:
        max_val = h1[-1]
        min_val = h1[0]
        answer = [max_val,min_val]
        
    return answer