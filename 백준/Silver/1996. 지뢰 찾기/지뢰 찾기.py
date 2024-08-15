import sys
input = sys.stdin.readline
def chk(x,y):
    global n,visit
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    cnt1 = 0
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] != '.' and board[nx][ny] != '*' and mine[nx][ny] != 'M':
                cnt1 += int(board[nx][ny])
    return cnt1
n = int(input())

board = []
for _ in range(n):
    arr = list(sys.stdin.readline().rstrip())
    board.append(arr)

mine = [[0]*n for _ in range(n+1)]
#visit = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            #visit[i][j] = 1
            cnt = chk(i,j)
            if cnt >= 10:
                mine[i][j] = 'M'
            else:
                mine[i][j] = str(cnt)
        elif board[i][j] != '.':
            mine[i][j] = '*'


for i in range(n):
    for j in range(n):
        print(mine[i][j],end='')
    print()