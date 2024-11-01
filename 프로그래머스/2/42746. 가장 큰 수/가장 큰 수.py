def solution(numbers):
    answer = ''
    arr = list(map(str,numbers))
    arr.sort(key=lambda x:x*3,reverse=True)
    for item in arr:
        answer += item
    answer = str(int(answer))
    return answer