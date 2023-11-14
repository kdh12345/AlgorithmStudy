import sys
p = int(sys.stdin.readline().rstrip())
for _ in range(p):
    arr = list(map(int,sys.stdin.readline().split()))
    idx = arr[0]
    arr = arr[1:]
    ans = 0
    #print(idx,arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
               ans+=1
    print(idx,ans)
