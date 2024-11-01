def solution(sizes):
    answer = 0
    
    max_lst = []
    min_lst = []
    for item in sizes:
        max_lst.append(max(item[0],item[1]))
        min_lst.append(min(item[0],item[1]))
    answer = max(max_lst) * max(min_lst)
    return answer