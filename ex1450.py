import sys
n,c=map(int,sys.stdin.readline().split())
weight=list(map(int,sys.stdin.readline().split()))
aw=weight[:n//2]
bw=weight[n//2:]
a_sum=[]
b_sum=[]


def brute_force(w_arr,sum_arr,idx,w):
    if idx>=len(w_arr):
        sum_arr.append(w)
        return
    brute_force(w_arr,sum_arr,idx+1,w)
    brute_force(w_arr,sum_arr,idx+1,w+w_arr[idx])


def binary_search(arr,target,s,e):
    while s<e:
        mid=(s+e)//2

        if arr[mid]<=target:
            s=mid+1
        else:
            e=mid
    return e

brute_force(aw,a_sum,0,0)
brute_force(bw,b_sum,0,0)
b_sum.sort()
ans=0
for item in a_sum:
    if c-item>=0:
        ans+=binary_search(b_sum,c-item,0,len(b_sum)) #가운데서 만나기

print(ans)



