def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    start = -30001
    for i in range(len(routes)):
        n_s = routes[i][0]
        n_e = routes[i][1]
        if n_s > start:
            answer += 1
            start = n_e
    return answer