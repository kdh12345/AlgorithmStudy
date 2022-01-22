from collections import defaultdict, deque

def solution(game_board,empty_board):
    answer=0
    n=len(game_board)
    visit,visit2=defaultdict(int),defaultdict(int)
    q=deque()
    q2=deque()
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    piece=[]
    piece2=[]

    for i in range(n):
        for j in range(n):
            if game_board[i][j]==0:
                if visit[(i,j)]==0:
                    l,t,r,b=i,j,i,j
                    visit[(i,j)]=1
                    q.append([i,j])
                    cnt=1

                    while q:
                        x,y=q.popleft()

                        for i in range(4):
                            nx=x+dx[i]
                            ny=y+dy[i]
                            if 0<=nx<n and 0<=ny<n and game_board[nx][ny]==0 and visit[(nx,ny)]==0:
                                q.append([nx,ny])
                                l=min(l,nx)
                                t=min(t,ny)
                                r=max(r,nx)
                                b=max(b,ny)
                                visit[(nx,ny)]=1
                                cnt+=1
                        piece.append([l,t,r,b,cnt])
            if empty_board[i][j]==1:
                if visit2[(i,j)]==0:
                    l,t,r,b=i,j,i,j
                    visit2[(i,j)]=1
                    q2.append([i,j])
                    cnt=1

                    while q2:
                        x,y=q2.popleft()

                        for i in range(4):
                            nx=x+dx[i]
                            ny=y+dy[i]
                            if 0<=nx<n and 0<=ny<n and empty_board[nx][ny]==1 and visit2[(nx,ny)]==0:
                                q.append([nx,ny])
                                l = min(l,nx)
                                t = min(t, nx)
                                r = max(r, nx)
                                b = max(b, nx)
                                visit2[(nx,ny)]=1
                                cnt+=1
                        piece2.append([l,t,r,b,cnt])

            for l,t,r,b,cnt in piece:
                for l2,t2,r2,b2,cnt2 in piece2:
                    A=[row[t:b+1] for row in game_board[l:r+1]]
                    B=[row[t2:b2+1] for row in empty_board[l2:r2+1]]
                    if cnt==cnt2:
                        c=0
                        isEnd=False
                        for i in range(4):
                            if not isEnd:
                                c+=1
                                n=len(A)
                                m=len(A[0])

                                if n==len(B) and m==len(B[0]):
                                    for i in range(n):
                                        for j in range(m):
                                            if A[i][j]+B[i][j]!=1:
                                                break
                                            if i==n-1 and j==m-1:
                                                isEnd=True
                                                break
                                        if A[i][j]+B[i][j]!=1 or isEnd:
                                            break
                                B=rotate(B)
                        if isEnd:
                            answer+=cnt
                            piece2.remove([l2,t2,r2,b2,cnt2])
                            break

        def rotate(arr):
            n=len(arr)
            m=len(arr[0])

            tmp=[[0]*n for _ in range(m)]

            for i in range(n):
                for j in range(m):
                    tmp[j][n-i-1]=arr[i][j]
            return  tmp