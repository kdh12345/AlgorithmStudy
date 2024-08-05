n,k,b = map(int,input().split())
arr = [0]*(n+1)
for _ in range(b):
    number = int(input())
    arr[number-1] = 1

min_val = sum(arr[:k])

cnt = min_val

for i in range(1,n-k+1):
    if arr[i-1] == 1:
        cnt -= 1
    if arr[i+k-1] == 1:
        cnt += 1
    min_val = min(min_val,cnt)

print(min_val)