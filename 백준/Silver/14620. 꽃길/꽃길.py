from itertools import combinations

def chk(lst):
    global ans
    visit = []
    total = 0
    for x,y in lst:
        visit.append((x,y))
        total += board[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (nx,ny) not in visit:
                total += board[nx][ny]
                visit.append((nx,ny))
            else:
                return
    ans = min(ans,total)

n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

res = []
board = []
ans = 987654321

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(1,n-1):
    for j in range(1,n-1):
        res.append((i,j))

for item in combinations(res,3):
    chk(item)
print(ans)