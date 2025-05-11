def solution(a, b):
    arr = []
    tmp = 0
    if a > b:
        a,b = b,a
    for i in range(a,b+1):
        arr.append(i)
    answer = sum(arr)
    return answer