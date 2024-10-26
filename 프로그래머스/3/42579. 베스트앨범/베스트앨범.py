def solution(genres, plays):
    answer = []
    dic = dict()
    for i in range(len(plays)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        elif genres[i] in dic:
            dic[genres[i]] += plays[i]
    
    res = []
    
    for i in range(len(plays)):
        val1 = dic[genres[i]]
        res.append([val1,plays[i],i,genres[i]])
    res.sort(key=lambda x:(-x[0],-x[1],x[2]))
    cnt_dic = dict()
    for item in res:
        if item[3] not in cnt_dic:
            cnt_dic[item[3]] = 1
        elif item[3] in cnt_dic:
            cnt_dic[item[3]] += 1
        if cnt_dic[item[3]] > 2:
            continue
        answer.append(item[2])
            
    return answer