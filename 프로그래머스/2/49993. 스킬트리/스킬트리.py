def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        arr = list(skill_trees[i])
        words = []
        for item in arr:
            if item in skill:
                words.append(item)
        tmp = list(skill)
        tmp_dic = dict()
        for i in range(len(tmp)):
            tmp_dic[tmp[i]] = i
        flag = True # 구분
        for i in range(len(words)):
            if i != tmp_dic[words[i]]:
                flag = False
                break
        if flag == True:
            answer+=1
    return answer