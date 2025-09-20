def conv(num,k1):
    lst = []
    
    while num != 0:
        lst.append(num%k1)
        num //= k1
    return lst[::-1]

def chk_cnt(numbers):
    numbers=''.join(map(str,numbers))
    
    
    numbers = numbers.split('0')
    
    cnt = 0
    for num in numbers:
        if len(num) == 0:
            continue
        if int(num) < 2: # 0,1 제외
            continue
        sosu=True
        for i in range(2,int(int(num)**0.5)+1):
            if int(num) % i ==0:
                sosu = False
                break
        if sosu == True:
            cnt += 1
    return cnt
    
def solution(n, k):
    answer = -1
    result = conv(n,k)
    
    # chk and count p
    
    answer = chk_cnt(result)
    return answer