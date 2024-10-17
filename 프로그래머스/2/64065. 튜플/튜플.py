def solution(s):
    answer = []
    s = list(s)
    s = s[1:-1]
    s = ''.join(s)
    s = s.split('},')
    stk = []
    res = []
    word = ''
    for i in range(len(s)):
        s[i] = s[i].replace('{','')
        s[i] = s[i].replace('}','')
        tmp = s[i].split(',')
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        res.append((tmp,len(tmp)))
    res.sort(key=lambda x:x[1])
    res_set = set()
    new_arr = []
    for item in res:
        numbers = item[0]
        for num in numbers:
            if num not in res_set:
                res_set.add(num)
                new_arr.append(num)
    for item in new_arr:
        answer.append(item)
    return answer