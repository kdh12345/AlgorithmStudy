def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
def binary_search2(arr,target,s,e):
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            e=mid-1
        else:
            s=mid+1
    return None