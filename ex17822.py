import sys
from collections import deque
n,m,t = map(int,sys.stdin.readline().split())
board = [deque(int(i) for i in sys.stdin.readline().split()) for _ in range(n)]
info  = [[int(i) for i in sys.stdin.readline().split()] for _ in range(t)]

# d==0 시계, d==1 반시계
for tc in range(t):
    x,d,k = info[tc]

    # 회전
    res = 0
    for i in range(n):
        res += sum(board[i])
        if (i+1)%x == 0:
            if d == 0:
                board[i].rotate(k)
            elif d == 1:
                board[i].rotate(-k)
    if res > 0:

        have_to_rmv = []
        for i in range(n):
            for j in range(m-1):
                if board[i][j] != 0 and board[i][j+1] !=0 and board[i][j] == board[i][j+1]:
                    have_to_rmv.append((i,j))
                    have_to_rmv.append((i, j+1))
            if board[i][0] != 0 and board[i][-1] != 0 and board[i][0] == board[i][-1]:
                have_to_rmv.append((i, 0))
                have_to_rmv.append((i, m-1))

        # 옆 원
        for j in range(m):
            for i in range(n-1):
                if board[i][j] != 0 and board[i+1][j] != 0 and board[i][j] == board[i+1][j]:
                    have_to_rmv.append((i,j))
                    have_to_rmv.append((i+1,j))

        have_to_rmv = list(set(have_to_rmv))

        for i in range(len(have_to_rmv)):
            x,y = have_to_rmv[i]
            board[x][y] = 0

        if len(have_to_rmv) == 0:
            avgSum  = 0
            zeroCnt = 0
            for i in range(n):
                avgSum += sum(board[i])
                zeroCnt += board[i].count(0)
            avg = avgSum / (n*m-zeroCnt)

            for i in range(n):
                for j in range(m):
                    if board[i][j] != 0 and board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] != 0 and board[i][j] < avg:
                        board[i][j] +=1
    else:
        break


ans = 0
for i in range(n):
    ans += sum(board[i])
print(ans)

