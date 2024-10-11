def solution(n):
    answer = int(1e9)
    x = 1
    while n%x != 1:
        x += 1
    answer = x
    return answer