def solution(s):
    answer = ''
    s_arr = s.split(' ')
    
    arr = []
    for item in s_arr:
        tmp = ''
        for i in range(len(item)):
            if i % 2 == 0:
                tmp += item[i].upper()
            else:
                tmp += item[i].lower()
        arr.append(tmp)
    answer = ' '.join(arr)
    return answer