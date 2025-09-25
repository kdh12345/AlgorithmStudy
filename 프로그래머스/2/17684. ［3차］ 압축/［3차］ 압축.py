from collections import deque
from string import ascii_uppercase
def solution(msg):
    answer = []
    dq = deque(msg)
    msg_lst = list(msg)
    arr = list(ascii_uppercase)
    
    # alpha dic
    alpha_dic = dict()
    for i in range(len(arr)):
        alpha_dic[arr[i]] = i+1
        
    w = c = 0 # 인덱스 초기화
    while True:
        c += 1	
        if c == len(msg):	
            answer.append((alpha_dic[msg[w:c]]))
            break
        
        # 만약 [현재글자+다음글자]가 사전에 없다면
        if msg[w:c+1] not in alpha_dic:
            alpha_dic[msg[w:c+1]] = len(alpha_dic) + 1 # 사전에 추가
            answer.append(alpha_dic[msg[w:c]])
            w = c	# 현재글자를 다음글자로 옮겨줌
    return answer