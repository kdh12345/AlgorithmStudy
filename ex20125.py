import sys
n = int(sys.stdin.readline().rstrip())
body = []
for _ in range(n):
    arr = list(sys.stdin.readline().strip())
    body.append(arr)

# heart
hx = 0
hy = 0
sign = False
for i in range(n):
    for j in range(n):
        if body[i][j] == '*':
            hx = i+2
            hy = j+1
            sign = True
            break
    if sign == True:
        break
print(hx,hy)

hx-=1
hy-=1
# left arm
left_arm = 0
for j in range(hy-1,-1,-1):
    if body[hx][j] == '*':
        left_arm+=1


# right arm
right_arm = 0
for j in range(hy+1,n,1):
    if body[hx][j] == '*':
        right_arm += 1



#waist
waist = 0
r = hx+1
for i in range(hx+1,n,1):
    if body[i][hy] == '*':
        waist += 1
        r+=1

#left leg
left_leg = 0
c = hy - 1
for i in range(r,n,1):
    if body[i][c] == '*':
        left_leg+=1


# right leg
right_leg = 0
c = hy + 1
for i in range(r,n,1):
    if body[i][c] == '*':
        right_leg+=1

print(left_arm, right_arm, waist, left_leg, right_leg)

