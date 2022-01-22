import sys
def get_long(arr):
    left=1
    right=arr[-1]
    res=0
    while left<=right:
        mid=(left+right)//2
        total=0
        for i in range(len(arr)):
            total+=arr[i]//mid # 같은길이
        if total>=m:
            res=mid
            left=mid+1
        else:
            right=mid-1
    return res


m,n=map(int,sys.stdin.readline().split())
snack=list(map(int,sys.stdin.readline().split()))
snack.sort()
ans=get_long(snack)
print(ans)