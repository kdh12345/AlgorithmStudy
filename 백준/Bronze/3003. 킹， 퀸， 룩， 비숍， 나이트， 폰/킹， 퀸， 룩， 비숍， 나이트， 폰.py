import sys

chess = [1,1,2,2,2,8]

in_arr = list(map(int,sys.stdin.readline().split()))

res = []
for i in range(len(in_arr)):
    diff = chess[i]-in_arr[i]
    res.append(diff)

for item in res:
    print(item,end=' ')