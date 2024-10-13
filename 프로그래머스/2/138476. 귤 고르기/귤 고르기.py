from collections import Counter
def solution(k, tangerine):
    answer = 0
    c_arr = Counter(tangerine)
    tmp = list(set(tangerine))
    res = []
    for i in range(len(tmp)):
        res.append([c_arr[tmp[i]], tmp[i]])
    
    res.sort(reverse=True)
    total = 0
    for item in res:
        cnt = item[0]
        total+=cnt
        if total >= k:
            answer+=1
            break
        else:
            answer+=1
    return answer