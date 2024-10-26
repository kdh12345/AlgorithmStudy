def solution(n, stations, w):
    answer = 0
    val = 2*w+1
    start = 1
    for s in stations:
        diff = s - w - start
        if diff > 0:
            answer += (s-w-start) // val
            if (s-w-start) % val != 0:
                answer += 1
        start = s+w+1
    
    if (n-start+1) >0:
        answer += (n-start+1) // val
        if (n-start+1) % val !=0:
            answer+=1
    

    return answer