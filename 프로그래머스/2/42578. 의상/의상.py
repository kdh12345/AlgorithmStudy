def solution(clothes):
    answer = 1
    c_dic = dict()
    for c in clothes:
        if c[1] not in c_dic:
            c_dic[c[1]] = [c[0]]
        elif c[1] in c_dic:
            c_dic[c[1]] += [c[0]]
    for i,val in c_dic.items():
        answer *= (len(val)+1)
    answer -= 1
    return answer