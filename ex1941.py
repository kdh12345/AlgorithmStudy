import sys
sys.setrecursionlimit(10**9)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
p=[]
def chk(now):
    global visit
    x=int(now/5)
    y=now%5
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            if visit[nx][ny]==0:
                if (nx*5+ny) in p:
                    visit[nx][ny]=1
                    chk((nx*5+ny))
def make_seven(idx,cnt,y_cnt):
    global ans
    global visit
    if y_cnt>=4 or 25-idx<7-cnt:
        return
    if cnt==7:
        chk(p[0])
        if sum(sum(visit,[]))==7: #1 방문횟수를 합했을때 7
            ans+=1
        visit = [[0] * 5 for _ in range(5)]
        return
    x=int(idx/5)
    y=idx%5
    p.append(idx)
    if board[x][y]=='Y':
        make_seven(idx+1,cnt+1,y_cnt+1)
    else:
        make_seven(idx + 1, cnt + 1, y_cnt)
    p.pop()
    make_seven(idx+1,cnt,y_cnt)



board=[]
for _ in range(5):
    arr=list(sys.stdin.readline().strip())
    board.append(arr)
visit=[[0]*5 for _ in range(5)]
ans=0
make_seven(0,0,0)
print(ans)