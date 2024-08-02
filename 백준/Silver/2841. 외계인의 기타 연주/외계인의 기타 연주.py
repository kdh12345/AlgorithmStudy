n,p = map(int,input().split())
stk = [[] for _ in range(7)]

ans = 0
for _ in range(n):
    a,b= map(int,input().split())
    while len(stk[a]):
        if stk[a][-1] > b:
            stk[a].pop()
            ans += 1
        else:
            break
    if len(stk[a]) != 0 and stk[a][-1] == b:
        continue
    stk[a].append(b)
    ans+=1
print(ans)