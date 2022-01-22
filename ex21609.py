import sys
n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def catch_block(s):
    global board,n
    area = 1
    visited=[[0]*n for _ in range(n)]
    color = board[s[0]][s[1]]
    blocks = [(s[0],s[1])]
    stack = [s]
    visited[s[0]][s[1]]=1
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    r_b = []
    num_rainbow  = 0
    while(stack):
        cur_x,cur_y =stack.pop()
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]
            if(nx>=n or ny>=n or nx<0 or ny<0):
                continue
            if(visited[nx][ny]==0):
                visited[nx][ny]=1
                if(board[nx][ny]!='-'):
                    if(board[nx][ny]==color or board[nx][ny]==0):
                        if(board[nx][ny]==0):
                            num_rainbow +=1
                        blocks.append((nx,ny))
                        stack.append((nx,ny))
                        area+=1
    if(area>=2):
        blocks = sorted(blocks,key=lambda x : (x[0],x[1]))
        for i in blocks:
            if(board[i[0]][i[1]]!=0):
                r_b = [i[0],i[1]]
                break
        return area,blocks,num_rainbow,r_b
    else:
        return 0,[],0,[-1,-1]


def max_area():
    global board, n

    max_area = 0
    b = []
    max_rainbow = -1
    r_b = [-1, -1]
    score = 0
    temp_area = 0
    temp_blocks = []
    temp_rainbow = 0
    temp_r_b = [-1, -1]

    for j in range(n):
        for i in range(n):
            if (board[i][j] != -1 and board[i][j] != '-' and board[i][j] != 0):
                temp_area, temp_blocks, temp_rainbow, temp_r_b = catch_block((i, j))
                if (temp_area > max_area):
                    max_area = temp_area
                    b = temp_blocks
                    max_rainbow = temp_rainbow
                    r_b = temp_r_b
                elif (temp_area == max_area):
                    if (temp_rainbow > max_rainbow):
                        max_rainbow = temp_rainbow
                        b = temp_blocks
                        max_area = temp_area
                        r_b = temp_r_b
                    elif (temp_rainbow == max_rainbow):
                        if (temp_r_b[0] > r_b[0]):
                            b = temp_blocks
                            # max_area =temp_area
                            # max_rainbow = temp_rainbow
                            r_b = temp_r_b
                        elif (temp_r_b[0] == r_b[0]):
                            if (temp_r_b[1] > r_b[1]):
                                b = temp_blocks
                                # max_area =temp_area
                                # max_rainbow = temp_rainbow
                                r_b = temp_r_b
    for i, j in b:
        board[i][j] = '-'
    score = max_area ** 2
    return score, b

def gravity():
    global board,n
    for j in range(n):
        for i in range(n-1,-1,-1):
            if board[i][j]!=-1 and board[i][j]!='-':
                cur_val=board[i][j]
                board[i][j]='-'
                cur_loc=i
                while True:
                    if cur_loc==n-1:
                        board[cur_loc][j]=cur_val
                        break
                    n_loc=cur_loc+1
                    if n_loc==n-1:
                        if board[n_loc][j]=='-':
                            board[n_loc][j]=cur_val
                            break
                        else:
                            board[cur_loc][j]=cur_val
                            break
                    else:
                        if board[n_loc][j]!='-':
                            board[cur_loc][j]=cur_val
                            break
                    cur_loc=n_loc

def rotate_arr():
    global board,n
    res=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-j-1][i]=board[i][j]
    board=res

ans=0
while True:
    temp_score,b=max_area()
    if temp_score>0:
        ans+=temp_score
    else:
        break

    gravity()
    rotate_arr()
    gravity()

print(ans)
