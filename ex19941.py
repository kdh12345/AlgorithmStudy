n,k = map(int,input().split())
loc = list(input())
cnt = 0

for i in range(n):
    if loc[i] == 'P':
        for j in range(max(i-k,0), min(i+k+1,n)): #k범위 안
            print(max(i-k,0))
            print(min(i+k+1,n))
            if loc[j] == 'H':
                loc[j] = 0
                cnt += 1
                break
print(cnt)