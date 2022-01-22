import sys
n=int(sys.stdin.readline().rstrip())
lv=[]
for _ in range(n):
    num=int(sys.stdin.readline().rstrip())
    lv.append(num)
ans=0
for i in range(n-1,0,-1):
    if lv[i]<=lv[i-1]:
        ans+=(lv[i-1]-lv[i]+1) # 자기자신도 카운트하니 +1
        lv[i-1]=lv[i]-1 # 1만큼 감소시키는 것이 1번
print(ans)

