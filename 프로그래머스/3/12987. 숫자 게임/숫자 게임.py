from bisect import bisect_left, bisect_right
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    siz = len(A)
    ai = 0
    bi = 0
    while siz > 0:
        if A[ai] < B[bi]:
            answer+=1
            bi+=1
        ai+=1
        siz-=1
    
    return answer