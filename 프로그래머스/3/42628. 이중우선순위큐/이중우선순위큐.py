import heapq
def solution(operations):
    answer = []
    """heap=[]
    for item in operations:
        inputs=item.split()
        cmd=inputs[0]
        num=inputs[1]
        if cmd=='I':
            heapq.heappush(heap,int(num))
        if cmd=='D':
            if len(heap)>0:
                if num=='1':
                    heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
                elif num=='-1':
                    heapq.heappop(heap)
    if len(heap)==0:
        answer.append(0)
        answer.append(0)
        return answer
    else:
        answer.append(heapq.nlargest(1,heap)[0])
        answer.append(heapq.nsmallest(1,heap)[0])"""
    h=[]
    for i in range(len(operations)):
        inputs=operations[i].split()
        cmd=inputs[0]
        num=inputs[1]
        if cmd=='I':
            heapq.heappush(h,int(num))
        elif cmd=='D':
            if len(h)>0:
                if num=='1':
                    h.pop(h.index(heapq.nlargest(1,h)[0]))
                elif num=='-1':
                    heapq.heappop(h)
    if len(h)==0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(heapq.nlargest(1,h)[0])
        answer.append(h[0])
    return answer