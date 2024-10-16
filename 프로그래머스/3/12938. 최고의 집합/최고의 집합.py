def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    number = s//n
    mod = s%n
    
    for i in range(n):
        answer.append(number)
    if mod != 0:
        for i in range(len(answer)):
            answer[i] += 1
            mod -= 1
            if mod == 0:
                break
    answer.sort()
    return answer