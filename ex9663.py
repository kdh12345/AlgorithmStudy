import sys
n=int(sys.stdin.readline().rstrip())
cnt = 0
col = [False] * n
right = [False] * 2 * n
left = [False] * 2 * n

def bt(row):
    global cnt
    if row == n:
        cnt+=1
        return
    for i in range(n if row else n // 2):
        if not col[i] and not right[row - i] and not left[row + i]:
            col[i] = True
            right[row - i] = True
            left[row + i] = True

            bt(row+1)

            col[i] = False
            right[row - i] = False
            left[row + i] =  False

if n % 2 == 1:
    bt(0)
    cnt *= 2

    i = n//2
    col[i] = right[-i] = left[i] = True
    bt(1)

    print(cnt)
else:
    bt(0)
    print(cnt*2)
