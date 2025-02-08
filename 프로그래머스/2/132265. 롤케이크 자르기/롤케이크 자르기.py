from collections import Counter
def solution(topping):
    answer = 0
    cnt_dic = Counter(topping)
    set_dic = set()
    for item in topping:
        cnt_dic[item] -= 1
        set_dic.add(item)
        if cnt_dic[item] == 0:
            cnt_dic.pop(item)
        if len(cnt_dic) == len(set_dic):
            answer+=1
    return answer