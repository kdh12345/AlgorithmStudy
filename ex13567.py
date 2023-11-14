import sys
dx = [1,0,-1,0]
dy = [0,-1,0,1]
m,n=map(int,sys.stdin.readline().split())
sx = 0
sy = 0
d  = 0
isChk = True
for _ in range(n):
    cmds = sys.stdin.readline().rstrip()
    cmd = cmds.split(' ')[0]
    num = int(cmds.split(' ')[1])
    if cmd == 'TURN' and num == 0:
        d = (d+3)%4
    elif cmd == 'TURN' and num == 1:
        d = (d + 1) % 4
    if cmd == 'MOVE':
        sx += dx[d]*num
        sy += dy[d]*num
    if sx < 0 or sx >= m or sy < 0 or sy >= m:
        isChk = False
        break

if isChk == False:
    print(-1)
else:
    print(sx,sy)

