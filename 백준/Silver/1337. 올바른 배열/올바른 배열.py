n = int(input())
arr = []
for _ in range(n):
    number = int(input())
    arr.append(number)
arr.sort()
tmp = []

for i in range(len(arr)):
    cnt = 0
    for j in range(arr[i],arr[i]+5):
        if j not in arr:
            cnt+=1
    tmp.append(cnt)

ans = min(tmp)
print(ans)