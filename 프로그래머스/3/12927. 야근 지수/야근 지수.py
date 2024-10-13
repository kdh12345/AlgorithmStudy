import heapq
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for i in range(n):
        now = heapq.heappop(works)
        now+=1
        heapq.heappush(works,now)
    for item in works:
        answer+=item*item
    return answer