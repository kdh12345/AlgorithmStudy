def solution(record):
    answer = []
    r_dic = dict()
    for r in record:
        arr = r.split()
        cmd = arr[0]
        uid = arr[1]
        if cmd in ['Enter','Change']:
            r_dic[uid] = arr[2]
    for item in record:
        arr2 = item.split()
        cmd = arr2[0]
        uid = arr2[1]
        if cmd == 'Enter':
            word = r_dic[uid]+'님이 들어왔습니다.'
            answer.append(word)
        elif cmd == 'Leave':
            word = r_dic[uid]+'님이 나갔습니다.'
            answer.append(word)
        
    return answer