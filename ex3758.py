import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, k, t, m = map(int, sys.stdin.readline().split())
    score_arr = [[0 for _ in range(k)] for _ in range(n)]
    submit_arr = [0 for _ in range(n)]
    time_arr = [0 for _ in range(n)]

    for num in range(m):
        i,j,s = map(int,sys.stdin.readline().split())
        score_arr[i-1][j-1] = max(score_arr[i-1][j-1], s)
        submit_arr[i-1] += 1
        time_arr[i-1] = num

    rank_arr = []

    for h in range(n):
        rank_arr.append([sum(score_arr[h]), submit_arr[h], time_arr[h], h])

    rank_arr.sort(key=lambda x:(-x[0], x[1], x[2]))

    for r in range(n):
        if rank_arr[r][3] == t - 1: # my team
            print(r+1) # 당신 팀보다 높은 점수를 받은 팀의 수) + 1