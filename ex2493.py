import sys
n=int(sys.stdin.readline().rstrip())
buildings=list(map(int,sys.stdin.readline().split()))
stack=[]
ans=[]
for i in range(n):
    while stack:
        if stack[-1][1]>buildings[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop(-1)
    if len(stack)==0:
        ans.append(0)
    stack.append([i,buildings[i]])
for item in ans:
    print(item,end=' ')


