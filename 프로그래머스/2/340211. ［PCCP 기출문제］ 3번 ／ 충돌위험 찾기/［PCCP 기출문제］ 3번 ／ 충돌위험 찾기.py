from collections import Counter
def mov(route,arr):
    idx = 0
    pa = []
    for i in range(len(route)-1):
        sx,sy = arr[route[i]-1]
        ex,ey = arr[route[i+1]-1]
        
        while sx!=ex:
            pa.append((sx,sy,idx))
            if sx < ex:
                sx += 1
            else:
                sx -= 1
            idx+=1
        while sy != ey:
            pa.append((sx,sy,idx))
            if sy < ey:
                sy += 1
            else:
                sy -= 1
            idx += 1
    pa.append((sx,sy,idx))
    return pa
def solution(points, routes):
    answer = 0
    
    arr = [i for i in points]
    result = []
    
    for r in routes:
        result.extend(mov(r,arr))
        
    tmp = Counter(result)
    for i in tmp.values():
        if i >= 2:
            answer+=1
        
            
    return answer
