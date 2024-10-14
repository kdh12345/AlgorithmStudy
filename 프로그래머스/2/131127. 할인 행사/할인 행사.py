def solution(want, number, discount):
    answer = 0
    dic = dict()
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount)-9):
        tmp = discount[i:i+10]
        dic2 = dict()
        for item in tmp:
            if item not in dic2:
                dic2[item] = 1
            elif item in dic2:
                dic2[item] += 1
        chk = False
        for k,v in dic2.items():
            if k in want and dic[k] == dic2[k]:
                chk = True
            else:
                chk = False
                break
        if chk == True:
            answer += 1
    return answer