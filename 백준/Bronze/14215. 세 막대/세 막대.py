a,b,c = map(int,input().split())


arr = []
arr.append(a)
arr.append(b)
arr.append(c)

arr.sort()

ans = 0
if arr[0]+arr[1] > arr[2]:
    ans = sum(arr)
else:
    ans = (arr[0]+arr[1])*2 - 1
print(ans)