def convertTime(n): # 분 단위로 변환
    h = n // 100
    m = n % 100
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    s = startday
    
    s_arr = []
    for time in schedules:
        val = convertTime(time)
        s_arr.append(val)
    
    for i in range(len(timelogs)):
        s = startday
        chk = True
        for j in range(len(timelogs[i])):
            if s == 6 or s == 7:
                s = s%7 + 1
                continue
            val2 = convertTime(timelogs[i][j])
            if val2 > s_arr[i]+10:
                chk = False
                break
            s = s%7 + 1
        if chk == True:
            answer+=1
    return answer