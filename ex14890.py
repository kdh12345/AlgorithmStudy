import sys

def chk(now):

    for i in range(1,n):
        if abs(now[i] - now[i-1]) > 1:
            return False
        if now[i] < now[i-1]:
            for j in range(l):
                if i+j >=n or used[i+j] or now[i] != now[i+j]:
                    return False
                if now[i] == now[i+j]:
                    used[i+j] = True
        elif now[i] > now[i-1]:
            for j in range(l):
                if i - j - 1 < 0 or used[i-j-1] or now[i-1] != now[i-j-1]:
                    return False
                if now[i-1] == now[i-j-1]:
                    used[i-j-1] = True
    return True


n,l    = map(int,sys.stdin.readline().split())
board  = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)
ans = 0

# 1.가로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if chk(board[i]):
        ans+=1

# 2. 세로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if chk([board[j][i] for j in range(n)]):
        ans+=1

print(ans)