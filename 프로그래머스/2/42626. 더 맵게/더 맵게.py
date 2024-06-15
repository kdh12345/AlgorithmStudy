import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for item in scoville:
        heapq.heappush(h,item)
    total = 0
    while h[0] < K:
        if len(h) <= 1:
            return -1
        fir = heapq.heappop(h)
        sec = heapq.heappop(h)
        total = fir + sec * 2
        
        answer+=1
        heapq.heappush(h,total)
    return answer