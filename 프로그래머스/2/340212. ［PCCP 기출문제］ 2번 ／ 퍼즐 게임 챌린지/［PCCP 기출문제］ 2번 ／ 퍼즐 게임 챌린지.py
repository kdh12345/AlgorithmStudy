def solution(diffs, times, limit):
    l = 1
    e = max(diffs)
    answer = e
    while l<e:
        level = (l+e) // 2
        time = times[0]
        for i in range(1,len(diffs)):
            if diffs[i] <= level:
                time += times[i]
            else:
                x = diffs[i] - level
                use = 0
                use = times[i] + times[i-1]
                use = use*x+times[i]    
                time += use
        if time <= limit:
            e = level
            answer = level
        else:
            l = level+1
    return answer