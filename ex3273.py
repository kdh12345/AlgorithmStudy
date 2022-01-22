import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().split()))
x=int(sys.stdin.readline().rstrip())
arr=sorted(arr)
start=0
end=n-1
total=0
cnt=0 # 부분합이 x인 케이스 cnt up
while start<end:
    total=arr[start]+arr[end]
    if total==x:
        cnt+=1
    if total<x:
        start+=1
    else:
        end-=1
print(cnt)