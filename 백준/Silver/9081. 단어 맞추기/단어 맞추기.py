def nxt_permu(w):
    for i in range(len(w)-1,0,-1):
        if w[i-1] < w[i]:
            for j in range(len(w)-1,i-1,-1):
                if w[i-1] < w[j]:
                    w[i-1],w[j] = w[j],w[i-1]
                    return (w[:i]+(w[i:][::-1]))
    return w



n = int(input())
for i in range(n):
    word = list(input().strip())
    res = ''.join(nxt_permu(word))
    print(res)