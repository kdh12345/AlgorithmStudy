def fx(number):
    """cnt = 0
    tar = 0
    idx = 1
    while True:
        tmp = bin(number)[2:]
        if len(bin(number)[2:]) < len(bin(number+idx)[2:]):
            leng = len(bin(number+idx)[2:]) - len(bin(number)[2:])
            for i in range(leng):
                tmp = '0'+tmp
        num2 = bin(number+idx)[2:]
    
    
        cnt = 0
        for i in range(len(tmp)):
            if tmp[i] != num2[i]:
                cnt+=1
    
        if 1<=cnt<=2:
            tar = int(num2,2)
            break
        idx+=1
    return tar
    """
    
    if number % 2 == 0: return number + 1

    # f-string을 사용해 문자 포맷팅, f''
    # f'0{}'은 2진수 값 앞에 0을 붙임. ex) 5 -> 0101
    x = f'0{bin(number)[2:]}' # 중괄호 안, 슬라이싱으로 순수하게 2진수 값만 남김

    # 10 왼쪽: 마지막 0이 나오기 이전의 비트들
    # 10 오른쪽: 마지막 0이 나오고 난 위치에서 2개 이후의 나머지 비트들
    x = f"{x[:x.rindex('0')]}10{x[x.rindex('0') + 2:]}"
    
    return int(x,2)
def solution(numbers):
    answer = []
    
    for num in numbers:
        res = fx(num)
        answer.append(res)
    return answer