import sys
import copy
r,c=map(int,sys.stdin.readline().split())
maps=[]
for _ in range(r):
    arr=list(sys.stdin.readline().strip())
    maps.append(arr)
new_maps=copy.deepcopy(maps) #동시 수정 막기 위해
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for x in range(r):

    for y in range(c):
        if maps[x][y]=='.':
            continue
        sea_cnt = 0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=r or ny<0 or ny>=c:
                sea_cnt+=1
                continue
            if maps[nx][ny]=='.':
                sea_cnt+=1
        if sea_cnt>=3:
            new_maps[x][y]='.'
start_row=0
end_row=0
min_idx=c-1
max_idx=0
for x in range(r):
    if 'X' in new_maps[x]:
        start_row=x
        break
for x in range(r-1,-1,-1):
    if 'X' in new_maps[x]:
        end_row=x
        break
for x in range(start_row,end_row+1):
    temp=[x for x,val in enumerate(new_maps[x]) if val=='X']
    if not temp: # X가 없으면 pass
        continue
    min_tmp=temp[0]
    max_tmp=temp[-1]
    min_idx=min(min_tmp,min_idx)
    max_idx=max(max_tmp,max_idx)

for x in range(start_row,end_row+1):
    for y in range(min_idx,max_idx+1):
        print(new_maps[x][y],end='')
    print()