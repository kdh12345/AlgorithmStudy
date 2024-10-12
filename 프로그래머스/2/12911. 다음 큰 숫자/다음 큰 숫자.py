def solution(n):
    answer = 0
    number = n+1
    while True:
        n_bin = bin(n)[2:]
        n_bin_len = str(n_bin).count('1')
        num_bin = bin(number)[2:]
        num_bin_len = str(num_bin).count('1')
        if n_bin_len == num_bin_len:
            answer = number
            break
        number+=1
    return answer