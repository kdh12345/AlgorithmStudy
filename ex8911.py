import sys
def rotate(cmd,dir):
    if cmd=='L':
        dir=(dir+3)%4
        return dir
    elif cmd=='R':
        dir=(dir+1)%4
        return dir
t=int(sys.stdin.readline().rstrip())
x=0
y=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
direction=0
for _ in range(t):
    comm=sys.stdin.readline().rstrip()
    maps = [[x,y]]
    for c in comm:
        if c=='F':
            nx=x+dx[direction]
            ny=y+dy[direction]
            x=nx
            y=ny
        elif c=='B':
            nx=x-dx[direction]
            ny=y-dy[direction]
            x=nx
            y=ny
        elif c=='L':
            direction=rotate('L',direction)
        elif c=='R':
            direction=rotate('R',direction)
        maps.append([x, y])
    width=max(maps,key=lambda x:x[0])[0]-min(maps,key=lambda x:x[0])[0]
    height=max(maps,key=lambda x:x[1])[1]-min(maps,key=lambda x:x[1])[1]
    ans=width*height
    print(ans)