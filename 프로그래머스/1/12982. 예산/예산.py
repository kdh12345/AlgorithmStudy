def solution(d, budget):
    answer = 0
    total = 0
    arr = sorted(d)
    for item in arr:
        total += item
        if total > budget:
            break
        answer+=1
            
    return answer