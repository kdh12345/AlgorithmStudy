def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    while s != '1':
        new_word=''
        for i in range(len(s)):
            if s[i] == '0':
                zero_cnt += 1
            else:
                new_word += s[i]
        s = str(bin(len(new_word)))[2:]
        cnt += 1
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer