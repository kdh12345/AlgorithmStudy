import sys
n,k=map(int,sys.stdin.readline().split())
temper=list(map(int,sys.stdin.readline().split()))
idx=0
total=sum(temper[:k])
max_total=total
if k==1:
    ans=max(temper)
    print(ans)
else:
    while True:
        total-=temper[idx]
        if idx+k>=n:
            break
        total+=temper[idx+k]
        max_total=max(total,max_total)
        idx+=1
    print(max_total)