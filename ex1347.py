import sys
n=int(sys.stdin.readline().rstrip())
word = list(sys.stdin.readline().strip())
direc = 0
# 남 서 북 동
dx = [1,0,-1,0]
dy = [0,-1,0,1]
miro = [(0,0)]


def turn_right(d):
    d = (d+1)%4
    return d

def turn_left(d):
    d = (d+3)%4
    return d
for w in word:
    if w == 'R':
        direc = turn_right(direc)
    elif w == 'L':
        direc = turn_left(direc)
    elif w == 'F':
        x = miro[-1][0] + dx[direc]
        y = miro[-1][1] + dy[direc]
        miro.append((x,y))

x_arr = sorted(miro,key=lambda x:x[0])
y_arr = sorted(miro,key=lambda x:x[1])

x_min = x_arr[0][0]
x_max = x_arr[-1][0]
y_min = y_arr[0][1]
y_max = y_arr[-1][1]

maps = [['#' for _ in range(y_min,y_max+1)] for _ in range(x_min,x_max+1)]

# 좌표 음수 방지
for i in range(len(miro)):
    miro[i] = (miro[i][0] - x_min, miro[i][1] - y_min)

for x,y in miro:
    maps[x][y] = '.'

for r in maps:
    print(''.join(r))