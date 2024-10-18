from itertools import permutations
def solution(k, dungeons):
    answer = 0
    arr = []
    for i in range(len(dungeons)):
        arr.append(i)
    permu = list(permutations(arr,len(dungeons)))
    
    # search
    tmp = k
    for p in permu:
        cnt = 0
        for idx in p:
            min_val = dungeons[idx][0]
            use_val = dungeons[idx][1]
            if tmp < min_val:
                continue
            tmp -= use_val
            cnt += 1
        answer = max(answer,cnt)
        tmp = k
        
    return answer