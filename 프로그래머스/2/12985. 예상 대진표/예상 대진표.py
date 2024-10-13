def solution(n,a,b):
    answer = 0
    
    while True:
        if a % 2 == 0:
            if b == (a-1):
                answer+=1
                break
        if a % 2 == 1:
            if b == (a+1):
                answer+=1
                break
        if b % 2 == 0:
            if a == (b-1):
                answer+=1
                break
        if b % 2 == 1:
            if a == (b+1):
                answer+=1
                break
        if a % 2 == 0:
            a = a//2
        elif a % 2 == 1:
            a=a//2+1
        if b % 2 == 0:
            b = b//2
        elif b % 2 == 1:
            b = b//2+1
        answer+=1
    

    return answer