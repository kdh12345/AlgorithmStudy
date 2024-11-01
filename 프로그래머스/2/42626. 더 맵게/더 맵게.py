import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for item in scoville:
        heapq.heappush(h,item)
    num = 0
    idx = 0
    while idx<len(scoville):
        if h[0] >= K:
            break
        first = 0
        if len(h) > 0:
            first = heapq.heappop(h)
        second = 0
        if len(h) > 0:
            second = heapq.heappop(h)
        num = first+second*2
        heapq.heappush(h,num)
        answer += 1
        idx += 1
    if idx == len(scoville):
        return -1
    return answer