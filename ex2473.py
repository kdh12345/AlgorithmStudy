import sys
def get_sol(sol):
    res=int(1e9)
    flag=False
    if sol[0]>=0 and sol[-1]>=0:
        return [sol[0],sol[1],sol[2]]
    if sol[0]<=0 and sol[-1]<=0:
        return [sol[-3],sol[-2],sol[-1]]
    for i in range(n-2):
        target=-sol[i]
        left=i+1
        right=len(sol)-1
        while left<right:
            tmp=sol[left]+sol[right]
            total=sol[left]+sol[right]+sol[i]
            total=abs(total)
            if res>total:
                res=total
                ans1,ans2,ans3=sol[i],sol[left],sol[right]
                if not total:
                    flag=True
                    break
            if tmp<target:
                left+=1
            else:
                right-=1
        if flag==True:
            break
    return [ans1,ans2,ans3]
n=int(sys.stdin.readline().rstrip())
solution=list(map(int,sys.stdin.readline().split()))
solution.sort()
ans=get_sol(solution)
for item in ans:
    print(item,end=' ')