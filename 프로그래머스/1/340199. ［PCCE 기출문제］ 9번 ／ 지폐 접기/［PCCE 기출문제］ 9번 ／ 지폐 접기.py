def solution(wallet, bill):
    answer = 0
    
    min_w = min(wallet)
    max_w = max(wallet)
    min_b = min(bill)
    max_b = max(bill)
    
    while (min_b > min_w ) or (max_b > max_w):
        # 2-1
        if bill[0] > bill[1]:
            bill[0] = bill[0]//2
        else:
            bill[1] = bill[1]//2
        answer+=1
        
        #update
        min_w = min(wallet)
        max_w = max(wallet)
        min_b = min(bill)
        max_b = max(bill)
    return answer