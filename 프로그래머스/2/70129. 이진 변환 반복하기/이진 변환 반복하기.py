def solution(s):
    answer = []
    tmp = s
    cnt = 0
    zero = 0
    while tmp != '1':
        #1
        tmp = tmp.replace('0','')
        zero += len(s) - len(tmp)
        
        #2
        tmp = len(tmp)
        
        #3
        tmp = bin(tmp)[2:]
        cnt+=1
        s = str(tmp)
    
    answer = [cnt, zero]
    return answer