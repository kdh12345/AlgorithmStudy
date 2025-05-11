def solution(n):
    answer = []
    arr = list(str(n))
    for item in arr:
        answer.append(int(item))
    answer = answer[::-1]
    return answer