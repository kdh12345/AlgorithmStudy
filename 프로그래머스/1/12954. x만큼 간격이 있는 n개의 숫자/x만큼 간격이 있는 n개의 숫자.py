def solution(x, n):
    answer = []
    jump = x
    for _ in range(n):
        answer.append(x)
        x+=jump
    return answer