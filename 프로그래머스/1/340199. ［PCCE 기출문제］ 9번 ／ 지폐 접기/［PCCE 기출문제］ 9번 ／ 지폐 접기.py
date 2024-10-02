def solution(wallet, bill):
    answer = 0
    # 반복문을 이용해 bill의 작은 값이 wallet의 작은 값 보다 크거나 bill의 큰 값이 wallet의 큰 값 보다 큰 동안 아래 과정을 반복합니다
    while ( min(bill) > min(wallet) ) or ( max(bill) > max(wallet) ):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
    return answer