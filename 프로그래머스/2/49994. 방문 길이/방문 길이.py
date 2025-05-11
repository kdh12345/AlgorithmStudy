def solution(dirs):
    answer = 0
    loc = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    x = 0
    y = 0
    ans_set = set()
    for d in dirs:
        dx = loc[d][0]
        dy = loc[d][1]
        nx = x + dx
        ny = y + dy
        if abs(nx) <= 5 and abs(ny) <= 5:
            ans_set.add((x,y,nx,ny))
            ans_set.add((nx,ny,x,y))
            x = nx
            y = ny
    answer = len(ans_set) // 2
    return answer