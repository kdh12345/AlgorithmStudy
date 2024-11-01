def solution(arr):
    answer = [arr[0]]
    prv = arr[0]
    for i in range(1,len(arr)):
        if prv != arr[i]:
            answer.append(arr[i])
        prv = arr[i]
    return answer