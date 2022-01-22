import sys
def sol(arr):
    ans=[0]*len(arr)
    # 짓는 것이 x
    for i in range(len(arr)):
        if len(arr[i])==2:
            ans[i]=arr[i][0]
    while 0 in ans:
        for i in range(len(arr)):
            build_time=arr[i][0]
            build_times=[]
            if ans[i]!=0: # 이미 처리
                continue
            else:
                for j in range(1,len(arr[i])):
                    if j==len(arr[i])-1:
                        ans[i]=max(build_times)
                    else:
                        if ans[arr[i][j]-1]!=0:
                            build_times.append(build_time+ans[arr[i][j]-1])
                        else:
                            break
    return ans

n=int(sys.stdin.readline().rstrip())
array=[]
for i in range(n):
    build=list(map(int,sys.stdin.readline().split()))
    array.append(build)

answer=sol(array)
for item in answer:
    print(item)