def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        fir = phone_book[i]
        sec = phone_book[i+1]
        if fir == sec[:len(fir)]:
            answer = False
            break
    return answer