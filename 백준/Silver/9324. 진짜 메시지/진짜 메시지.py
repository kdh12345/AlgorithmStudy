
n = int(input())
def chk(msg):
    # char dic
    msg_char_dic = dict()
    # is third
    is_third = 0
    flag = True

    for ch in msg:
        if is_third:
            if ch == is_third:
                is_third = 0
                msg_char_dic[ch] = 0
                continue
            else:
                print('FAKE')
                return
        if ch not in msg_char_dic.keys():
            msg_char_dic.update({ch:1}) # 없으면 추가
        elif msg_char_dic[ch] == 2:
            msg_char_dic[ch] = 0
            is_third = ch
        else:
            msg_char_dic[ch] += 1
    if flag and is_third == 0:
        print('OK')
    else:
        print('FAKE')
msg_lst = []
for _ in range(n):
    msg_lst.append(input())

for msg in msg_lst:
    chk(msg)