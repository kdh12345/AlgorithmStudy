n = int(input())

arr = []

for _ in range(n):
    number = int(input())
    arr.append(number)

diff = [0]*(2*n+1)
for i in range(2*n):
    diff[i+1] = diff[i]+arr[i%n]

ans = 0
total = sum(arr)
e = 1

for s in range(2*n):
    while e < 2*n+1 and diff[e]-diff[s] <= total - diff[e]+diff[s]:#시계<=반시계
        ans = max(ans,diff[e]-diff[s])
        e+=1
print(ans)