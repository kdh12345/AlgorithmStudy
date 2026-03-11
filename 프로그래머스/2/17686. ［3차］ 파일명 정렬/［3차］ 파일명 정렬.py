def solution(files):
    answer = []
    
    for f in files:
        head,num,tail='','',''
        
        for i in range(len(f)):
            if f[i].isdigit():
                head = f[:i]
                f = f[i:]
                break
        
        for j in range(len(f)):
            if not f[j].isdigit():
                num = f[:j]
                tail = f[j:]
                break
            else:
                num = f
        
        answer.append([head,num,tail])
    
    answer.sort(key=lambda name:(name[0].lower(), int(name[1])))
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer