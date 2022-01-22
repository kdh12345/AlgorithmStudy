import sys
n=int(sys.stdin.readline().rstrip())
arr=[[0]*n for _ in range(n+1)]
word=list(sys.stdin.readline().strip())
v,k=[],0

def chk(idx):
    total=0
    for i in range(idx,-1,-1):
        total+=v[i]
        if arr[i][idx]=='+' and total<=0:
            return False
        if arr[i][idx]=='0' and total!=0:
            return False
        if arr[i][idx]=='-' and total>=0:
            return False
    return True

def solve(idx):
    if idx==n:
        print(' '.join(map(str,v)))
        exit(0)
    for i in range(-10,11):
        v.append(i)
        if chk(idx):
            solve(idx+1)
        v.pop()


for i in range(n):
    for j in range(i,n):
        arr[i][j]=word[k]
        k+=1
solve(0)
