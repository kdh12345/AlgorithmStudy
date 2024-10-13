def solution(n, words):
    answer = []
    
    word_set = set()
    idx = 0
    cnt = 0
    for i in range(len(words)):
        if words[i] in word_set or (i > 0 and (words[i][0] != words[i-1][-1])) or len(words[i]) == 1:
            idx = i%n+1
            cnt = i//n+1
            break
        else:
            word_set.add(words[i])
    answer = [idx,cnt]
    return answer