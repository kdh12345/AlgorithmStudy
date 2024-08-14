import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []
for _ in range(m):
    price = int(input())
    arr.append(price)

arr.sort()

ans = 0 # 총 수익
price = 0
total = 0
for i in range(m):
    cnt = m - i

    if n <= cnt:
        total = n * arr[i]
    else:
        total = cnt*arr[i]

    if ans < total:
        ans = total
        price = arr[i]

print(price,ans)