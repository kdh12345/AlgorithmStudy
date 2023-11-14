import sys
vowel = {'a','e','i','o','u'}
while True:
    word = sys.stdin.readline().rstrip()
    if word == 'end':
        break

    pw = list(word)
    v_flag = 0
    v_cnt = 0
    c_cnt = 0
    case = 0

    for i in range(len(pw)):

        # 1
        if pw[i] in vowel:
            v_flag = 1
            v_cnt += 1
            c_cnt = 0
            if v_cnt == 3:
                case = 1
                break
        else:
            v_cnt = 0
            c_cnt += 1
            if c_cnt == 3:
                case = 1
                break
        if i > 0:
            if pw[i-1] == pw[i]:
                if pw[i] != 'e' and pw[i] != 'o':
                    case = 1
                    break

    if case != 1 and v_flag == 1:
        print('<'+word+'> is acceptable.')
    else:
        print('<'+word+'> is not acceptable.')