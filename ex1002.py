import math
import sys
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
        continue
    diff_x=abs(x2-x1)
    diff_y=abs(y2-y1)
    diff=math.sqrt(diff_x*diff_x+diff_y*diff_y)
    radius=r2+r1
    radius2=abs(r2-r1)
    if radius2<diff<radius:
        print(2)
    elif diff==radius or diff==radius2:
        print(1)
    elif radius<diff or diff<radius2:
        print(0)
