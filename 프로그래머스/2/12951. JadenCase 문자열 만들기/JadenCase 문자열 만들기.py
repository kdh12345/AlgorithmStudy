def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in range(len(arr)):
        words = list(arr[i])
        for j in range(len(words)):
            if j == 0 and not words[j].isdigit():
                answer += words[j].upper()
            else:
                answer += words[j].lower()
        if i < len(arr) -1:
            answer+=' '
    return answer