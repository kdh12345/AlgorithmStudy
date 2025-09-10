def solution(price, money, count):
    answer = 0
    total = 0
    tmp = price
    for i in range(count):
        total+=tmp
        tmp += price
    
    answer = total - money
    if answer < 0:
        answer = 0
    return answer