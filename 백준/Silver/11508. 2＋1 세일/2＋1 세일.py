n = int(input())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
arr.sort(reverse=True)

total = 0
for i in range(2,len(arr),3):
    total+=arr[i]
print(sum(arr) - total)