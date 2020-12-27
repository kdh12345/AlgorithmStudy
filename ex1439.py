n=input()
cnt0=0 # 0으로 바꾸는 경우
cnt1=0 # 1로 바꾸는 경우

if n[0]=='1':
    cnt0+=1
else:
    cnt1+=1

for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        if n[i+1]=='1':
            cnt0+=1
        else:
            cnt1+=1
ans=min(cnt0,cnt1)
print(ans)