def solution(x):
    answer = True
    num = 0
    tmp = x
    while x!=0:
        num += x%10
        x//=10
    if tmp % num == 0:
        answer = True
    else:
        answer = False
    return answer