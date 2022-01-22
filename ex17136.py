import sys
def func(x,y,cnt):
    global ans
    if y>=10:
        ans=min(ans,cnt)
        return
    if x>=10:
        func(0,y+1,cnt)
        return
    if board[x][y]==1:
        for k in range(5):
            if paper[k]==5:
                continue
            if x+k>=10 or y+k>=10:
                continue
            flag=False
            for i in range(x,x+k+1):
                for j in range(y,y+k+1):
                    if board[i][j]==0:
                        flag=True
                        break
                if flag==True:
                    break
            if flag==False:
                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        board[i][j]=0
                paper[k]+=1
                func(x+k+1,y,cnt+1)
                paper[k]-=1
                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        board[i][j]=1
    else:
        func(x+1,y,cnt)

ans=987654321
paper=[0 for _ in range(5)]
board=[]
for _ in range(10):
    arr=list(map(int,sys.stdin.readline().split()))
    board.append(arr)
func(0,0,0)
if ans==987654321:
    print(-1)
else:
    print(ans)
