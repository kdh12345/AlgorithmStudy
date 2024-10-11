def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    if op_start <= pos <= op_end:
        pos = op_end
    for c in commands:
        if c == 'prev':
            tmp = pos.split(':')
            m = int(tmp[0])
            s = int(tmp[1])
            if (s-10<0) and (m>=1):
                m -= 1
                s = (s-10)+60
            else:
                s = max(s-10,0)
        
        elif c == 'next':
            tmp = pos.split(':')
            m = int(tmp[0])
            s = int(tmp[1])
            
            tmp2 = video_len.split(':')
            m2 = int(tmp2[0])
            s2 = int(tmp2[1])
            if (s+10>=60) and (m<m2):
                m += 1
            if m == m2:
                s = min((s+10)%60,s2)
            else:
                s = (s+10)%60
        pos = str(m).zfill(2)+':'+str(s).zfill(2)
        if op_start <= pos <= op_end:
            pos = op_end
    answer = pos
    return answer