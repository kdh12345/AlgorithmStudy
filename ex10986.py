import sys
n,m=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
total=0
res=[]
cnt=[0]*1001
for num in numbers:
    total+=num
    res.append(total)
for item in res:
    cnt[item%m]+=1
ans=0
for i in range(1001):
    ans+=cnt[i]*(cnt[i]-1)//2 # 부분수열의 합 구하기
ans=cnt[0]+ans
print(ans)