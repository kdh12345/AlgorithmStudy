def dfs(result):
    global ans
    if len(arr) == 2:
        ans=max(ans,result)
        return
    else:
        for i in range(1,len(arr)-1):
            number = arr[i]
            arr.pop(i)
            dfs(result+arr[i-1]*arr[i])
            arr.insert(i,number)
n = int(input())
arr = list(map(int,input().split()))

ans = 0
dfs(0)
print(ans)