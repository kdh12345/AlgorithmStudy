import sys

n,k,p,x = map(int,sys.stdin.readline().split())

cur_x = ''
if len(str(x)) < k:
    cur_x = '0'*(k - len(str(x))) + str(x)
else:
    cur_x = str(x)

number = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011', '1011111', '1110000', '1111111', '1111011']

arr = []

for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            d = 0
            for h in range(7):
                if number[i][h] != number[j][h]:
                    d += 1
            arr[i].append(d) #바꾸는 횟수


def dfs(depth, cnt, cx):
    if depth >= len(cx):
        if int(cx) == x:
            return 0
        elif 1<=int(cx) <= n:
            return 1
        else:
            return 0

    ans, cur = 0,int(cx[depth])
    for i in range(10):
        if cur != i and (arr[cur][i] <= cnt):
            nx = cx[:depth] + str(i) + cx[depth+1:]
            ans += dfs(depth+1,cnt-arr[cur][i], nx)
        elif cur == i:
            ans += dfs(depth+1,cnt, cx)
    return ans


answer = dfs(0,p,cur_x)
print(answer)