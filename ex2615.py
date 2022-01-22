import sys
def chk(r,c,maps):
    start=maps[r][c]
    chk=False
    #1
    cnt=0
    for i in range(r,19):
        for j in range(c,19):
            if maps[i][j]!=0 and start==maps[i][j]:
                cnt+=1
                chk=True
            else:
                chk=False
                break
    if start==1 and chk==True and cnt==5:
        return 1
    if start==2 and chk==True and cnt==5:
        return 2
    #2
    chk = False
    cnt=0
    for i in range(r,-1,-1):
        for j in range(c,19):
            if maps[i][j]!=0 and start==maps[i][j]:
                cnt+=1
                chk=True
            else:
                chk=False
                break
    if start==1 and chk==True and cnt==5:
        return 1
    if start==2 and chk==True and cnt==5:
        return 2
    #3
    chk=False
    cnt=0
    for i in range(c,19):
        if maps[r][i]!=0 and start==maps[r][i]:
            cnt+=1
            chk=True
        else:
            chk=False
            break
    if start==1 and chk==True and cnt==5:
        return 1
    if start==2 and chk==True and cnt==5:
        return 2
    #4
    chk=False
    cnt=0
    for i in range(r,19):
        if maps[i][c]!=0 and start==maps[i][c]:
            cnt+=1
            chk=True
        else:
            chk=False
            break
    if start==1 and chk==True and cnt==5:
        return 1
    if start==2 and chk==True and cnt==5:
        return 2
    return 0
board=[]
for _ in range(19):
    arr=list(map(int,sys.stdin.readline().split()))
    board.append(arr)
flag=False
res_row=0
res_col=0
res=0
for row in range(19):
    for col in range(19):
        if chk(row,col,board)==1:
            res=1
            flag=True
            res_row=row
            res_col=col
            break
        elif chk(row,col,board)==2:
            res=2
            flag=True
            res_row=row
            res_col=col
            break
        elif chk(row,col,board)==0:
            res=0
            res_row=row
            res_col=col
    if flag==True:
        break
print(res)
print(res_row, res_col)