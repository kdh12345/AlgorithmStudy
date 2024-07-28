n = int(input())

arr = []
for _ in range(n):
    number = int(input())
    arr.append(number)
"""
result = []
s = 0
e = 1
cnt = 0
while s < e < len(arr):
    if arr[s] > arr[e]:
        cnt += 1
        e+=1
    else:
        result.append(cnt)
        cnt = 0
        s+=1
        e = s+1

cnt = 0
if arr[-2] > arr[-1]:
    cnt+=1
    result.append(cnt)

ans = sum(result)
print(ans)
"""

ans = 0
stk = []
for cur in arr:
    while stk and stk[-1] <=cur: #볼 수 없는 것 제거
        stk.pop()

    ans += len(stk)
    stk.append(cur)

print(ans)