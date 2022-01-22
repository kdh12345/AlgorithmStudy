import sys
from collections import defaultdict
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(sys.stdin.readline().rstrip())
arr=[[0]*n for _ in range(n)]
like_dic=defaultdict(list)
res=0

for _ in range(n*n):
    _input=list(map(int,sys.stdin.readline().split()))
    like_dic[_input[0]]=_input[1:]

    max_x=0
    max_y=0
    max_like=-1
    max_empty=-1
    for x in range(n):
        for y in range(n):
            if arr[x][y]==0:
                like_cnt=0
                empty_cnt=0
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] in _input:
                            like_cnt+=1
                        if arr[nx][ny] ==0:
                            empty_cnt+=1
                if max_like<like_cnt or (max_like==like_cnt and max_empty<empty_cnt):
                    max_x=x
                    max_y=y
                    max_like=like_cnt
                    max_empty=empty_cnt
    arr[max_x][max_y]=_input[0]


for x in range(n):
    for y in range(n):
        cnt=0
        like=like_dic[arr[x][y]]
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] in like:
                    cnt+=1
        if cnt>0:
            res+=10**(cnt-1) #만족도 계산식
print(res)
