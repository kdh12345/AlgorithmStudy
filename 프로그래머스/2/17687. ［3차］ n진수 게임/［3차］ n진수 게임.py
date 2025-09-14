def conv(num,n):
    if num == 0:
        return '0'
    word='0123456789ABCDEF'
    result =''
    while num > 0:
        num, mod = divmod(num,n)
        result += word[mod]
    return result[::-1]
def solution(n, t, m, p):
    answer = ''
    game =''
    cur = p - 1
    for number in range(t*m):
        game += conv(number,n)
    
    while True:
        if len(answer) == t:
            break
        answer += game[cur]
        cur += m
    return answer