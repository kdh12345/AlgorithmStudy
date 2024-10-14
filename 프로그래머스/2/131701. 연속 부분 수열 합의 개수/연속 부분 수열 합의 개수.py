def solution(elements):
    answer = 0
    n = len(elements)
    r_set = set()
    elements = elements * 2
    for i in range(n):
        for j in range(n):
            r_set.add(sum(elements[j:j+i+1]))
    answer = len(r_set)
    return answer