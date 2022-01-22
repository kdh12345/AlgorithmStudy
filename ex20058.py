import sys
sys.setrecursionlimit(10**5)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n,q=map(int,sys.stdin.readline().split())
n=2**n
ice=[list(map(int,sys.stdin.readline().split()))
      for _ in range(n)]
lv=list(map(int,sys.stdin.readline().split()))
for l in lv:
    # rotate
    k=2**l
    for x in range(0,n,k):
        for y in range(0,n,k):
            temp=[ice[i][y:y+k] for i in range(x,x+k)]
            for i in range(k):
                for j in range(k):
                    ice[x+j][y+k-1-i]=temp[i][j]

    # 인접 얼음 카운팅
    cnt=[[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if 0<=nx<n and 0<=ny<n and ice[nx][ny]>0:
                    cnt[x][y]+=1
    # melt
    for x in range(n):
        for y in range(n):
            if ice[x][y]>0 and cnt[x][y]<3:
                ice[x][y]-=1
    # ice total
print(sum(sum(item) for item in ice))
    # (x,y)가 속한 덩어리 크기
def dfs(x,y):
    res=1
    ice[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and ice[nx][ny]>0:
            res+=dfs(nx,ny)
    return res
ans=0
for x in range(n):
     for y in range(n):
        if ice[x][y]>0:
            ans=max(ans,dfs(x,y))
print(ans)