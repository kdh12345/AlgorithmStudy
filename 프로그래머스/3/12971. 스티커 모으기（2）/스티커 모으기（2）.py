def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    
    siz = len(sticker)
    # 1
    dp1 = [0]+sticker[:-1]
    for i in range(2,siz):
        dp1[i] = max(dp1[i-1],dp1[i-2]+dp1[i])
    
    # 2
    dp2 = [0]+sticker[1:]
    for i in range(2,siz):
        dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])
    
    answer = max(dp1[-1],dp2[-1])

    return answer