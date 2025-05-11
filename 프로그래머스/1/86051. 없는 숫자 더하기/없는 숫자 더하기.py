def solution(numbers):
    answer = 0
    num_set = set(numbers)
    for i in range(10):
        if i not in num_set:
            answer+=i
    return answer