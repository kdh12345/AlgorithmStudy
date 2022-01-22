import sys
n,m=map(int,sys.stdin.readline().split())
set1=set()
arr=[]
for i in range(n):
    word=sys.stdin.readline().rstrip()
    set1.add(word)
for i in range(m):
    word=sys.stdin.readline().rstrip()
    arr.append(word)
ans=0
for item in arr:
    if item in set1:
        ans+=1
print(ans)
