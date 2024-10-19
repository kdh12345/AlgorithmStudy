from collections import deque
def solution(priorities, location):
    answer = 0
    dq = deque()
    for item in priorities:
        dq.append(item)
    names = deque()
    for i in range(len(priorities)):
        names.append(chr(ord('A')+i))
    tmp = names[location]
    
    process = []
    index = 0
    while True:
        num = 0
        name = ''
        if len(dq) > 0 and len(names) > 0:
            num = dq.popleft()
            name = names.popleft()
        chk = False
        for i in range(len(dq)):
            if num < dq[i]:
                chk = True
                break
        if chk == True:
            dq.append(num)
            names.append(name)
            continue
        index+=1
        process.append([index,num,name])
        if name == tmp:
            break
    for item in process:
        if item[2] == tmp:
            answer = item[0]
            break
    return answer