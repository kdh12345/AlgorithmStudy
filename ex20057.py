import sys
n=int(sys.stdin.readline().rstrip())
maps=[]
for _ in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    maps.append(arr)
out_sand=0 # 정답
def move_sand(dir,sand,x,y):
    global maps,out_sand,n
    first_sand=sand
    move_left = [(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01),
                 (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05)]
    move_right = [(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, -1, 0.01), (1, -1, 0.01),
                  (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05)]
    move_up = [(-1, -1, 0.1), (-1, 1, 0.1), (0, 1, 0.07), (0, -1, 0.07), (1, -1, 0.01), (1, 1, 0.01),
               (-2, 0, 0.05), (0, -2, 0.02), (0, 2, 0.02)]
    move_down = [(-1, -1, 0.01), (-1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), (0, 2, 0.02),
                 (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05)]
    move_list=[move_up,move_right,move_down,move_left]
    last_move=[(-1,0,1),(0,1,1),(1,0,1),(0,-1,1)]
    for i in move_list[dir]:
        nx=x+i[0]
        ny=y+i[1]
        n_sand=int(first_sand*i[2]) #소수점버림
        sand-=n_sand
        if nx<0 or nx>=n or ny<0 or ny>=n:
            out_sand+=n_sand
            continue
        maps[nx][ny]+=n_sand
    last_x=x+last_move[dir][0]
    last_y=y+last_move[dir][1]
    if last_x<0 or last_x>=n or last_y<0 or last_y>=n:
        out_sand+=sand
    else:
        maps[last_x][last_y]+=sand
point_x=n//2
point_y=n//2
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for idx in range(n-1):
    if idx%2==0: # left down
        for _ in range(idx+1):
            point_x = point_x + dx[3]
            point_y = point_y + dy[3]
            tmp = maps[point_x][point_y]
            maps[point_x][point_y] = 0
            move_sand(3, tmp, point_x, point_y)
        for _ in range(idx+1):
            point_x=point_x+dx[2]
            point_y=point_y+dy[2]
            tmp=maps[point_x][point_y]
            maps[point_x][point_y]=0
            move_sand(2,tmp,point_x,point_y)
    else:
        # right up
        for _ in range(idx+1):
            point_x = point_x + dx[1]
            point_y = point_y + dy[1]
            tmp = maps[point_x][point_y]
            maps[point_x][point_y] = 0
            move_sand(1, tmp, point_x, point_y)
        for _ in range(idx+1):
            point_x = point_x + dx[0]
            point_y = point_y + dy[0]
            tmp = maps[point_x][point_y]
            maps[point_x][point_y] = 0
            move_sand(0, tmp, point_x, point_y)
# n-1
for _ in range(n): #left
    point_x = point_x + dx[3]
    point_y = point_y + dy[3]
    tmp = maps[point_x][point_y]
    maps[point_x][point_y] = 0
    move_sand(3, tmp, point_x, point_y)
print(out_sand)
