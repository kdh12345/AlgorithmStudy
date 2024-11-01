from string import ascii_uppercase
def solution(name):
    answer = 0
    names = list(name)
    
    total = 0
    cur_mov = len(name) - 1
    for i,item in enumerate(names):
        diff1 = ord(item) - ord('A')
        diff2 = ord('Z') - ord(item) + 1
        total += min(diff1,diff2)
        
        nxt = i+1
        while nxt < len(name) and names[nxt] == 'A':
            nxt += 1
        cur_mov = min([cur_mov,2*i+len(names)-nxt,i+2*(len(names) - nxt)])
    answer = total+cur_mov
    return answer