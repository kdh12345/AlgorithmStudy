import sys
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
visit=[[0]*5 for _ in range(5)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(x,y,cnt,now):
    if cnt==5:
        num_set.add(now)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,cnt+1,now+str(maps[nx][ny]))
num_set=set()
ans=0
for i in range(5):
    for j in range(5):
        dfs(i,j,0,str(maps[i][j]))
ans=len(num_set)
print(ans)