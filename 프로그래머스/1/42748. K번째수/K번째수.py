def solution(array, commands):
    answer = []
    for item in commands:
        i=item[0]
        i-=1
        j=item[1]
        k=item[2]
        arr=array[i:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer