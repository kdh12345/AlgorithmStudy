def can_place(park,siz):
    r = len(park)
    c = len(park[0])
    
    chk = False
    for i in range(r-siz+1):
        for j in range(c-siz+1):
            for x in range(i,i+siz):
                for y in range(j,j+siz):
                    print(park[x][y])
                    if park[x][y] == '-1':
                        chk = True
                    else:
                        chk = False
                        break
                if chk == False:
                    break
            if chk == True:
                return chk
    return False
def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)
    
    for m in mats:
        if can_place(park,m):
            return m
    return answer