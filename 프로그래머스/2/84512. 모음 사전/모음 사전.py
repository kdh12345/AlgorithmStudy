from itertools import product
def solution(word):
    answer = []
    alpha = ['A','E','I','O','U']
    for i in range(1,6):
        for p in product(alpha,repeat = i):
            answer.append(''.join(p))
    answer.sort()
    ans = answer.index(word)+1
    return ans