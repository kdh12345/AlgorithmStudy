def solution(s):
    answer = []
    dic = dict()
    idx_dic = dict()
    arr = list(s)
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = -1
            idx_dic[arr[i]] = i
            answer.append(-1)
        elif arr[i] in dic:
            dic[arr[i]] = i - idx_dic[arr[i]]
            idx = i - idx_dic[arr[i]]
            idx_dic[arr[i]] = i
            answer.append(idx)
    return answer