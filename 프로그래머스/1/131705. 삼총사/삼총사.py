from itertools import combinations
def solution(number):
    answer = 0
    combi = list(combinations(number,3))
    for c in combi:
        arr = list(c)
        total = sum(arr)
        if total == 0:
            answer+=1
    return answer