import sys

n = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(n):
    num = sys.stdin.readline().rstrip()
    leng = len(num)
    lst = list(num)
    total = 0
    for item in lst:
        if item.isdigit():
            total += int(item)
    arr.append([num,leng,total,num])

arr.sort(key=lambda x:(x[1],x[2],x[3]))
res = []
for item in arr:
    res.append(item[0])

for item in res:
    print(item)
