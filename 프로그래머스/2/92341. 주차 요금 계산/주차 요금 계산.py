from datetime import datetime
import math
def solution(fees, records):
    answer = []
    st_time = fees[0] # 기본 시간
    st_money = fees[1] # 기본 요금
    f_time = fees[2]
    money = fees[3]
    
    r_dic = dict()
    res_dic = dict()
    for r in records:
        r = r.split(' ')
        time = r[0]
        num = r[1]
        go_out = r[2]
        
        if go_out == 'IN':
            r_dic[num] = time
        elif go_out == 'OUT':
            in_time = datetime.strptime(r_dic[num],'%H:%M')
            out_time = datetime.strptime(time,'%H:%M')
            diff = out_time - in_time
            diffs = str(diff).split(':')
            
            s = int(diffs[2])
            h = int(diffs[0])
            m = int(diffs[1])+(h*60)+(s//60)
            if num not in res_dic:
                res_dic[num] = m
            elif num in res_dic:
                res_dic[num] += m
            del r_dic[num]
    
    for k,v in r_dic.items():
        in_time = datetime.strptime(v,'%H:%M')
        out_time = datetime.strptime('23:59','%H:%M')
        diff = out_time - in_time
        diffs = str(diff).split(':')
            
        s = int(diffs[2])
        h = int(diffs[0])
        m = int(diffs[1])+(h*60)+(s//60)
        
        if k in res_dic:
            res_dic[k] += m
        elif k not in res_dic:
            res_dic[k] = m
    
    # total
    lst = []
    for k,v in res_dic.items():
        tmp = math.ceil((v-st_time)/f_time)
        total = st_money+tmp*money
        if v <= st_time:
            total = st_money
        lst.append([k,total])
    lst.sort(key=lambda x:x[0])
    for item in lst:
        answer.append(item[1])
    return answer